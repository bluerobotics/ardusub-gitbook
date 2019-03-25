# Arming Checks

Arming checks are enabled and disabled individually. This is a list of arming checks that may be enabled. Arming checks are performed each time there is an attempt to arm the vehicle.

## All

All of the arming checks are performed.

## Barometer

Fails if any of the *Barometers* detected at boot are unhealthy. *bug*

## Compass

Fails if the on board compass is enabled and any of the following are true:
- The compass is unhealthy
- The compass offsets have not been set and learning offsets is disabled
- The compass is currently calibrating
- The compass calibration requires a reboot
- The compass offsets are too large
- The current magnetic field vector length is too large
- Individual compasses have inconsistent measurements

## GPS lock

> **GPS** This feature requires an [under water positioning system](http://www.bluerobotics.com/store/electronics/underwater-gps/aps-wl-11001/). A GPS antenna will not work under water.

Fails if the home position is unset and the GPS is not reporting a 3D fix.

## INS

Fails if 
- Any of the gyros are unhealthy
- Any of the gyros have a poor calibration
- Any of the accelerometers are unhealthy
- Any of the accelerometers have a poor calibration
- The accelerometer calibration requires a reboot
- Individual accelerometers have inconsistent measurements
- Individual gyros have inconsistent measurements
- The AHRS is unhealthy

## Parameters

Does nothing! Not Implemented.

## RC

Fails if the configured RC input ranges are invalid.

## Board voltage

> **Info** This feature is not supported on all boards

Fails if the board voltage is below 4.3V or above 5.8V.

## Battery Level

Fails if the battery failsafe is active, of if a battery voltage is below the threshold configured by the *ARMING_MIN_VOLT* or *ARMING_MIN_VOLT2* parameters.

## Airspeed

> **Aerial** This setting does not apply to ArduSub. It <em>should</em> have no effect, and should be left at the default value. It will be removed in the future.

## Logging Available

Fails if there is no sd card inserted or if writing a log failed.

## Hardware safety switch

Fails if the hardware safety switch is enabled and the hardware safety switch is not in the armed state. The hardware switch is optional, it can be cumbersome to access the electronics in order to arm the autopilot at the hardware level.

## GPS Configuration

Fails if any of the following is true:
- Any gps requires further configuration.
- Individual gps inputs are giving inconsistent readings.
- Blending of multiple gps inputs is unhealthy.