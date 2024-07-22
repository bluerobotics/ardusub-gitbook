# OpenCV

OpenCV (Open Source Computer Vision) is a library to help the development of computer vision software.
To perform any real-time image processing with the companion camera, we highly suggest OpenCV to do the job.

Take a look in the OpenCV [website](https://opencv.org/) and [tutorials](https://docs.opencv.org/master/d9/df8/tutorial_root.html) for further information.

## Recommendation

OpenCV support both Python 2 and Python 3, it's recommended to install it via your package manager.

## Installation

#### Ubuntu 20.04
```sh
# Update list of available packages
sudo apt update

# Install opencv and dependencies
sudo apt install python3-numpy python3-opencv libopencv-dev

# Install gstreamer and plugins
sudo apt install python3-gst-1.0 gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-libav
```

### Companion
```sh
# Update list of available packages
sudo apt update

# Install opencv and dependencies
sudo apt install python-numpy python-opencv libopencv-dev

# Install gstreamer and plugins
sudo apt install python-gst-1.0 gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad gstreamer1.0-libav \
    gir1.2-gst-plugins-base-1.0 gir1.2-gstreamer-1.0
```

# Examples
Take a look in the [diagram of the software components](/developers/software-components.html) to see how the communication between all the modules work.

The video raw data goes to gstreamer that send it via udp (:5600) inside the companion board to the topside computer.

### Top side computer

To capture video stream with the python script and QGC at same time, it's necessary to modify [gstreamer options](http://192.168.2.2:2770/camera), changing `! udpsink host=192.168.2.1 port=5600` to `! multiudpsink clients=192.168.2.1:5600,192.168.2.1:4777` and add the new `port` parameter when calling `Video` (`video = Video(port=4777)`).

#### Receive and display stream
##### Python
```py
#!/usr/bin/env python
"""
BlueRov video capture class
"""

import cv2
import gi
import numpy as np

gi.require_version('Gst', '1.0')
from gi.repository import Gst


class Video():
    """BlueRov video capture class constructor

    Attributes:
        port (int): Video UDP port
        video_codec (string): Source h264 parser
        video_decode (string): Transform YUV (12bits) to BGR (24bits)
        video_pipe (object): GStreamer top-level pipeline
        video_sink (object): Gstreamer sink element
        video_sink_conf (string): Sink configuration
        video_source (string): Udp source ip and port
        latest_frame (np.ndarray): Latest retrieved video frame
    """

    def __init__(self, port=5600):
        """Summary

        Args:
            port (int, optional): UDP port
        """

        Gst.init(None)

        self.port = port
        self.latest_frame = self._new_frame = None

        # [Software component diagram](https://www.ardusub.com/software/components.html)
        # UDP video stream (:5600)
        self.video_source = 'udpsrc port={}'.format(self.port)
        # [Rasp raw image](http://picamera.readthedocs.io/en/release-0.7/recipes2.html#raw-image-capture-yuv-format)
        # Cam -> CSI-2 -> H264 Raw (YUV 4-4-4 (12bits) I420)
        self.video_codec = '! application/x-rtp, payload=96 ! rtph264depay ! h264parse ! avdec_h264'
        # Python don't have nibble, convert YUV nibbles (4-4-4) to OpenCV standard BGR bytes (8-8-8)
        self.video_decode = \
            '! decodebin ! videoconvert ! video/x-raw,format=(string)BGR ! videoconvert'
        # Create a sink to get data
        self.video_sink_conf = \
            '! appsink emit-signals=true sync=false max-buffers=2 drop=true'

        self.video_pipe = None
        self.video_sink = None

        self.run()

    def start_gst(self, config=None):
        """ Start gstreamer pipeline and sink
        Pipeline description list e.g:
            [
                'videotestsrc ! decodebin', \
                '! videoconvert ! video/x-raw,format=(string)BGR ! videoconvert',
                '! appsink'
            ]

        Args:
            config (list, optional): Gstreamer pileline description list
        """

        if not config:
            config = \
                [
                    'videotestsrc ! decodebin',
                    '! videoconvert ! video/x-raw,format=(string)BGR ! videoconvert',
                    '! appsink'
                ]

        command = ' '.join(config)
        self.video_pipe = Gst.parse_launch(command)
        self.video_pipe.set_state(Gst.State.PLAYING)
        self.video_sink = self.video_pipe.get_by_name('appsink0')

    @staticmethod
    def gst_to_opencv(sample):
        """Transform byte array into np array

        Args:
            sample (TYPE): Description

        Returns:
            TYPE: Description
        """
        buf = sample.get_buffer()
        caps_structure = sample.get_caps().get_structure(0)
        array = np.ndarray(
            (
                caps_structure.get_value('height'),
                caps_structure.get_value('width'),
                3
            ),
            buffer=buf.extract_dup(0, buf.get_size()), dtype=np.uint8)
        return array

    def frame(self):
        """ Get Frame

        Returns:
            np.ndarray: latest retrieved image frame
        """
        if self.frame_available:
            self.latest_frame = self._new_frame
            # reset to indicate latest frame has been 'consumed'
            self._new_frame = None
        return self.latest_frame

    def frame_available(self):
        """Check if a new frame is available

        Returns:
            bool: true if a new frame is available
        """
        return self._new_frame is not None

    def run(self):
        """ Get frame to update _new_frame
        """

        self.start_gst(
            [
                self.video_source,
                self.video_codec,
                self.video_decode,
                self.video_sink_conf
            ])

        self.video_sink.connect('new-sample', self.callback)

    def callback(self, sink):
        sample = sink.emit('pull-sample')
        self._new_frame = self.gst_to_opencv(sample)

        return Gst.FlowReturn.OK


if __name__ == '__main__':
    # Create the video object
    # Add port= if is necessary to use a different one
    video = Video()
    
    print('Initialising stream...')
    waited = 0
    while not video.frame_available():
        waited += 1
        print('\r  Frame not available (x{})'.format(waited), end='')
        cv2.waitKey(30)
    print('\nSuccess!\nStarting streaming - press "q" to quit.')

    while True:
        # Wait for the next frame to become available
        if video.frame_available():
            # Only retrieve and display a frame if it's new
            frame = video.frame()
            cv2.imshow('frame', frame)
        # Allow frame to display, and check if user wants to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
```

##### C++
```cpp
/**
 * BlueRov video capture example
 * Based on:
 * https://stackoverflow.com/questions/10403588/adding-opencv-processing-to-gstreamer-application
 * Should be compiled with: g++ -g main.cpp `pkg-config --cflags --libs opencv4 gstreamer-1.0 gstreamer-app-1.0` -o example && ./example
 */
#include <atomic>
#include <cstdio>
#include <gst/gst.h>
#include <gst/app/app.h>
#include <opencv2/opencv.hpp>

// Share frame between main loop and gstreamer callback
std::atomic<cv::Mat*> atomicFrame;

/**
 * @brief Check preroll to get a new frame using callback
 *  https://gstreamer.freedesktop.org/documentation/design/preroll.html
 * @return GstFlowReturn
 */
GstFlowReturn new_preroll(GstAppSink* /*appsink*/, gpointer /*data*/)
{
    return GST_FLOW_OK;
}

/**
 * @brief This is a callback that get a new frame when a preroll exist
 *
 * @param appsink
 * @return GstFlowReturn
 */
GstFlowReturn new_sample(GstAppSink *appsink, gpointer /*data*/)
{
    static int framecount = 0;

    // Get caps and frame
    GstSample *sample = gst_app_sink_pull_sample(appsink);
    GstCaps *caps = gst_sample_get_caps(sample);
    GstBuffer *buffer = gst_sample_get_buffer(sample);
    GstStructure *structure = gst_caps_get_structure(caps, 0);
    const int width = g_value_get_int(gst_structure_get_value(structure, "width"));
    const int height = g_value_get_int(gst_structure_get_value(structure, "height"));

    // Print dot every 30 frames
    if(!(framecount%30)) {
        g_print(".");
    }

    // Show caps on first frame
    if(!framecount) {
        g_print("caps: %s\n", gst_caps_to_string(caps));
    }
    framecount++;

    // Get frame data
    GstMapInfo map;
    gst_buffer_map(buffer, &map, GST_MAP_READ);

    // Convert gstreamer data to OpenCV Mat
    cv::Mat* prevFrame;
    prevFrame = atomicFrame.exchange(new cv::Mat(cv::Size(width, height), CV_8UC3, (char*)map.data, cv::Mat::AUTO_STEP));
    if(prevFrame) {
        delete prevFrame;
    }

    gst_buffer_unmap(buffer, &map);
    gst_sample_unref(sample);

    return GST_FLOW_OK;
}

/**
 * @brief Bus callback
 *  Print important messages
 *
 * @param bus
 * @param message
 * @param data
 * @return gboolean
 */
static gboolean my_bus_callback(GstBus *bus, GstMessage *message, gpointer data)
{
    // Debug message
    //g_print("Got %s message\n", GST_MESSAGE_TYPE_NAME(message));
    switch(GST_MESSAGE_TYPE(message)) {
        case GST_MESSAGE_ERROR: {
            GError *err;
            gchar *debug;

            gst_message_parse_error(message, &err, &debug);
            g_print("Error: %s\n", err->message);
            g_error_free(err);
            g_free(debug);
            break;
        }
        case GST_MESSAGE_EOS:
            /* end-of-stream */
            break;
        default:
            /* unhandled message */
            break;
    }
    /* we want to be notified again the next time there is a message
     * on the bus, so returning TRUE (FALSE means we want to stop watching
     * for messages on the bus and our callback should not be called again)
     */
    return true;
}

int main(int argc, char *argv[]) {
    gst_init(&argc, &argv);

    gchar *descr = g_strdup(
        "udpsrc port=5600 "
        "! application/x-rtp, payload=96 ! rtph264depay ! h264parse ! avdec_h264 "
        "! videoconvert ! video/x-raw,format=(string)BGR ! videoconvert "
        "! appsink name=sink emit-signals=true sync=false max-buffers=1 drop=true"
    );

    // Check pipeline
    GError *error = nullptr;
    GstElement *pipeline = gst_parse_launch(descr, &error);

    if(error) {
        g_print("could not construct pipeline: %s\n", error->message);
        g_error_free(error);
        exit(-1);
    }

    // Get sink
    GstElement *sink = gst_bin_get_by_name(GST_BIN(pipeline), "sink");

    /**
     * @brief Get sink signals and check for a preroll
     *  If preroll exists, we do have a new frame
     */
    gst_app_sink_set_emit_signals((GstAppSink*)sink, true);
    gst_app_sink_set_drop((GstAppSink*)sink, true);
    gst_app_sink_set_max_buffers((GstAppSink*)sink, 1);
    GstAppSinkCallbacks callbacks = { nullptr, new_preroll, new_sample };
    gst_app_sink_set_callbacks(GST_APP_SINK(sink), &callbacks, nullptr, nullptr);

    // Declare bus
    GstBus *bus;
    bus = gst_pipeline_get_bus(GST_PIPELINE(pipeline));
    gst_bus_add_watch(bus, my_bus_callback, nullptr);
    gst_object_unref(bus);

    gst_element_set_state(GST_ELEMENT(pipeline), GST_STATE_PLAYING);

    // Main loop
    while(1) {
        g_main_iteration(false);

        const cv::Mat* frame = atomicFrame.exchange(nullptr);
        if(frame) {
            cv::imshow("Frame", *frame);
            cv::waitKey(30);
        }
    }

    gst_element_set_state(GST_ELEMENT(pipeline), GST_STATE_NULL);
    gst_object_unref(GST_OBJECT(pipeline));
    return 0;
}
```

### Companion

Before running any program in the companion board, keep in mind that the hardware of a SBC may not run with high performance or with real-time requirements.

It's possible to get some frames while the stream is in progress, however this can result in some delays in the top side computer.

#### Get a frame and save it

```py
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Capture frame-by-frame
ret, frame = cap.read()

# Save the frame
cv2.imwrite('frame.png', frame)

# When everything done, release the capture
cap.release()
```

#### Get a frame from gstreamer and save it
Update the gstreamer options to enable multiudpsink like in **Top side computer**, but changing the ip
of the second output to 192.168.2.2.

```py
# Add or use the Video class here

if __name__ == '__main__':
    # Create the video object
    # Add port= if is necessary to use a different one
    video = Video(port=4777)

    # Wait for the next frame
    while not video.frame_available():
        continue

    frame = video.frame()
    # Save the frame
    cv2.imwrite('frame.png', frame)
```
