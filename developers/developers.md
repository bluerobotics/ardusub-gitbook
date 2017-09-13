# Developers

## How to Get the Code

ArduSub is hosted and maintained on [github](https://github.com/ardupilot/ardupilot.git). You can clone the repository or download the source code as a zip file from [github](https://github.com/ardupilot/ardupilot.git).

	git clone https://github.com/ardupilot/ardupilot.git

## Compiling

- [Mac Instructions](http://dev.ardupilot.com/wiki/building-px4-with-make-on-mac/)
- [Linux Instructions](http://dev.ardupilot.com/wiki/building-px4-for-linux-with-make/)
- [Windows Instructions](http://dev.ardupilot.com/wiki/building-px4-with-make/)

To compile the ArduSub branch, first `cd ArduSub` to enter the directory and then use a command with the following format:

	make [board type]

For example, to build for the Pixhawk 1:

	make px4-v2

The available board types can be seen by entering `make` with no arguments.

## Uploading Locally

To upload the code to a PixHawk or similar controller, add `-upload` to the build command. For example:

	make px4-v2-upload

This only works with a direct USB connection to the Pixhawk.

## Uploading Remotely

With an Ethernet tether and companion computer, it is possible to flash the Pixhawk firmware through the companion computer - no need to directly access the Pixhawk.

#### Flashing From the Command Line

	ssh pi@192.168.2.2 "/home/pi/companion/tools/flash_px4.py --stdin" < ArduSub-v2.px4
	
#### Flashing Via Web Interface

	Navigate to [192.168.2.2:2770/system](http://192.168.2.2:2770/system) in your browser. Under the 'Pixhawk Firmware Update' section, click 'Browse' and select the firmware file (.px4) saved on your computer. Click 'Upload' and wait for the flashing process to complete.

## Running

The code begins running immediately once uploaded. For Linux-based autopilots, it must be launched or started with launch script. Please see the documentation for your respective autopilot.

## Making a Custom Configuration

One of the biggest additions to the ArduSub code is a six degree-of-freedom motor library that allows a wide variety of motor configurations to be set up easily. The motors libraries for each configuration are built on a set of higher-level motor classes as follows:

    AP_Motors
        |---- AP_MotorsMulticopter
                       |---- AP_MotorsMatrix
                                    |---- AP_Motors6DOF

To add a new motor configuration, you will need to add your custom motor setup to [AP_Motors6DOF.cpp](https://github.com/bluerobotics/ardusub/blob/master/libraries/AP_Motors/AP_Motors6DOF.cpp). Find the following line, and add your frame configuration there. The frame is configured at boot according to the FRAME_CONFIG parameter. You will need to change this parameter to CUSTOM to use your custom frame.

    case AS_MOTORS_CUSTOM_FRAME:
        // Put your custom motor setup here

The behavior of each motor will be defined by its assigned contributions to each of the 6 degrees of freedom in AP_Motors6DOF.cpp. You can use the other frame configurations as a reference guide to defining your own custom configuration. Here is the BlueROV1 frame configuration as an example:

| Motor # | Roll Factor | Pitch Factor | Yaw Factor | Throttle Factor | Forward Factor | Lateral Factor |
| ------- | ----------- | ------------ | ---------- | --------------- | -------------- | -------------- |
| 1       | 0           | 0            | -1.0       | 0               | 1.0            | 0              |
| 2       | 0           | 0            | 1.0        | 0               | 1.0            | 0              |
| 3       | -0.5        | 0.5          | 0          | 0.45            | 0              | 0              |
| 4       | 0.5         | 0.5          | 0          | 0.45            | 0              | 0              |
| 5       | 0           | -1.0         | 0          | 1.0             | 0              | 0              |
| 6       | -0.25       | 0            | 0          | 0               | 0              | 1.0            |

<img src="/images/bluerov-frame.png" class="img-responsive img-center" style="max-height:250px;">

<p style="font-size:10px; text-align:center">
Sponsored by <a href="http://www.bluerobotics.com/">Blue Robotics</a>. Code released under the <a href="https://github.com/bluerobotics/ardusub/blob/master/COPYING.txt">GPLv3 License</a>. Documentation released under the <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC-NC-SA 4.0</a>.<br />
<a href="https://github.com/bluerobotics/ardusub-docs/issues/">Submit a Documentation GitHub Issue here</a> to report any errors, suggestions, or missing information in this documentation.<br />
<a href="https://github.com/bluerobotics/ardusub/issues/">Submit an ArduSub GitHub Issue here</a> to report issues with the ArduSub software.
</p>
