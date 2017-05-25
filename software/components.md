# Software Components

There are three major software components involved in the operation of ArduSub:

- [ArduSub](https://github.com/ArduPilot/ardupilot): ArduSub is the autopilot software responsible for processing pilot input and controlling the ROV. ArduSub is the 'brains' of the ROV.
- [QGroundControl](https://github.com/mavlink/qgroundcontrol): QGroundControl is the user interface for operating the ROV.
- [Companion](https://github.com/bluerobotics/companion): The Raspberry Pi *Companion Computer* runs software that relays communications between the autopilot and QGroundControl via Ethernet communications. The Companion software also streams HD video to QGroundControl.

Here is a typical diagram of the software components and their interactions:

<img src="/images/software-components.jpg" class="img-responsive img-center" style="max-height:600px;">

<p style="font-size:10px; text-align:center">
Sponsored by <a href="http://www.bluerobotics.com/">Blue Robotics</a>. Code released under the <a href="https://github.com/bluerobotics/ardusub/blob/master/COPYING.txt">GPLv3 License</a>. Documentation released under the <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC-NC-SA 4.0</a>.<br />
<a href="https://github.com/bluerobotics/ardusub-docs/issues/">Submit a Documentation GitHub Issue here</a> to report any errors, suggestions, or missing information in this documentation.<br />
<a href="https://github.com/bluerobotics/ardusub/issues/">Submit an ArduSub GitHub Issue here</a> to report issues with the ArduSub software.
</p>
