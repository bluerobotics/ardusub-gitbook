# Parameters

Parameters are the user configurable settings for the autopilot. They are stored on internal memory on the autopilot, and are loaded when the autopilot boots up. Most of the configuration in the *Vehicle Setup* page in QGroundControl takes place by changing parameter values on the autopilot behind the scenes. Some parameters require a reboot to take effect, but most do not.

## Saving and Loading

The entire set of parameters on the autopilot can be saved to a text file. Parameters can also be loaded from a text file, overwriting the current parameters on the autopilot. The parameter file reflects all of the settings that the user can adjust in the autopilot. This makes it a very useful tool for troubleshooting, and it is important to save and share a parameter file with the community if you need support with setting up or operating.

To save or load parameters using QGroundControl, go to the *Vehicle Setup Page*, and click the *Parameters* tab. Click the *Tools* dropdown menu in the upper right hand corner and select *Save to file* or *Load from file*.

#### Refreshing

Some of the parameters are dynamic and will change under certain circumstances or after different events. In order to reload the current parameter values on the autopilot click *Refresh*.

#### Resetting

The entire set of parameters can be erased and reset to the default values that are configured in the autopilot firmware by clicking *Reset all to defaults* (ArduSub V3.5+ only).

<img src="/images/configuring/save-parameters.png" class="img-responsive img-center" style="max-height:600px;">

## Parameter Files

These files have the recommended parameters for ArduSub, making it easy to setup and update parameters on your vehicle. These parameters will not adjust your accelerometer calibration, compass calibration, or motor directions, but will change joystick button setup, PID controller values, lights and other peripheral configurations, and all other parameters.

#### Parameters for ArduSub V3.4 on BlueROV2

<i class="fa fa-download" aria-hidden="true"></i> [Standard ArduSub Parameters](http://firmware.ardusub.com/parameters/latest/bluerov2.params)


# Failsafes

Individual failsafes are triggered when a certain set of conditions are met. Failsafe actions can be configured individually for each failsafe trigger. When a failsafe is triggered, the cooresponding failsafe action is executed. Some failsafes have additional settings that allow you to adjust the trigger conditions, such as maximum acceptable pressure or temperature.

Failsafe actions are only executed once when a failsafe is triggered. The vehicle can be armed during an active failsafe condition if the arming checks are passing. The flight mode can be changed as long as the failsafe conditions do not prevent it. If an active failsafe is cleared, the failsafe action will be executed again if the failsafe re-triggers.

## Triggers

### Leak

Triggered immediately when a configured *Leak Detector* detects a leak. The failsafe is cleared if the leak detector reports no leaks for two seconds.

### Internal Pressure

This is triggered when the internal pressure of the water tight enclosure (WTE) exceeds the threshold set by the *FS_PRESS_MAX* parameter for two seconds. The failsafe is cleared immediately when the internal pressure is less than the threshold value.

### Internal Temperature

This is triggered when the internal temperature of the water tight enclosure (WTE) exceeds the threshold set by the *FS_TEMP_MAX* parameter. The failsafe is cleared immediately when the internal temperature is less than the treshold value.

### Ground Control Station HEARTBEAT

Triggered when a HEARTBEAT from the ground control station matching *SYSID_MYGCS* hasn't been received for more than 2.5 seconds. The failsafe is cleared immediately when a HEARTBEAT is received.

*Note* If the system id of the companion computer is a match with *SYSID_MYGCS* , then the heartebeats originating from a process (ie MAVProxy) on the companion computer may prevent this failsafe from triggering when expected.

### Pilot Input (ArduSub 3.5+)

Triggered when pilot manual control input has not been received since the amount of time specified by the *FS_PILOT_TIMEOUT* parameter.

### Sensors (ArduSub 3.5+)

Triggered when a sensor failure prevents the current flight mode to proceed. This occurs if the depth sensor fails while in depth hold mode. The autopilot will switch into *MANUAL* mode when triggered. This failsafe is always enabled, and is not configurable.

### Battery (ArduSub 3.5+)

Triggered when the battery voltage drops below the voltage specified by the *FS_BATT_VOLTAGE* parameter, or if the remaining capacity drops below the capacity specified by the *FS_BATT_MAH* parameter.

### EKF (ArduSub 3.5+)

Triggered when the EKF compass or velocity variances exceed the threshold set by the *FS_EKF_THRESH* parameter.

### Crash (ArduSub 3.5+)

Triggered when the angle error exceeds 30 degrees for more than 2 seconds. This is never triggered in *Manual* or *Acro* flight modes.

## Actions

### Disabled

The failsafe is disabled, and nothing (not even event logging) will happen.

### Warn Only

A message will be sent to the ground control station indicating the failsafe conditions have been met. The warning is sent via STATUSTEXT messages, there is no mechanism to immediately re-send the message in the case that it was not received by the ground control station. The warning is sent repeatedly at 20~30 second intervals as long as the failsafe conditions are met.

These warnings are also sent if the failsafe action is set to anything other than *Disabled*.

### Disarm

If the vehicle is armed, the vehicle will disarm immediately when the failsafe conditions are met. The vehicle can be re-armed after the failsafe triggers, even while the failsafe conditions are met, as long as the arming checks are passing. If the failsafe clears due to resolved conditions, the vehicle will disarm again if the failsafe is re-triggered. 

### Surface

If the vehicle is armed, the vehicle will enter *Surface* flight mode. The flight mode can be changed by the pilot, and the vehicle may be disarmed at any point.

### Hold

If the vehicle is armed, the vehicle will enter *Position Hold* mode, or *Depth Hold* mode, if positioning is not possible.

<p style="font-size:10px; text-align:center">
Sponsored by <a href="http://www.bluerobotics.com/">Blue Robotics</a>. Code released under the <a href="https://github.com/bluerobotics/ardusub/blob/master/COPYING.txt">GPLv3 License</a>. Documentation released under the <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC-NC-SA 4.0</a>.<br />
<a href="https://github.com/bluerobotics/ardusub-docs/issues/">Submit a Documentation GitHub Issue here</a> to report any errors, suggestions, or missing information in this documentation.<br />
<a href="https://github.com/bluerobotics/ardusub/issues/">Submit an ArduSub GitHub Issue here</a> to report issues with the ArduSub software.
</p>
