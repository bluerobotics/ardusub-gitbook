---
layout: default
title: "Downloads"
permalink: /downloads/
nav:
- Downloads: downloads
---

# Downloads

## Firmware Files

Compiled firmware is now available and can be downloaded from [firmware.ardusub.com](http://firmware.ardusub.com). See here for [instructions on how to flash the Pixhawk](/initial-setup/#loading-firmware-on-pixhawk). Firmware is available for the following hardware:

#### Pixhawk (px4-v2)

**Stable Release:** <i class="fa fa-download" aria-hidden="true"></i> [ArduSub V3.4](http://firmware.ardusub.com/Sub/stable/v3.4/)

The stable release is the recommended download for most users.

**Current Beta:** <i class="fa fa-download" aria-hidden="true"></i> [ArduSub V3.5-rc1](http://firmware.us.ardupilot.org/Sub/beta/PX4/ArduSub-v2.px4)

The beta is for testing, and is not recommended for most users.

**Latest Build:** <i class="fa fa-download" aria-hidden="true"></i> [ArduSub V3.6-dev](http://firmware.us.ardupilot.org/Sub/latest/PX4/ArduSub-v2.px4)

This is the latest build of the developmental master branch. This build should only be used by developers and advanced users.

## Release History

**ArduSub V3.5-rc1** *(2017-04-17)* Download [ArduSub V3.5-rc1 here](http://firmware.us.ardupilot.org/Sub/beta/PX4/ArduSub-v2.px4)

Major changes:

- Merge with ardupilot project
- Implement autotest suite (autotest.ardupilot.org)
- Firmware available on firmware.ardupilot.org and through QGC dropdown

- All supported frames are included in one binary. Select your frame with the FRAME_CONFIG parameter
- Improved pilot control in depth hold mode. Now depth hold behaves like STABLIZE when pilot commands
  ascent/descent, rather than setting desired climb rate.
- Implemented arming checks and the AP_Arming libraries
- Added pilot input failsafe requiring MANUAL_CONTROL or RC_CHANNELS_OVERRRIDE messages to be received
  at regular intervals. This addresses issue of joystick being disconnected while GCS connection remains
  unbroken.
- Add failsafe for depth sensor malfunction, vehicle will automatically enter MANUAL mode when
  depth sensor malfunctions.
- Drastically reduced latency between IMU updates and motor output (Thanks Randy and Tridge!)
- RC/Servo Channel library and parameters split
- Allow MS5837 pressure sensor on boards other than pixhawk, use GND_EXT_BUS parameter to select
  I2C bus to look for sensor on. -1 = Disabled; default to 1, which is Pixhawk external I2C bus
- Rework parameters, unused or irrelevant parameters have been removed

Other changes:

- No more ch5 mode selection, modes are configured by assigning modes directly to
  joystick button functions. Forward/lateral inputs are now on channel 5/6 (was 6/7)
- Default FS_LEAK_ENABLE to FS_LEAK_WARN_ONLY (was disabled)
- Added support for BlueRobotics Celsius temperature sensor (TSYS01). Temperature is output on
  SCALED_PRESSURE3 message as a workaround.
- No longer report battery percent remaining, as the measurement algorithm is flawed and does not work
  on partially charged batteries.
- Implement auto circle mode (loiter turns)
- Implement circle mode
- Implement guided mode
- Implement auto surface mode (NAV_CMD_LAND)
- Implement spline waypoints
- Implement crash check failsafe
- Implement ekf failsafe
- Implement battery failsafe
- Implement relay joystick button functions
- Add joystick button functions to control servos
- Add joystick button function to toggle between foward/lateral input and roll/pitch input
- Remove BASE_RESET and BASE_PRESS baro parameters. Barometer reset is now done via mavlink cmd.
- Implement parameter reset to defaults via mavlink cmd.
- Fixed bug with camera tilt smoothing conflicting with RC_OVERRIDE messages
- Fix bug preventing LOG_FILE_DSRMROT parameter from working correctly
- Detect external pressure sensor according to BARO_TYPE == BARO_TYPE_WATER rather than hard-coding baro instance index
- Use default StorageManager layout instead of Copter layout
- Add support for AHRS View
- Remove experimental/deprecated VELHOLD and TRANSECT modes
- Some refactoring of code and files to improve readability
- Disable untested CAMERA object and parameters by default
- Only allow negative altitudes and ALT_FRAME_ABOVE_HOME for mission commands
- Remove lots of dead code left over from ArduCopter:

    - RC receiver
    - Landing
    - Unused/unsupported modes
    - Remove channel 5 mode logic
    - Remove aux switches
    - Throttle zero flag
    - Auto trim
    - Unsupported mavlink messages
    - Compassmot calibration
    - Simple mode
    - Ch6 tuning
    - Esc calibration
    - CLI
    - Motor test
    - Helicopter references
    - HIL_MODE
    - Various unused flags, members and methods

**ArduSub V3.4** *(2016-12-30)* Download [ArduSub-3.4 here](http://firmware.ardusub.com/Sub/stable/v3.4/)

ArduSub v3.4 is the first official stable release of ArduSub. After nearly a year of steady development, testing, and improvement, ArduSub has become one of the most capable ROV control systems available.

**Important Note for ArduSub-3.4:** Many unused and inapplicable parameters that ArduSub inherited from ArduCopter have been removed. As a consequence, after upgrading to V3.4 and later, all of the parameters will be erased, and the default parameters will be loaded. **You should save your parameters before flashing this firmware.** After upgrading the firmware, you can load your saved parameter file through QGroundControl. When loading your old parameter file through QGroundControl, you will see many errors about parameters that have been removed, this is okay. After you load your parameter file, you need to change the SYSID_SW_MREV parameter to 1 before rebooting in order to prevent the default parameters from being reloaded. This procedure will only have to be done when upgrading from firmware version 3.4-dev. Subsequent releases will keep the same parameter format, so this will only have to be done once. If you are using a BlueROV2, it is recommended that you load the [Standard ArduSub Parameters](http://firmware.ardusub.com/parameters/latest/bluerov2.params) after upgrading. The upgrade process is demonstrated in the video below.

<div align="center">
	<iframe width="560" height="315" src="https://www.youtube.com/embed/siJoON6hgq4" frameborder="0" allowfullscreen></iframe>
</div>

# Images

A fully set up image for the Raspberry Pi is available here. This image is used to set up the Raspberry Pi 3 computer as a *companion computer* for the Pixhawk autopilot. See here for [instructions on how to flash the image to the SD card](/raspi-setup/#easy-setup-with-disk-image).

<i class="fa fa-download" aria-hidden="true"></i> [Latest Ardusub-Raspbian Image](http://img.ardusub.com/2017-01-12-ardusub-raspbian.img.zip) *(1.6 GB, Updated 2017-01-12)*

<p style="font-size:10px; text-align:center">
Sponsored by <a href="http://www.bluerobotics.com/">Blue Robotics</a>. Code released under the <a href="https://github.com/bluerobotics/ardusub/blob/master/COPYING.txt">GPLv3 License</a>. Documentation released under the <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC-NC-SA 4.0</a>.<br />
<a href="https://github.com/bluerobotics/ardusub-docs/issues/">Submit a Documentation GitHub Issue here</a> to report any errors, suggestions, or missing information in this documentation.<br />
<a href="https://github.com/bluerobotics/ardusub/issues/">Submit an ArduSub GitHub Issue here</a> to report issues with the ArduSub software.
</p>
