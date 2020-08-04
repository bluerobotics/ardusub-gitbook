# Safety Setup Page (Failsafes)

The Safety Setup page allows you to configure the failsafe settings.

<img src="/images/reference/reference-ardusub-safety.png" class="img-responsive img-center" style="max-height:600px;">

## Failsafe Triggers

Individual failsafes are triggered when a certain set of conditions are met. Failsafe actions can be configured individually for each failsafe trigger. When a failsafe is triggered, the cooresponding failsafe action is executed. Some failsafes have additional settings that allow you to adjust the trigger conditions, such as maximum acceptable pressure or temperature.

Failsafe actions are only executed once when a failsafe is triggered. The vehicle can be armed during an active failsafe condition if the arming checks are passing. The flight mode can be changed as long as the failsafe conditions do not prevent it. If an active failsafe is cleared, the failsafe action will be executed again if the failsafe re-triggers.

### GCS (Ground Control Station) Heartbeat

Triggered when a HEARTBEAT from the ground control station matching SYSID_MYGCS hasn't been received for more than 2.5 seconds. The failsafe is cleared immediately when a HEARTBEAT is received.

Note If the system id of the companion computer is a match with SYSID_MYGCS , then the heartebeats originating from a process (ie MAVProxy) on the companion computer may prevent this failsafe from triggering when expected.

### Leak

Triggered immediately when a configured Leak Detector detects a leak. The failsafe is cleared if the leak detector reports no leaks for two seconds.

### Battery

Triggered when the battery voltage drops below the voltage specified by the FS_BATT_VOLTAGE parameter, or if the remaining capacity drops below the capacity specified by the FS_BATT_MAH parameter.

### EKF

Triggered when the EKF compass or velocity variances exceed the threshold set by the FS_EKF_THRESH parameter.

### Pilot Input

Triggered when pilot manual control input has not been received since the amount of time specified by the FS_PILOT_TIMEOUT parameter.

### Internal Temperature

This is triggered when the internal temperature of the water tight enclosure (WTE) exceeds the threshold set by the FS_TEMP_MAX parameter. The failsafe is cleared immediately when the internal temperature is less than the threshold value.

### Internal Pressure

This is triggered when the internal pressure of the water tight enclosure (WTE) exceeds the threshold set by the FS_PRESS_MAX parameter for two seconds. The failsafe is cleared immediately when the internal pressure is less than the threshold value.

## Failsafe Actions

### Disabled

The failsafe is disabled, and nothing (not even event logging) will happen.

### Warn Only

A message will be sent to the ground control station indicating the failsafe conditions have been met. The warning is sent via STATUSTEXT messages, there is no mechanism to immediately re-send the message in the case that it was not received by the ground control station. The warning is sent repeatedly at 20~30 second intervals as long as the failsafe conditions are met.

These warnings are also sent if the failsafe action is set to anything other than Disabled.

### Disarm

If the vehicle is armed, the vehicle will disarm immediately when the failsafe conditions are met. The vehicle can be re-armed after the failsafe triggers, even while the failsafe conditions are met, as long as the arming checks are passing. If the failsafe clears due to resolved conditions, the vehicle will disarm again if the failsafe is re-triggered.

### Enter Position or Depth Hold

If the vehicle is armed, the vehicle will enter **Position Hold** mode, or **Depth Hold** mode, if positioning is not possible.

### Enter Surface Mode

If the vehicle is armed, the vehicle will enter Surface flight mode. The flight mode can be changed by the pilot, and the vehicle may be disarmed at any point.

## Arming Checks

This panel sets which Pre-ARM Safety Checks are enabled.

Arming checks are enabled and disabled individually. This is a list of arming checks that may be enabled. Arming checks are performed each time there is an attempt to arm the vehicle.

### All

All of the arming checks are performed.

### Barometer

Fails if any of the *Barometers* detected at boot are unhealthy. *bug*

### Compass

Fails if the on board compass is enabled and any of the following are true:
- The compass is unhealthy
- The compass offsets have not been set and learning offsets is disabled
- The compass is currently calibrating
- The compass calibration requires a reboot
- The compass offsets are too large
- The current magnetic field vector length is too large
- Individual compasses have inconsistent measurements

### GPS lock

> **GPS** This feature requires an [under water positioning system](/introduction/hardware-options/additional-peripheral-devices/underwater-positioning.md). A GPS antenna will not work under water.

Fails if the home position is unset and the GPS is not reporting a 3D fix.

### INS

Fails if 
- Any of the gyros are unhealthy
- Any of the gyros have a poor calibration
- Any of the accelerometers are unhealthy
- Any of the accelerometers have a poor calibration
- The accelerometer calibration requires a reboot
- Individual accelerometers have inconsistent measurements
- Individual gyros have inconsistent measurements
- The AHRS is unhealthy

### Parameters

Does nothing! Not Implemented.

### RC

Fails if the configured RC input ranges are invalid.

### Board voltage

> **Info** This feature is not supported on all boards

Fails if the board voltage is below 4.3V or above 5.8V.

### Battery Level

Fails if the battery failsafe is active, of if a battery voltage is below the threshold configured by the *ARMING_MIN_VOLT* or *ARMING_MIN_VOLT2* parameters.

### Airspeed

> **Aerial** This setting does not apply to ArduSub. It <em>should</em> have no effect, and should be left at the default value. It will be removed in the future.

### Logging Available

Fails if there is no SD card inserted or if writing a log failed.

### Hardware Safety switch

Fails if the hardware safety switch is enabled and the hardware safety switch is not in the armed state. The hardware switch is optional, it can be cumbersome to access the electronics in order to arm the autopilot at the hardware level. This is normally diabled.

### GPS Configuration

Fails if any of the following is true:
- Any gps requires further configuration.
- Individual gps inputs are giving inconsistent readings.
- Blending of multiple gps inputs is unhealthy.
