# Other Features

## Video Overlay

When QGroundControl is recording a video stream to file, it will also export a subtitle file with telemetry data that can be used to overlay the telemetry on the video during playback. Whichever telemetry values are selected for display in the telemetry values widget will also be exported to the overlay. The overlay values are updated at 1Hz.

<img src="/images/reference/reference-qgc-overlay-widget.png" class="img-responsive img-center" style="max-height:600px;">

The selected values are laid out in three columns to optimize the screen utilization.

<img src="/images/reference/reference-qgc-overlay-capture.png" class="img-responsive img-center" style="max-height:600px;">

### Playing a File

The overlay can be used with any player that supports the SubStation Alpha subtitle format. Most players will open both files together when you try to play the video. They need to be in the same folder and with the same name, which is how they are created by QGC.
