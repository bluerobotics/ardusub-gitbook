> **Note** The information in this guide applies to ArduSub V3.5 and up. If you are running an older version, you should update.

## What is ArduSub?

The *ArduSub* project is a fully-featured, open-source controller for remotely operated underwater vehicles (ROVs) and autonomous underwater vehicles (AUVs). Based on the popular *ArduCopter* code, the *ArduSub* code has extensive capabilities out of the box including feedback stability control, depth and heading hold, and autonomous position control if provided with position feedback.

*ArduSub* is designed to be safe, feature-rich, open-ended, and easy to use even for novice users.

## ArduSub in Use

These videos show ArduSub in use on the Blue Robotics BlueROV1 and BlueROV2. Keep in mind that *ArduSub* can be used on many different ROV designs from unique DIY configurations to professional vehicles.

<div class="row">
    <iframe width="300" height="225" src="https://www.youtube.com/embed/iK9AmuqVN4I" frameborder="0" allowfullscreen></iframe>
    <iframe width="300" height="225" src="https://www.youtube.com/embed/IQBVRbQAQto" frameborder="0" allowfullscreen></iframe>
</div>

<div class="row">
    <iframe width="300" height="225" src="https://www.youtube.com/embed/BV91zgzEFHs" frameborder="0" allowfullscreen></iframe>
    <iframe width="300" height="225" src="https://www.youtube.com/embed/qVMpD-v-dfY" frameborder="0" allowfullscreen></iframe>
</div>

<div class="row">
        <iframe width="300" height="225" src="https://www.youtube.com/embed/hNuHMLZZWbw" frameborder="0" allowfullscreen></iframe>
        <!--<iframe width="300" height="225" src="https://www.youtube.com/embed/qVMpD-v-dfY" frameborder="0" allowfullscreen></iframe>-->
</div>

## System Components

- A PixHawk or other DroneCode-compatible autopilot loaded with the latest version of the [ArduSub firmware](/firmware/).
- [QGroundControl software](http://qgroundcontrol.org) for setup, configuration, and operation of the vehicle.
- A [suitable ROV or AUV](http://bluerobotics.com) for use with the software
- Many other useful additions: depth sensors, tether communications, cameras, and other sensors and actuators



<p style="font-size:10px; text-align:center">
Sponsored by <a href="http://www.bluerobotics.com/">Blue Robotics</a>. Code released under the <a href="https://github.com/bluerobotics/ardusub/blob/master/COPYING.txt">GPLv3 License</a>. Documentation released under the <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC-NC-SA 4.0</a>.
<a href="https://github.com/bluerobotics/ardusub-docs/issues/">Submit a Documentation GitHub Issue here</a> to report any errors, suggestions, or missing information in this documentation.<br />
<a href="https://github.com/bluerobotics/ardusub/issues/">Submit an ArduSub GitHub Issue here</a> to report issues with the ArduSub software.
</p>