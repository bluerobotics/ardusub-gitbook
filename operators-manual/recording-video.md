# Recording Video

QGroundControl supports recording the raw video stream. If you would like to record your video with the QGroundControl application elements displayed, you should use a separate screen recording software. To record video with QGroundControl, you must first select a path for saving video files. Choose a path in the *General* tab of the *Application Settings* page.

<img src="/images/qgc/qgc-recording-video.png" class="img-responsive img-center" style="max-height:400px;">

To record video in QGroundControl, click the red circle in the lower right-hand corner of the video window. The red video recording icon is a square when QGroundControl is currently recording the video stream to a file. When QGroundControl is not recording video, the red video recording icon is a circle. Each time the red circle is clicked to start recording, a new video file is created. The videos are saved in Matroska format (.mkv). Matroska was chosen because it is robust when saving raw streams, and it is harder to corrupt the file. If you would like to use your video in another format, you must convert the .mkv file with a transcoding program like VLC.

<img src="/images/qgc/video-record-button.png" class="img-responsive img-center" style="max-height:400px;" align="middle">
<img src="/images/qgc/qgc-save-location.png" class="img-responsive img-center" style="max-height:400px;" align="middle">
