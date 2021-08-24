# Software Components

There are three major software components involved in the operation of ArduSub:

- [ArduSub](https://github.com/ArduPilot/ardupilot): ArduSub is the autopilot software responsible for processing pilot input and controlling the ROV. ArduSub is the 'brains' of the ROV.
- [QGroundControl](https://github.com/mavlink/qgroundcontrol): QGroundControl is the user interface for operating the ROV.
- [Companion](https://github.com/bluerobotics/companion): The Raspberry Pi *Companion Computer* runs software that relays communications between the autopilot and QGroundControl via Ethernet communications. The Companion software also streams HD video to QGroundControl.

Here is a typical diagram of the software components and their interactions:

<iframe width="770" height="612" src="https://miro.com/app/live-embed/o9J_l8JeRj8=/?moveToViewport=-2715,-5,2902,2304&embedAutoplay=true" frameBorder="0" scrolling="no" allowFullScreen></iframe>

To use the above diagram, you can scroll to zoom, click and drag to pan, and double-click to focus onto an element. Some elements have a (square) link in their top right corner, which can be clicked to go to the relevant documentation/product page. Optional components are shown as faded/translucent.

<p style="font-size:10px; text-align:center">
Sponsored by <a href="http://www.bluerobotics.com/">Blue Robotics</a>. Code released under the <a href="https://github.com/bluerobotics/ardusub/blob/master/COPYING.txt">GPLv3 License</a>. Documentation released under the <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC-NC-SA 4.0</a>.<br />
<a href="https://github.com/bluerobotics/ardusub-gitbook/issues/">Submit a Documentation GitHub Issue here</a> to report any errors, suggestions, or missing information in this documentation.<br />
<a href="https://github.com/bluerobotics/ardusub/issues/">Submit an ArduSub GitHub Issue here</a> to report issues with the ArduSub software.
</p>
