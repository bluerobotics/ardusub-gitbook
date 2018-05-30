# Recording Video

QGroundControl supports recording the video stream directly to the receiving device. If you would like to record your video with the QGroundControl application elements displayed, you should use a separate screen recording software. The video is saved under the path selected in the *General* tab of the *Application Settings* page. The default path is User/Documents/QGroundControl.

<img src="/images/qgc/qgc-recording-video.png" class="img-responsive img-center" style="max-height:600px;">

To record video in QGroundControl, click the red circle in the lower right-hand corner of the video window. The red video recording icon is a square when QGroundControl is currently recording the video stream to a file. When QGroundControl is not recording video, the red video recording icon is a circle. Each time the red circle is clicked to start recording, a new video file is created. The videos are saved in Matroska format (.mkv) by default. Matroska was chosen because it is robust against corruption in case of errors. Other formats are supported and can be selected on the *General* tab of the *Application Settings* page. If you would like to use your video in another format, you must convert the .mkv file with a transcoding program like VLC.

<img src="/images/qgc/video-record-button.png" class="img-responsive img-center" style="max-height:400px;" align="middle">

<p style="font-size:10px; text-align:center">
Sponsored by <a href="http://www.bluerobotics.com/">Blue Robotics</a>. Code released under the <a href="https://github.com/bluerobotics/ardusub/blob/master/COPYING.txt">GPLv3 License</a>. Documentation released under the <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC-NC-SA 4.0</a>.<br />
<a href="https://github.com/bluerobotics/ardusub-docs/issues/">Submit a Documentation GitHub Issue here</a> to report any errors, suggestions, or missing information in this documentation.<br />
<a href="https://github.com/bluerobotics/ardusub/issues/">Submit an ArduSub GitHub Issue here</a> to report issues with the ArduSub software.
</p>