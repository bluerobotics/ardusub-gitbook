# Other Features

## Video Overlay

When QGroundControl is recording a video stream to file, it will also export a subtitle file with telemetry data that can be used to overlay the telemetry on the video during playback. Whichever telemetry values are selected for display in the telemetry values widget will also be exported to the overlay. The overlay values are updated at 1Hz.

<img src="/images/reference/reference-qgc-overlay-widget.png" class="img-responsive img-center" style="max-height:600px;">

The selected values are laid out in three columns to optimize the screen utilization.

<img src="/images/reference/reference-qgc-overlay-capture.png" class="img-responsive img-center" style="max-height:600px;">

### Playing a File

The overlay can be used with any player that [supports the SubStation Alpha](https://en.wikipedia.org/wiki/SubStation_Alpha#Players_and_renderers) subtitle format. Most players will open both files together when you try to play the video. They need to be in the same folder and with the same name, which is how they are created by QGC.

### Combining the Video and Subtitle Files (VLC)

#### Playing

1. Download and install the [VLC media player](https://www.videolan.org/vlc/index.html) for your operating system.
2. From the toolbar select Media -> Open Multiple files.
3. In the "File Selection", Add the desired video file from the default video save path (QGroundControl\Video\).
4. Check the box for "Use a subtitle file".
5. Click on "Browse..." and select the corresponding ".ass" file. The timestamp will be the same as the video file.
6. Select "Play" from the dropdown.

#### Converting

1. Download and install the [VLC media player](https://www.videolan.org/vlc/index.html) for your operating system.
2. From the toolbar select Media -> Open Multiple files.
3. In the "File Selection", Add the desired video file from the default video save path (QGroundControl\Video\).
4. Check the box for "Use a subtitle file".
5. Click on "Browse..." and select the corresponding ".ass" file. The timestamp will be the same as the video file.
6. Select "Convert" from the dropdown.
7. Select "Video - H.265 + MP3 (MP4)" for the profile.
8. Click on the wrench icon to the right of the profile to configure it.
9. In the Subtitles tab, check the box for "Subtitles" and "Overlay subtitles on the video". Click Save.
10. Choose a desintation file location and name.
11. Click Start.

