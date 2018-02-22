# OpenCV

OpenCV (Open Source Computer Vision) is a library to help the development of computer vision software.
To perform any real-time image processing with the companion camera, we highly suggest OpenCV to do the job.

Take a look in the OpenCV [website](https://opencv.org/) and [tutorials](https://docs.opencv.org/master/d9/df8/tutorial_root.html) for further information.

## Recommendation

OpenCV support both Python 2 and Python 3, it's recommended to install it via your package manager.

## Installation

#### Ubuntu 16.04
```sh
# Update list of available packages
sudo apt update

# Install opencv and dependencies
sudo apt install python-numpy python-opencv libopencv-dev

# Install gstreamer and plugins
sudo apt install python-gst-1.0 gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-libav
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
Take a look in the [diagram of the software components](software/components.md) to see how the communication between all the modules work.

The video raw data goes to gstreamer that send it via udp (:5600) inside the companion board to the topside computer.

### Top side computer

To capture video stream with the python script and QGC at same time, it's necessary to modify [gstreamer options](http://192.168.2.2:2770/camera), changing `! udpsink host=192.168.2.1 port=5600` to `! multiudpsink clients=192.168.2.1:5600,192.168.2.1:4777` and add the new `port` parameter when calling `Video` (`video = Video(port=4777)`).

#### Receive and display stream
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
    """

    def __init__(self, port=5600):
        """Summary

        Args:
            port (int, optional): UDP port
        """

        Gst.init(None)

        self.port = port
        self._frame = None

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
        caps = sample.get_caps()
        array = np.ndarray(
            (
                caps.get_structure(0).get_value('height'),
                caps.get_structure(0).get_value('width'),
                3
            ),
            buffer=buf.extract_dup(0, buf.get_size()), dtype=np.uint8)
        return array

    def frame(self):
        """ Get Frame

        Returns:
            iterable: bool and image frame, cap.read() output
        """
        return self._frame

    def frame_available(self):
        """Check if frame is available

        Returns:
            bool: true if frame is available
        """
        return type(self._frame) != type(None)

    def run(self):
        """ Get frame to update _frame
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
        new_frame = self.gst_to_opencv(sample)
        self._frame = new_frame

        return Gst.FlowReturn.OK


if __name__ == '__main__':
    # Create the video object
    # Add port= if is necessary to use a different one
    video = Video()

    while True:
        # Wait for the next frame
        if not video.frame_available():
            continue

        frame = video.frame()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
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