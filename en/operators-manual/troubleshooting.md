# Troubleshooting

This page shares issues that users have run into and how they were resolved. Hopefully this will help to solves issues for others.

## Vehicle Control

**Vehicle flips itself over**

Check that the motor directions are [configured correctly](/initial-setup/#configuring-motor-directions). Also check that the motors are connected to the correct motor outputs on the flight controller, according to the [supported frame diagrams](/introduction/#supported-frames).

**Vehicle turns or moves even when not controlled to do so.**

Please check RCx_TRIM parameters to make sure that all trims are set to 1500, with the exception of RC3_TRIM, which should be set to 1100.

**Motors spin as soon as the vehicle is armed.**

Make sure that the vehicle is in *Manual* mode.

The flight controller attempts to stabilize the vehicle's attitude so that it is perfectly level. If the vehicle's attitude is off from level, even a fraction of a degree, the flight controller will spin the motors in an attempt to correct the error. If the vehicle is sitting on land, the error will not change, and the flight controller will spin the motors faster and faster as it tries harder and harder to correct the error. Testing the vehicle on land should be done in MANUAL mode, which just passes pilot inputs to the motors with no stabilization.

## No Telemetry (No Pixhawk Connection)

Install the latest [stable version](http://qgroundcontrol.com/downloads/) of QGroundControl.

Make sure the companion computer is powered with a supply that is capable of delivering at least 2A.

Make sure that the QGroundControl is configured to automatically connect to UDP links. Click on the 'Q' icon in the upper left to view the Application Settings. Click on the 'General Settings' tab. In the options for 'Autoconnect to:', make sure the UDP option is checked.

<img src="/images/qgc-autoconnect-settings.png" class="img-responsive img-center" style="max-height:400px;">

#### Check Your Network

You should be able to ping the companion computer from the surface computer. On the surface computer's command line enter:

	ping 192.168.2.2

If you do not get a ping response, then something is wrong with the network communication between the surface computer and the companion computer.

Check your network settings. The surface computer should have a static IP address of 192.168.2.1. You may have to adjust your firewall settings to allow QGrouncControl access to the network. 

Check the activity lights on the Raspberry Pi ethernet Jack. The lights should be on or blinking.

If the lights are not on, make sure that you are using a network patch cable, not a crossover cable. Look closely at the color of the wires inside connectors on either end of the network cable, the order of the wires should be the same on both ends of the cable.

#### Check MAVProxy

If your network is configured correctly, but you still have no telemetry, we need to make sure that MAVProxy is running on the companion computer and that the Pixhawk and the Raspberry Pi are communicating. Please note that the Pixhawk must be connected to the companion computer before the companion computer is powered on. The MAVProxy process is started at boot, and if the Pixhawk is not connected at this point the MAVProxy process will exit until the companion computer is rebooted.

Check that mavproxy is running on the pi. Log into the Pi via ssh or PuTTY, and type

	sudo screen -r mavproxy

Mavproxy and the Pixhawk are working correctly if the output contains something like this:

	APM: ArduSub V3.4 (422c10cf)
	APM: PX4: 96a4c296 NuttX: 580f5354
	APM: Frame: ROV_VECTORED_FRAME
	APM: PX4v2 0048003B 3135510C 35333436
	Received 608 parameters
	Saved 608 parameters to mav.parm

To return to the command line and keep the mavproxy process running, hit control+a then type 'd' (to detach).

If you do not see the above lines in the output, or if you see something like this:

	There is no screen to be resumed matching mavproxy.

then there was an error starting MAVProxy. You can restart the MAVProxy process by typing:

	~/companion/RPI2/Raspbian/start_mavproxy_telem_splitter.sh

Make sure that the Pixhawk is plugged into the companion computer (Raspberry Pi) with a micro USB cable. Make sure that the USB cable has data lines, some USB cables only provide power and will not allow communication. You can connect the Pixhawk to the surface computer directly with the USB cable to verify that the USB cable works.

If you still do not have telemetry after all of these steps, please reboot the surface computer and the companion computer, and try again. If it is still not working after rebooting, please leave a comment on discuss.bluerobotics.com.

## No Video

If you do not have telemetry, please troubleshoot that first according to the above instructions.

If you have telemetry, but no video, make sure the video settings are correct in QGroundControl. The video settings are found in the General tab of the Application Settings (Q icon) view. The video source should be set to UDP video, and the port should be 5600. These are the default settings.

<img src="/images/qgc-video-settings.png" class="img-responsive img-center" style="max-height:400px;">

If the video settings are correct, and there is no video stream, the most likely cause is a faulty physical connection with the camera ribbon cable. Disconnect power to the ROV/Raspberry Pi and reseat the ribbon cable on both ends, ensuring that the contact side of the cable is oriented correctly. The contacts should face towards the board on the camera module, and towards the HDMI connector on the Raspberry Pi.

If you have checked all of the above and still don't have a video stream, you can check the video streaming process for errors. Log into the Raspberry Pi via SSH or PuTTY and enter the following command into the Raspberry Pi command line:

	sudo screen -r video

If the camera is working and the video stream is running, the output should end in something like this:

	Pipeline is PREROLLED ...
	Setting pipeline to PLAYING ...
	New clock: GstSystemClock

To return to the command line and keep the streaming process running, hit control+a then type 'd' (to detach).

If the video stream isn't running the output of the `screen` command will be:

	There is no screen to be resumed matching video.

You can relaunch the video streaming process by entering:

	~/companion/RPI2/Raspbian/start_video.sh

If the output of this command contains something like this:

	mmal: Failed to create camera component

Then the camera isn't working. Double check the camera ribbon cable, and try running `sudo rpi-update`.

## Miscellaneous

### Camera does not tilt

The output servo rail on the Pixhawk requires a separate 5V power supply. The power module and USB power inputs on the Pixhawk will not power the servo rail. Make sure you have a 5V input on the servo rail via an ESC BEC or standalone BEC.

Check that input/output channels are [configured for camera tilt](/initial-setup/#camera-tilt-setup-if-used).

Check that joystick buttons [have been assigned](/initial-setup/#button-setup) to camera tilt functions.

### "No io thread heartbeat" message constantly appears.

This message indicates that the APM io thread has stopped running. The most likely cause is a corrupted filesystem on the micro SD card. Remove the card from the pixhawk, and format it as FAT32. If the error persists, you will need to replace the SD card, or disable dataflash log files by setting the LOG_BACKEND_TYPE parameter to None (0).

# Issue Reporting

We're always trying to make our documentation, instructions, software, and user experience better. If you're having an issue with anything, please report it so that we can address it as soon as possible! Here's where to do that depending on what's wrong:

- **ArduSub Issues:** For anything related to the ArduSub software that runs on the Pixhawk and controls the ROV, reports issues on the [ArduSub Github Issues Page](https://github.com/bluerobotics/ardusub/issues). If you're unsure where your issue should be posted, you can report it here.
- **QGroundControl Issues:** For anything related to the QGroundControl software, joystick setup, video streaming, etc., please report an issue on the [QGroundControl Github Issues Page](https://github.com/mavlink/qgroundcontrol/issues).
- **Documentation:** For anything related to the documentation and instructions here, please report an issue on the [ArduSub Documentation Github Issues Page](https://github.com/bluerobotics/ardusub-docs/issues).

<p style="font-size:10px; text-align:center">
Sponsored by <a href="http://www.bluerobotics.com/">Blue Robotics</a>. Code released under the <a href="https://github.com/bluerobotics/ardusub/blob/master/COPYING.txt">GPLv3 License</a>. Documentation released under the <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC-NC-SA 4.0</a>.<br />
<a href="https://github.com/bluerobotics/ardusub-docs/issues/">Submit a Documentation GitHub Issue here</a> to report any errors, suggestions, or missing information in this documentation.<br />
<a href="https://github.com/bluerobotics/ardusub/issues/">Submit an ArduSub GitHub Issue here</a> to report issues with the ArduSub software.
</p>
