{% include "../archive-notice.html" %}

<meta http-equiv="refresh" content="0; URL=https://ardupilot.org/sub/docs/parameters-Sub-stable-V4.1.2.html" />

# This documentation has been moved to [https://ardupilot.org/sub/docs/parameters.html](https://ardupilot.org/sub/docs/parameters.html).

## You should be automatically redirected.

---

This is a complete list of the parameters which can be set via the MAVLink protocol in the EEPROM of your APM to control vehicle behaviour. This list is automatically generated from the latest ardupilot source code, and so may contain parameters which are not yet in the stable released versions of the code. Some parameters may only be available for developers, and are enabled at compile-time.

# ArduSub Parameters

## SURFACE_DEPTH: Depth reading at surface

The depth the external pressure sensor will read when the vehicle is considered at the surface (in centimeters)

- Units: cm

- Range: -100 0

## SYSID_SW_MREV: Eeprom format version number

*Note: This parameter is for advanced users*

This value is incremented when changes are made to the eeprom format

- ReadOnly: True

## SYSID_THISMAV: MAVLink system ID of this vehicle

*Note: This parameter is for advanced users*

Allows setting an individual MAVLink system id for this vehicle to distinguish it from others on the same network

- Range: 1 255

## SYSID_MYGCS: My ground station number

*Note: This parameter is for advanced users*

Allows restricting radio overrides to only come from my ground station

## PILOT_THR_FILT: Throttle filter cutoff

*Note: This parameter is for advanced users*

Throttle filter cutoff (Hz) - active whenever altitude control is inactive - 0 to disable

- Units: Hz

- Range: 0 10

- Increment: .5

## GCS_PID_MASK: GCS PID tuning mask

*Note: This parameter is for advanced users*

bitmask of PIDs to send MAVLink PID_TUNING messages for

|Value|Meaning|
|:---:|:---:|
|0|None|
|1|Roll|
|2|Pitch|
|4|Yaw|

- Bitmask: 0:Roll,1:Pitch,2:Yaw

## RNGFND_GAIN: Rangefinder gain

Used to adjust the speed with which the target altitude is changed when objects are sensed below the sub

- Range: 0.01 2.0

- Increment: 0.01

## FS_GCS_ENABLE: Ground Station Failsafe Enable

Controls what action to take when GCS heartbeat is lost.

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Warn only|
|2|Disarm|
|3|Enter depth hold mode|
|4|Enter surface mode|

## FS_LEAK_ENABLE: Leak Failsafe Enable

Controls what action to take if a leak is detected.

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Warn only|
|2|Enter surface mode|

## FS_PRESS_ENABLE: Internal Pressure Failsafe Enable

Controls what action to take if internal pressure exceeds FS_PRESS_MAX parameter.

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Warn only|

## FS_TEMP_ENABLE: Internal Temperature Failsafe Enable

Controls what action to take if internal temperature exceeds FS_TEMP_MAX parameter.

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Warn only|

## FS_PRESS_MAX: Internal Pressure Failsafe Threshold

The maximum internal pressure allowed before triggering failsafe. Failsafe action is determined by FS_PRESS_ENABLE parameter

- Units: Pa

## FS_TEMP_MAX: Internal Temperature Failsafe Threshold

The maximum internal temperature allowed before triggering failsafe. Failsafe action is determined by FS_TEMP_ENABLE parameter.

- Units: degC

## FS_TERRAIN_ENAB: Terrain Failsafe Enable

Controls what action to take if terrain information is lost during AUTO mode

|Value|Meaning|
|:---:|:---:|
|0|Disarm|
| 1|Hold Position|
| 2|Surface|

## FS_PILOT_INPUT: Pilot input failsafe action

Controls what action to take if no pilot input has been received after the timeout period specified by the FS_PILOT_TIMEOUT parameter

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
| 1|Warn Only|
| 2|Disarm|

## FS_PILOT_TIMEOUT: Timeout for activation of pilot input failsafe

Controls the maximum interval between received pilot inputs before the failsafe action is triggered

- Units: s

- Range: 0.1 3.0

## XTRACK_ANG_LIM: Crosstrack correction angle limit

Maximum allowed angle (in degrees) between current track and desired heading during waypoint navigation

- Range: 10 90

## WP_YAW_BEHAVIOR: Yaw behaviour during missions

Determines how the autopilot controls the yaw during missions and RTL

|Value|Meaning|
|:---:|:---:|
|0|Never change yaw|
| 1|Face next waypoint|
| 2|Face next waypoint except RTL|
| 3|Face along GPS course|
| 4|Correct crosstrack error|

## PILOT_SPEED_UP: Pilot maximum vertical ascending speed

The maximum vertical ascending velocity the pilot may request in cm/s

- Units: cm/s

- Range: 50 500

- Increment: 10

## PILOT_SPEED_DN: Pilot maximum vertical descending speed

The maximum vertical descending velocity the pilot may request in cm/s

- Units: cm/s

- Range: 50 500

- Increment: 10

## PILOT_ACCEL_Z: Pilot vertical acceleration

The vertical acceleration used when pilot is controlling the altitude

- Units: cm/s/s

- Range: 50 500

- Increment: 10

## THR_DZ: Throttle deadzone

The PWM deadzone in microseconds above and below mid throttle. Used in AltHold, Loiter, PosHold flight modes

- Range: 0 300

- Units: PWM

- Increment: 1

## LOG_BITMASK: Log bitmask

4 byte bitmap of log types to enable

|Value|Meaning|
|:---:|:---:|
|830|Default|
|894|Default+RCIN|
|958|Default+IMU|
|1854|Default+Motors|
|-6146|NearlyAll-AC315|
|45054|NearlyAll|
|131071|All+FastATT|
|262142|All+MotBatt|
|393214|All+FastIMU|
|397310|All+FastIMU+PID|
|655358|All+FullIMU|
|0|Disabled|

- Bitmask: 0:ATTITUDE_FAST,1:ATTITUDE_MED,2:GPS,3:PM,4:CTUN,5:NTUN,6:RCIN,7:IMU,8:CMD,9:CURRENT,10:RCOUT,11:OPTFLOW,12:PID,13:COMPASS,14:INAV,15:CAMERA,17:MOTBATT,18:IMU_FAST,19:IMU_RAW

## ANGLE_MAX: Angle Max

*Note: This parameter is for advanced users*

Maximum lean angle in all flight modes

- Units: cdeg

- Range: 1000 8000

## FS_EKF_ACTION: EKF Failsafe Action

*Note: This parameter is for advanced users*

Controls the action that will be taken when an EKF failsafe is invoked

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
| 1|Warn only|
| 2|Disarm|

## FS_EKF_THRESH: EKF failsafe variance threshold

*Note: This parameter is for advanced users*

Allows setting the maximum acceptable compass and velocity variance

- Values: 0.6:Strict, 0.8:Default, 1.0:Relaxed

## FS_CRASH_CHECK: Crash check enable

*Note: This parameter is for advanced users*

This enables automatic crash checking. When enabled the motors will disarm if a crash is detected.

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Warn only|
|2|Disarm|

## JS_GAIN_DEFAULT: Default gain at boot

Default gain at boot, must be in range [JS_GAIN_MIN , JS_GAIN_MAX]

- Range: 0.1 1.0

## JS_GAIN_MAX: Maximum joystick gain

Maximum joystick gain

- Range: 0.2 1.0

## JS_GAIN_MIN: Minimum joystick gain

Minimum joystick gain

- Range: 0.1 0.8

## JS_GAIN_STEPS: Gain steps

Controls the number of steps between minimum and maximum joystick gain when the gain is adjusted using buttons. Set to 1 to always use JS_GAIN_DEFAULT.

- Range: 1 10

## JS_LIGHTS_STEPS: Lights brightness steps

Number of steps in brightness between minimum and maximum brightness

- Range: 1 10

- Units: PWM

## JS_THR_GAIN: Throttle gain scalar

Scalar for gain on the throttle channel

- Range: 0.5 4.0

## FRAME_CONFIG: Frame configuration

Set this parameter according to your vehicle/motor configuration

- RebootRequired: True

|Value|Meaning|
|:---:|:---:|
|0|BlueROV1|
| 1|Vectored|
| 2|Vectored_6DOF|
| 3|Vectored_6DOF_90|
| 4|SimpleROV-3|
| 5|SimpleROV-4|
| 6|SimpleROV-5|
| 7|Custom|

## RC_SPEED: ESC Update Speed

*Note: This parameter is for advanced users*

This is the speed in Hertz that your ESCs will receive updates

- Units: Hz

- Range: 50 490

- Increment: 1

## ACRO_RP_P: Acro Roll and Pitch P gain

Converts pilot roll and pitch into a desired rate of rotation in ACRO and SPORT mode.  Higher values mean faster rate of rotation.

- Range: 1 10

## ACRO_YAW_P: Acro Yaw P gain

Converts pilot yaw input into a desired rate of rotation.  Higher values mean faster rate of rotation.

- Range: 1 10

## ACRO_BAL_ROLL: Acro Balance Roll

*Note: This parameter is for advanced users*

rate at which roll angle returns to level in acro mode.  A higher value causes the vehicle to return to level faster.

- Range: 0 3

- Increment: 0.1

## ACRO_BAL_PITCH: Acro Balance Pitch

*Note: This parameter is for advanced users*

rate at which pitch angle returns to level in acro mode.  A higher value causes the vehicle to return to level faster.

- Range: 0 3

- Increment: 0.1

## ACRO_TRAINER: Acro Trainer

*Note: This parameter is for advanced users*

Type of trainer used in acro mode

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Leveling|
|2|Leveling and Limited|

## ACRO_EXPO: Acro Expo

*Note: This parameter is for advanced users*

Acro roll/pitch Expo to allow faster rotation when stick at edges

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|0.1|Very Low|
|0.2|Low|
|0.3|Medium|
|0.4|High|
|0.5|Very High|

## TERRAIN_FOLLOW: Terrain Following use control

This enables terrain following for RTL and SURFACE flight modes. To use this option TERRAIN_ENABLE must be 1 and the GCS must  support sending terrain data to the aircraft.  In RTL the RTL_ALT will be considered a height above the terrain.  In LAND mode the vehicle will slow to LAND_SPEED 10m above terrain (instead of 10m above home).  This parameter does not affect AUTO and Guided which use a per-command flag to determine if the height is above-home, absolute or above-terrain.

|Value|Meaning|
|:---:|:---:|
|0|Do Not Use in RTL and SURFACE|
|1|Use in RTL and SURFACE|

# AHRS Parameters

## AHRS_GPS_GAIN: AHRS GPS gain

*Note: This parameter is for advanced users*

This controls how much to use the GPS to correct the attitude. This should never be set to zero for a plane as it would result in the plane losing control in turns. For a plane please use the default value of 1.0.

- Range: 0.0 1.0

- Increment: .01

## AHRS_GPS_USE: AHRS use GPS for navigation

*Note: This parameter is for advanced users*

This controls whether to use dead-reckoning or GPS based navigation. If set to 0 then the GPS won't be used for navigation, and only dead reckoning will be used. A value of zero should never be used for normal flight. Currently this affects only the DCM-based AHRS: the EKF uses GPS whenever it is available.

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|

## AHRS_YAW_P: Yaw P

*Note: This parameter is for advanced users*

This controls the weight the compass or GPS has on the heading. A higher value means the heading will track the yaw source (GPS or compass) more rapidly.

- Range: 0.1 0.4

- Increment: .01

## AHRS_RP_P: AHRS RP_P

*Note: This parameter is for advanced users*

This controls how fast the accelerometers correct the attitude

- Range: 0.1 0.4

- Increment: .01

## AHRS_WIND_MAX: Maximum wind

*Note: This parameter is for advanced users*

This sets the maximum allowable difference between ground speed and airspeed. This allows the plane to cope with a failing airspeed sensor. A value of zero means to use the airspeed as is.

- Range: 0 127

- Units: m/s

- Increment: 1

## AHRS_TRIM_X: AHRS Trim Roll

Compensates for the roll angle difference between the control board and the frame. Positive values make the vehicle roll right.

- Units: rad

- Range: -0.1745 +0.1745

- Increment: 0.01

## AHRS_TRIM_Y: AHRS Trim Pitch

Compensates for the pitch angle difference between the control board and the frame. Positive values make the vehicle pitch up/back.

- Units: rad

- Range: -0.1745 +0.1745

- Increment: 0.01

## AHRS_TRIM_Z: AHRS Trim Yaw

*Note: This parameter is for advanced users*

Not Used

- Units: rad

- Range: -0.1745 +0.1745

- Increment: 0.01

## AHRS_ORIENTATION: Board Orientation

*Note: This parameter is for advanced users*

Overall board orientation relative to the standard orientation for the board type. This rotates the IMU and compass readings to allow the board to be oriented in your vehicle at any 90 or 45 degree angle. This option takes affect on next boot. After changing you will need to re-level your vehicle.

|Value|Meaning|
|:---:|:---:|
|0|None|
|1|Yaw45|
|2|Yaw90|
|3|Yaw135|
|4|Yaw180|
|5|Yaw225|
|6|Yaw270|
|7|Yaw315|
|8|Roll180|
|9|Roll180Yaw45|
|10|Roll180Yaw90|
|11|Roll180Yaw135|
|12|Pitch180|
|13|Roll180Yaw225|
|14|Roll180Yaw270|
|15|Roll180Yaw315|
|16|Roll90|
|17|Roll90Yaw45|
|18|Roll90Yaw90|
|19|Roll90Yaw135|
|20|Roll270|
|21|Roll270Yaw45|
|22|Roll270Yaw90|
|23|Roll270Yaw135|
|24|Pitch90|
|25|Pitch270|
|26|Pitch180Yaw90|
|27|Pitch180Yaw270|
|28|Roll90Pitch90|
|29|Roll180Pitch90|
|30|Roll270Pitch90|
|31|Roll90Pitch180|
|32|Roll270Pitch180|
|33|Roll90Pitch270|
|34|Roll180Pitch270|
|35|Roll270Pitch270|
|36|Roll90Pitch180Yaw90|
|37|Roll90Yaw270|
|38|Yaw293Pitch68Roll180|
|39|Pitch315|
|40|Roll90Pitch315|
|100|Custom|

## AHRS_COMP_BETA: AHRS Velocity Complementary Filter Beta Coefficient

*Note: This parameter is for advanced users*

This controls the time constant for the cross-over frequency used to fuse AHRS (airspeed and heading) and GPS data to estimate ground velocity. Time constant is 0.1/beta. A larger time constant will use GPS data less and a small time constant will use air data less.

- Range: 0.001 0.5

- Increment: .01

## AHRS_GPS_MINSATS: AHRS GPS Minimum satellites

*Note: This parameter is for advanced users*

Minimum number of satellites visible to use GPS for velocity based corrections attitude correction. This defaults to 6, which is about the point at which the velocity numbers from a GPS become too unreliable for accurate correction of the accelerometers.

- Range: 0 10

- Increment: 1

## AHRS_EKF_TYPE: Use NavEKF Kalman filter for attitude and position estimation

*Note: This parameter is for advanced users*

This controls which NavEKF Kalman filter version is used for attitude and position estimation

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|2|Enable EKF2|
|3|Enable EKF3|

## AHRS_CUSTOM_ROLL: Board orientation roll offset

*Note: This parameter is for advanced users*

Autopilot mounting position roll offset. Positive values = roll right, negative values = roll left. This parameter is only used when AHRS_ORIENTATION is set to CUSTOM.

- Range: -180 180

- Units: deg

- Increment: 1

## AHRS_CUSTOM_PIT: Board orientation pitch offset

*Note: This parameter is for advanced users*

Autopilot mounting position pitch offset. Positive values = pitch up, negative values = pitch down. This parameter is only used when AHRS_ORIENTATION is set to CUSTOM.

- Range: -180 180

- Units: deg

- Increment: 1

## AHRS_CUSTOM_YAW: Board orientation yaw offset

*Note: This parameter is for advanced users*

Autopilot mounting position yaw offset. Positive values = yaw right, negative values = yaw left. This parameter is only used when AHRS_ORIENTATION is set to CUSTOM.

- Range: -180 180

- Units: deg

- Increment: 1

# ARMING Parameters

## ARMING_REQUIRE: Require Arming Motors 

*Note: This parameter is for advanced users*

Arming disabled until some requirements are met. If 0, there are no requirements (arm immediately).  If 1, require rudder stick or GCS arming before arming motors and sends the minimum throttle PWM value to the throttle channel when disarmed.  If 2, require rudder stick or GCS arming and send 0 PWM to throttle channel when disarmed. See the ARMING_CHECK_* parameters to see what checks are done before arming. Note, if setting this parameter to 0 a reboot is required to arm the plane.  Also note, even with this parameter at 0, if ARMING_CHECK parameter is not also zero the plane may fail to arm throttle at boot due to a pre-arm check failure.

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|THR_MIN PWM when disarmed|
|2|0 PWM when disarmed|

## ARMING_ACCTHRESH: Accelerometer error threshold

*Note: This parameter is for advanced users*

Accelerometer error threshold used to determine inconsistent accelerometers. Compares this error range to other accelerometers to detect a hardware or calibration error. Lower value means tighter check and harder to pass arming check. Not all accelerometers are created equal.

- Units: m/s/s

- Range: 0.25 3.0

## ARMING_RUDDER: Arming with Rudder enable/disable

*Note: This parameter is for advanced users*

Allow arm/disarm by rudder input. When enabled arming can be done with right rudder, disarming with left rudder. Rudder arming only works in manual throttle modes with throttle at zero +- deadzone (RCx_DZ)

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|ArmingOnly|
|2|ArmOrDisarm|

## ARMING_MIS_ITEMS: Required mission items

*Note: This parameter is for advanced users*

Bitmask of mission items that are required to be planned in order to arm the aircraft

- Bitmask: 0:Land,1:VTOL Land,2:DO_LAND_START,3:Takeoff,4:VTOL Takeoff,5:Rallypoint

## ARMING_CHECK: Arm Checks to Peform (bitmask)

Checks prior to arming motor. This is a bitmask of checks that will be performed before allowing arming. The default is no checks, allowing arming at any time. You can select whatever checks you prefer by adding together the values of each check type to set this parameter. For example, to only allow arming when you have GPS lock and no RC failsafe you would set ARMING_CHECK to 72. For most users it is recommended that you set this to 1 to enable all checks.

|Value|Meaning|
|:---:|:---:|
|0|None|
|1|All|
|2|Barometer|
|4|Compass|
|8|GPS Lock|
|16|INS(INertial Sensors - accels & gyros)|
|32|Parameters(unused)|
|64|RC Channels|
|128|Board voltage|
|256|Battery Level|
|512|Airspeed|
|1024|LoggingAvailable|
|2048|Hardware safety switch|
|4096|GPS configuration|
|8192|System|

- Bitmask: 0:All,1:Barometer,2:Compass,3:GPS lock,4:INS,5:Parameters,6:RC Channels,7:Board voltage,8:Battery Level,9:Airspeed,10:Logging Available,11:Hardware safety switch,12:GPS Configuration,13:System,14:Mission,15:Rangefinder

# ATC Parameters

## ATC_SLEW_YAW: Yaw target slew rate

*Note: This parameter is for advanced users*

Maximum rate the yaw target can be updated in Loiter, RTL, Auto flight modes

- Units: cdeg/s

- Range: 500 18000

- Increment: 100

## ATC_ACCEL_Y_MAX: Acceleration Max for Yaw

*Note: This parameter is for advanced users*

Maximum acceleration in yaw axis

- Units: cdeg/s/s

- Range: 0 72000

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
| 9000|VerySlow|
| 18000|Slow|
| 36000|Medium|
| 54000|Fast|

- Increment: 1000

## ATC_RATE_FF_ENAB: Rate Feedforward Enable

*Note: This parameter is for advanced users*

Controls whether body-frame rate feedfoward is enabled or disabled

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
| 1|Enabled|

## ATC_ACCEL_R_MAX: Acceleration Max for Roll

*Note: This parameter is for advanced users*

Maximum acceleration in roll axis

- Units: cdeg/s/s

- Range: 0 180000

- Increment: 1000

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
| 30000|VerySlow|
| 72000|Slow|
| 108000|Medium|
| 162000|Fast|

## ATC_ACCEL_P_MAX: Acceleration Max for Pitch

*Note: This parameter is for advanced users*

Maximum acceleration in pitch axis

- Units: cdeg/s/s

- Range: 0 180000

- Increment: 1000

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
| 30000|VerySlow|
| 72000|Slow|
| 108000|Medium|
| 162000|Fast|

## ATC_ANGLE_BOOST: Angle Boost

*Note: This parameter is for advanced users*

Angle Boost increases output throttle as the vehicle leans to reduce loss of altitude

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
| 1|Enabled|

## ATC_ANG_RLL_P: Roll axis angle controller P gain

Roll axis angle controller P gain.  Converts the error between the desired roll angle and actual angle to a desired roll rate

- Range: 0.0 12.000

## ATC_ANG_PIT_P: Pitch axis angle controller P gain

Pitch axis angle controller P gain.  Converts the error between the desired pitch angle and actual angle to a desired pitch rate

- Range: 0.0 12.000

## ATC_ANG_YAW_P: Yaw axis angle controller P gain

Yaw axis angle controller P gain.  Converts the error between the desired yaw angle and actual angle to a desired yaw rate

- Range: 0.0 6.000

## ATC_ANG_LIM_TC: Angle Limit (to maintain altitude) Time Constant

*Note: This parameter is for advanced users*

Angle Limit (to maintain altitude) Time Constant

- Range: 0.5 10.0

## ATC_RATE_R_MAX: Angular Velocity Max for Roll

*Note: This parameter is for advanced users*

Maximum angular velocity in roll axis

- Units: deg/s

- Range: 0 1080

- Increment: 1

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
| 360|Slow|
| 720|Medium|
| 1080|Fast|

## ATC_RATE_P_MAX: Angular Velocity Max for Pitch

*Note: This parameter is for advanced users*

Maximum angular velocity in pitch axis

- Units: deg/s

- Range: 0 1080

- Increment: 1

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
| 360|Slow|
| 720|Medium|
| 1080|Fast|

## ATC_RATE_Y_MAX: Angular Velocity Max for Yaw

*Note: This parameter is for advanced users*

Maximum angular velocity in yaw axis

- Units: deg/s

- Range: 0 1080

- Increment: 1

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
| 360|Slow|
| 720|Medium|
| 1080|Fast|

## ATC_INPUT_TC: Attitude control input time constant

Attitude control input time constant.  Low numbers lead to sharper response, higher numbers to softer response

- Units: s

- Range: 0 1

- Increment: 0.01

- Values: 0.5:Very Soft, 0.2:Soft, 0.15:Medium, 0.1:Crisp, 0.05:Very Crisp

## ATC_RAT_RLL_P: Roll axis rate controller P gain

Roll axis rate controller P gain.  Converts the difference between desired roll rate and actual roll rate into a motor speed output

- Range: 0.0 0.30

- Increment: 0.005

## ATC_RAT_RLL_I: Roll axis rate controller I gain

Roll axis rate controller I gain.  Corrects long-term difference in desired roll rate vs actual roll rate

- Range: 0.0 0.5

- Increment: 0.01

## ATC_RAT_RLL_IMAX: Roll axis rate controller I gain maximum

Roll axis rate controller I gain maximum.  Constrains the maximum motor output that the I gain will output

- Range: 0 1

- Increment: 0.01

- Units: %

## ATC_RAT_RLL_D: Roll axis rate controller D gain

Roll axis rate controller D gain.  Compensates for short-term change in desired roll rate vs actual roll rate

- Range: 0.0 0.02

- Increment: 0.001

## ATC_RAT_RLL_FF: Roll axis rate controller feed forward

Roll axis rate controller feed forward

- Range: 0 0.5

- Increment: 0.001

## ATC_RAT_RLL_FLTT: Roll axis rate controller input frequency in Hz

Roll axis rate controller input frequency in Hz

- Range: 1 100

- Increment: 1

- Units: Hz

## ATC_RAT_RLL_FLTE: Roll axis rate controller input frequency in Hz

Roll axis rate controller input frequency in Hz

- Range: 1 100

- Increment: 1

- Units: Hz

## ATC_RAT_RLL_FLTD: Roll axis rate controller input frequency in Hz

Roll axis rate controller input frequency in Hz

- Range: 1 100

- Increment: 1

- Units: Hz

## ATC_RAT_PIT_P: Pitch axis rate controller P gain

Pitch axis rate controller P gain.  Converts the difference between desired pitch rate and actual pitch rate into a motor speed output

- Range: 0.0 0.30

- Increment: 0.005

## ATC_RAT_PIT_I: Pitch axis rate controller I gain

Pitch axis rate controller I gain.  Corrects long-term difference in desired pitch rate vs actual pitch rate

- Range: 0.0 0.5

- Increment: 0.01

## ATC_RAT_PIT_IMAX: Pitch axis rate controller I gain maximum

Pitch axis rate controller I gain maximum.  Constrains the maximum motor output that the I gain will output

- Range: 0 1

- Increment: 0.01

- Units: %

## ATC_RAT_PIT_D: Pitch axis rate controller D gain

Pitch axis rate controller D gain.  Compensates for short-term change in desired pitch rate vs actual pitch rate

- Range: 0.0 0.02

- Increment: 0.001

## ATC_RAT_PIT_FF: Pitch axis rate controller feed forward

Pitch axis rate controller feed forward

- Range: 0 0.5

- Increment: 0.001

## ATC_RAT_PIT_FLTT: Pitch axis rate controller input frequency in Hz

Pitch axis rate controller input frequency in Hz

- Range: 1 100

- Increment: 1

- Units: Hz

## ATC_RAT_PIT_FLTE: Pitch axis rate controller input frequency in Hz

Pitch axis rate controller input frequency in Hz

- Range: 1 100

- Increment: 1

- Units: Hz

## ATC_RAT_PIT_FLTD: Pitch axis rate controller input frequency in Hz

Pitch axis rate controller input frequency in Hz

- Range: 1 100

- Increment: 1

- Units: Hz

## ATC_RAT_YAW_P: Yaw axis rate controller P gain

Yaw axis rate controller P gain.  Converts the difference between desired yaw rate and actual yaw rate into a motor speed output

- Range: 0.0 0.50

- Increment: 0.005

## ATC_RAT_YAW_I: Yaw axis rate controller I gain

Yaw axis rate controller I gain.  Corrects long-term difference in desired yaw rate vs actual yaw rate

- Range: 0.0 0.05

- Increment: 0.01

## ATC_RAT_YAW_IMAX: Yaw axis rate controller I gain maximum

Yaw axis rate controller I gain maximum.  Constrains the maximum motor output that the I gain will output

- Range: 0 1

- Increment: 0.01

- Units: %

## ATC_RAT_YAW_D: Yaw axis rate controller D gain

Yaw axis rate controller D gain.  Compensates for short-term change in desired yaw rate vs actual yaw rate

- Range: 0.000 0.02

- Increment: 0.001

## ATC_RAT_YAW_FF: Yaw axis rate controller feed forward

Yaw axis rate controller feed forward

- Range: 0 0.5

- Increment: 0.001

## ATC_RAT_YAW_FLTT: Yaw axis rate controller input frequency in Hz

Yaw axis rate controller input frequency in Hz

- Range: 1 100

- Increment: 1

- Units: Hz

## ATC_RAT_YAW_FLTE: Yaw axis rate controller input frequency in Hz

Yaw axis rate controller input frequency in Hz

- Range: 1 100

- Increment: 1

- Units: Hz

## ATC_RAT_YAW_FLTD: Yaw axis rate controller input frequency in Hz

Yaw axis rate controller input frequency in Hz

- Range: 1 100

- Increment: 1

- Units: Hz

## ATC_THR_MIX_MIN: Throttle Mix Minimum

*Note: This parameter is for advanced users*

Throttle vs attitude control prioritisation used when landing (higher values mean we prioritise attitude control over throttle)

- Range: 0.1 0.25

## ATC_THR_MIX_MAX: Throttle Mix Maximum

*Note: This parameter is for advanced users*

Throttle vs attitude control prioritisation used during active flight (higher values mean we prioritise attitude control over throttle)

- Range: 0.5 0.9

## ATC_THR_MIX_MAN: Throttle Mix Manual

*Note: This parameter is for advanced users*

Throttle vs attitude control prioritisation used during manual flight (higher values mean we prioritise attitude control over throttle)

- Range: 0.5 0.9

## ATC_RAT_RLL_FILT: Roll axis rate controller input frequency in Hz

Roll axis rate controller input frequency in Hz

- Range: 1 100

- Increment: 1

- Units: Hz

## ATC_RAT_PIT_FILT: Pitch axis rate controller input frequency in Hz

Pitch axis rate controller input frequency in Hz

- Range: 1 100

- Increment: 1

- Units: Hz

## ATC_RAT_YAW_FILT: Yaw axis rate controller input frequency in Hz

Yaw axis rate controller input frequency in Hz

- Range: 1 100

- Increment: 1

- Units: Hz

# BATT2 Parameters

## BATT2_MONITOR: Battery monitoring

Controls enabling monitoring of the battery's voltage and current

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|3|Analog Voltage Only|
|4|Analog Voltage and Current|
|5|Solo|
|6|Bebop|
|7|SMBus-Maxell|
|8|UAVCAN-BatteryInfo|
|9|BLHeli ESC|
|10|SumOfFollowing|
|11|FuelFlow|
|12|FuelLevelPWM|

- RebootRequired: True

## BATT2_VOLT_PIN: Battery Voltage sensing pin

Sets the analog input pin that should be used for voltage monitoring.

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
| 2|Pixhawk/Pixracer/Navio2/Pixhawk2_PM1|
| 13|Pixhawk2_PM2|
| 14|CubeOrange|
| 13|CubeOrange_PM2|
| 100|PX4-v1|

- RebootRequired: True

## BATT2_CURR_PIN: Battery Current sensing pin

Sets the analog input pin that should be used for current monitoring.

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
| 3|Pixhawk/Pixracer/Navio2/Pixhawk2_PM1|
| 14|Pixhawk2_PM2|
| 15|CubeOrange|
| 4|CubeOrange_PM2|
| 101|PX4-v1|

- RebootRequired: True

## BATT2_VOLT_MULT: Voltage Multiplier

*Note: This parameter is for advanced users*

Used to convert the voltage of the voltage sensing pin (BATT2_VOLT_PIN) to the actual battery's voltage (pin_voltage * VOLT_MULT). For the 3DR Power brick with a Pixhawk, this should be set to 10.1. For the Pixhawk with the 3DR 4in1 ESC this should be 12.02. For the PX using the PX4IO power supply this should be set to 1.

## BATT2_AMP_PERVLT: Amps per volt

Number of amps that a 1V reading on the current sensor corresponds to. With a Pixhawk using the 3DR Power brick this should be set to 17. For the Pixhawk with the 3DR 4in1 ESC this should be 17.

- Units: A/V

## BATT2_AMP_OFFSET: AMP offset

Voltage offset at zero current on current sensor

- Units: V

## BATT2_CAPACITY: Battery capacity

Capacity of the battery in mAh when full

- Units: mAh

- Increment: 50

## BATT2_WATT_MAX: Maximum allowed power (Watts)

*Note: This parameter is for advanced users*

If battery wattage (voltage * current) exceeds this value then the system will reduce max throttle (THR_MAX, TKOFF_THR_MAX and THR_MIN for reverse thrust) to satisfy this limit. This helps limit high current to low C rated batteries regardless of battery voltage. The max throttle will slowly grow back to THR_MAX (or TKOFF_THR_MAX ) and THR_MIN if demanding the current max and under the watt max. Use 0 to disable.

- Units: W

- Increment: 1

## BATT2_SERIAL_NUM: Battery serial number

*Note: This parameter is for advanced users*

Battery serial number, automatically filled in for SMBus batteries, otherwise will be -1. With UAVCAN it is the battery_id.

## BATT2_LOW_TIMER: Low voltage timeout

*Note: This parameter is for advanced users*

This is the timeout in seconds before a low voltage event will be triggered. For aircraft with low C batteries it may be necessary to raise this in order to cope with low voltage on long takeoffs. A value of zero disables low voltage errors.

- Units: s

- Increment: 1

- Range: 0 120

## BATT2_FS_VOLTSRC: Failsafe voltage source

*Note: This parameter is for advanced users*

Voltage type used for detection of low voltage event

|Value|Meaning|
|:---:|:---:|
|0|Raw Voltage|
| 1|Sag Compensated Voltage|

## BATT2_LOW_VOLT: Low battery voltage

Battery voltage that triggers a low battery failsafe. Set to 0 to disable. If the battery voltage drops below this voltage continuously for more then the period specified by the BATT2_LOW_TIMER parameter then the vehicle will perform the failsafe specified by the BATT2_FS_LOW_ACT parameter.

- Units: V

- Increment: 0.1

## BATT2_LOW_MAH: Low battery capacity

Battery capacity at which the low battery failsafe is triggered. Set to 0 to disable battery remaining failsafe. If the battery capacity drops below this level the vehicle will perform the failsafe specified by the BATT2_FS_LOW_ACT parameter.

- Units: mAh

- Increment: 50

## BATT2_CRT_VOLT: Critical battery voltage

Battery voltage that triggers a critical battery failsafe. Set to 0 to disable. If the battery voltage drops below this voltage continuously for more then the period specified by the BATT2_LOW_TIMER parameter then the vehicle will perform the failsafe specified by the BATT2_FS_CRT_ACT parameter.

- Units: V

- Increment: 0.1

## BATT2_CRT_MAH: Battery critical capacity

Battery capacity at which the critical battery failsafe is triggered. Set to 0 to disable battery remaining failsafe. If the battery capacity drops below this level the vehicle will perform the failsafe specified by the BATT2__FS_CRT_ACT parameter.

- Units: mAh

- Increment: 50

## BATT2_FS_LOW_ACT: Low battery failsafe action

What action the vehicle should perform if it hits a low battery failsafe

|Value|Meaning|
|:---:|:---:|
|0|None|
|2|Disarm|
|3|Enter surface mode|

## BATT2_FS_CRT_ACT: Critical battery failsafe action

What action the vehicle should perform if it hits a critical battery failsafe

|Value|Meaning|
|:---:|:---:|
|0|None|
|2|Disarm|
|3|Enter surface mode|

## BATT2_ARM_VOLT: Required arming voltage

*Note: This parameter is for advanced users*

Battery voltage level which is required to arm the aircraft. Set to 0 to allow arming at any voltage.

- Units: V

- Increment: 0.1

## BATT2_ARM_MAH: Required arming remaining capacity

*Note: This parameter is for advanced users*

Battery capacity remaining which is required to arm the aircraft. Set to 0 to allow arming at any capacity. Note that execept for smart batteries rebooting the vehicle will always reset the remaining capacity estimate, which can lead to this check not providing sufficent protection, it is recommended to always use this in conjunction with the BATT2__ARM_VOLT parameter.

- Units: mAh

- Increment: 50

# BATT3 Parameters

## BATT3_MONITOR: Battery monitoring

Controls enabling monitoring of the battery's voltage and current

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|3|Analog Voltage Only|
|4|Analog Voltage and Current|
|5|Solo|
|6|Bebop|
|7|SMBus-Maxell|
|8|UAVCAN-BatteryInfo|
|9|BLHeli ESC|
|10|SumOfFollowing|
|11|FuelFlow|
|12|FuelLevelPWM|

- RebootRequired: True

## BATT3_VOLT_PIN: Battery Voltage sensing pin

Sets the analog input pin that should be used for voltage monitoring.

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
| 2|Pixhawk/Pixracer/Navio2/Pixhawk2_PM1|
| 13|Pixhawk2_PM2|
| 14|CubeOrange|
| 13|CubeOrange_PM2|
| 100|PX4-v1|

- RebootRequired: True

## BATT3_CURR_PIN: Battery Current sensing pin

Sets the analog input pin that should be used for current monitoring.

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
| 3|Pixhawk/Pixracer/Navio2/Pixhawk2_PM1|
| 14|Pixhawk2_PM2|
| 15|CubeOrange|
| 4|CubeOrange_PM2|
| 101|PX4-v1|

- RebootRequired: True

## BATT3_VOLT_MULT: Voltage Multiplier

*Note: This parameter is for advanced users*

Used to convert the voltage of the voltage sensing pin (BATT3_VOLT_PIN) to the actual battery's voltage (pin_voltage * VOLT_MULT). For the 3DR Power brick with a Pixhawk, this should be set to 10.1. For the Pixhawk with the 3DR 4in1 ESC this should be 12.02. For the PX using the PX4IO power supply this should be set to 1.

## BATT3_AMP_PERVLT: Amps per volt

Number of amps that a 1V reading on the current sensor corresponds to. With a Pixhawk using the 3DR Power brick this should be set to 17. For the Pixhawk with the 3DR 4in1 ESC this should be 17.

- Units: A/V

## BATT3_AMP_OFFSET: AMP offset

Voltage offset at zero current on current sensor

- Units: V

## BATT3_CAPACITY: Battery capacity

Capacity of the battery in mAh when full

- Units: mAh

- Increment: 50

## BATT3_WATT_MAX: Maximum allowed power (Watts)

*Note: This parameter is for advanced users*

If battery wattage (voltage * current) exceeds this value then the system will reduce max throttle (THR_MAX, TKOFF_THR_MAX and THR_MIN for reverse thrust) to satisfy this limit. This helps limit high current to low C rated batteries regardless of battery voltage. The max throttle will slowly grow back to THR_MAX (or TKOFF_THR_MAX ) and THR_MIN if demanding the current max and under the watt max. Use 0 to disable.

- Units: W

- Increment: 1

## BATT3_SERIAL_NUM: Battery serial number

*Note: This parameter is for advanced users*

Battery serial number, automatically filled in for SMBus batteries, otherwise will be -1. With UAVCAN it is the battery_id.

## BATT3_LOW_TIMER: Low voltage timeout

*Note: This parameter is for advanced users*

This is the timeout in seconds before a low voltage event will be triggered. For aircraft with low C batteries it may be necessary to raise this in order to cope with low voltage on long takeoffs. A value of zero disables low voltage errors.

- Units: s

- Increment: 1

- Range: 0 120

## BATT3_FS_VOLTSRC: Failsafe voltage source

*Note: This parameter is for advanced users*

Voltage type used for detection of low voltage event

|Value|Meaning|
|:---:|:---:|
|0|Raw Voltage|
| 1|Sag Compensated Voltage|

## BATT3_LOW_VOLT: Low battery voltage

Battery voltage that triggers a low battery failsafe. Set to 0 to disable. If the battery voltage drops below this voltage continuously for more then the period specified by the BATT3_LOW_TIMER parameter then the vehicle will perform the failsafe specified by the BATT3_FS_LOW_ACT parameter.

- Units: V

- Increment: 0.1

## BATT3_LOW_MAH: Low battery capacity

Battery capacity at which the low battery failsafe is triggered. Set to 0 to disable battery remaining failsafe. If the battery capacity drops below this level the vehicle will perform the failsafe specified by the BATT3_FS_LOW_ACT parameter.

- Units: mAh

- Increment: 50

## BATT3_CRT_VOLT: Critical battery voltage

Battery voltage that triggers a critical battery failsafe. Set to 0 to disable. If the battery voltage drops below this voltage continuously for more then the period specified by the BATT3_LOW_TIMER parameter then the vehicle will perform the failsafe specified by the BATT3_FS_CRT_ACT parameter.

- Units: V

- Increment: 0.1

## BATT3_CRT_MAH: Battery critical capacity

Battery capacity at which the critical battery failsafe is triggered. Set to 0 to disable battery remaining failsafe. If the battery capacity drops below this level the vehicle will perform the failsafe specified by the BATT3__FS_CRT_ACT parameter.

- Units: mAh

- Increment: 50

## BATT3_FS_LOW_ACT: Low battery failsafe action

What action the vehicle should perform if it hits a low battery failsafe

|Value|Meaning|
|:---:|:---:|
|0|None|
|2|Disarm|
|3|Enter surface mode|

## BATT3_FS_CRT_ACT: Critical battery failsafe action

What action the vehicle should perform if it hits a critical battery failsafe

|Value|Meaning|
|:---:|:---:|
|0|None|
|2|Disarm|
|3|Enter surface mode|

## BATT3_ARM_VOLT: Required arming voltage

*Note: This parameter is for advanced users*

Battery voltage level which is required to arm the aircraft. Set to 0 to allow arming at any voltage.

- Units: V

- Increment: 0.1

## BATT3_ARM_MAH: Required arming remaining capacity

*Note: This parameter is for advanced users*

Battery capacity remaining which is required to arm the aircraft. Set to 0 to allow arming at any capacity. Note that execept for smart batteries rebooting the vehicle will always reset the remaining capacity estimate, which can lead to this check not providing sufficent protection, it is recommended to always use this in conjunction with the BATT3__ARM_VOLT parameter.

- Units: mAh

- Increment: 50

# BATT4 Parameters

## BATT4_MONITOR: Battery monitoring

Controls enabling monitoring of the battery's voltage and current

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|3|Analog Voltage Only|
|4|Analog Voltage and Current|
|5|Solo|
|6|Bebop|
|7|SMBus-Maxell|
|8|UAVCAN-BatteryInfo|
|9|BLHeli ESC|
|10|SumOfFollowing|
|11|FuelFlow|
|12|FuelLevelPWM|

- RebootRequired: True

## BATT4_VOLT_PIN: Battery Voltage sensing pin

Sets the analog input pin that should be used for voltage monitoring.

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
| 2|Pixhawk/Pixracer/Navio2/Pixhawk2_PM1|
| 13|Pixhawk2_PM2|
| 14|CubeOrange|
| 13|CubeOrange_PM2|
| 100|PX4-v1|

- RebootRequired: True

## BATT4_CURR_PIN: Battery Current sensing pin

Sets the analog input pin that should be used for current monitoring.

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
| 3|Pixhawk/Pixracer/Navio2/Pixhawk2_PM1|
| 14|Pixhawk2_PM2|
| 15|CubeOrange|
| 4|CubeOrange_PM2|
| 101|PX4-v1|

- RebootRequired: True

## BATT4_VOLT_MULT: Voltage Multiplier

*Note: This parameter is for advanced users*

Used to convert the voltage of the voltage sensing pin (BATT4_VOLT_PIN) to the actual battery's voltage (pin_voltage * VOLT_MULT). For the 3DR Power brick with a Pixhawk, this should be set to 10.1. For the Pixhawk with the 3DR 4in1 ESC this should be 12.02. For the PX using the PX4IO power supply this should be set to 1.

## BATT4_AMP_PERVLT: Amps per volt

Number of amps that a 1V reading on the current sensor corresponds to. With a Pixhawk using the 3DR Power brick this should be set to 17. For the Pixhawk with the 3DR 4in1 ESC this should be 17.

- Units: A/V

## BATT4_AMP_OFFSET: AMP offset

Voltage offset at zero current on current sensor

- Units: V

## BATT4_CAPACITY: Battery capacity

Capacity of the battery in mAh when full

- Units: mAh

- Increment: 50

## BATT4_WATT_MAX: Maximum allowed power (Watts)

*Note: This parameter is for advanced users*

If battery wattage (voltage * current) exceeds this value then the system will reduce max throttle (THR_MAX, TKOFF_THR_MAX and THR_MIN for reverse thrust) to satisfy this limit. This helps limit high current to low C rated batteries regardless of battery voltage. The max throttle will slowly grow back to THR_MAX (or TKOFF_THR_MAX ) and THR_MIN if demanding the current max and under the watt max. Use 0 to disable.

- Units: W

- Increment: 1

## BATT4_SERIAL_NUM: Battery serial number

*Note: This parameter is for advanced users*

Battery serial number, automatically filled in for SMBus batteries, otherwise will be -1. With UAVCAN it is the battery_id.

## BATT4_LOW_TIMER: Low voltage timeout

*Note: This parameter is for advanced users*

This is the timeout in seconds before a low voltage event will be triggered. For aircraft with low C batteries it may be necessary to raise this in order to cope with low voltage on long takeoffs. A value of zero disables low voltage errors.

- Units: s

- Increment: 1

- Range: 0 120

## BATT4_FS_VOLTSRC: Failsafe voltage source

*Note: This parameter is for advanced users*

Voltage type used for detection of low voltage event

|Value|Meaning|
|:---:|:---:|
|0|Raw Voltage|
| 1|Sag Compensated Voltage|

## BATT4_LOW_VOLT: Low battery voltage

Battery voltage that triggers a low battery failsafe. Set to 0 to disable. If the battery voltage drops below this voltage continuously for more then the period specified by the BATT4_LOW_TIMER parameter then the vehicle will perform the failsafe specified by the BATT4_FS_LOW_ACT parameter.

- Units: V

- Increment: 0.1

## BATT4_LOW_MAH: Low battery capacity

Battery capacity at which the low battery failsafe is triggered. Set to 0 to disable battery remaining failsafe. If the battery capacity drops below this level the vehicle will perform the failsafe specified by the BATT4_FS_LOW_ACT parameter.

- Units: mAh

- Increment: 50

## BATT4_CRT_VOLT: Critical battery voltage

Battery voltage that triggers a critical battery failsafe. Set to 0 to disable. If the battery voltage drops below this voltage continuously for more then the period specified by the BATT4_LOW_TIMER parameter then the vehicle will perform the failsafe specified by the BATT4_FS_CRT_ACT parameter.

- Units: V

- Increment: 0.1

## BATT4_CRT_MAH: Battery critical capacity

Battery capacity at which the critical battery failsafe is triggered. Set to 0 to disable battery remaining failsafe. If the battery capacity drops below this level the vehicle will perform the failsafe specified by the BATT4__FS_CRT_ACT parameter.

- Units: mAh

- Increment: 50

## BATT4_FS_LOW_ACT: Low battery failsafe action

What action the vehicle should perform if it hits a low battery failsafe

|Value|Meaning|
|:---:|:---:|
|0|None|
|2|Disarm|
|3|Enter surface mode|

## BATT4_FS_CRT_ACT: Critical battery failsafe action

What action the vehicle should perform if it hits a critical battery failsafe

|Value|Meaning|
|:---:|:---:|
|0|None|
|2|Disarm|
|3|Enter surface mode|

## BATT4_ARM_VOLT: Required arming voltage

*Note: This parameter is for advanced users*

Battery voltage level which is required to arm the aircraft. Set to 0 to allow arming at any voltage.

- Units: V

- Increment: 0.1

## BATT4_ARM_MAH: Required arming remaining capacity

*Note: This parameter is for advanced users*

Battery capacity remaining which is required to arm the aircraft. Set to 0 to allow arming at any capacity. Note that execept for smart batteries rebooting the vehicle will always reset the remaining capacity estimate, which can lead to this check not providing sufficent protection, it is recommended to always use this in conjunction with the BATT4__ARM_VOLT parameter.

- Units: mAh

- Increment: 50

# BATT5 Parameters

## BATT5_MONITOR: Battery monitoring

Controls enabling monitoring of the battery's voltage and current

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|3|Analog Voltage Only|
|4|Analog Voltage and Current|
|5|Solo|
|6|Bebop|
|7|SMBus-Maxell|
|8|UAVCAN-BatteryInfo|
|9|BLHeli ESC|
|10|SumOfFollowing|
|11|FuelFlow|
|12|FuelLevelPWM|

- RebootRequired: True

## BATT5_VOLT_PIN: Battery Voltage sensing pin

Sets the analog input pin that should be used for voltage monitoring.

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
| 2|Pixhawk/Pixracer/Navio2/Pixhawk2_PM1|
| 13|Pixhawk2_PM2|
| 14|CubeOrange|
| 13|CubeOrange_PM2|
| 100|PX4-v1|

- RebootRequired: True

## BATT5_CURR_PIN: Battery Current sensing pin

Sets the analog input pin that should be used for current monitoring.

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
| 3|Pixhawk/Pixracer/Navio2/Pixhawk2_PM1|
| 14|Pixhawk2_PM2|
| 15|CubeOrange|
| 4|CubeOrange_PM2|
| 101|PX4-v1|

- RebootRequired: True

## BATT5_VOLT_MULT: Voltage Multiplier

*Note: This parameter is for advanced users*

Used to convert the voltage of the voltage sensing pin (BATT5_VOLT_PIN) to the actual battery's voltage (pin_voltage * VOLT_MULT). For the 3DR Power brick with a Pixhawk, this should be set to 10.1. For the Pixhawk with the 3DR 4in1 ESC this should be 12.02. For the PX using the PX4IO power supply this should be set to 1.

## BATT5_AMP_PERVLT: Amps per volt

Number of amps that a 1V reading on the current sensor corresponds to. With a Pixhawk using the 3DR Power brick this should be set to 17. For the Pixhawk with the 3DR 4in1 ESC this should be 17.

- Units: A/V

## BATT5_AMP_OFFSET: AMP offset

Voltage offset at zero current on current sensor

- Units: V

## BATT5_CAPACITY: Battery capacity

Capacity of the battery in mAh when full

- Units: mAh

- Increment: 50

## BATT5_WATT_MAX: Maximum allowed power (Watts)

*Note: This parameter is for advanced users*

If battery wattage (voltage * current) exceeds this value then the system will reduce max throttle (THR_MAX, TKOFF_THR_MAX and THR_MIN for reverse thrust) to satisfy this limit. This helps limit high current to low C rated batteries regardless of battery voltage. The max throttle will slowly grow back to THR_MAX (or TKOFF_THR_MAX ) and THR_MIN if demanding the current max and under the watt max. Use 0 to disable.

- Units: W

- Increment: 1

## BATT5_SERIAL_NUM: Battery serial number

*Note: This parameter is for advanced users*

Battery serial number, automatically filled in for SMBus batteries, otherwise will be -1. With UAVCAN it is the battery_id.

## BATT5_LOW_TIMER: Low voltage timeout

*Note: This parameter is for advanced users*

This is the timeout in seconds before a low voltage event will be triggered. For aircraft with low C batteries it may be necessary to raise this in order to cope with low voltage on long takeoffs. A value of zero disables low voltage errors.

- Units: s

- Increment: 1

- Range: 0 120

## BATT5_FS_VOLTSRC: Failsafe voltage source

*Note: This parameter is for advanced users*

Voltage type used for detection of low voltage event

|Value|Meaning|
|:---:|:---:|
|0|Raw Voltage|
| 1|Sag Compensated Voltage|

## BATT5_LOW_VOLT: Low battery voltage

Battery voltage that triggers a low battery failsafe. Set to 0 to disable. If the battery voltage drops below this voltage continuously for more then the period specified by the BATT5_LOW_TIMER parameter then the vehicle will perform the failsafe specified by the BATT5_FS_LOW_ACT parameter.

- Units: V

- Increment: 0.1

## BATT5_LOW_MAH: Low battery capacity

Battery capacity at which the low battery failsafe is triggered. Set to 0 to disable battery remaining failsafe. If the battery capacity drops below this level the vehicle will perform the failsafe specified by the BATT5_FS_LOW_ACT parameter.

- Units: mAh

- Increment: 50

## BATT5_CRT_VOLT: Critical battery voltage

Battery voltage that triggers a critical battery failsafe. Set to 0 to disable. If the battery voltage drops below this voltage continuously for more then the period specified by the BATT5_LOW_TIMER parameter then the vehicle will perform the failsafe specified by the BATT5_FS_CRT_ACT parameter.

- Units: V

- Increment: 0.1

## BATT5_CRT_MAH: Battery critical capacity

Battery capacity at which the critical battery failsafe is triggered. Set to 0 to disable battery remaining failsafe. If the battery capacity drops below this level the vehicle will perform the failsafe specified by the BATT5__FS_CRT_ACT parameter.

- Units: mAh

- Increment: 50

## BATT5_FS_LOW_ACT: Low battery failsafe action

What action the vehicle should perform if it hits a low battery failsafe

|Value|Meaning|
|:---:|:---:|
|0|None|
|2|Disarm|
|3|Enter surface mode|

## BATT5_FS_CRT_ACT: Critical battery failsafe action

What action the vehicle should perform if it hits a critical battery failsafe

|Value|Meaning|
|:---:|:---:|
|0|None|
|2|Disarm|
|3|Enter surface mode|

## BATT5_ARM_VOLT: Required arming voltage

*Note: This parameter is for advanced users*

Battery voltage level which is required to arm the aircraft. Set to 0 to allow arming at any voltage.

- Units: V

- Increment: 0.1

## BATT5_ARM_MAH: Required arming remaining capacity

*Note: This parameter is for advanced users*

Battery capacity remaining which is required to arm the aircraft. Set to 0 to allow arming at any capacity. Note that execept for smart batteries rebooting the vehicle will always reset the remaining capacity estimate, which can lead to this check not providing sufficent protection, it is recommended to always use this in conjunction with the BATT5__ARM_VOLT parameter.

- Units: mAh

- Increment: 50

# BATT6 Parameters

## BATT6_MONITOR: Battery monitoring

Controls enabling monitoring of the battery's voltage and current

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|3|Analog Voltage Only|
|4|Analog Voltage and Current|
|5|Solo|
|6|Bebop|
|7|SMBus-Maxell|
|8|UAVCAN-BatteryInfo|
|9|BLHeli ESC|
|10|SumOfFollowing|
|11|FuelFlow|
|12|FuelLevelPWM|

- RebootRequired: True

## BATT6_VOLT_PIN: Battery Voltage sensing pin

Sets the analog input pin that should be used for voltage monitoring.

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
| 2|Pixhawk/Pixracer/Navio2/Pixhawk2_PM1|
| 13|Pixhawk2_PM2|
| 14|CubeOrange|
| 13|CubeOrange_PM2|
| 100|PX4-v1|

- RebootRequired: True

## BATT6_CURR_PIN: Battery Current sensing pin

Sets the analog input pin that should be used for current monitoring.

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
| 3|Pixhawk/Pixracer/Navio2/Pixhawk2_PM1|
| 14|Pixhawk2_PM2|
| 15|CubeOrange|
| 4|CubeOrange_PM2|
| 101|PX4-v1|

- RebootRequired: True

## BATT6_VOLT_MULT: Voltage Multiplier

*Note: This parameter is for advanced users*

Used to convert the voltage of the voltage sensing pin (BATT6_VOLT_PIN) to the actual battery's voltage (pin_voltage * VOLT_MULT). For the 3DR Power brick with a Pixhawk, this should be set to 10.1. For the Pixhawk with the 3DR 4in1 ESC this should be 12.02. For the PX using the PX4IO power supply this should be set to 1.

## BATT6_AMP_PERVLT: Amps per volt

Number of amps that a 1V reading on the current sensor corresponds to. With a Pixhawk using the 3DR Power brick this should be set to 17. For the Pixhawk with the 3DR 4in1 ESC this should be 17.

- Units: A/V

## BATT6_AMP_OFFSET: AMP offset

Voltage offset at zero current on current sensor

- Units: V

## BATT6_CAPACITY: Battery capacity

Capacity of the battery in mAh when full

- Units: mAh

- Increment: 50

## BATT6_WATT_MAX: Maximum allowed power (Watts)

*Note: This parameter is for advanced users*

If battery wattage (voltage * current) exceeds this value then the system will reduce max throttle (THR_MAX, TKOFF_THR_MAX and THR_MIN for reverse thrust) to satisfy this limit. This helps limit high current to low C rated batteries regardless of battery voltage. The max throttle will slowly grow back to THR_MAX (or TKOFF_THR_MAX ) and THR_MIN if demanding the current max and under the watt max. Use 0 to disable.

- Units: W

- Increment: 1

## BATT6_SERIAL_NUM: Battery serial number

*Note: This parameter is for advanced users*

Battery serial number, automatically filled in for SMBus batteries, otherwise will be -1. With UAVCAN it is the battery_id.

## BATT6_LOW_TIMER: Low voltage timeout

*Note: This parameter is for advanced users*

This is the timeout in seconds before a low voltage event will be triggered. For aircraft with low C batteries it may be necessary to raise this in order to cope with low voltage on long takeoffs. A value of zero disables low voltage errors.

- Units: s

- Increment: 1

- Range: 0 120

## BATT6_FS_VOLTSRC: Failsafe voltage source

*Note: This parameter is for advanced users*

Voltage type used for detection of low voltage event

|Value|Meaning|
|:---:|:---:|
|0|Raw Voltage|
| 1|Sag Compensated Voltage|

## BATT6_LOW_VOLT: Low battery voltage

Battery voltage that triggers a low battery failsafe. Set to 0 to disable. If the battery voltage drops below this voltage continuously for more then the period specified by the BATT6_LOW_TIMER parameter then the vehicle will perform the failsafe specified by the BATT6_FS_LOW_ACT parameter.

- Units: V

- Increment: 0.1

## BATT6_LOW_MAH: Low battery capacity

Battery capacity at which the low battery failsafe is triggered. Set to 0 to disable battery remaining failsafe. If the battery capacity drops below this level the vehicle will perform the failsafe specified by the BATT6_FS_LOW_ACT parameter.

- Units: mAh

- Increment: 50

## BATT6_CRT_VOLT: Critical battery voltage

Battery voltage that triggers a critical battery failsafe. Set to 0 to disable. If the battery voltage drops below this voltage continuously for more then the period specified by the BATT6_LOW_TIMER parameter then the vehicle will perform the failsafe specified by the BATT6_FS_CRT_ACT parameter.

- Units: V

- Increment: 0.1

## BATT6_CRT_MAH: Battery critical capacity

Battery capacity at which the critical battery failsafe is triggered. Set to 0 to disable battery remaining failsafe. If the battery capacity drops below this level the vehicle will perform the failsafe specified by the BATT6__FS_CRT_ACT parameter.

- Units: mAh

- Increment: 50

## BATT6_FS_LOW_ACT: Low battery failsafe action

What action the vehicle should perform if it hits a low battery failsafe

|Value|Meaning|
|:---:|:---:|
|0|None|
|2|Disarm|
|3|Enter surface mode|

## BATT6_FS_CRT_ACT: Critical battery failsafe action

What action the vehicle should perform if it hits a critical battery failsafe

|Value|Meaning|
|:---:|:---:|
|0|None|
|2|Disarm|
|3|Enter surface mode|

## BATT6_ARM_VOLT: Required arming voltage

*Note: This parameter is for advanced users*

Battery voltage level which is required to arm the aircraft. Set to 0 to allow arming at any voltage.

- Units: V

- Increment: 0.1

## BATT6_ARM_MAH: Required arming remaining capacity

*Note: This parameter is for advanced users*

Battery capacity remaining which is required to arm the aircraft. Set to 0 to allow arming at any capacity. Note that execept for smart batteries rebooting the vehicle will always reset the remaining capacity estimate, which can lead to this check not providing sufficent protection, it is recommended to always use this in conjunction with the BATT6__ARM_VOLT parameter.

- Units: mAh

- Increment: 50

# BATT7 Parameters

## BATT7_MONITOR: Battery monitoring

Controls enabling monitoring of the battery's voltage and current

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|3|Analog Voltage Only|
|4|Analog Voltage and Current|
|5|Solo|
|6|Bebop|
|7|SMBus-Maxell|
|8|UAVCAN-BatteryInfo|
|9|BLHeli ESC|
|10|SumOfFollowing|
|11|FuelFlow|
|12|FuelLevelPWM|

- RebootRequired: True

## BATT7_VOLT_PIN: Battery Voltage sensing pin

Sets the analog input pin that should be used for voltage monitoring.

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
| 2|Pixhawk/Pixracer/Navio2/Pixhawk2_PM1|
| 13|Pixhawk2_PM2|
| 14|CubeOrange|
| 13|CubeOrange_PM2|
| 100|PX4-v1|

- RebootRequired: True

## BATT7_CURR_PIN: Battery Current sensing pin

Sets the analog input pin that should be used for current monitoring.

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
| 3|Pixhawk/Pixracer/Navio2/Pixhawk2_PM1|
| 14|Pixhawk2_PM2|
| 15|CubeOrange|
| 4|CubeOrange_PM2|
| 101|PX4-v1|

- RebootRequired: True

## BATT7_VOLT_MULT: Voltage Multiplier

*Note: This parameter is for advanced users*

Used to convert the voltage of the voltage sensing pin (BATT7_VOLT_PIN) to the actual battery's voltage (pin_voltage * VOLT_MULT). For the 3DR Power brick with a Pixhawk, this should be set to 10.1. For the Pixhawk with the 3DR 4in1 ESC this should be 12.02. For the PX using the PX4IO power supply this should be set to 1.

## BATT7_AMP_PERVLT: Amps per volt

Number of amps that a 1V reading on the current sensor corresponds to. With a Pixhawk using the 3DR Power brick this should be set to 17. For the Pixhawk with the 3DR 4in1 ESC this should be 17.

- Units: A/V

## BATT7_AMP_OFFSET: AMP offset

Voltage offset at zero current on current sensor

- Units: V

## BATT7_CAPACITY: Battery capacity

Capacity of the battery in mAh when full

- Units: mAh

- Increment: 50

## BATT7_WATT_MAX: Maximum allowed power (Watts)

*Note: This parameter is for advanced users*

If battery wattage (voltage * current) exceeds this value then the system will reduce max throttle (THR_MAX, TKOFF_THR_MAX and THR_MIN for reverse thrust) to satisfy this limit. This helps limit high current to low C rated batteries regardless of battery voltage. The max throttle will slowly grow back to THR_MAX (or TKOFF_THR_MAX ) and THR_MIN if demanding the current max and under the watt max. Use 0 to disable.

- Units: W

- Increment: 1

## BATT7_SERIAL_NUM: Battery serial number

*Note: This parameter is for advanced users*

Battery serial number, automatically filled in for SMBus batteries, otherwise will be -1. With UAVCAN it is the battery_id.

## BATT7_LOW_TIMER: Low voltage timeout

*Note: This parameter is for advanced users*

This is the timeout in seconds before a low voltage event will be triggered. For aircraft with low C batteries it may be necessary to raise this in order to cope with low voltage on long takeoffs. A value of zero disables low voltage errors.

- Units: s

- Increment: 1

- Range: 0 120

## BATT7_FS_VOLTSRC: Failsafe voltage source

*Note: This parameter is for advanced users*

Voltage type used for detection of low voltage event

|Value|Meaning|
|:---:|:---:|
|0|Raw Voltage|
| 1|Sag Compensated Voltage|

## BATT7_LOW_VOLT: Low battery voltage

Battery voltage that triggers a low battery failsafe. Set to 0 to disable. If the battery voltage drops below this voltage continuously for more then the period specified by the BATT7_LOW_TIMER parameter then the vehicle will perform the failsafe specified by the BATT7_FS_LOW_ACT parameter.

- Units: V

- Increment: 0.1

## BATT7_LOW_MAH: Low battery capacity

Battery capacity at which the low battery failsafe is triggered. Set to 0 to disable battery remaining failsafe. If the battery capacity drops below this level the vehicle will perform the failsafe specified by the BATT7_FS_LOW_ACT parameter.

- Units: mAh

- Increment: 50

## BATT7_CRT_VOLT: Critical battery voltage

Battery voltage that triggers a critical battery failsafe. Set to 0 to disable. If the battery voltage drops below this voltage continuously for more then the period specified by the BATT7_LOW_TIMER parameter then the vehicle will perform the failsafe specified by the BATT7_FS_CRT_ACT parameter.

- Units: V

- Increment: 0.1

## BATT7_CRT_MAH: Battery critical capacity

Battery capacity at which the critical battery failsafe is triggered. Set to 0 to disable battery remaining failsafe. If the battery capacity drops below this level the vehicle will perform the failsafe specified by the BATT7__FS_CRT_ACT parameter.

- Units: mAh

- Increment: 50

## BATT7_FS_LOW_ACT: Low battery failsafe action

What action the vehicle should perform if it hits a low battery failsafe

|Value|Meaning|
|:---:|:---:|
|0|None|
|2|Disarm|
|3|Enter surface mode|

## BATT7_FS_CRT_ACT: Critical battery failsafe action

What action the vehicle should perform if it hits a critical battery failsafe

|Value|Meaning|
|:---:|:---:|
|0|None|
|2|Disarm|
|3|Enter surface mode|

## BATT7_ARM_VOLT: Required arming voltage

*Note: This parameter is for advanced users*

Battery voltage level which is required to arm the aircraft. Set to 0 to allow arming at any voltage.

- Units: V

- Increment: 0.1

## BATT7_ARM_MAH: Required arming remaining capacity

*Note: This parameter is for advanced users*

Battery capacity remaining which is required to arm the aircraft. Set to 0 to allow arming at any capacity. Note that execept for smart batteries rebooting the vehicle will always reset the remaining capacity estimate, which can lead to this check not providing sufficent protection, it is recommended to always use this in conjunction with the BATT7__ARM_VOLT parameter.

- Units: mAh

- Increment: 50

# BATT8 Parameters

## BATT8_MONITOR: Battery monitoring

Controls enabling monitoring of the battery's voltage and current

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|3|Analog Voltage Only|
|4|Analog Voltage and Current|
|5|Solo|
|6|Bebop|
|7|SMBus-Maxell|
|8|UAVCAN-BatteryInfo|
|9|BLHeli ESC|
|10|SumOfFollowing|
|11|FuelFlow|
|12|FuelLevelPWM|

- RebootRequired: True

## BATT8_VOLT_PIN: Battery Voltage sensing pin

Sets the analog input pin that should be used for voltage monitoring.

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
| 2|Pixhawk/Pixracer/Navio2/Pixhawk2_PM1|
| 13|Pixhawk2_PM2|
| 14|CubeOrange|
| 13|CubeOrange_PM2|
| 100|PX4-v1|

- RebootRequired: True

## BATT8_CURR_PIN: Battery Current sensing pin

Sets the analog input pin that should be used for current monitoring.

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
| 3|Pixhawk/Pixracer/Navio2/Pixhawk2_PM1|
| 14|Pixhawk2_PM2|
| 15|CubeOrange|
| 4|CubeOrange_PM2|
| 101|PX4-v1|

- RebootRequired: True

## BATT8_VOLT_MULT: Voltage Multiplier

*Note: This parameter is for advanced users*

Used to convert the voltage of the voltage sensing pin (BATT8_VOLT_PIN) to the actual battery's voltage (pin_voltage * VOLT_MULT). For the 3DR Power brick with a Pixhawk, this should be set to 10.1. For the Pixhawk with the 3DR 4in1 ESC this should be 12.02. For the PX using the PX4IO power supply this should be set to 1.

## BATT8_AMP_PERVLT: Amps per volt

Number of amps that a 1V reading on the current sensor corresponds to. With a Pixhawk using the 3DR Power brick this should be set to 17. For the Pixhawk with the 3DR 4in1 ESC this should be 17.

- Units: A/V

## BATT8_AMP_OFFSET: AMP offset

Voltage offset at zero current on current sensor

- Units: V

## BATT8_CAPACITY: Battery capacity

Capacity of the battery in mAh when full

- Units: mAh

- Increment: 50

## BATT8_WATT_MAX: Maximum allowed power (Watts)

*Note: This parameter is for advanced users*

If battery wattage (voltage * current) exceeds this value then the system will reduce max throttle (THR_MAX, TKOFF_THR_MAX and THR_MIN for reverse thrust) to satisfy this limit. This helps limit high current to low C rated batteries regardless of battery voltage. The max throttle will slowly grow back to THR_MAX (or TKOFF_THR_MAX ) and THR_MIN if demanding the current max and under the watt max. Use 0 to disable.

- Units: W

- Increment: 1

## BATT8_SERIAL_NUM: Battery serial number

*Note: This parameter is for advanced users*

Battery serial number, automatically filled in for SMBus batteries, otherwise will be -1. With UAVCAN it is the battery_id.

## BATT8_LOW_TIMER: Low voltage timeout

*Note: This parameter is for advanced users*

This is the timeout in seconds before a low voltage event will be triggered. For aircraft with low C batteries it may be necessary to raise this in order to cope with low voltage on long takeoffs. A value of zero disables low voltage errors.

- Units: s

- Increment: 1

- Range: 0 120

## BATT8_FS_VOLTSRC: Failsafe voltage source

*Note: This parameter is for advanced users*

Voltage type used for detection of low voltage event

|Value|Meaning|
|:---:|:---:|
|0|Raw Voltage|
| 1|Sag Compensated Voltage|

## BATT8_LOW_VOLT: Low battery voltage

Battery voltage that triggers a low battery failsafe. Set to 0 to disable. If the battery voltage drops below this voltage continuously for more then the period specified by the BATT8_LOW_TIMER parameter then the vehicle will perform the failsafe specified by the BATT8_FS_LOW_ACT parameter.

- Units: V

- Increment: 0.1

## BATT8_LOW_MAH: Low battery capacity

Battery capacity at which the low battery failsafe is triggered. Set to 0 to disable battery remaining failsafe. If the battery capacity drops below this level the vehicle will perform the failsafe specified by the BATT8_FS_LOW_ACT parameter.

- Units: mAh

- Increment: 50

## BATT8_CRT_VOLT: Critical battery voltage

Battery voltage that triggers a critical battery failsafe. Set to 0 to disable. If the battery voltage drops below this voltage continuously for more then the period specified by the BATT8_LOW_TIMER parameter then the vehicle will perform the failsafe specified by the BATT8_FS_CRT_ACT parameter.

- Units: V

- Increment: 0.1

## BATT8_CRT_MAH: Battery critical capacity

Battery capacity at which the critical battery failsafe is triggered. Set to 0 to disable battery remaining failsafe. If the battery capacity drops below this level the vehicle will perform the failsafe specified by the BATT8__FS_CRT_ACT parameter.

- Units: mAh

- Increment: 50

## BATT8_FS_LOW_ACT: Low battery failsafe action

What action the vehicle should perform if it hits a low battery failsafe

|Value|Meaning|
|:---:|:---:|
|0|None|
|2|Disarm|
|3|Enter surface mode|

## BATT8_FS_CRT_ACT: Critical battery failsafe action

What action the vehicle should perform if it hits a critical battery failsafe

|Value|Meaning|
|:---:|:---:|
|0|None|
|2|Disarm|
|3|Enter surface mode|

## BATT8_ARM_VOLT: Required arming voltage

*Note: This parameter is for advanced users*

Battery voltage level which is required to arm the aircraft. Set to 0 to allow arming at any voltage.

- Units: V

- Increment: 0.1

## BATT8_ARM_MAH: Required arming remaining capacity

*Note: This parameter is for advanced users*

Battery capacity remaining which is required to arm the aircraft. Set to 0 to allow arming at any capacity. Note that execept for smart batteries rebooting the vehicle will always reset the remaining capacity estimate, which can lead to this check not providing sufficent protection, it is recommended to always use this in conjunction with the BATT8__ARM_VOLT parameter.

- Units: mAh

- Increment: 50

# BATT9 Parameters

## BATT9_MONITOR: Battery monitoring

Controls enabling monitoring of the battery's voltage and current

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|3|Analog Voltage Only|
|4|Analog Voltage and Current|
|5|Solo|
|6|Bebop|
|7|SMBus-Maxell|
|8|UAVCAN-BatteryInfo|
|9|BLHeli ESC|
|10|SumOfFollowing|
|11|FuelFlow|
|12|FuelLevelPWM|

- RebootRequired: True

## BATT9_VOLT_PIN: Battery Voltage sensing pin

Sets the analog input pin that should be used for voltage monitoring.

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
| 2|Pixhawk/Pixracer/Navio2/Pixhawk2_PM1|
| 13|Pixhawk2_PM2|
| 14|CubeOrange|
| 13|CubeOrange_PM2|
| 100|PX4-v1|

- RebootRequired: True

## BATT9_CURR_PIN: Battery Current sensing pin

Sets the analog input pin that should be used for current monitoring.

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
| 3|Pixhawk/Pixracer/Navio2/Pixhawk2_PM1|
| 14|Pixhawk2_PM2|
| 15|CubeOrange|
| 4|CubeOrange_PM2|
| 101|PX4-v1|

- RebootRequired: True

## BATT9_VOLT_MULT: Voltage Multiplier

*Note: This parameter is for advanced users*

Used to convert the voltage of the voltage sensing pin (BATT9_VOLT_PIN) to the actual battery's voltage (pin_voltage * VOLT_MULT). For the 3DR Power brick with a Pixhawk, this should be set to 10.1. For the Pixhawk with the 3DR 4in1 ESC this should be 12.02. For the PX using the PX4IO power supply this should be set to 1.

## BATT9_AMP_PERVLT: Amps per volt

Number of amps that a 1V reading on the current sensor corresponds to. With a Pixhawk using the 3DR Power brick this should be set to 17. For the Pixhawk with the 3DR 4in1 ESC this should be 17.

- Units: A/V

## BATT9_AMP_OFFSET: AMP offset

Voltage offset at zero current on current sensor

- Units: V

## BATT9_CAPACITY: Battery capacity

Capacity of the battery in mAh when full

- Units: mAh

- Increment: 50

## BATT9_WATT_MAX: Maximum allowed power (Watts)

*Note: This parameter is for advanced users*

If battery wattage (voltage * current) exceeds this value then the system will reduce max throttle (THR_MAX, TKOFF_THR_MAX and THR_MIN for reverse thrust) to satisfy this limit. This helps limit high current to low C rated batteries regardless of battery voltage. The max throttle will slowly grow back to THR_MAX (or TKOFF_THR_MAX ) and THR_MIN if demanding the current max and under the watt max. Use 0 to disable.

- Units: W

- Increment: 1

## BATT9_SERIAL_NUM: Battery serial number

*Note: This parameter is for advanced users*

Battery serial number, automatically filled in for SMBus batteries, otherwise will be -1. With UAVCAN it is the battery_id.

## BATT9_LOW_TIMER: Low voltage timeout

*Note: This parameter is for advanced users*

This is the timeout in seconds before a low voltage event will be triggered. For aircraft with low C batteries it may be necessary to raise this in order to cope with low voltage on long takeoffs. A value of zero disables low voltage errors.

- Units: s

- Increment: 1

- Range: 0 120

## BATT9_FS_VOLTSRC: Failsafe voltage source

*Note: This parameter is for advanced users*

Voltage type used for detection of low voltage event

|Value|Meaning|
|:---:|:---:|
|0|Raw Voltage|
| 1|Sag Compensated Voltage|

## BATT9_LOW_VOLT: Low battery voltage

Battery voltage that triggers a low battery failsafe. Set to 0 to disable. If the battery voltage drops below this voltage continuously for more then the period specified by the BATT9_LOW_TIMER parameter then the vehicle will perform the failsafe specified by the BATT9_FS_LOW_ACT parameter.

- Units: V

- Increment: 0.1

## BATT9_LOW_MAH: Low battery capacity

Battery capacity at which the low battery failsafe is triggered. Set to 0 to disable battery remaining failsafe. If the battery capacity drops below this level the vehicle will perform the failsafe specified by the BATT9_FS_LOW_ACT parameter.

- Units: mAh

- Increment: 50

## BATT9_CRT_VOLT: Critical battery voltage

Battery voltage that triggers a critical battery failsafe. Set to 0 to disable. If the battery voltage drops below this voltage continuously for more then the period specified by the BATT9_LOW_TIMER parameter then the vehicle will perform the failsafe specified by the BATT9_FS_CRT_ACT parameter.

- Units: V

- Increment: 0.1

## BATT9_CRT_MAH: Battery critical capacity

Battery capacity at which the critical battery failsafe is triggered. Set to 0 to disable battery remaining failsafe. If the battery capacity drops below this level the vehicle will perform the failsafe specified by the BATT9__FS_CRT_ACT parameter.

- Units: mAh

- Increment: 50

## BATT9_FS_LOW_ACT: Low battery failsafe action

What action the vehicle should perform if it hits a low battery failsafe

|Value|Meaning|
|:---:|:---:|
|0|None|
|2|Disarm|
|3|Enter surface mode|

## BATT9_FS_CRT_ACT: Critical battery failsafe action

What action the vehicle should perform if it hits a critical battery failsafe

|Value|Meaning|
|:---:|:---:|
|0|None|
|2|Disarm|
|3|Enter surface mode|

## BATT9_ARM_VOLT: Required arming voltage

*Note: This parameter is for advanced users*

Battery voltage level which is required to arm the aircraft. Set to 0 to allow arming at any voltage.

- Units: V

- Increment: 0.1

## BATT9_ARM_MAH: Required arming remaining capacity

*Note: This parameter is for advanced users*

Battery capacity remaining which is required to arm the aircraft. Set to 0 to allow arming at any capacity. Note that execept for smart batteries rebooting the vehicle will always reset the remaining capacity estimate, which can lead to this check not providing sufficent protection, it is recommended to always use this in conjunction with the BATT9__ARM_VOLT parameter.

- Units: mAh

- Increment: 50

# BATT Parameters

## BATT_MONITOR: Battery monitoring

Controls enabling monitoring of the battery's voltage and current

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|3|Analog Voltage Only|
|4|Analog Voltage and Current|
|5|Solo|
|6|Bebop|
|7|SMBus-Maxell|
|8|UAVCAN-BatteryInfo|
|9|BLHeli ESC|
|10|SumOfFollowing|
|11|FuelFlow|
|12|FuelLevelPWM|

- RebootRequired: True

## BATT_VOLT_PIN: Battery Voltage sensing pin

Sets the analog input pin that should be used for voltage monitoring.

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
| 2|Pixhawk/Pixracer/Navio2/Pixhawk2_PM1|
| 13|Pixhawk2_PM2|
| 14|CubeOrange|
| 13|CubeOrange_PM2|
| 100|PX4-v1|

- RebootRequired: True

## BATT_CURR_PIN: Battery Current sensing pin

Sets the analog input pin that should be used for current monitoring.

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
| 3|Pixhawk/Pixracer/Navio2/Pixhawk2_PM1|
| 14|Pixhawk2_PM2|
| 15|CubeOrange|
| 4|CubeOrange_PM2|
| 101|PX4-v1|

- RebootRequired: True

## BATT_VOLT_MULT: Voltage Multiplier

*Note: This parameter is for advanced users*

Used to convert the voltage of the voltage sensing pin (BATT_VOLT_PIN) to the actual battery's voltage (pin_voltage * VOLT_MULT). For the 3DR Power brick with a Pixhawk, this should be set to 10.1. For the Pixhawk with the 3DR 4in1 ESC this should be 12.02. For the PX using the PX4IO power supply this should be set to 1.

## BATT_AMP_PERVLT: Amps per volt

Number of amps that a 1V reading on the current sensor corresponds to. With a Pixhawk using the 3DR Power brick this should be set to 17. For the Pixhawk with the 3DR 4in1 ESC this should be 17.

- Units: A/V

## BATT_AMP_OFFSET: AMP offset

Voltage offset at zero current on current sensor

- Units: V

## BATT_CAPACITY: Battery capacity

Capacity of the battery in mAh when full

- Units: mAh

- Increment: 50

## BATT_WATT_MAX: Maximum allowed power (Watts)

*Note: This parameter is for advanced users*

If battery wattage (voltage * current) exceeds this value then the system will reduce max throttle (THR_MAX, TKOFF_THR_MAX and THR_MIN for reverse thrust) to satisfy this limit. This helps limit high current to low C rated batteries regardless of battery voltage. The max throttle will slowly grow back to THR_MAX (or TKOFF_THR_MAX ) and THR_MIN if demanding the current max and under the watt max. Use 0 to disable.

- Units: W

- Increment: 1

## BATT_SERIAL_NUM: Battery serial number

*Note: This parameter is for advanced users*

Battery serial number, automatically filled in for SMBus batteries, otherwise will be -1. With UAVCAN it is the battery_id.

## BATT_LOW_TIMER: Low voltage timeout

*Note: This parameter is for advanced users*

This is the timeout in seconds before a low voltage event will be triggered. For aircraft with low C batteries it may be necessary to raise this in order to cope with low voltage on long takeoffs. A value of zero disables low voltage errors.

- Units: s

- Increment: 1

- Range: 0 120

## BATT_FS_VOLTSRC: Failsafe voltage source

*Note: This parameter is for advanced users*

Voltage type used for detection of low voltage event

|Value|Meaning|
|:---:|:---:|
|0|Raw Voltage|
| 1|Sag Compensated Voltage|

## BATT_LOW_VOLT: Low battery voltage

Battery voltage that triggers a low battery failsafe. Set to 0 to disable. If the battery voltage drops below this voltage continuously for more then the period specified by the BATT_LOW_TIMER parameter then the vehicle will perform the failsafe specified by the BATT_FS_LOW_ACT parameter.

- Units: V

- Increment: 0.1

## BATT_LOW_MAH: Low battery capacity

Battery capacity at which the low battery failsafe is triggered. Set to 0 to disable battery remaining failsafe. If the battery capacity drops below this level the vehicle will perform the failsafe specified by the BATT_FS_LOW_ACT parameter.

- Units: mAh

- Increment: 50

## BATT_CRT_VOLT: Critical battery voltage

Battery voltage that triggers a critical battery failsafe. Set to 0 to disable. If the battery voltage drops below this voltage continuously for more then the period specified by the BATT_LOW_TIMER parameter then the vehicle will perform the failsafe specified by the BATT_FS_CRT_ACT parameter.

- Units: V

- Increment: 0.1

## BATT_CRT_MAH: Battery critical capacity

Battery capacity at which the critical battery failsafe is triggered. Set to 0 to disable battery remaining failsafe. If the battery capacity drops below this level the vehicle will perform the failsafe specified by the BATT__FS_CRT_ACT parameter.

- Units: mAh

- Increment: 50

## BATT_FS_LOW_ACT: Low battery failsafe action

What action the vehicle should perform if it hits a low battery failsafe

|Value|Meaning|
|:---:|:---:|
|0|None|
|2|Disarm|
|3|Enter surface mode|

## BATT_FS_CRT_ACT: Critical battery failsafe action

What action the vehicle should perform if it hits a critical battery failsafe

|Value|Meaning|
|:---:|:---:|
|0|None|
|2|Disarm|
|3|Enter surface mode|

## BATT_ARM_VOLT: Required arming voltage

*Note: This parameter is for advanced users*

Battery voltage level which is required to arm the aircraft. Set to 0 to allow arming at any voltage.

- Units: V

- Increment: 0.1

## BATT_ARM_MAH: Required arming remaining capacity

*Note: This parameter is for advanced users*

Battery capacity remaining which is required to arm the aircraft. Set to 0 to allow arming at any capacity. Note that execept for smart batteries rebooting the vehicle will always reset the remaining capacity estimate, which can lead to this check not providing sufficent protection, it is recommended to always use this in conjunction with the BATT__ARM_VOLT parameter.

- Units: mAh

- Increment: 50

# BRD Parameters

## BRD_PWM_COUNT: Auxiliary pin config

*Note: This parameter is for advanced users*

Controls number of FMU outputs which are setup for PWM. All unassigned pins can be used for GPIO

|Value|Meaning|
|:---:|:---:|
|0|No PWMs|
|1|One PWMs|
|2|Two PWMs|
|3|Three PWMs|
|4|Four PWMs|
|5|Five PWMs|
|6|Six PWMs|
|7|Seven PWMs|
|8|Eight PWMs|

- RebootRequired: True

## BRD_SER1_RTSCTS: Serial 1 flow control

*Note: This parameter is for advanced users*

Enable flow control on serial 1 (telemetry 1) on Pixhawk. You must have the RTS and CTS pins connected to your radio. The standard DF13 6 pin connector for a 3DR radio does have those pins connected. If this is set to 2 then flow control will be auto-detected by checking for the output buffer filling on startup. Note that the PX4v1 does not have hardware flow control pins on this port, so you should leave this disabled.

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|
|2|Auto|

- RebootRequired: True

## BRD_SER2_RTSCTS: Serial 2 flow control

*Note: This parameter is for advanced users*

Enable flow control on serial 2 (telemetry 2) on Pixhawk and STATE. You must have the RTS and CTS pins connected to your radio. The standard DF13 6 pin connector for a 3DR radio does have those pins connected. If this is set to 2 then flow control will be auto-detected by checking for the output buffer filling on startup.

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|
|2|Auto|

- RebootRequired: True

## BRD_SAFETYENABLE: Enable use of safety arming switch

This controls the default state of the safety switch at startup. When set to 1 the safety switch will start in the safe state (flashing) at boot. When set to zero the safety switch will start in the unsafe state (solid) at startup. Note that if a safety switch is fitted the user can still control the safety state after startup using the switch. The safety state can also be controlled in software using a MAVLink message.

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|

- RebootRequired: True

## BRD_SBUS_OUT:  SBUS output rate

*Note: This parameter is for advanced users*

This sets the SBUS output frame rate in Hz

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|50Hz|
|2|75Hz|
|3|100Hz|
|4|150Hz|
|5|200Hz|
|6|250Hz|
|7|300Hz|

- RebootRequired: True

## BRD_SERIAL_NUM: User-defined serial number

User-defined serial number of this vehicle, it can be any arbitrary number you want and has no effect on the autopilot

- Range: -32768 32767

## BRD_SAFETY_MASK: Channels which ignore the safety switch state

*Note: This parameter is for advanced users*

A bitmask which controls what channels can move while the safety switch has not been pressed

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|

- Bitmask: 0:Ch1,1:Ch2,2:Ch3,3:Ch4,4:Ch5,5:Ch6,6:Ch7,7:Ch8,8:Ch9,9:Ch10,10:Ch11,11:Ch12,12:Ch13,13:Ch14

- RebootRequired: True

## BRD_IMU_TARGTEMP: Target IMU temperature

*Note: This parameter is for advanced users*

This sets the target IMU temperature for boards with controllable IMU heating units. DO NOT SET -1 on The Cube. A value of -1 sets PH1 behaviour 

- Range: -1 80

- Units: degC

## BRD_TYPE: Board type

*Note: This parameter is for advanced users*

This allows selection of a PX4 or VRBRAIN board type. If set to zero then the board type is auto-detected (PX4)

|Value|Meaning|
|:---:|:---:|
|0|AUTO|
|1|PX4V1|
|2|Pixhawk|
|3|Cube/Pixhawk2|
|4|Pixracer|
|5|PixhawkMini|
|6|Pixhawk2Slim|
|7|VRBrain 5.1|
|8|VRBrain 5.2|
|9|VR Micro Brain 5.1|
|10|VR Micro Brain 5.2|
|11|VRBrain Core 1.0|
|12|VRBrain 5.4|
|13|Intel Aero FC|
|20|AUAV2.1|

- RebootRequired: True

## BRD_IO_ENABLE: Enable IO co-processor

*Note: This parameter is for advanced users*

This allows for the IO co-processor on FMUv1 and FMUv2 to be disabled

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|

- RebootRequired: True

## BRD_SAFETYOPTION: Options for safety button behavior

This controls the activation of the safety button. It allows you to control if the safety button can be used for safety enable and/or disable, and whether the button is only active when disarmed

- Bitmask: 0:ActiveForSafetyEnable,1:ActiveForSafetyDisable,2:ActiveWhenArmed,3:Force safety on when the aircraft disarms

## BRD_VBUS_MIN: Autopilot board voltage requirement

*Note: This parameter is for advanced users*

Minimum voltage on the autopilot power rail to allow the aircraft to arm. 0 to disable the check.

- Units: V

- Range: 4.0 5.5

- Increment: 0.1

## BRD_VSERVO_MIN: Servo voltage requirement

*Note: This parameter is for advanced users*

Minimum voltage on the servo rail to allow the aircraft to arm. 0 to disable the check.

- Units: V

- Range: 3.3 12.0

- Increment: 0.1

## BRD_SD_SLOWDOWN: microSD slowdown

*Note: This parameter is for advanced users*

This is a scaling factor to slow down microSD operation. It can be used on flight board and microSD card combinations where full speed is not reliable. For normal full speed operation a value of 0 should be used.

- Range: 0 32

- Increment: 1

## BRD_PWM_VOLT_SEL: Set PWM Out Voltage

*Note: This parameter is for advanced users*

This sets the voltage max for PWM output pulses. 0 for 3.3V and 1 for 5V output.

|Value|Meaning|
|:---:|:---:|
|0|3.3V|
|1|5V|

## BRD_OPTIONS: Board options

*Note: This parameter is for advanced users*

Board specific option flags

- Bitmask: 0:Enable hardware watchdog

## BRD_BOOT_DELAY: Boot delay

*Note: This parameter is for advanced users*

This adds a delay in milliseconds to boot to ensure peripherals initialise fully

- Range: 0 10000

- Units: ms

# BRDRADIO Parameters

## BRD_RADIO_TYPE: Set type of direct attached radio

This enables support for direct attached radio receivers

|Value|Meaning|
|:---:|:---:|
|0|None|
|1|CYRF6936|
|2|CC2500|
|3|BK2425|

## BRD_RADIO_PROT: protocol

*Note: This parameter is for advanced users*

Select air protocol

|Value|Meaning|
|:---:|:---:|
|0|Auto|
|1|DSM2|
|2|DSMX|

## BRD_RADIO_DEBUG: debug level

*Note: This parameter is for advanced users*

radio debug level

- Range: 0 4

## BRD_RADIO_DISCRC: disable receive CRC

*Note: This parameter is for advanced users*

disable receive CRC (for debug)

|Value|Meaning|
|:---:|:---:|
|0|NotDisabled|
|1|Disabled|

## BRD_RADIO_SIGCH: RSSI signal strength

*Note: This parameter is for advanced users*

Channel to show receive RSSI signal strength, or zero for disabled

- Range: 0 16

## BRD_RADIO_PPSCH: Packet rate channel

*Note: This parameter is for advanced users*

Channel to show received packet-per-second rate, or zero for disabled

- Range: 0 16

## BRD_RADIO_TELEM: Enable telemetry

*Note: This parameter is for advanced users*

If this is non-zero then telemetry packets will be sent over DSM

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|

## BRD_RADIO_TXPOW: Telemetry Transmit power

*Note: This parameter is for advanced users*

Set telemetry transmit power. This is the power level (from 1 to 8) for telemetry packets sent from the RX to the TX

- Range: 1 8

## BRD_RADIO_FCCTST: Put radio into FCC test mode

*Note: This parameter is for advanced users*

If this is enabled then the radio will continuously transmit as required for FCC testing. The transmit channel is set by the value of the parameter. The radio will not work for RC input while this is enabled

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|MinChannel|
|2|MidChannel|
|3|MaxChannel|
|4|MinChannelCW|
|5|MidChannelCW|
|6|MaxChannelCW|

## BRD_RADIO_STKMD: Stick input mode

*Note: This parameter is for advanced users*

This selects between different stick input modes. The default is mode2, which has throttle on the left stick and pitch on the right stick. You can instead set mode1, which has throttle on the right stick and pitch on the left stick.

|Value|Meaning|
|:---:|:---:|
|1|Mode1|
|2|Mode2|

## BRD_RADIO_TESTCH: Set radio to factory test channel

*Note: This parameter is for advanced users*

This sets the radio to a fixed test channel for factory testing. Using a fixed channel avoids the need for binding in factory testing.

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|TestChan1|
|2|TestChan2|
|3|TestChan3|
|4|TestChan4|
|5|TestChan5|
|6|TestChan6|
|7|TestChan7|
|8|TestChan8|

## BRD_RADIO_TSIGCH: RSSI value channel for telemetry data on transmitter

*Note: This parameter is for advanced users*

Channel to show telemetry RSSI value as received by TX

- Range: 0 16

## BRD_RADIO_TPPSCH: Telemetry PPS channel

*Note: This parameter is for advanced users*

Channel to show telemetry packets-per-second value, as received at TX

- Range: 0 16

## BRD_RADIO_TXMAX: Transmitter transmit power

*Note: This parameter is for advanced users*

Set transmitter maximum transmit power (from 1 to 8)

- Range: 1 8

## BRD_RADIO_BZOFS: Transmitter buzzer adjustment

*Note: This parameter is for advanced users*

Set transmitter buzzer note adjustment (adjust frequency up)

- Range: 0 40

## BRD_RADIO_ABTIME: Auto-bind time

*Note: This parameter is for advanced users*

When non-zero this sets the time with no transmitter packets before we start looking for auto-bind packets.

- Range: 0 120

## BRD_RADIO_ABLVL: Auto-bind level

*Note: This parameter is for advanced users*

This sets the minimum RSSI of an auto-bind packet for it to be accepted. This should be set so that auto-bind will only happen at short range to minimise the change of an auto-bind happening accidentially

- Range: 0 31

# BRDRTC Parameters

## BRD_RTC_TYPES: Allowed sources of RTC time

*Note: This parameter is for advanced users*

Specifies which sources of UTC time will be accepted

- Bitmask: 0:GPS,1:MAVLINK_SYSTEM_TIME,2:HW

# BTNn Parameters

## BTNn_FUNCTION: Function for button

Set to 0 to disable or choose a function

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|shift|
|2|arm_toggle|
|3|arm|
|4|disarm|
|5|mode_manual|
|6|mode_stabilize|
|7|mode_depth_hold|
|8|mode_poshold|
|9|mode_auto|
|10|mode_circle|
|11|mode_guided|
|12|mode_acro|
|21|mount_center|
|22|mount_tilt_up|
|23|mount_tilt_down|
|24|camera_trigger|
|25|camera_source_toggle|
|26|mount_pan_right|
|27|mount_pan_left|
|31|lights1_cycle|
|32|lights1_brighter|
|33|lights1_dimmer|
|34|lights2_cycle|
|35|lights2_brighter|
|36|lights2_dimmer|
|41|gain_toggle|
|42|gain_inc|
|43|gain_dec|
|44|trim_roll_inc|
|45|trim_roll_dec|
|46|trim_pitch_inc|
|47|trim_pitch_dec|
|48|input_hold_set|
|49|roll_pitch_toggle|
|51|relay_1_on|
|52|relay_1_off|
|53|relay_1_toggle|
|54|relay_2_on|
|55|relay_2_off|
|56|relay_2_toggle|
|57|relay_3_on|
|58|relay_3_off|
|59|relay_3_toggle|
|61|servo_1_inc|
|62|servo_1_dec|
|63|servo_1_min|
|64|servo_1_max|
|65|servo_1_center|
|66|servo_2_inc|
|67|servo_2_dec|
|68|servo_2_min|
|69|servo_2_max|
|70|servo_2_center|
|71|servo_3_inc|
|72|servo_3_dec|
|73|servo_3_min|
|74|servo_3_max|
|75|servo_3_center|
|76|servo_1_min_momentary|
|77|servo_1_max_momentary|
|78|servo_1_min_toggle|
|79|servo_1_max_toggle|
|80|servo_2_min_momentary|
|81|servo_2_max_momentary|
|82|servo_2_min_toggle|
|83|servo_2_max_toggle|
|84|servo_3_min_momentary|
|85|servo_3_max_momentary|
|86|servo_3_min_toggle|
|87|servo_3_max_toggle|
|91|custom_1|
|92|custom_2|
|93|custom_3|
|94|custom_4|
|95|custom_5|
|96|custom_6|
|101|relay_4_on|
|102|relay_4_off|
|103|relay_4_toggle|
|104|relay_1_momentary|
|105|relay_2_momentary|
|106|relay_3_momentary|
|107|relay_4_momentary|

## BTNn_SFUNCTION: Function for button when the shift mode is toggled on

Set to 0 to disable or choose a function

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|shift|
|2|arm_toggle|
|3|arm|
|4|disarm|
|5|mode_manual|
|6|mode_stabilize|
|7|mode_depth_hold|
|8|mode_poshold|
|9|mode_auto|
|10|mode_circle|
|11|mode_guided|
|12|mode_acro|
|21|mount_center|
|22|mount_tilt_up|
|23|mount_tilt_down|
|24|camera_trigger|
|25|camera_source_toggle|
|26|mount_pan_right|
|27|mount_pan_left|
|31|lights1_cycle|
|32|lights1_brighter|
|33|lights1_dimmer|
|34|lights2_cycle|
|35|lights2_brighter|
|36|lights2_dimmer|
|41|gain_toggle|
|42|gain_inc|
|43|gain_dec|
|44|trim_roll_inc|
|45|trim_roll_dec|
|46|trim_pitch_inc|
|47|trim_pitch_dec|
|48|input_hold_set|
|49|roll_pitch_toggle|
|51|relay_1_on|
|52|relay_1_off|
|53|relay_1_toggle|
|54|relay_2_on|
|55|relay_2_off|
|56|relay_2_toggle|
|57|relay_3_on|
|58|relay_3_off|
|59|relay_3_toggle|
|61|servo_1_inc|
|62|servo_1_dec|
|63|servo_1_min|
|64|servo_1_max|
|65|servo_1_center|
|66|servo_2_inc|
|67|servo_2_dec|
|68|servo_2_min|
|69|servo_2_max|
|70|servo_2_center|
|71|servo_3_inc|
|72|servo_3_dec|
|73|servo_3_min|
|74|servo_3_max|
|75|servo_3_center|
|76|servo_1_min_momentary|
|77|servo_1_max_momentary|
|78|servo_1_min_toggle|
|79|servo_1_max_toggle|
|80|servo_2_min_momentary|
|81|servo_2_max_momentary|
|82|servo_2_min_toggle|
|83|servo_2_max_toggle|
|84|servo_3_min_momentary|
|85|servo_3_max_momentary|
|86|servo_3_min_toggle|
|87|servo_3_max_toggle|
|91|custom_1|
|92|custom_2|
|93|custom_3|
|94|custom_4|
|95|custom_5|
|96|custom_6|
|101|relay_4_on|
|102|relay_4_off|
|103|relay_4_toggle|
|104|relay_1_momentary|
|105|relay_2_momentary|
|106|relay_3_momentary|
|107|relay_4_momentary|

# CAM Parameters

## CAM_TRIGG_TYPE: Camera shutter (trigger) type

how to trigger the camera to take a picture

|Value|Meaning|
|:---:|:---:|
|0|Servo|
|1|Relay|

## CAM_DURATION: Duration that shutter is held open

How long the shutter will be held open in 10ths of a second (i.e. enter 10 for 1second, 50 for 5seconds)

- Units: ds

- Range: 0 50

## CAM_SERVO_ON: Servo ON PWM value

PWM value in microseconds to move servo to when shutter is activated

- Units: PWM

- Range: 1000 2000

## CAM_SERVO_OFF: Servo OFF PWM value

PWM value in microseconds to move servo to when shutter is deactivated

- Units: PWM

- Range: 1000 2000

## CAM_TRIGG_DIST: Camera trigger distance

Distance in meters between camera triggers. If this value is non-zero then the camera will trigger whenever the GPS position changes by this number of meters regardless of what mode the APM is in. Note that this parameter can also be set in an auto mission using the DO_SET_CAM_TRIGG_DIST command, allowing you to enable/disable the triggering of the camera during the flight.

- Units: m

- Range: 0 1000

## CAM_RELAY_ON: Relay ON value

This sets whether the relay goes high or low when it triggers. Note that you should also set RELAY_DEFAULT appropriately for your camera

|Value|Meaning|
|:---:|:---:|
|0|Low|
|1|High|

## CAM_MIN_INTERVAL: Minimum time between photos

Postpone shooting if previous picture was taken less than preset time(ms) ago.

- Units: ms

- Range: 0 10000

## CAM_MAX_ROLL: Maximum photo roll angle.

Postpone shooting if roll is greater than limit. (0=Disable, will shoot regardless of roll).

- Units: deg

- Range: 0 180

## CAM_FEEDBACK_PIN: Camera feedback pin

pin number to use for save accurate camera feedback messages. If set to -1 then don't use a pin flag for this, otherwise this is a pin number which if held high after a picture trigger order, will save camera messages when camera really takes a picture. A universal camera hot shoe is needed. The pin should be held high for at least 2 milliseconds for reliable trigger detection. See also the CAM_FEEDBACK_POL option.

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
|50|AUX1|
|51|AUX2|
|52|AUX3|
|53|AUX4|
|54|AUX5|
|55|AUX6|

- RebootRequired: True

## CAM_FEEDBACK_POL: Camera feedback pin polarity

Polarity for feedback pin. If this is 1 then the feedback pin should go high on trigger. If set to 0 then it should go low

|Value|Meaning|
|:---:|:---:|
|0|TriggerLow|
|1|TriggerHigh|

## CAM_AUTO_ONLY: Distance-trigging in AUTO mode only

When enabled, trigging by distance is done in AUTO mode only.

|Value|Meaning|
|:---:|:---:|
|0|Always|
|1|Only when in AUTO|

## CAM_TYPE: Type of camera (0: None, 1: BMMCC)

Set the camera type that is being used, certain cameras have custom functions that need further configuration, this enables that.

|Value|Meaning|
|:---:|:---:|
|0|Default|
|1|BMMCC|

# CAND1 Parameters

## CAN_D1_PROTOCOL: Enable use of specific protocol over virtual driver

*Note: This parameter is for advanced users*

Enabling this option starts selected protocol that will use this virtual driver

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|UAVCAN|
|2|KDECAN|
|3|ToshibaCAN|

- RebootRequired: True

# CAND1KDE Parameters

## CAN_D1_KDE_NPOLE: Number of motor poles

Sets the number of motor poles to calculate the correct RPM value

# CAND1UC Parameters

## CAN_D1_UC_NODE: UAVCAN node that is used for this network

*Note: This parameter is for advanced users*

UAVCAN node should be set implicitly

- Range: 1 250

## CAN_D1_UC_SRV_BM: RC Out channels to be transmitted as servo over UAVCAN

*Note: This parameter is for advanced users*

Bitmask with one set for channel to be transmitted as a servo command over UAVCAN

- Bitmask: 0: Servo 1, 1: Servo 2, 2: Servo 3, 3: Servo 4, 4: Servo 5, 5: Servo 6, 6: Servo 7, 7: Servo 8, 8: Servo 9, 9: Servo 10, 10: Servo 11, 11: Servo 12, 12: Servo 13, 13: Servo 14, 14: Servo 15

## CAN_D1_UC_ESC_BM: RC Out channels to be transmitted as ESC over UAVCAN

*Note: This parameter is for advanced users*

Bitmask with one set for channel to be transmitted as a ESC command over UAVCAN

- Bitmask: 0: ESC 1, 1: ESC 2, 2: ESC 3, 3: ESC 4, 4: ESC 5, 5: ESC 6, 6: ESC 7, 7: ESC 8, 8: ESC 9, 9: ESC 10, 10: ESC 11, 11: ESC 12, 12: ESC 13, 13: ESC 14, 14: ESC 15, 15: ESC 16

## CAN_D1_UC_SRV_RT: Servo output rate

*Note: This parameter is for advanced users*

Maximum transmit rate for servo outputs

- Range: 1 200

- Units: Hz

# CAND2 Parameters

## CAN_D2_PROTOCOL: Enable use of specific protocol over virtual driver

*Note: This parameter is for advanced users*

Enabling this option starts selected protocol that will use this virtual driver

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|UAVCAN|
|2|KDECAN|
|3|ToshibaCAN|

- RebootRequired: True

# CAND2KDE Parameters

## CAN_D2_KDE_NPOLE: Number of motor poles

Sets the number of motor poles to calculate the correct RPM value

# CAND2UC Parameters

## CAN_D2_UC_NODE: UAVCAN node that is used for this network

*Note: This parameter is for advanced users*

UAVCAN node should be set implicitly

- Range: 1 250

## CAN_D2_UC_SRV_BM: RC Out channels to be transmitted as servo over UAVCAN

*Note: This parameter is for advanced users*

Bitmask with one set for channel to be transmitted as a servo command over UAVCAN

- Bitmask: 0: Servo 1, 1: Servo 2, 2: Servo 3, 3: Servo 4, 4: Servo 5, 5: Servo 6, 6: Servo 7, 7: Servo 8, 8: Servo 9, 9: Servo 10, 10: Servo 11, 11: Servo 12, 12: Servo 13, 13: Servo 14, 14: Servo 15

## CAN_D2_UC_ESC_BM: RC Out channels to be transmitted as ESC over UAVCAN

*Note: This parameter is for advanced users*

Bitmask with one set for channel to be transmitted as a ESC command over UAVCAN

- Bitmask: 0: ESC 1, 1: ESC 2, 2: ESC 3, 3: ESC 4, 4: ESC 5, 5: ESC 6, 6: ESC 7, 7: ESC 8, 8: ESC 9, 9: ESC 10, 10: ESC 11, 11: ESC 12, 12: ESC 13, 13: ESC 14, 14: ESC 15, 15: ESC 16

## CAN_D2_UC_SRV_RT: Servo output rate

*Note: This parameter is for advanced users*

Maximum transmit rate for servo outputs

- Range: 1 200

- Units: Hz

# CAND3 Parameters

## CAN_D3_PROTOCOL: Enable use of specific protocol over virtual driver

*Note: This parameter is for advanced users*

Enabling this option starts selected protocol that will use this virtual driver

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|UAVCAN|
|2|KDECAN|
|3|ToshibaCAN|

- RebootRequired: True

# CAND3KDE Parameters

## CAN_D3_KDE_NPOLE: Number of motor poles

Sets the number of motor poles to calculate the correct RPM value

# CAND3UC Parameters

## CAN_D3_UC_NODE: UAVCAN node that is used for this network

*Note: This parameter is for advanced users*

UAVCAN node should be set implicitly

- Range: 1 250

## CAN_D3_UC_SRV_BM: RC Out channels to be transmitted as servo over UAVCAN

*Note: This parameter is for advanced users*

Bitmask with one set for channel to be transmitted as a servo command over UAVCAN

- Bitmask: 0: Servo 1, 1: Servo 2, 2: Servo 3, 3: Servo 4, 4: Servo 5, 5: Servo 6, 6: Servo 7, 7: Servo 8, 8: Servo 9, 9: Servo 10, 10: Servo 11, 11: Servo 12, 12: Servo 13, 13: Servo 14, 14: Servo 15

## CAN_D3_UC_ESC_BM: RC Out channels to be transmitted as ESC over UAVCAN

*Note: This parameter is for advanced users*

Bitmask with one set for channel to be transmitted as a ESC command over UAVCAN

- Bitmask: 0: ESC 1, 1: ESC 2, 2: ESC 3, 3: ESC 4, 4: ESC 5, 5: ESC 6, 6: ESC 7, 7: ESC 8, 8: ESC 9, 9: ESC 10, 10: ESC 11, 11: ESC 12, 12: ESC 13, 13: ESC 14, 14: ESC 15, 15: ESC 16

## CAN_D3_UC_SRV_RT: Servo output rate

*Note: This parameter is for advanced users*

Maximum transmit rate for servo outputs

- Range: 1 200

- Units: Hz

# CANP1 Parameters

## CAN_P1_DRIVER: Index of virtual driver to be used with physical CAN interface

Enabling this option enables use of CAN buses.

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|First driver|
|2|Second driver|

- RebootRequired: True

## CAN_P1_BITRATE: Bitrate of CAN interface

*Note: This parameter is for advanced users*

Bit rate can be set up to from 10000 to 1000000

- Range: 10000 1000000

## CAN_P1_DEBUG: Level of debug for CAN devices

*Note: This parameter is for advanced users*

Enabling this option will provide debug messages

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Major messages|
|2|All messages|

# CANP2 Parameters

## CAN_P2_DRIVER: Index of virtual driver to be used with physical CAN interface

Enabling this option enables use of CAN buses.

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|First driver|
|2|Second driver|

- RebootRequired: True

## CAN_P2_BITRATE: Bitrate of CAN interface

*Note: This parameter is for advanced users*

Bit rate can be set up to from 10000 to 1000000

- Range: 10000 1000000

## CAN_P2_DEBUG: Level of debug for CAN devices

*Note: This parameter is for advanced users*

Enabling this option will provide debug messages

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Major messages|
|2|All messages|

# CANP3 Parameters

## CAN_P3_DRIVER: Index of virtual driver to be used with physical CAN interface

Enabling this option enables use of CAN buses.

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|First driver|
|2|Second driver|

- RebootRequired: True

## CAN_P3_BITRATE: Bitrate of CAN interface

*Note: This parameter is for advanced users*

Bit rate can be set up to from 10000 to 1000000

- Range: 10000 1000000

## CAN_P3_DEBUG: Level of debug for CAN devices

*Note: This parameter is for advanced users*

Enabling this option will provide debug messages

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Major messages|
|2|All messages|

# CANSLCAN Parameters

## CAN_SLCAN_CPORT: SLCAN Route

CAN Driver ID to be routed to SLCAN, 0 means no routing

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|First driver|
|2|Second driver|

- RebootRequired: True

## CAN_SLCAN_SERNUM: SLCAN Serial Port

Serial Port ID to be used for temporary SLCAN iface, -1 means no temporary serial. This parameter is automatically reset on reboot or on timeout. See CAN_SLCAN_TIMOUT for timeout details

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
|0|Serial0|
|1|Serial1|
|2|Serial2|
|3|Serial3|
|4|Serial4|
|5|Serial5|
|6|Serial6|

## CAN_SLCAN_TIMOUT: SLCAN Timeout

Duration of inactivity after which SLCAN is switched back to original protocol in seconds.

- Range: 0 32767

# COMPASS Parameters

## COMPASS_OFS_X: Compass offsets in milligauss on the X axis

*Note: This parameter is for advanced users*

Offset to be added to the compass x-axis values to compensate for metal in the frame

- Range: -400 400

- Units: mGauss

- Increment: 1

## COMPASS_OFS_Y: Compass offsets in milligauss on the Y axis

*Note: This parameter is for advanced users*

Offset to be added to the compass y-axis values to compensate for metal in the frame

- Range: -400 400

- Units: mGauss

- Increment: 1

## COMPASS_OFS_Z: Compass offsets in milligauss on the Z axis

*Note: This parameter is for advanced users*

Offset to be added to the compass z-axis values to compensate for metal in the frame

- Range: -400 400

- Units: mGauss

- Increment: 1

## COMPASS_DEC: Compass declination

An angle to compensate between the true north and magnetic north

- Range: -3.142 3.142

- Units: rad

- Increment: 0.01

## COMPASS_LEARN: Learn compass offsets automatically

*Note: This parameter is for advanced users*

Enable or disable the automatic learning of compass offsets. You can enable learning either using a compass-only method that is suitable only for fixed wing aircraft or using the offsets learnt by the active EKF state estimator. If this option is enabled then the learnt offsets are saved when you disarm the vehicle. If InFlight learning is enabled then the compass with automatically start learning once a flight starts (must be armed). While InFlight learning is running you cannot use position control modes.

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Internal-Learning|
|2|EKF-Learning|
|3|InFlight-Learning|

## COMPASS_USE: Use compass for yaw

*Note: This parameter is for advanced users*

Enable or disable the use of the compass (instead of the GPS) for determining heading

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|

## COMPASS_AUTODEC: Auto Declination

*Note: This parameter is for advanced users*

Enable or disable the automatic calculation of the declination based on gps location

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|

## COMPASS_MOTCT: Motor interference compensation type

*Note: This parameter is for advanced users*

Set motor interference compensation type to disabled, throttle or current.  Do not change manually.

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Use Throttle|
|2|Use Current|

## COMPASS_MOT_X: Motor interference compensation for body frame X axis

*Note: This parameter is for advanced users*

Multiplied by the current throttle and added to the compass's x-axis values to compensate for motor interference (Offset per Amp or at Full Throttle)

- Range: -1000 1000

- Units: mGauss/A

- Increment: 1

## COMPASS_MOT_Y: Motor interference compensation for body frame Y axis

*Note: This parameter is for advanced users*

Multiplied by the current throttle and added to the compass's y-axis values to compensate for motor interference (Offset per Amp or at Full Throttle)

- Range: -1000 1000

- Units: mGauss/A

- Increment: 1

## COMPASS_MOT_Z: Motor interference compensation for body frame Z axis

*Note: This parameter is for advanced users*

Multiplied by the current throttle and added to the compass's z-axis values to compensate for motor interference (Offset per Amp or at Full Throttle)

- Range: -1000 1000

- Units: mGauss/A

- Increment: 1

## COMPASS_ORIENT: Compass orientation

*Note: This parameter is for advanced users*

The orientation of the first external compass relative to the vehicle frame. This value will be ignored unless this compass is set as an external compass. When set correctly in the northern hemisphere, pointing the nose and right side down should increase the MagX and MagY values respectively. Rolling the vehicle upside down should decrease the MagZ value. For southern hemisphere, switch increase and decrease. NOTE: For internal compasses, AHRS_ORIENT is used.

|Value|Meaning|
|:---:|:---:|
|0|None|
|1|Yaw45|
|2|Yaw90|
|3|Yaw135|
|4|Yaw180|
|5|Yaw225|
|6|Yaw270|
|7|Yaw315|
|8|Roll180|
|9|Roll180Yaw45|
|10|Roll180Yaw90|
|11|Roll180Yaw135|
|12|Pitch180|
|13|Roll180Yaw225|
|14|Roll180Yaw270|
|15|Roll180Yaw315|
|16|Roll90|
|17|Roll90Yaw45|
|18|Roll90Yaw90|
|19|Roll90Yaw135|
|20|Roll270|
|21|Roll270Yaw45|
|22|Roll270Yaw90|
|23|Roll270Yaw135|
|24|Pitch90|
|25|Pitch270|
|26|Pitch180Yaw90|
|27|Pitch180Yaw270|
|28|Roll90Pitch90|
|29|Roll180Pitch90|
|30|Roll270Pitch90|
|31|Roll90Pitch180|
|32|Roll270Pitch180|
|33|Roll90Pitch270|
|34|Roll180Pitch270|
|35|Roll270Pitch270|
|36|Roll90Pitch180Yaw90|
|37|Roll90Yaw270|
|38|Yaw293Pitch68Roll180|
|39|Pitch315|
|40|Roll90Pitch315|

## COMPASS_EXTERNAL: Compass is attached via an external cable

*Note: This parameter is for advanced users*

Configure compass so it is attached externally. This is auto-detected on PX4 and Pixhawk. Set to 1 if the compass is externally connected. When externally connected the COMPASS_ORIENT option operates independently of the AHRS_ORIENTATION board orientation option. If set to 0 or 1 then auto-detection by bus connection can override the value. If set to 2 then auto-detection will be disabled.

|Value|Meaning|
|:---:|:---:|
|0|Internal|
|1|External|
|2|ForcedExternal|

## COMPASS_OFS2_X: Compass2 offsets in milligauss on the X axis

*Note: This parameter is for advanced users*

Offset to be added to compass2's x-axis values to compensate for metal in the frame

- Range: -400 400

- Units: mGauss

- Increment: 1

## COMPASS_OFS2_Y: Compass2 offsets in milligauss on the Y axis

*Note: This parameter is for advanced users*

Offset to be added to compass2's y-axis values to compensate for metal in the frame

- Range: -400 400

- Units: mGauss

- Increment: 1

## COMPASS_OFS2_Z: Compass2 offsets in milligauss on the Z axis

*Note: This parameter is for advanced users*

Offset to be added to compass2's z-axis values to compensate for metal in the frame

- Range: -400 400

- Units: mGauss

- Increment: 1

## COMPASS_MOT2_X: Motor interference compensation to compass2 for body frame X axis

*Note: This parameter is for advanced users*

Multiplied by the current throttle and added to compass2's x-axis values to compensate for motor interference (Offset per Amp or at Full Throttle)

- Range: -1000 1000

- Units: mGauss/A

- Increment: 1

## COMPASS_MOT2_Y: Motor interference compensation to compass2 for body frame Y axis

*Note: This parameter is for advanced users*

Multiplied by the current throttle and added to compass2's y-axis values to compensate for motor interference (Offset per Amp or at Full Throttle)

- Range: -1000 1000

- Units: mGauss/A

- Increment: 1

## COMPASS_MOT2_Z: Motor interference compensation to compass2 for body frame Z axis

*Note: This parameter is for advanced users*

Multiplied by the current throttle and added to compass2's z-axis values to compensate for motor interference (Offset per Amp or at Full Throttle)

- Range: -1000 1000

- Units: mGauss/A

- Increment: 1

## COMPASS_PRIMARY: Choose primary compass

*Note: This parameter is for advanced users*

If more than one compass is available, this selects which compass is the primary. When external compasses are connected, they will be ordered first. NOTE: If no external compass is attached, this parameter is ignored.

|Value|Meaning|
|:---:|:---:|
|0|FirstCompass|
|1|SecondCompass|
|2|ThirdCompass|

## COMPASS_OFS3_X: Compass3 offsets in milligauss on the X axis

*Note: This parameter is for advanced users*

Offset to be added to compass3's x-axis values to compensate for metal in the frame

- Range: -400 400

- Units: mGauss

- Increment: 1

## COMPASS_OFS3_Y: Compass3 offsets in milligauss on the Y axis

*Note: This parameter is for advanced users*

Offset to be added to compass3's y-axis values to compensate for metal in the frame

- Range: -400 400

- Units: mGauss

- Increment: 1

## COMPASS_OFS3_Z: Compass3 offsets in milligauss on the Z axis

*Note: This parameter is for advanced users*

Offset to be added to compass3's z-axis values to compensate for metal in the frame

- Range: -400 400

- Units: mGauss

- Increment: 1

## COMPASS_MOT3_X: Motor interference compensation to compass3 for body frame X axis

*Note: This parameter is for advanced users*

Multiplied by the current throttle and added to compass3's x-axis values to compensate for motor interference (Offset per Amp or at Full Throttle)

- Range: -1000 1000

- Units: mGauss/A

- Increment: 1

## COMPASS_MOT3_Y: Motor interference compensation to compass3 for body frame Y axis

*Note: This parameter is for advanced users*

Multiplied by the current throttle and added to compass3's y-axis values to compensate for motor interference (Offset per Amp or at Full Throttle)

- Range: -1000 1000

- Units: mGauss/A

- Increment: 1

## COMPASS_MOT3_Z: Motor interference compensation to compass3 for body frame Z axis

*Note: This parameter is for advanced users*

Multiplied by the current throttle and added to compass3's z-axis values to compensate for motor interference (Offset per Amp or at Full Throttle)

- Range: -1000 1000

- Units: mGauss/A

- Increment: 1

## COMPASS_DEV_ID: Compass device id

*Note: This parameter is for advanced users*

Compass device id.  Automatically detected, do not set manually

- ReadOnly: True

## COMPASS_DEV_ID2: Compass2 device id

*Note: This parameter is for advanced users*

Second compass's device id.  Automatically detected, do not set manually

- ReadOnly: True

## COMPASS_DEV_ID3: Compass3 device id

*Note: This parameter is for advanced users*

Third compass's device id.  Automatically detected, do not set manually

- ReadOnly: True

## COMPASS_USE2: Compass2 used for yaw

*Note: This parameter is for advanced users*

Enable or disable the second compass for determining heading.

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|

## COMPASS_ORIENT2: Compass2 orientation

*Note: This parameter is for advanced users*

The orientation of a second external compass relative to the vehicle frame. This value will be ignored unless this compass is set as an external compass. When set correctly in the northern hemisphere, pointing the nose and right side down should increase the MagX and MagY values respectively. Rolling the vehicle upside down should decrease the MagZ value. For southern hemisphere, switch increase and decrease. NOTE: For internal compasses, AHRS_ORIENT is used.

|Value|Meaning|
|:---:|:---:|
|0|None|
|1|Yaw45|
|2|Yaw90|
|3|Yaw135|
|4|Yaw180|
|5|Yaw225|
|6|Yaw270|
|7|Yaw315|
|8|Roll180|
|9|Roll180Yaw45|
|10|Roll180Yaw90|
|11|Roll180Yaw135|
|12|Pitch180|
|13|Roll180Yaw225|
|14|Roll180Yaw270|
|15|Roll180Yaw315|
|16|Roll90|
|17|Roll90Yaw45|
|18|Roll90Yaw90|
|19|Roll90Yaw135|
|20|Roll270|
|21|Roll270Yaw45|
|22|Roll270Yaw90|
|23|Roll270Yaw135|
|24|Pitch90|
|25|Pitch270|
|26|Pitch180Yaw90|
|27|Pitch180Yaw270|
|28|Roll90Pitch90|
|29|Roll180Pitch90|
|30|Roll270Pitch90|
|31|Roll90Pitch180|
|32|Roll270Pitch180|
|33|Roll90Pitch270|
|34|Roll180Pitch270|
|35|Roll270Pitch270|
|36|Roll90Pitch180Yaw90|
|37|Roll90Yaw270|
|38|Yaw293Pitch68Roll180|
|39|Pitch315|
|40|Roll90Pitch315|

## COMPASS_EXTERN2: Compass2 is attached via an external cable

*Note: This parameter is for advanced users*

Configure second compass so it is attached externally. This is auto-detected on PX4 and Pixhawk. If set to 0 or 1 then auto-detection by bus connection can override the value. If set to 2 then auto-detection will be disabled.

|Value|Meaning|
|:---:|:---:|
|0|Internal|
|1|External|
|2|ForcedExternal|

## COMPASS_USE3: Compass3 used for yaw

*Note: This parameter is for advanced users*

Enable or disable the third compass for determining heading.

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|

## COMPASS_ORIENT3: Compass3 orientation

*Note: This parameter is for advanced users*

The orientation of a third external compass relative to the vehicle frame. This value will be ignored unless this compass is set as an external compass. When set correctly in the northern hemisphere, pointing the nose and right side down should increase the MagX and MagY values respectively. Rolling the vehicle upside down should decrease the MagZ value. For southern hemisphere, switch increase and decrease. NOTE: For internal compasses, AHRS_ORIENT is used.

|Value|Meaning|
|:---:|:---:|
|0|None|
|1|Yaw45|
|2|Yaw90|
|3|Yaw135|
|4|Yaw180|
|5|Yaw225|
|6|Yaw270|
|7|Yaw315|
|8|Roll180|
|9|Roll180Yaw45|
|10|Roll180Yaw90|
|11|Roll180Yaw135|
|12|Pitch180|
|13|Roll180Yaw225|
|14|Roll180Yaw270|
|15|Roll180Yaw315|
|16|Roll90|
|17|Roll90Yaw45|
|18|Roll90Yaw90|
|19|Roll90Yaw135|
|20|Roll270|
|21|Roll270Yaw45|
|22|Roll270Yaw90|
|23|Roll270Yaw135|
|24|Pitch90|
|25|Pitch270|
|26|Pitch180Yaw90|
|27|Pitch180Yaw270|
|28|Roll90Pitch90|
|29|Roll180Pitch90|
|30|Roll270Pitch90|
|31|Roll90Pitch180|
|32|Roll270Pitch180|
|33|Roll90Pitch270|
|34|Roll180Pitch270|
|35|Roll270Pitch270|
|36|Roll90Pitch180Yaw90|
|37|Roll90Yaw270|
|38|Yaw293Pitch68Roll180|
|39|Pitch315|
|40|Roll90Pitch315|

## COMPASS_EXTERN3: Compass3 is attached via an external cable

*Note: This parameter is for advanced users*

Configure third compass so it is attached externally. This is auto-detected on PX4 and Pixhawk. If set to 0 or 1 then auto-detection by bus connection can override the value. If set to 2 then auto-detection will be disabled.

|Value|Meaning|
|:---:|:---:|
|0|Internal|
|1|External|
|2|ForcedExternal|

## COMPASS_DIA_X: Compass soft-iron diagonal X component

*Note: This parameter is for advanced users*

DIA_X in the compass soft-iron calibration matrix: [[DIA_X, ODI_X, ODI_Y], [ODI_X, DIA_Y, ODI_Z], [ODI_Y, ODI_Z, DIA_Z]]

## COMPASS_DIA_Y: Compass soft-iron diagonal Y component

*Note: This parameter is for advanced users*

DIA_Y in the compass soft-iron calibration matrix: [[DIA_X, ODI_X, ODI_Y], [ODI_X, DIA_Y, ODI_Z], [ODI_Y, ODI_Z, DIA_Z]]

## COMPASS_DIA_Z: Compass soft-iron diagonal Z component

*Note: This parameter is for advanced users*

DIA_Z in the compass soft-iron calibration matrix: [[DIA_X, ODI_X, ODI_Y], [ODI_X, DIA_Y, ODI_Z], [ODI_Y, ODI_Z, DIA_Z]]

## COMPASS_ODI_X: Compass soft-iron off-diagonal X component

*Note: This parameter is for advanced users*

ODI_X in the compass soft-iron calibration matrix: [[DIA_X, ODI_X, ODI_Y], [ODI_X, DIA_Y, ODI_Z], [ODI_Y, ODI_Z, DIA_Z]]

## COMPASS_ODI_Y: Compass soft-iron off-diagonal Y component

*Note: This parameter is for advanced users*

ODI_Y in the compass soft-iron calibration matrix: [[DIA_X, ODI_X, ODI_Y], [ODI_X, DIA_Y, ODI_Z], [ODI_Y, ODI_Z, DIA_Z]]

## COMPASS_ODI_Z: Compass soft-iron off-diagonal Z component

*Note: This parameter is for advanced users*

ODI_Z in the compass soft-iron calibration matrix: [[DIA_X, ODI_X, ODI_Y], [ODI_X, DIA_Y, ODI_Z], [ODI_Y, ODI_Z, DIA_Z]]

## COMPASS_DIA2_X: Compass2 soft-iron diagonal X component

*Note: This parameter is for advanced users*

DIA_X in the compass2 soft-iron calibration matrix: [[DIA_X, ODI_X, ODI_Y], [ODI_X, DIA_Y, ODI_Z], [ODI_Y, ODI_Z, DIA_Z]]

## COMPASS_DIA2_Y: Compass2 soft-iron diagonal Y component

*Note: This parameter is for advanced users*

DIA_Y in the compass2 soft-iron calibration matrix: [[DIA_X, ODI_X, ODI_Y], [ODI_X, DIA_Y, ODI_Z], [ODI_Y, ODI_Z, DIA_Z]]

## COMPASS_DIA2_Z: Compass2 soft-iron diagonal Z component

*Note: This parameter is for advanced users*

DIA_Z in the compass2 soft-iron calibration matrix: [[DIA_X, ODI_X, ODI_Y], [ODI_X, DIA_Y, ODI_Z], [ODI_Y, ODI_Z, DIA_Z]]

## COMPASS_ODI2_X: Compass2 soft-iron off-diagonal X component

*Note: This parameter is for advanced users*

ODI_X in the compass2 soft-iron calibration matrix: [[DIA_X, ODI_X, ODI_Y], [ODI_X, DIA_Y, ODI_Z], [ODI_Y, ODI_Z, DIA_Z]]

## COMPASS_ODI2_Y: Compass2 soft-iron off-diagonal Y component

*Note: This parameter is for advanced users*

ODI_Y in the compass2 soft-iron calibration matrix: [[DIA_X, ODI_X, ODI_Y], [ODI_X, DIA_Y, ODI_Z], [ODI_Y, ODI_Z, DIA_Z]]

## COMPASS_ODI2_Z: Compass2 soft-iron off-diagonal Z component

*Note: This parameter is for advanced users*

ODI_Z in the compass2 soft-iron calibration matrix: [[DIA_X, ODI_X, ODI_Y], [ODI_X, DIA_Y, ODI_Z], [ODI_Y, ODI_Z, DIA_Z]]

## COMPASS_DIA3_X: Compass3 soft-iron diagonal X component

*Note: This parameter is for advanced users*

DIA_X in the compass3 soft-iron calibration matrix: [[DIA_X, ODI_X, ODI_Y], [ODI_X, DIA_Y, ODI_Z], [ODI_Y, ODI_Z, DIA_Z]]

## COMPASS_DIA3_Y: Compass3 soft-iron diagonal Y component

*Note: This parameter is for advanced users*

DIA_Y in the compass3 soft-iron calibration matrix: [[DIA_X, ODI_X, ODI_Y], [ODI_X, DIA_Y, ODI_Z], [ODI_Y, ODI_Z, DIA_Z]]

## COMPASS_DIA3_Z: Compass3 soft-iron diagonal Z component

*Note: This parameter is for advanced users*

DIA_Z in the compass3 soft-iron calibration matrix: [[DIA_X, ODI_X, ODI_Y], [ODI_X, DIA_Y, ODI_Z], [ODI_Y, ODI_Z, DIA_Z]]

## COMPASS_ODI3_X: Compass3 soft-iron off-diagonal X component

*Note: This parameter is for advanced users*

ODI_X in the compass3 soft-iron calibration matrix: [[DIA_X, ODI_X, ODI_Y], [ODI_X, DIA_Y, ODI_Z], [ODI_Y, ODI_Z, DIA_Z]]

## COMPASS_ODI3_Y: Compass3 soft-iron off-diagonal Y component

*Note: This parameter is for advanced users*

ODI_Y in the compass3 soft-iron calibration matrix: [[DIA_X, ODI_X, ODI_Y], [ODI_X, DIA_Y, ODI_Z], [ODI_Y, ODI_Z, DIA_Z]]

## COMPASS_ODI3_Z: Compass3 soft-iron off-diagonal Z component

*Note: This parameter is for advanced users*

ODI_Z in the compass3 soft-iron calibration matrix: [[DIA_X, ODI_X, ODI_Y], [ODI_X, DIA_Y, ODI_Z], [ODI_Y, ODI_Z, DIA_Z]]

## COMPASS_CAL_FIT: Compass calibration fitness

*Note: This parameter is for advanced users*

This controls the fitness level required for a successful compass calibration. A lower value makes for a stricter fit (less likely to pass). This is the value used for the primary magnetometer. Other magnetometers get double the value.

- Range: 4 32

|Value|Meaning|
|:---:|:---:|
|4|Very Strict|
|8|Strict|
|16|Default|
|32|Relaxed|

- Increment: 0.1

## COMPASS_OFFS_MAX: Compass maximum offset

*Note: This parameter is for advanced users*

This sets the maximum allowed compass offset in calibration and arming checks

- Range: 500 3000

- Increment: 1

## COMPASS_TYPEMASK: Compass disable driver type mask

*Note: This parameter is for advanced users*

This is a bitmask of driver types to disable. If a driver type is set in this mask then that driver will not try to find a sensor at startup

- Bitmask: 0:HMC5883,1:LSM303D,2:AK8963,3:BMM150,4:LSM9DS1,5:LIS3MDL,6:AK09916,7:IST8310,8:ICM20948,9:MMC3416,11:UAVCAN,12:QMC5883,14:MAG3110,15:IST8308

## COMPASS_FLTR_RNG: Range in which sample is accepted

This sets the range around the average value that new samples must be within to be accepted. This can help reduce the impact of noise on sensors that are on long I2C cables. The value is a percentage from the average value. A value of zero disables this filter.

- Units: %

- Range: 0 100

- Increment: 1

## COMPASS_AUTO_ROT: Automatically check orientation

When enabled this will automatically check the orientation of compasses on successful completion of compass calibration. If set to 2 then external compasses will have their orientation automatically corrected.

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|CheckOnly|
|2|CheckAndFix|

## COMPASS_EXP_DID: Compass device id expected

*Note: This parameter is for advanced users*

The expected value of COMPASS_DEV_ID, used by arming checks. Setting this to -1 means "don't care."

## COMPASS_EXP_DID2: Compass2 device id expected

*Note: This parameter is for advanced users*

The expected value of COMPASS_DEV_ID2, used by arming checks. Setting this to -1 means "don't care."

## COMPASS_EXP_DID3: Compass3 device id expected

*Note: This parameter is for advanced users*

The expected value of COMPASS_DEV_ID3, used by arming checks. Setting this to -1 means "don't care."

## COMPASS_ENABLE: Enable Compass

Setting this to Enabled(1) will enable the compass. Setting this to Disabled(0) will disable the compass. Note that this is separate from COMPASS_USE. This will enable the low level senor, and will enable logging of magnetometer data. To use the compass for navigation you must also set COMPASS_USE to 1.

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|

# COMPASSPMOT Parameters

## COMPASS_PMOT_EN: per-motor compass correction enable

*Note: This parameter is for advanced users*

This enables per-motor compass corrections

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|

## COMPASS_PMOT_EXP: per-motor exponential correction

*Note: This parameter is for advanced users*

This is the exponential correction for the power output of the motor for per-motor compass correction

- Range: 0 2

- Increment: 0.01

## COMPASS_PMOT1_X: Compass per-motor1 X

*Note: This parameter is for advanced users*

Compensation for X axis of motor1

## COMPASS_PMOT1_Y: Compass per-motor1 Y

*Note: This parameter is for advanced users*

Compensation for Y axis of motor1

## COMPASS_PMOT1_Z: Compass per-motor1 Z

*Note: This parameter is for advanced users*

Compensation for Z axis of motor1

## COMPASS_PMOT2_X: Compass per-motor2 X

*Note: This parameter is for advanced users*

Compensation for X axis of motor2

## COMPASS_PMOT2_Y: Compass per-motor2 Y

*Note: This parameter is for advanced users*

Compensation for Y axis of motor2

## COMPASS_PMOT2_Z: Compass per-motor2 Z

*Note: This parameter is for advanced users*

Compensation for Z axis of motor2

## COMPASS_PMOT3_X: Compass per-motor3 X

*Note: This parameter is for advanced users*

Compensation for X axis of motor3

## COMPASS_PMOT3_Y: Compass per-motor3 Y

*Note: This parameter is for advanced users*

Compensation for Y axis of motor3

## COMPASS_PMOT3_Z: Compass per-motor3 Z

*Note: This parameter is for advanced users*

Compensation for Z axis of motor3

## COMPASS_PMOT4_X: Compass per-motor4 X

*Note: This parameter is for advanced users*

Compensation for X axis of motor4

## COMPASS_PMOT4_Y: Compass per-motor4 Y

*Note: This parameter is for advanced users*

Compensation for Y axis of motor4

## COMPASS_PMOT4_Z: Compass per-motor4 Z

*Note: This parameter is for advanced users*

Compensation for Z axis of motor4

# EK2 Parameters

## EK2_ENABLE: Enable EKF2

*Note: This parameter is for advanced users*

This enables EKF2. Enabling EKF2 only makes the maths run, it does not mean it will be used for flight control. To use it for flight control set AHRS_EKF_TYPE=2. A reboot or restart will need to be performed after changing the value of EK2_ENABLE for it to take effect.

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
| 1|Enabled|

- RebootRequired: True

## EK2_GPS_TYPE: GPS mode control

*Note: This parameter is for advanced users*

This controls use of GPS measurements : 0 = use 3D velocity & 2D position, 1 = use 2D velocity and 2D position, 2 = use 2D position, 3 = Inhibit GPS use - this can be useful when flying with an optical flow sensor in an environment where GPS quality is poor and subject to large multipath errors.

|Value|Meaning|
|:---:|:---:|
|0|GPS 3D Vel and 2D Pos|
| 1|GPS 2D vel and 2D pos|
| 2|GPS 2D pos|
| 3|No GPS|

## EK2_VELNE_M_NSE: GPS horizontal velocity measurement noise (m/s)

*Note: This parameter is for advanced users*

This sets a lower limit on the speed accuracy reported by the GPS receiver that is used to set horizontal velocity observation noise. If the model of receiver used does not provide a speed accurcy estimate, then the parameter value will be used. Increasing it reduces the weighting of the GPS horizontal velocity measurements.

- Range: 0.05 5.0

- Increment: 0.05

- Units: m/s

## EK2_VELD_M_NSE: GPS vertical velocity measurement noise (m/s)

*Note: This parameter is for advanced users*

This sets a lower limit on the speed accuracy reported by the GPS receiver that is used to set vertical velocity observation noise. If the model of receiver used does not provide a speed accurcy estimate, then the parameter value will be used. Increasing it reduces the weighting of the GPS vertical velocity measurements.

- Range: 0.05 5.0

- Increment: 0.05

- Units: m/s

## EK2_VEL_I_GATE: GPS velocity innovation gate size

*Note: This parameter is for advanced users*

This sets the percentage number of standard deviations applied to the GPS velocity measurement innovation consistency check. Decreasing it makes it more likely that good measurements willbe rejected. Increasing it makes it more likely that bad measurements will be accepted.

- Range: 100 1000

- Increment: 25

## EK2_POSNE_M_NSE: GPS horizontal position measurement noise (m)

*Note: This parameter is for advanced users*

This sets the GPS horizontal position or external navigation system position observation noise. Increasing it reduces the weighting of GPS horizontal position or external navigation system position measurements.

- Range: 0.1 10.0

- Increment: 0.1

- Units: m

## EK2_POS_I_GATE: GPS position measurement gate size

*Note: This parameter is for advanced users*

This sets the percentage number of standard deviations applied to the GPS position measurement innovation consistency check. Decreasing it makes it more likely that good measurements will be rejected. Increasing it makes it more likely that bad measurements will be accepted.

- Range: 100 1000

- Increment: 25

## EK2_GLITCH_RAD: GPS glitch radius gate size (m)

*Note: This parameter is for advanced users*

This controls the maximum radial uncertainty in position between the value predicted by the filter and the value measured by the GPS before the filter position and velocity states are reset to the GPS. Making this value larger allows the filter to ignore larger GPS glitches but also means that non-GPS errors such as IMU and compass can create a larger error in position before the filter is forced back to the GPS position.

- Range: 10 100

- Increment: 5

- Units: m

## EK2_ALT_SOURCE: Primary altitude sensor source

*Note: This parameter is for advanced users*

Primary height sensor used by the EKF. If the selected option cannot be used, baro is used. 1 uses the range finder and only with optical flow navigation (EK2_GPS_TYPE = 3), Do not use "1" for terrain following. NOTE: the EK2_RNG_USE_HGT parameter can be used to switch to range-finder when close to the ground.

|Value|Meaning|
|:---:|:---:|
|0|Use Baro|
| 1|Use Range Finder|
| 2|Use GPS|
| 3|Use Range Beacon|

- RebootRequired: True

## EK2_ALT_M_NSE: Altitude measurement noise (m)

*Note: This parameter is for advanced users*

This is the RMS value of noise in the altitude measurement. Increasing it reduces the weighting of the baro measurement and will make the filter respond more slowly to baro measurement errors, but will make it more sensitive to GPS and accelerometer errors.

- Range: 0.1 10.0

- Increment: 0.1

- Units: m

## EK2_HGT_I_GATE: Height measurement gate size

*Note: This parameter is for advanced users*

This sets the percentage number of standard deviations applied to the height measurement innovation consistency check. Decreasing it makes it more likely that good measurements will be rejected. Increasing it makes it more likely that bad measurements will be accepted.

- Range: 100 1000

- Increment: 25

## EK2_HGT_DELAY: Height measurement delay (msec)

*Note: This parameter is for advanced users*

This is the number of msec that the Height measurements lag behind the inertial measurements.

- Range: 0 250

- Increment: 10

- Units: ms

- RebootRequired: True

## EK2_MAG_M_NSE: Magnetometer measurement noise (Gauss)

*Note: This parameter is for advanced users*

This is the RMS value of noise in magnetometer measurements. Increasing it reduces the weighting on these measurements.

- Range: 0.01 0.5

- Increment: 0.01

- Units: Gauss

## EK2_MAG_CAL: Magnetometer default fusion mode

*Note: This parameter is for advanced users*

This determines when the filter will use the 3-axis magnetometer fusion model that estimates both earth and body fixed magnetic field states and when it will use a simpler magnetic heading fusion model that does not use magnetic field states. The 3-axis magnetometer fusion is only suitable for use when the external magnetic field environment is stable. EK2_MAG_CAL = 0 uses heading fusion on ground, 3-axis fusion in-flight, and is the default setting for Plane users. EK2_MAG_CAL = 1 uses 3-axis fusion only when manoeuvring. EK2_MAG_CAL = 2 uses heading fusion at all times, is recommended if the external magnetic field is varying and is the default for rovers. EK2_MAG_CAL = 3 uses heading fusion on the ground and 3-axis fusion after the first in-air field and yaw reset has completed, and is the default for copters. EK2_MAG_CAL = 4 uses 3-axis fusion at all times. NOTE : Use of simple heading magnetometer fusion makes vehicle compass calibration and alignment errors harder for the EKF to detect which reduces the sensitivity of the Copter EKF failsafe algorithm. NOTE: The fusion mode can be forced to 2 for specific EKF cores using the EK2_MAG_MASK parameter.

|Value|Meaning|
|:---:|:---:|
|0|When flying|
|1|When manoeuvring|
|2|Never|
|3|After first climb yaw reset|
|4|Always|

## EK2_MAG_I_GATE: Magnetometer measurement gate size

*Note: This parameter is for advanced users*

This sets the percentage number of standard deviations applied to the magnetometer measurement innovation consistency check. Decreasing it makes it more likely that good measurements will be rejected. Increasing it makes it more likely that bad measurements will be accepted.

- Range: 100 1000

- Increment: 25

## EK2_EAS_M_NSE: Equivalent airspeed measurement noise (m/s)

*Note: This parameter is for advanced users*

This is the RMS value of noise in equivalent airspeed measurements used by planes. Increasing it reduces the weighting of airspeed measurements and will make wind speed estimates less noisy and slower to converge. Increasing also increases navigation errors when dead-reckoning without GPS measurements.

- Range: 0.5 5.0

- Increment: 0.1

- Units: m/s

## EK2_EAS_I_GATE: Airspeed measurement gate size

*Note: This parameter is for advanced users*

This sets the percentage number of standard deviations applied to the airspeed measurement innovation consistency check. Decreasing it makes it more likely that good measurements will be rejected. Increasing it makes it more likely that bad measurements will be accepted.

- Range: 100 1000

- Increment: 25

## EK2_RNG_M_NSE: Range finder measurement noise (m)

*Note: This parameter is for advanced users*

This is the RMS value of noise in the range finder measurement. Increasing it reduces the weighting on this measurement.

- Range: 0.1 10.0

- Increment: 0.1

- Units: m

## EK2_RNG_I_GATE: Range finder measurement gate size

*Note: This parameter is for advanced users*

This sets the percentage number of standard deviations applied to the range finder innovation consistency check. Decreasing it makes it more likely that good measurements will be rejected. Increasing it makes it more likely that bad measurements will be accepted.

- Range: 100 1000

- Increment: 25

## EK2_MAX_FLOW: Maximum valid optical flow rate

*Note: This parameter is for advanced users*

This sets the magnitude maximum optical flow rate in rad/sec that will be accepted by the filter

- Range: 1.0 4.0

- Increment: 0.1

- Units: rad/s

## EK2_FLOW_M_NSE: Optical flow measurement noise (rad/s)

*Note: This parameter is for advanced users*

This is the RMS value of noise and errors in optical flow measurements. Increasing it reduces the weighting on these measurements.

- Range: 0.05 1.0

- Increment: 0.05

- Units: rad/s

## EK2_FLOW_I_GATE: Optical Flow measurement gate size

*Note: This parameter is for advanced users*

This sets the percentage number of standard deviations applied to the optical flow innovation consistency check. Decreasing it makes it more likely that good measurements will be rejected. Increasing it makes it more likely that bad measurements will be accepted.

- Range: 100 1000

- Increment: 25

## EK2_FLOW_DELAY: Optical Flow measurement delay (msec)

*Note: This parameter is for advanced users*

This is the number of msec that the optical flow measurements lag behind the inertial measurements. It is the time from the end of the optical flow averaging period and does not include the time delay due to the 100msec of averaging within the flow sensor.

- Range: 0 127

- Increment: 10

- Units: ms

- RebootRequired: True

## EK2_GYRO_P_NSE: Rate gyro noise (rad/s)

*Note: This parameter is for advanced users*

This control disturbance noise controls the growth of estimated error due to gyro measurement errors excluding bias. Increasing it makes the flter trust the gyro measurements less and other measurements more.

- Range: 0.0001 0.1

- Increment: 0.0001

- Units: rad/s

## EK2_ACC_P_NSE: Accelerometer noise (m/s^2)

*Note: This parameter is for advanced users*

This control disturbance noise controls the growth of estimated error due to accelerometer measurement errors excluding bias. Increasing it makes the flter trust the accelerometer measurements less and other measurements more.

- Range: 0.01 1.0

- Increment: 0.01

- Units: m/s/s

## EK2_GBIAS_P_NSE: Rate gyro bias stability (rad/s/s)

*Note: This parameter is for advanced users*

This state  process noise controls growth of the gyro delta angle bias state error estimate. Increasing it makes rate gyro bias estimation faster and noisier.

- Range: 0.00001 0.001

- Units: rad/s/s

## EK2_GSCL_P_NSE: Rate gyro scale factor stability (1/s)

*Note: This parameter is for advanced users*

This noise controls the rate of gyro scale factor learning. Increasing it makes rate gyro scale factor estimation faster and noisier.

- Range: 0.000001 0.001

- Units: Hz

## EK2_ABIAS_P_NSE: Accelerometer bias stability (m/s^3)

*Note: This parameter is for advanced users*

This noise controls the growth of the vertical accelerometer delta velocity bias state error estimate. Increasing it makes accelerometer bias estimation faster and noisier.

- Range: 0.00001 0.005

- Units: m/s/s/s

## EK2_WIND_P_NSE: Wind velocity process noise (m/s^2)

*Note: This parameter is for advanced users*

This state process noise controls the growth of wind state error estimates. Increasing it makes wind estimation faster and noisier.

- Range: 0.01 1.0

- Increment: 0.1

- Units: m/s/s

## EK2_WIND_PSCALE: Height rate to wind process noise scaler

*Note: This parameter is for advanced users*

This controls how much the process noise on the wind states is increased when gaining or losing altitude to take into account changes in wind speed and direction with altitude. Increasing this parameter increases how rapidly the wind states adapt when changing altitude, but does make wind velocity estimation noiser.

- Range: 0.0 1.0

- Increment: 0.1

## EK2_GPS_CHECK: GPS preflight check

*Note: This parameter is for advanced users*

This is a 1 byte bitmap controlling which GPS preflight checks are performed. Set to 0 to bypass all checks. Set to 255 perform all checks. Set to 3 to check just the number of satellites and HDoP. Set to 31 for the most rigorous checks that will still allow checks to pass when the copter is moving, eg launch from a boat.

- Bitmask: 0:NSats,1:HDoP,2:speed error,3:position error,4:yaw error,5:pos drift,6:vert speed,7:horiz speed

## EK2_IMU_MASK: Bitmask of active IMUs

*Note: This parameter is for advanced users*

1 byte bitmap of IMUs to use in EKF2. A separate instance of EKF2 will be started for each IMU selected. Set to 1 to use the first IMU only (default), set to 2 to use the second IMU only, set to 3 to use the first and second IMU. Additional IMU's can be used up to a maximum of 6 if memory and processing resources permit. There may be insufficient memory and processing resources to run multiple instances. If this occurs EKF2 will fail to start.

- Bitmask: 0:FirstIMU,1:SecondIMU,2:ThirdIMU,3:FourthIMU,4:FifthIMU,5:SixthIMU

- RebootRequired: True

## EK2_CHECK_SCALE: GPS accuracy check scaler (%)

*Note: This parameter is for advanced users*

This scales the thresholds that are used to check GPS accuracy before it is used by the EKF. A value of 100 is the default. Values greater than 100 increase and values less than 100 reduce the maximum GPS error the EKF will accept. A value of 200 will double the allowable GPS error.

- Range: 50 200

- Units: %

## EK2_NOAID_M_NSE: Non-GPS operation position uncertainty (m)

*Note: This parameter is for advanced users*

This sets the amount of position variation that the EKF allows for when operating without external measurements (eg GPS or optical flow). Increasing this parameter makes the EKF attitude estimate less sensitive to vehicle manoeuvres but more sensitive to IMU errors.

- Range: 0.5 50.0

- Units: m

## EK2_LOG_MASK: EKF sensor logging IMU mask

*Note: This parameter is for advanced users*

This sets the IMU mask of sensors to do full logging for

- Bitmask: 0:FirstIMU,1:SecondIMU,2:ThirdIMU,3:FourthIMU,4:FifthIMU,5:SixthIMU

- RebootRequired: True

## EK2_YAW_M_NSE: Yaw measurement noise (rad)

*Note: This parameter is for advanced users*

This is the RMS value of noise in yaw measurements from the magnetometer. Increasing it reduces the weighting on these measurements.

- Range: 0.05 1.0

- Increment: 0.05

- Units: rad

## EK2_YAW_I_GATE: Yaw measurement gate size

*Note: This parameter is for advanced users*

This sets the percentage number of standard deviations applied to the magnetometer yaw measurement innovation consistency check. Decreasing it makes it more likely that good measurements will be rejected. Increasing it makes it more likely that bad measurements will be accepted.

- Range: 100 1000

- Increment: 25

## EK2_TAU_OUTPUT: Output complementary filter time constant (centi-sec)

*Note: This parameter is for advanced users*

Sets the time constant of the output complementary filter/predictor in centi-seconds.

- Range: 10 50

- Increment: 5

- Units: cs

## EK2_MAGE_P_NSE: Earth magnetic field process noise (gauss/s)

*Note: This parameter is for advanced users*

This state process noise controls the growth of earth magnetic field state error estimates. Increasing it makes earth magnetic field estimation faster and noisier.

- Range: 0.00001 0.01

- Units: Gauss/s

## EK2_MAGB_P_NSE: Body magnetic field process noise (gauss/s)

*Note: This parameter is for advanced users*

This state process noise controls the growth of body magnetic field state error estimates. Increasing it makes magnetometer bias error estimation faster and noisier.

- Range: 0.00001 0.01

- Units: Gauss/s

## EK2_RNG_USE_HGT: Range finder switch height percentage

*Note: This parameter is for advanced users*

Range finder can be used as the primary height source when below this percentage of its maximum range (see RNGFND_MAX_CM). Set to -1 when EK2_ALT_SOURCE is not set to range finder.  This is not for terrain following.

- Range: -1 70

- Increment: 1

- Units: %

## EK2_TERR_GRAD: Maximum terrain gradient

*Note: This parameter is for advanced users*

Specifies the maximum gradient of the terrain below the vehicle assumed when it is fusing range finder or optical flow to estimate terrain height.

- Range: 0 0.2

- Increment: 0.01

## EK2_BCN_M_NSE: Range beacon measurement noise (m)

*Note: This parameter is for advanced users*

This is the RMS value of noise in the range beacon measurement. Increasing it reduces the weighting on this measurement.

- Range: 0.1 10.0

- Increment: 0.1

- Units: m

## EK2_BCN_I_GTE: Range beacon measurement gate size

*Note: This parameter is for advanced users*

This sets the percentage number of standard deviations applied to the range beacon measurement innovation consistency check. Decreasing it makes it more likely that good measurements will be rejected. Increasing it makes it more likely that bad measurements will be accepted.

- Range: 100 1000

- Increment: 25

## EK2_BCN_DELAY: Range beacon measurement delay (msec)

*Note: This parameter is for advanced users*

This is the number of msec that the range beacon measurements lag behind the inertial measurements. It is the time from the end of the optical flow averaging period and does not include the time delay due to the 100msec of averaging within the flow sensor.

- Range: 0 127

- Increment: 10

- Units: ms

- RebootRequired: True

## EK2_RNG_USE_SPD: Range finder max ground speed

*Note: This parameter is for advanced users*

The range finder will not be used as the primary height source when the horizontal ground speed is greater than this value.

- Range: 2.0 6.0

- Increment: 0.5

- Units: m/s

## EK2_MAG_MASK: Bitmask of active EKF cores that will always use heading fusion

*Note: This parameter is for advanced users*

1 byte bitmap of EKF cores that will disable magnetic field states and use simple magnetic heading fusion at all times. This parameter enables specified cores to be used as a backup for flight into an environment with high levels of external magnetic interference which may degrade the EKF attitude estimate when using 3-axis magnetometer fusion. NOTE : Use of a different magnetometer fusion algorithm on different cores makes unwanted EKF core switches due to magnetometer errors more likely.

- Bitmask: 0:FirstEKF,1:SecondEKF,2:ThirdEKF,3:FourthEKF,4:FifthEKF,5:SixthEKF

- RebootRequired: True

## EK2_OGN_HGT_MASK: Bitmask control of EKF reference height correction

*Note: This parameter is for advanced users*

When a height sensor other than GPS is used as the primary height source by the EKF, the position of the zero height datum is defined by that sensor and its frame of reference. If a GPS height measurement is also available, then the height of the WGS-84 height datum used by the EKF can be corrected so that the height returned by the getLLH() function is compensated for primary height sensor drift and change in datum over time. The first two bit positions control when the height datum will be corrected. Correction is performed using a Bayes filter and only operates when GPS quality permits. The third bit position controls where the corrections to the GPS reference datum are applied. Corrections can be applied to the local vertical position or to the reported EKF origin height (default).

- Bitmask: 0:Correct when using Baro height,1:Correct when using range finder height,2:Apply corrections to local position

- RebootRequired: True

## EK2_EXTNAV_DELAY: external navigation system measurement delay (msec)

*Note: This parameter is for advanced users*

This is the number of msec that the external navigation system measurements lag behind the inertial measurements.

- Range: 0 127

- Increment: 1

- Units: ms

- RebootRequired: True

## EK2_FLOW_USE: Optical flow use bitmask

*Note: This parameter is for advanced users*

Controls if the optical flow data is fused into the 24-state navigation estimator OR the 1-state terrain height estimator.

|Value|Meaning|
|:---:|:---:|
|0|None|
|1|Navigation|
|2|Terrain|

- RebootRequired: True

## EK2_MAG_EF_LIM: EarthField error limit

*Note: This parameter is for advanced users*

This limits the difference between the learned earth magnetic field and the earth field from the world magnetic model tables. A value of zero means to disable the use of the WMM tables.

- Range: 0 500

- Units: mGauss

# EK3 Parameters

## EK3_ENABLE: Enable EKF3

*Note: This parameter is for advanced users*

This enables EKF3. Enabling EKF3 only makes the maths run, it does not mean it will be used for flight control. To use it for flight control set AHRS_EKF_TYPE=3. A reboot or restart will need to be performed after changing the value of EK3_ENABLE for it to take effect.

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
| 1|Enabled|

- RebootRequired: True

## EK3_GPS_TYPE: GPS mode control

*Note: This parameter is for advanced users*

This controls use of GPS measurements : 0 = use 3D velocity & 2D position, 1 = use 2D velocity and 2D position, 2 = use 2D position, 3 = Inhibit GPS use - this can be useful when flying with an optical flow sensor in an environment where GPS quality is poor and subject to large multipath errors.

|Value|Meaning|
|:---:|:---:|
|0|GPS 3D Vel and 2D Pos|
| 1|GPS 2D vel and 2D pos|
| 2|GPS 2D pos|
| 3|No GPS|

## EK3_VELNE_M_NSE: GPS horizontal velocity measurement noise (m/s)

*Note: This parameter is for advanced users*

This sets a lower limit on the speed accuracy reported by the GPS receiver that is used to set horizontal velocity observation noise. If the model of receiver used does not provide a speed accurcy estimate, then the parameter value will be used. Increasing it reduces the weighting of the GPS horizontal velocity measurements.

- Range: 0.05 5.0

- Increment: 0.05

- Units: m/s

## EK3_VELD_M_NSE: GPS vertical velocity measurement noise (m/s)

*Note: This parameter is for advanced users*

This sets a lower limit on the speed accuracy reported by the GPS receiver that is used to set vertical velocity observation noise. If the model of receiver used does not provide a speed accurcy estimate, then the parameter value will be used. Increasing it reduces the weighting of the GPS vertical velocity measurements.

- Range: 0.05 5.0

- Increment: 0.05

- Units: m/s

## EK3_VEL_I_GATE: GPS velocity innovation gate size

*Note: This parameter is for advanced users*

This sets the percentage number of standard deviations applied to the GPS velocity measurement innovation consistency check. Decreasing it makes it more likely that good measurements willbe rejected. Increasing it makes it more likely that bad measurements will be accepted.

- Range: 100 1000

- Increment: 25

## EK3_POSNE_M_NSE: GPS horizontal position measurement noise (m)

*Note: This parameter is for advanced users*

This sets the GPS horizontal position observation noise. Increasing it reduces the weighting of GPS horizontal position measurements.

- Range: 0.1 10.0

- Increment: 0.1

- Units: m

## EK3_POS_I_GATE: GPS position measurement gate size

*Note: This parameter is for advanced users*

This sets the percentage number of standard deviations applied to the GPS position measurement innovation consistency check. Decreasing it makes it more likely that good measurements will be rejected. Increasing it makes it more likely that bad measurements will be accepted.

- Range: 100 1000

- Increment: 25

## EK3_GLITCH_RAD: GPS glitch radius gate size (m)

*Note: This parameter is for advanced users*

This controls the maximum radial uncertainty in position between the value predicted by the filter and the value measured by the GPS before the filter position and velocity states are reset to the GPS. Making this value larger allows the filter to ignore larger GPS glitches but also means that non-GPS errors such as IMU and compass can create a larger error in position before the filter is forced back to the GPS position.

- Range: 10 100

- Increment: 5

- Units: m

## EK3_ALT_SOURCE: Primary altitude sensor source

*Note: This parameter is for advanced users*

Primary height sensor used by the EKF. If the selected option cannot be used, baro is used. 1 uses the range finder and only with optical flow navigation (EK2_GPS_TYPE = 3), Do not use "1" for terrain following. NOTE: the EK3_RNG_USE_HGT parameter can be used to switch to range-finder when close to the ground.

|Value|Meaning|
|:---:|:---:|
|0|Use Baro|
| 1|Use Range Finder|
| 2|Use GPS|
| 3|Use Range Beacon|

- RebootRequired: True

## EK3_ALT_M_NSE: Altitude measurement noise (m)

*Note: This parameter is for advanced users*

This is the RMS value of noise in the altitude measurement. Increasing it reduces the weighting of the baro measurement and will make the filter respond more slowly to baro measurement errors, but will make it more sensitive to GPS and accelerometer errors.

- Range: 0.1 10.0

- Increment: 0.1

- Units: m

## EK3_HGT_I_GATE: Height measurement gate size

*Note: This parameter is for advanced users*

This sets the percentage number of standard deviations applied to the height measurement innovation consistency check. Decreasing it makes it more likely that good measurements will be rejected. Increasing it makes it more likely that bad measurements will be accepted.

- Range: 100 1000

- Increment: 25

## EK3_HGT_DELAY: Height measurement delay (msec)

*Note: This parameter is for advanced users*

This is the number of msec that the Height measurements lag behind the inertial measurements.

- Range: 0 250

- Increment: 10

- RebootRequired: True

- Units: ms

## EK3_MAG_M_NSE: Magnetometer measurement noise (Gauss)

*Note: This parameter is for advanced users*

This is the RMS value of noise in magnetometer measurements. Increasing it reduces the weighting on these measurements.

- Range: 0.01 0.5

- Increment: 0.01

- Units: Gauss

## EK3_MAG_CAL: Magnetometer default fusion mode

*Note: This parameter is for advanced users*

This determines when the filter will use the 3-axis magnetometer fusion model that estimates both earth and body fixed magnetic field states and when it will use a simpler magnetic heading fusion model that does not use magnetic field states. The 3-axis magnetometer fusion is only suitable for use when the external magnetic field environment is stable. EK3_MAG_CAL = 0 uses heading fusion on ground, 3-axis fusion in-flight, and is the default setting for Plane users. EK3_MAG_CAL = 1 uses 3-axis fusion only when manoeuvring. EK3_MAG_CAL = 2 uses heading fusion at all times, is recommended if the external magnetic field is varying and is the default for rovers. EK3_MAG_CAL = 3 uses heading fusion on the ground and 3-axis fusion after the first in-air field and yaw reset has completed, and is the default for copters. EK3_MAG_CAL = 4 uses 3-axis fusion at all times. EK3_MAG_CAL = 5 uses an external yaw sensor with simple heading fusion. NOTE : Use of simple heading magnetometer fusion makes vehicle compass calibration and alignment errors harder for the EKF to detect which reduces the sensitivity of the Copter EKF failsafe algorithm. NOTE: The fusion mode can be forced to 2 for specific EKF cores using the EK3_MAG_MASK parameter.

|Value|Meaning|
|:---:|:---:|
|0|When flying|
|1|When manoeuvring|
|2|Never|
|3|After first climb yaw reset|
|4|Always|
|5|Use external yaw sensor|

- RebootRequired: True

## EK3_MAG_I_GATE: Magnetometer measurement gate size

*Note: This parameter is for advanced users*

This sets the percentage number of standard deviations applied to the magnetometer measurement innovation consistency check. Decreasing it makes it more likely that good measurements will be rejected. Increasing it makes it more likely that bad measurements will be accepted.

- Range: 100 1000

- Increment: 25

## EK3_EAS_M_NSE: Equivalent airspeed measurement noise (m/s)

*Note: This parameter is for advanced users*

This is the RMS value of noise in equivalent airspeed measurements used by planes. Increasing it reduces the weighting of airspeed measurements and will make wind speed estimates less noisy and slower to converge. Increasing also increases navigation errors when dead-reckoning without GPS measurements.

- Range: 0.5 5.0

- Increment: 0.1

- Units: m/s

## EK3_EAS_I_GATE: Airspeed measurement gate size

*Note: This parameter is for advanced users*

This sets the percentage number of standard deviations applied to the airspeed measurement innovation consistency check. Decreasing it makes it more likely that good measurements will be rejected. Increasing it makes it more likely that bad measurements will be accepted.

- Range: 100 1000

- Increment: 25

## EK3_RNG_M_NSE: Range finder measurement noise (m)

*Note: This parameter is for advanced users*

This is the RMS value of noise in the range finder measurement. Increasing it reduces the weighting on this measurement.

- Range: 0.1 10.0

- Increment: 0.1

- Units: m

## EK3_RNG_I_GATE: Range finder measurement gate size

*Note: This parameter is for advanced users*

This sets the percentage number of standard deviations applied to the range finder innovation consistency check. Decreasing it makes it more likely that good measurements will be rejected. Increasing it makes it more likely that bad measurements will be accepted.

- Range: 100 1000

- Increment: 25

## EK3_MAX_FLOW: Maximum valid optical flow rate

*Note: This parameter is for advanced users*

This sets the magnitude maximum optical flow rate in rad/sec that will be accepted by the filter

- Range: 1.0 4.0

- Increment: 0.1

- Units: rad/s

## EK3_FLOW_M_NSE: Optical flow measurement noise (rad/s)

*Note: This parameter is for advanced users*

This is the RMS value of noise and errors in optical flow measurements. Increasing it reduces the weighting on these measurements.

- Range: 0.05 1.0

- Increment: 0.05

- Units: rad/s

## EK3_FLOW_I_GATE: Optical Flow measurement gate size

*Note: This parameter is for advanced users*

This sets the percentage number of standard deviations applied to the optical flow innovation consistency check. Decreasing it makes it more likely that good measurements will be rejected. Increasing it makes it more likely that bad measurements will be accepted.

- Range: 100 1000

- Increment: 25

## EK3_FLOW_DELAY: Optical Flow measurement delay (msec)

*Note: This parameter is for advanced users*

This is the number of msec that the optical flow measurements lag behind the inertial measurements. It is the time from the end of the optical flow averaging period and does not include the time delay due to the 100msec of averaging within the flow sensor.

- Range: 0 250

- Increment: 10

- RebootRequired: True

- Units: ms

## EK3_GYRO_P_NSE: Rate gyro noise (rad/s)

*Note: This parameter is for advanced users*

This control disturbance noise controls the growth of estimated error due to gyro measurement errors excluding bias. Increasing it makes the flter trust the gyro measurements less and other measurements more.

- Range: 0.0001 0.1

- Increment: 0.0001

- Units: rad/s

## EK3_ACC_P_NSE: Accelerometer noise (m/s^2)

*Note: This parameter is for advanced users*

This control disturbance noise controls the growth of estimated error due to accelerometer measurement errors excluding bias. Increasing it makes the flter trust the accelerometer measurements less and other measurements more.

- Range: 0.01 1.0

- Increment: 0.01

- Units: m/s/s

## EK3_GBIAS_P_NSE: Rate gyro bias stability (rad/s/s)

*Note: This parameter is for advanced users*

This state  process noise controls growth of the gyro delta angle bias state error estimate. Increasing it makes rate gyro bias estimation faster and noisier.

- Range: 0.00001 0.001

- Units: rad/s/s

## EK3_ABIAS_P_NSE: Accelerometer bias stability (m/s^3)

*Note: This parameter is for advanced users*

This noise controls the growth of the vertical accelerometer delta velocity bias state error estimate. Increasing it makes accelerometer bias estimation faster and noisier.

- Range: 0.00001 0.005

- Units: m/s/s/s

## EK3_WIND_P_NSE: Wind velocity process noise (m/s^2)

*Note: This parameter is for advanced users*

This state process noise controls the growth of wind state error estimates. Increasing it makes wind estimation faster and noisier.

- Range: 0.01 1.0

- Increment: 0.1

- Units: m/s/s

## EK3_WIND_PSCALE: Height rate to wind process noise scaler

*Note: This parameter is for advanced users*

This controls how much the process noise on the wind states is increased when gaining or losing altitude to take into account changes in wind speed and direction with altitude. Increasing this parameter increases how rapidly the wind states adapt when changing altitude, but does make wind velocity estimation noiser.

- Range: 0.0 1.0

- Increment: 0.1

## EK3_GPS_CHECK: GPS preflight check

*Note: This parameter is for advanced users*

This is a 1 byte bitmap controlling which GPS preflight checks are performed. Set to 0 to bypass all checks. Set to 255 perform all checks. Set to 3 to check just the number of satellites and HDoP. Set to 31 for the most rigorous checks that will still allow checks to pass when the copter is moving, eg launch from a boat.

- Bitmask: 0:NSats,1:HDoP,2:speed error,3:position error,4:yaw error,5:pos drift,6:vert speed,7:horiz speed

## EK3_IMU_MASK: Bitmask of active IMUs

*Note: This parameter is for advanced users*

1 byte bitmap of IMUs to use in EKF3. A separate instance of EKF3 will be started for each IMU selected. Set to 1 to use the first IMU only (default), set to 2 to use the second IMU only, set to 3 to use the first and second IMU. Additional IMU's can be used up to a maximum of 6 if memory and processing resources permit. There may be insufficient memory and processing resources to run multiple instances. If this occurs EKF3 will fail to start.

- Bitmask: 0:FirstIMU,1:SecondIMU,2:ThirdIMU,3:FourthIMU,4:FifthIMU,5:SixthIMU

- RebootRequired: True

## EK3_CHECK_SCALE: GPS accuracy check scaler (%)

*Note: This parameter is for advanced users*

This scales the thresholds that are used to check GPS accuracy before it is used by the EKF. A value of 100 is the default. Values greater than 100 increase and values less than 100 reduce the maximum GPS error the EKF will accept. A value of 200 will double the allowable GPS error.

- Range: 50 200

- Units: %

## EK3_NOAID_M_NSE: Non-GPS operation position uncertainty (m)

*Note: This parameter is for advanced users*

This sets the amount of position variation that the EKF allows for when operating without external measurements (eg GPS or optical flow). Increasing this parameter makes the EKF attitude estimate less sensitive to vehicle manoeuvres but more sensitive to IMU errors.

- Range: 0.5 50.0

- Units: m

## EK3_LOG_MASK: EKF sensor logging IMU mask

*Note: This parameter is for advanced users*

This sets the IMU mask of sensors to do full logging for

- Bitmask: 0:FirstIMU,1:SecondIMU,2:ThirdIMU,3:FourthIMU,4:FifthIMU,5:SixthIMU

- RebootRequired: True

## EK3_YAW_M_NSE: Yaw measurement noise (rad)

*Note: This parameter is for advanced users*

This is the RMS value of noise in yaw measurements from the magnetometer. Increasing it reduces the weighting on these measurements.

- Range: 0.05 1.0

- Increment: 0.05

- Units: rad

## EK3_YAW_I_GATE: Yaw measurement gate size

*Note: This parameter is for advanced users*

This sets the percentage number of standard deviations applied to the magnetometer yaw measurement innovation consistency check. Decreasing it makes it more likely that good measurements will be rejected. Increasing it makes it more likely that bad measurements will be accepted.

- Range: 100 1000

- Increment: 25

## EK3_TAU_OUTPUT: Output complementary filter time constant (centi-sec)

*Note: This parameter is for advanced users*

Sets the time constant of the output complementary filter/predictor in centi-seconds.

- Range: 10 50

- Increment: 5

- Units: cs

## EK3_MAGE_P_NSE: Earth magnetic field process noise (gauss/s)

*Note: This parameter is for advanced users*

This state process noise controls the growth of earth magnetic field state error estimates. Increasing it makes earth magnetic field estimation faster and noisier.

- Range: 0.00001 0.01

- Units: Gauss/s

## EK3_MAGB_P_NSE: Body magnetic field process noise (gauss/s)

*Note: This parameter is for advanced users*

This state process noise controls the growth of body magnetic field state error estimates. Increasing it makes magnetometer bias error estimation faster and noisier.

- Range: 0.00001 0.01

- Units: Gauss/s

## EK3_RNG_USE_HGT: Range finder switch height percentage

*Note: This parameter is for advanced users*

Range finder can be used as the primary height source when below this percentage of its maximum range (see RNGFND_MAX_CM). Set to -1 when EK3_ALT_SOURCE is not set to range finder.  This is not for terrain following.

- Range: -1 70

- Increment: 1

- Units: %

## EK3_TERR_GRAD: Maximum terrain gradient

*Note: This parameter is for advanced users*

Specifies the maximum gradient of the terrain below the vehicle when it is using range finder as a height reference

- Range: 0 0.2

- Increment: 0.01

## EK3_BCN_M_NSE: Range beacon measurement noise (m)

*Note: This parameter is for advanced users*

This is the RMS value of noise in the range beacon measurement. Increasing it reduces the weighting on this measurement.

- Range: 0.1 10.0

- Increment: 0.1

- Units: m

## EK3_BCN_I_GTE: Range beacon measurement gate size

*Note: This parameter is for advanced users*

This sets the percentage number of standard deviations applied to the range beacon measurement innovation consistency check. Decreasing it makes it more likely that good measurements will be rejected. Increasing it makes it more likely that bad measurements will be accepted.

- Range: 100 1000

- Increment: 25

## EK3_BCN_DELAY: Range beacon measurement delay (msec)

*Note: This parameter is for advanced users*

This is the number of msec that the range beacon measurements lag behind the inertial measurements.

- Range: 0 250

- Increment: 10

- RebootRequired: True

- Units: ms

## EK3_RNG_USE_SPD: Range finder max ground speed

*Note: This parameter is for advanced users*

The range finder will not be used as the primary height source when the horizontal ground speed is greater than this value.

- Range: 2.0 6.0

- Increment: 0.5

- Units: m/s

## EK3_ACC_BIAS_LIM: Accelerometer bias limit

*Note: This parameter is for advanced users*

The accelerometer bias state will be limited to +- this value

- Range: 0.5 2.5

- Increment: 0.1

- Units: m/s/s

## EK3_MAG_MASK: Bitmask of active EKF cores that will always use heading fusion

*Note: This parameter is for advanced users*

1 byte bitmap of EKF cores that will disable magnetic field states and use simple magnetic heading fusion at all times. This parameter enables specified cores to be used as a backup for flight into an environment with high levels of external magnetic interference which may degrade the EKF attitude estimate when using 3-axis magnetometer fusion. NOTE : Use of a different magnetometer fusion algorithm on different cores makes unwanted EKF core switches due to magnetometer errors more likely.

- Bitmask: 0:FirstEKF,1:SecondEKF,2:ThirdEKF,3:FourthEKF,4:FifthEKF,5:SixthEKF

- RebootRequired: True

## EK3_OGN_HGT_MASK: Bitmask control of EKF reference height correction

*Note: This parameter is for advanced users*

When a height sensor other than GPS is used as the primary height source by the EKF, the position of the zero height datum is defined by that sensor and its frame of reference. If a GPS height measurement is also available, then the height of the WGS-84 height datum used by the EKF can be corrected so that the height returned by the getLLH() function is compensated for primary height sensor drift and change in datum over time. The first two bit positions control when the height datum will be corrected. Correction is performed using a Bayes filter and only operates when GPS quality permits. The third bit position controls where the corrections to the GPS reference datum are applied. Corrections can be applied to the local vertical position or to the reported EKF origin height (default).

- Bitmask: 0:Correct when using Baro height,1:Correct when using range finder height,2:Apply corrections to local position

- RebootRequired: True

## EK3_VIS_VERR_MIN: Visual odometry minimum velocity error

*Note: This parameter is for advanced users*

This is the 1-STD odometry velocity observation error that will be assumed when maximum quality is reported by the sensor. When quality is between max and min, the error will be calculated using linear interpolation between VIS_VERR_MIN and VIS_VERR_MAX.

- Range: 0.05 0.5

- Increment: 0.05

- Units: m/s

## EK3_VIS_VERR_MAX: Visual odometry maximum velocity error

*Note: This parameter is for advanced users*

This is the 1-STD odometry velocity observation error that will be assumed when minimum quality is reported by the sensor. When quality is between max and min, the error will be calculated using linear interpolation between VIS_VERR_MIN and VIS_VERR_MAX.

- Range: 0.5 5.0

- Increment: 0.1

- Units: m/s

## EK3_WENC_VERR: Wheel odometry velocity error

*Note: This parameter is for advanced users*

This is the 1-STD odometry velocity observation error that will be assumed when wheel encoder data is being fused.

- Range: 0.01 1.0

- Increment: 0.1

- Units: m/s

## EK3_FLOW_USE: Optical flow use bitmask

*Note: This parameter is for advanced users*

Controls if the optical flow data is fused into the 24-state navigation estimator OR the 1-state terrain height estimator.

|Value|Meaning|
|:---:|:---:|
|0|None|
|1|Navigation|
|2|Terrain|

- RebootRequired: True

# FENCE Parameters

## FENCE_ENABLE: Fence enable/disable

Allows you to enable (1) or disable (0) the fence functionality

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|

## FENCE_TYPE: Fence Type

Enabled fence types held as bitmask

|Value|Meaning|
|:---:|:---:|
|0|None|
|1|Altitude|
|2|Circle|
|3|Altitude and Circle|
|4|Polygon|
|5|Altitude and Polygon|
|6|Circle and Polygon|
|7|All|

- Bitmask: 0:Altitude,1:Circle,2:Polygon

## FENCE_ACTION: Fence Action

What action should be taken when fence is breached

|Value|Meaning|
|:---:|:---:|
|0|Report Only|
|1|RTL or Land|
|2|Always Land|
|3|SmartRTL or RTL or Land|
|4|Brake or Land|

## FENCE_ALT_MAX: Fence Maximum Altitude

Maximum altitude allowed before geofence triggers

- Units: m

- Range: 10 1000

- Increment: 1

## FENCE_RADIUS: Circular Fence Radius

Circle fence radius which when breached will cause an RTL

- Units: m

- Range: 30 10000

## FENCE_MARGIN: Fence Margin

Distance that autopilot's should maintain from the fence to avoid a breach

- Units: m

- Range: 1 10

## FENCE_TOTAL: Fence polygon point total

Number of polygon points saved in eeprom (do not update manually)

- Range: 1 20

## FENCE_ALT_MIN: Fence Minimum Altitude

Minimum altitude allowed before geofence triggers

- Units: m

- Range: -100 100

- Increment: 1

# GND Parameters

## GND_ABS_PRESS: Absolute Pressure

*Note: This parameter is for advanced users*

calibrated ground pressure in Pascals

- Units: Pa

- Increment: 1

- ReadOnly: True

- Volatile: True

## GND_TEMP: ground temperature

*Note: This parameter is for advanced users*

User provided ambient ground temperature in degrees Celsius. This is used to improve the calculation of the altitude the vehicle is at. This parameter is not persistent and will be reset to 0 every time the vehicle is rebooted. A value of 0 means use the internal measurement ambient temperature.

- Units: degC

- Increment: 1

- Volatile: True

## GND_ALT_OFFSET: altitude offset

*Note: This parameter is for advanced users*

altitude offset in meters added to barometric altitude. This is used to allow for automatic adjustment of the base barometric altitude by a ground station equipped with a barometer. The value is added to the barometric altitude read by the aircraft. It is automatically reset to 0 when the barometer is calibrated on each reboot or when a preflight calibration is performed.

- Units: m

- Increment: 0.1

## GND_PRIMARY: Primary barometer

*Note: This parameter is for advanced users*

This selects which barometer will be the primary if multiple barometers are found

|Value|Meaning|
|:---:|:---:|
|0|FirstBaro|
|1|2ndBaro|
|2|3rdBaro|

## GND_EXT_BUS: External baro bus

*Note: This parameter is for advanced users*

This selects the bus number for looking for an I2C barometer. When set to -1 it will probe all external i2c buses based on the GND_PROBE_EXT parameter.

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
|0|Bus0|
|1|Bus1|

## GND_SPEC_GRAV: Specific Gravity (For water depth measurement)

This sets the specific gravity of the fluid when flying an underwater ROV.

- Values: 1.0:Freshwater,1.024:Saltwater

## GND_ABS_PRESS2: Absolute Pressure

*Note: This parameter is for advanced users*

calibrated ground pressure in Pascals

- Units: Pa

- Increment: 1

- ReadOnly: True

- Volatile: True

## GND_ABS_PRESS3: Absolute Pressure

*Note: This parameter is for advanced users*

calibrated ground pressure in Pascals

- Units: Pa

- Increment: 1

- ReadOnly: True

- Volatile: True

## GND_FLTR_RNG: Range in which sample is accepted

This sets the range around the average value that new samples must be within to be accepted. This can help reduce the impact of noise on sensors that are on long I2C cables. The value is a percentage from the average value. A value of zero disables this filter.

- Units: %

- Range: 0 100

- Increment: 1

## GND_PROBE_EXT: External barometers to probe

*Note: This parameter is for advanced users*

This sets which types of external i2c barometer to look for. It is a bitmask of barometer types. The I2C buses to probe is based on GND_EXT_BUS. If GND_EXT_BUS is -1 then it will probe all external buses, otherwise it will probe just the bus number given in GND_EXT_BUS.

- Bitmask: 0:BMP085,1:BMP280,2:MS5611,3:MS5607,4:MS5637,5:FBM320,6:DPS280,7:LPS25H,8:Keller,10:MS5837,11:BMP388

|Value|Meaning|
|:---:|:---:|
|1|BMP085|
|2|BMP280|
|4|MS5611|
|8|MS5607|
|16|MS5637|
|32|FBM320|
|64|DPS280|
|128|LPS25H|
|256|Keller|
|512|MS5837|
|1024|BMP388|

# GPS Parameters

## GPS_TYPE: GPS type

*Note: This parameter is for advanced users*

GPS type

|Value|Meaning|
|:---:|:---:|
|0|None|
|1|AUTO|
|2|uBlox|
|3|MTK|
|4|MTK19|
|5|NMEA|
|6|SiRF|
|7|HIL|
|8|SwiftNav|
|9|UAVCAN|
|10|SBF|
|11|GSOF|
|13|ERB|
|14|MAV|
|15|NOVA|
|16|HemisphereNMEA|

- RebootRequired: True

## GPS_TYPE2: 2nd GPS type

*Note: This parameter is for advanced users*

GPS type of 2nd GPS

|Value|Meaning|
|:---:|:---:|
|0|None|
|1|AUTO|
|2|uBlox|
|3|MTK|
|4|MTK19|
|5|NMEA|
|6|SiRF|
|7|HIL|
|8|SwiftNav|
|9|UAVCAN|
|10|SBF|
|11|GSOF|
|13|ERB|
|14|MAV|
|15|NOVA|
|16|HemisphereNMEA|

- RebootRequired: True

## GPS_NAVFILTER: Navigation filter setting

*Note: This parameter is for advanced users*

Navigation filter engine setting

|Value|Meaning|
|:---:|:---:|
|0|Portable|
|2|Stationary|
|3|Pedestrian|
|4|Automotive|
|5|Sea|
|6|Airborne1G|
|7|Airborne2G|
|8|Airborne4G|

## GPS_AUTO_SWITCH: Automatic Switchover Setting

*Note: This parameter is for advanced users*

Automatic switchover to GPS reporting best lock

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|UseBest|
|2|Blend|
|3|UseSecond|

## GPS_MIN_DGPS: Minimum Lock Type Accepted for DGPS

*Note: This parameter is for advanced users*

Sets the minimum type of differential GPS corrections required before allowing to switch into DGPS mode.

|Value|Meaning|
|:---:|:---:|
|0|Any|
|50|FloatRTK|
|100|IntegerRTK|

- RebootRequired: True

## GPS_SBAS_MODE: SBAS Mode

*Note: This parameter is for advanced users*

This sets the SBAS (satellite based augmentation system) mode if available on this GPS. If set to 2 then the SBAS mode is not changed in the GPS. Otherwise the GPS will be reconfigured to enable/disable SBAS. Disabling SBAS may be worthwhile in some parts of the world where an SBAS signal is available but the baseline is too long to be useful.

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|
|2|NoChange|

## GPS_MIN_ELEV: Minimum elevation

*Note: This parameter is for advanced users*

This sets the minimum elevation of satellites above the horizon for them to be used for navigation. Setting this to -100 leaves the minimum elevation set to the GPS modules default.

- Range: -100 90

- Units: deg

## GPS_INJECT_TO: Destination for GPS_INJECT_DATA MAVLink packets

*Note: This parameter is for advanced users*

The GGS can send raw serial packets to inject data to multiple GPSes.

|Value|Meaning|
|:---:|:---:|
|0|send to first GPS|
|1|send to 2nd GPS|
|127|send to all|

## GPS_SBP_LOGMASK: Swift Binary Protocol Logging Mask

*Note: This parameter is for advanced users*

Masked with the SBP msg_type field to determine whether SBR1/SBR2 data is logged

|Value|Meaning|
|:---:|:---:|
|0|None (0x0000)|
|-1|All (0xFFFF)|
|-256|External only (0xFF00)|

## GPS_RAW_DATA: Raw data logging

*Note: This parameter is for advanced users*

Handles logging raw data; on uBlox chips that support raw data this will log RXM messages into logger; on Septentrio this will log on the equipment's SD card and when set to 2, the autopilot will try to stop logging after disarming and restart after arming

|Value|Meaning|
|:---:|:---:|
|0|Ignore|
|1|Always log|
|2|Stop logging when disarmed (SBF only)|
|5|Only log every five samples (uBlox only)|

- RebootRequired: True

## GPS_GNSS_MODE: GNSS system configuration

*Note: This parameter is for advanced users*

Bitmask for what GNSS system to use on the first GPS (all unchecked or zero to leave GPS as configured)

|Value|Meaning|
|:---:|:---:|
|0|Leave as currently configured|
| 1|GPS-NoSBAS|
| 3|GPS+SBAS|
| 4|Galileo-NoSBAS|
| 6|Galileo+SBAS|
| 8|Beidou|
| 51|GPS+IMES+QZSS+SBAS (Japan Only)|
| 64|GLONASS|
| 66|GLONASS+SBAS|
| 67|GPS+GLONASS+SBAS|

- Bitmask: 0:GPS,1:SBAS,2:Galileo,3:Beidou,4:IMES,5:QZSS,6:GLOSNASS

## GPS_SAVE_CFG: Save GPS configuration

*Note: This parameter is for advanced users*

Determines whether the configuration for this GPS should be written to non-volatile memory on the GPS. Currently working for UBlox 6 series and above.

|Value|Meaning|
|:---:|:---:|
|0|Do not save config|
|1|Save config|
|2|Save only when needed|

## GPS_GNSS_MODE2: GNSS system configuration

*Note: This parameter is for advanced users*

Bitmask for what GNSS system to use on the second GPS (all unchecked or zero to leave GPS as configured)

|Value|Meaning|
|:---:|:---:|
|0|Leave as currently configured|
| 1|GPS-NoSBAS|
| 3|GPS+SBAS|
| 4|Galileo-NoSBAS|
| 6|Galileo+SBAS|
| 8|Beidou|
| 51|GPS+IMES+QZSS+SBAS (Japan Only)|
| 64|GLONASS|
| 66|GLONASS+SBAS|
| 67|GPS+GLONASS+SBAS|

- Bitmask: 0:GPS,1:SBAS,2:Galileo,3:Beidou,4:IMES,5:QZSS,6:GLOSNASS

## GPS_AUTO_CONFIG: Automatic GPS configuration

*Note: This parameter is for advanced users*

Controls if the autopilot should automatically configure the GPS based on the parameters and default settings

|Value|Meaning|
|:---:|:---:|
|0|Disables automatic configuration|
|1|Enable automatic configuration|

## GPS_RATE_MS: GPS update rate in milliseconds

*Note: This parameter is for advanced users*

Controls how often the GPS should provide a position update. Lowering below 5Hz is not allowed

- Units: ms

|Value|Meaning|
|:---:|:---:|
|100|10Hz|
|125|8Hz|
|200|5Hz|

- Range: 50 200

## GPS_RATE_MS2: GPS 2 update rate in milliseconds

*Note: This parameter is for advanced users*

Controls how often the GPS should provide a position update. Lowering below 5Hz is not allowed

- Units: ms

|Value|Meaning|
|:---:|:---:|
|100|10Hz|
|125|8Hz|
|200|5Hz|

- Range: 50 200

## GPS_POS1_X: Antenna X position offset

*Note: This parameter is for advanced users*

X position of the first GPS antenna in body frame. Positive X is forward of the origin. Use antenna phase centroid location if provided by the manufacturer.

- Units: m

- Range: -10 10

## GPS_POS1_Y: Antenna Y position offset

*Note: This parameter is for advanced users*

Y position of the first GPS antenna in body frame. Positive Y is to the right of the origin. Use antenna phase centroid location if provided by the manufacturer.

- Units: m

- Range: -10 10

## GPS_POS1_Z: Antenna Z position offset

*Note: This parameter is for advanced users*

Z position of the first GPS antenna in body frame. Positive Z is down from the origin. Use antenna phase centroid location if provided by the manufacturer.

- Units: m

- Range: -10 10

## GPS_POS2_X: Antenna X position offset

*Note: This parameter is for advanced users*

X position of the second GPS antenna in body frame. Positive X is forward of the origin. Use antenna phase centroid location if provided by the manufacturer.

- Units: m

- Range: -10 10

## GPS_POS2_Y: Antenna Y position offset

*Note: This parameter is for advanced users*

Y position of the second GPS antenna in body frame. Positive Y is to the right of the origin. Use antenna phase centroid location if provided by the manufacturer.

- Units: m

- Range: -10 10

## GPS_POS2_Z: Antenna Z position offset

*Note: This parameter is for advanced users*

Z position of the second GPS antenna in body frame. Positive Z is down from the origin. Use antenna phase centroid location if provided by the manufacturer.

- Units: m

- Range: -10 10

## GPS_DELAY_MS: GPS delay in milliseconds

*Note: This parameter is for advanced users*

Controls the amount of GPS  measurement delay that the autopilot compensates for. Set to zero to use the default delay for the detected GPS type.

- Units: ms

- Range: 0 250

- RebootRequired: True

## GPS_DELAY_MS2: GPS 2 delay in milliseconds

*Note: This parameter is for advanced users*

Controls the amount of GPS  measurement delay that the autopilot compensates for. Set to zero to use the default delay for the detected GPS type.

- Units: ms

- Range: 0 250

- RebootRequired: True

## GPS_BLEND_MASK: Multi GPS Blending Mask

*Note: This parameter is for advanced users*

Determines which of the accuracy measures Horizontal position, Vertical Position and Speed are used to calculate the weighting on each GPS receiver when soft switching has been selected by setting GPS_AUTO_SWITCH to 2

- Bitmask: 0:Horiz Pos,1:Vert Pos,2:Speed

## GPS_BLEND_TC: Blending time constant

*Note: This parameter is for advanced users*

Controls the slowest time constant applied to the calculation of GPS position and height offsets used to adjust different GPS receivers for steady state position differences.

- Units: s

- Range: 5.0 30.0

# GRIP Parameters

## GRIP_ENABLE: Gripper Enable/Disable

Gripper enable/disable

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
| 1|Enabled|

## GRIP_TYPE: Gripper Type

Gripper enable/disable

|Value|Meaning|
|:---:|:---:|
|0|None|
|1|Servo|
|2|EPM|

## GRIP_GRAB: Gripper Grab PWM

*Note: This parameter is for advanced users*

PWM value in microseconds sent to Gripper to initiate grabbing the cargo

- Range: 1000 2000

- Units: PWM

## GRIP_RELEASE: Gripper Release PWM

*Note: This parameter is for advanced users*

PWM value in microseconds sent to Gripper to release the cargo

- Range: 1000 2000

- Units: PWM

## GRIP_NEUTRAL: Neutral PWM

*Note: This parameter is for advanced users*

PWM value in microseconds sent to grabber when not grabbing or releasing

- Range: 1000 2000

- Units: PWM

## GRIP_REGRAB: Gripper Regrab interval

*Note: This parameter is for advanced users*

Time in seconds that gripper will regrab the cargo to ensure grip has not weakened; 0 to disable

- Range: 0 255

- Units: s

## GRIP_UAVCAN_ID: EPM UAVCAN Hardpoint ID

Refer to https://docs.zubax.com/opengrab_epm_v3#UAVCAN_interface

- Range: 0 255

# INS Parameters

## INS_GYROFFS_X: Gyro offsets of X axis

*Note: This parameter is for advanced users*

Gyro sensor offsets of X axis. This is setup on each boot during gyro calibrations

- Units: rad/s

## INS_GYROFFS_Y: Gyro offsets of Y axis

*Note: This parameter is for advanced users*

Gyro sensor offsets of Y axis. This is setup on each boot during gyro calibrations

- Units: rad/s

## INS_GYROFFS_Z: Gyro offsets of Z axis

*Note: This parameter is for advanced users*

Gyro sensor offsets of Z axis. This is setup on each boot during gyro calibrations

- Units: rad/s

## INS_GYR2OFFS_X: Gyro2 offsets of X axis

*Note: This parameter is for advanced users*

Gyro2 sensor offsets of X axis. This is setup on each boot during gyro calibrations

- Units: rad/s

## INS_GYR2OFFS_Y: Gyro2 offsets of Y axis

*Note: This parameter is for advanced users*

Gyro2 sensor offsets of Y axis. This is setup on each boot during gyro calibrations

- Units: rad/s

## INS_GYR2OFFS_Z: Gyro2 offsets of Z axis

*Note: This parameter is for advanced users*

Gyro2 sensor offsets of Z axis. This is setup on each boot during gyro calibrations

- Units: rad/s

## INS_GYR3OFFS_X: Gyro3 offsets of X axis

*Note: This parameter is for advanced users*

Gyro3 sensor offsets of X axis. This is setup on each boot during gyro calibrations

- Units: rad/s

## INS_GYR3OFFS_Y: Gyro3 offsets of Y axis

*Note: This parameter is for advanced users*

Gyro3 sensor offsets of Y axis. This is setup on each boot during gyro calibrations

- Units: rad/s

## INS_GYR3OFFS_Z: Gyro3 offsets of Z axis

*Note: This parameter is for advanced users*

Gyro3 sensor offsets of Z axis. This is setup on each boot during gyro calibrations

- Units: rad/s

## INS_ACCSCAL_X: Accelerometer scaling of X axis

*Note: This parameter is for advanced users*

Accelerometer scaling of X axis.  Calculated during acceleration calibration routine

- Range: 0.8 1.2

## INS_ACCSCAL_Y: Accelerometer scaling of Y axis

*Note: This parameter is for advanced users*

Accelerometer scaling of Y axis  Calculated during acceleration calibration routine

- Range: 0.8 1.2

## INS_ACCSCAL_Z: Accelerometer scaling of Z axis

*Note: This parameter is for advanced users*

Accelerometer scaling of Z axis  Calculated during acceleration calibration routine

- Range: 0.8 1.2

## INS_ACCOFFS_X: Accelerometer offsets of X axis

*Note: This parameter is for advanced users*

Accelerometer offsets of X axis. This is setup using the acceleration calibration or level operations

- Units: m/s/s

- Range: -3.5 3.5

## INS_ACCOFFS_Y: Accelerometer offsets of Y axis

*Note: This parameter is for advanced users*

Accelerometer offsets of Y axis. This is setup using the acceleration calibration or level operations

- Units: m/s/s

- Range: -3.5 3.5

## INS_ACCOFFS_Z: Accelerometer offsets of Z axis

*Note: This parameter is for advanced users*

Accelerometer offsets of Z axis. This is setup using the acceleration calibration or level operations

- Units: m/s/s

- Range: -3.5 3.5

## INS_ACC2SCAL_X: Accelerometer2 scaling of X axis

*Note: This parameter is for advanced users*

Accelerometer2 scaling of X axis.  Calculated during acceleration calibration routine

- Range: 0.8 1.2

## INS_ACC2SCAL_Y: Accelerometer2 scaling of Y axis

*Note: This parameter is for advanced users*

Accelerometer2 scaling of Y axis  Calculated during acceleration calibration routine

- Range: 0.8 1.2

## INS_ACC2SCAL_Z: Accelerometer2 scaling of Z axis

*Note: This parameter is for advanced users*

Accelerometer2 scaling of Z axis  Calculated during acceleration calibration routine

- Range: 0.8 1.2

## INS_ACC2OFFS_X: Accelerometer2 offsets of X axis

*Note: This parameter is for advanced users*

Accelerometer2 offsets of X axis. This is setup using the acceleration calibration or level operations

- Units: m/s/s

- Range: -3.5 3.5

## INS_ACC2OFFS_Y: Accelerometer2 offsets of Y axis

*Note: This parameter is for advanced users*

Accelerometer2 offsets of Y axis. This is setup using the acceleration calibration or level operations

- Units: m/s/s

- Range: -3.5 3.5

## INS_ACC2OFFS_Z: Accelerometer2 offsets of Z axis

*Note: This parameter is for advanced users*

Accelerometer2 offsets of Z axis. This is setup using the acceleration calibration or level operations

- Units: m/s/s

- Range: -3.5 3.5

## INS_ACC3SCAL_X: Accelerometer3 scaling of X axis

*Note: This parameter is for advanced users*

Accelerometer3 scaling of X axis.  Calculated during acceleration calibration routine

- Range: 0.8 1.2

## INS_ACC3SCAL_Y: Accelerometer3 scaling of Y axis

*Note: This parameter is for advanced users*

Accelerometer3 scaling of Y axis  Calculated during acceleration calibration routine

- Range: 0.8 1.2

## INS_ACC3SCAL_Z: Accelerometer3 scaling of Z axis

*Note: This parameter is for advanced users*

Accelerometer3 scaling of Z axis  Calculated during acceleration calibration routine

- Range: 0.8 1.2

## INS_ACC3OFFS_X: Accelerometer3 offsets of X axis

*Note: This parameter is for advanced users*

Accelerometer3 offsets of X axis. This is setup using the acceleration calibration or level operations

- Units: m/s/s

- Range: -3.5 3.5

## INS_ACC3OFFS_Y: Accelerometer3 offsets of Y axis

*Note: This parameter is for advanced users*

Accelerometer3 offsets of Y axis. This is setup using the acceleration calibration or level operations

- Units: m/s/s

- Range: -3.5 3.5

## INS_ACC3OFFS_Z: Accelerometer3 offsets of Z axis

*Note: This parameter is for advanced users*

Accelerometer3 offsets of Z axis. This is setup using the acceleration calibration or level operations

- Units: m/s/s

- Range: -3.5 3.5

## INS_GYRO_FILTER: Gyro filter cutoff frequency

*Note: This parameter is for advanced users*

Filter cutoff frequency for gyroscopes. This can be set to a lower value to try to cope with very high vibration levels in aircraft. A value of zero means no filtering (not recommended!)

- Units: Hz

- Range: 0 256

## INS_ACCEL_FILTER: Accel filter cutoff frequency

*Note: This parameter is for advanced users*

Filter cutoff frequency for accelerometers. This can be set to a lower value to try to cope with very high vibration levels in aircraft. A value of zero means no filtering (not recommended!)

- Units: Hz

- Range: 0 256

## INS_USE: Use first IMU for attitude, velocity and position estimates

*Note: This parameter is for advanced users*

Use first IMU for attitude, velocity and position estimates

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|

## INS_USE2: Use second IMU for attitude, velocity and position estimates

*Note: This parameter is for advanced users*

Use second IMU for attitude, velocity and position estimates

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|

## INS_USE3: Use third IMU for attitude, velocity and position estimates

*Note: This parameter is for advanced users*

Use third IMU for attitude, velocity and position estimates

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|

## INS_STILL_THRESH: Stillness threshold for detecting if we are moving

*Note: This parameter is for advanced users*

Threshold to tolerate vibration to determine if vehicle is motionless. This depends on the frame type and if there is a constant vibration due to motors before launch or after landing. Total motionless is about 0.05. Suggested values: Planes/rover use 0.1, multirotors use 1, tradHeli uses 5

- Range: 0.05 50

## INS_GYR_CAL: Gyro Calibration scheme

*Note: This parameter is for advanced users*

Conrols when automatic gyro calibration is performed

|Value|Meaning|
|:---:|:---:|
|0|Never|
| 1|Start-up only|

## INS_TRIM_OPTION: Accel cal trim option

*Note: This parameter is for advanced users*

Specifies how the accel cal routine determines the trims

|Value|Meaning|
|:---:|:---:|
|0|Don't adjust the trims|
|1|Assume first orientation was level|
|2|Assume ACC_BODYFIX is perfectly aligned to the vehicle|

## INS_ACC_BODYFIX: Body-fixed accelerometer

*Note: This parameter is for advanced users*

The body-fixed accelerometer to be used for trim calculation

|Value|Meaning|
|:---:|:---:|
|1|IMU 1|
|2|IMU 2|
|3|IMU 3|

## INS_POS1_X: IMU accelerometer X position

*Note: This parameter is for advanced users*

X position of the first IMU Accelerometer in body frame. Positive X is forward of the origin. Attention: The IMU should be located as close to the vehicle c.g. as practical so that the value of this parameter is minimised. Failure to do so can result in noisy navigation velocity measurements due to vibration and IMU gyro noise. If the IMU cannot be moved and velocity noise is a problem, a location closer to the IMU can be used as the body frame origin.

- Units: m

- Range: -10 10

## INS_POS1_Y: IMU accelerometer Y position

*Note: This parameter is for advanced users*

Y position of the first IMU accelerometer in body frame. Positive Y is to the right of the origin. Attention: The IMU should be located as close to the vehicle c.g. as practical so that the value of this parameter is minimised. Failure to do so can result in noisy navigation velocity measurements due to vibration and IMU gyro noise. If the IMU cannot be moved and velocity noise is a problem, a location closer to the IMU can be used as the body frame origin.

- Units: m

- Range: -10 10

## INS_POS1_Z: IMU accelerometer Z position

*Note: This parameter is for advanced users*

Z position of the first IMU accelerometer in body frame. Positive Z is down from the origin. Attention: The IMU should be located as close to the vehicle c.g. as practical so that the value of this parameter is minimised. Failure to do so can result in noisy navigation velocity measurements due to vibration and IMU gyro noise. If the IMU cannot be moved and velocity noise is a problem, a location closer to the IMU can be used as the body frame origin.

- Units: m

- Range: -10 10

## INS_POS2_X: IMU accelerometer X position

*Note: This parameter is for advanced users*

X position of the second IMU accelerometer in body frame. Positive X is forward of the origin. Attention: The IMU should be located as close to the vehicle c.g. as practical so that the value of this parameter is minimised. Failure to do so can result in noisy navigation velocity measurements due to vibration and IMU gyro noise. If the IMU cannot be moved and velocity noise is a problem, a location closer to the IMU can be used as the body frame origin.

- Units: m

- Range: -10 10

## INS_POS2_Y: IMU accelerometer Y position

*Note: This parameter is for advanced users*

Y position of the second IMU accelerometer in body frame. Positive Y is to the right of the origin. Attention: The IMU should be located as close to the vehicle c.g. as practical so that the value of this parameter is minimised. Failure to do so can result in noisy navigation velocity measurements due to vibration and IMU gyro noise. If the IMU cannot be moved and velocity noise is a problem, a location closer to the IMU can be used as the body frame origin.

- Units: m

- Range: -10 10

## INS_POS2_Z: IMU accelerometer Z position

*Note: This parameter is for advanced users*

Z position of the second IMU accelerometer in body frame. Positive Z is down from the origin. Attention: The IMU should be located as close to the vehicle c.g. as practical so that the value of this parameter is minimised. Failure to do so can result in noisy navigation velocity measurements due to vibration and IMU gyro noise. If the IMU cannot be moved and velocity noise is a problem, a location closer to the IMU can be used as the body frame origin.

- Units: m

- Range: -10 10

## INS_POS3_X: IMU accelerometer X position

*Note: This parameter is for advanced users*

X position of the third IMU accelerometer in body frame. Positive X is forward of the origin. Attention: The IMU should be located as close to the vehicle c.g. as practical so that the value of this parameter is minimised. Failure to do so can result in noisy navigation velocity measurements due to vibration and IMU gyro noise. If the IMU cannot be moved and velocity noise is a problem, a location closer to the IMU can be used as the body frame origin.

- Units: m

- Range: -10 10

## INS_POS3_Y: IMU accelerometer Y position

*Note: This parameter is for advanced users*

Y position of the third IMU accelerometer in body frame. Positive Y is to the right of the origin. Attention: The IMU should be located as close to the vehicle c.g. as practical so that the value of this parameter is minimised. Failure to do so can result in noisy navigation velocity measurements due to vibration and IMU gyro noise. If the IMU cannot be moved and velocity noise is a problem, a location closer to the IMU can be used as the body frame origin.

- Units: m

- Range: -10 10

## INS_POS3_Z: IMU accelerometer Z position

*Note: This parameter is for advanced users*

Z position of the third IMU accelerometer in body frame. Positive Z is down from the origin. Attention: The IMU should be located as close to the vehicle c.g. as practical so that the value of this parameter is minimised. Failure to do so can result in noisy navigation velocity measurements due to vibration and IMU gyro noise. If the IMU cannot be moved and velocity noise is a problem, a location closer to the IMU can be used as the body frame origin.

- Units: m

- Range: -10 10

## INS_GYR_ID: Gyro ID

*Note: This parameter is for advanced users*

Gyro sensor ID, taking into account its type, bus and instance

- ReadOnly: True

## INS_GYR2_ID: Gyro2 ID

*Note: This parameter is for advanced users*

Gyro2 sensor ID, taking into account its type, bus and instance

- ReadOnly: True

## INS_GYR3_ID: Gyro3 ID

*Note: This parameter is for advanced users*

Gyro3 sensor ID, taking into account its type, bus and instance

- ReadOnly: True

## INS_ACC_ID: Accelerometer ID

*Note: This parameter is for advanced users*

Accelerometer sensor ID, taking into account its type, bus and instance

- ReadOnly: True

## INS_ACC2_ID: Accelerometer2 ID

*Note: This parameter is for advanced users*

Accelerometer2 sensor ID, taking into account its type, bus and instance

- ReadOnly: True

## INS_ACC3_ID: Accelerometer3 ID

*Note: This parameter is for advanced users*

Accelerometer3 sensor ID, taking into account its type, bus and instance

- ReadOnly: True

## INS_FAST_SAMPLE: Fast sampling mask

*Note: This parameter is for advanced users*

Mask of IMUs to enable fast sampling on, if available

|Value|Meaning|
|:---:|:---:|
|1|FirstIMUOnly|
|3|FirstAndSecondIMU|

- Bitmask: 0:FirstIMU,1:SecondIMU,2:ThirdIMU

## INS_ENABLE_MASK: IMU enable mask

*Note: This parameter is for advanced users*

Bitmask of IMUs to enable. It can be used to prevent startup of specific detected IMUs

|Value|Meaning|
|:---:|:---:|
|1|FirstIMUOnly|
|3|FirstAndSecondIMU|
|7|FirstSecondAndThirdIMU|
|127|AllIMUs|

- Bitmask: 0:FirstIMU,1:SecondIMU,2:ThirdIMU

# INSHNTCH Parameters

## INS_HNTCH_ENABLE: Harmonic Notch Filter enable

*Note: This parameter is for advanced users*

Harmonic Notch Filter enable

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|

## INS_HNTCH_FREQ: Harmonic Notch Filter base frequency

*Note: This parameter is for advanced users*

Harmonic Notch Filter base center frequency in Hz

- Range: 10 400

- Units: Hz

## INS_HNTCH_BW: Harmonic Notch Filter bandwidth

*Note: This parameter is for advanced users*

Harmonic Notch Filter bandwidth in Hz

- Range: 5 100

- Units: Hz

## INS_HNTCH_ATT: Harmonic Notch Filter attenuation

*Note: This parameter is for advanced users*

Harmonic Notch Filter attenuation in dB

- Range: 5 30

- Units: dB

## INS_HNTCH_HMNCS: Harmonic Notch Filter harmonics

*Note: This parameter is for advanced users*

Bitmask of harmonic frequencies to apply Harmonic Notch Filter to. This option takes effect on the next reboot. A maximum of 3 harmonics can be used at any one time

- Bitmask: 0:1st harmonic,1:2nd harmonic,2:3rd harmonic,3:4th hamronic,4:5th harmonic,5:6th harmonic,6:7th harmonic,7:8th harmonic

- RebootRequired: True

## INS_HNTCH_REF: Harmonic Notch Filter reference value

*Note: This parameter is for advanced users*

Reference value associated with the specified frequency to facilitate frequency scaling of the Harmonic Notch Filter

- Range: 0.1 0.9

- RebootRequired: True

# INSLOG Parameters

## INS_LOG_BAT_CNT: sample count per batch

*Note: This parameter is for advanced users*

Number of samples to take when logging streams of IMU sensor readings.  Will be rounded down to a multiple of 32. This option takes effect on the next reboot.

- Increment: 32

- RebootRequired: True

## INS_LOG_BAT_MASK: Sensor Bitmask

*Note: This parameter is for advanced users*

Bitmap of which IMUs to log batch data for. This option takes effect on the next reboot.

|Value|Meaning|
|:---:|:---:|
|0|None|
|1|First IMU|
|255|All|

- Bitmask: 0:IMU1,1:IMU2,2:IMU3

- RebootRequired: True

## INS_LOG_BAT_OPT: Batch Logging Options Mask

*Note: This parameter is for advanced users*

Options for the BatchSampler

- Bitmask: 0:Sensor-Rate Logging (sample at full sensor rate seen by AP), 1: Sample post-filtering

## INS_LOG_BAT_LGIN: logging interval

Interval between pushing samples to the AP_Logger log

- Units: ms

- Increment: 10

## INS_LOG_BAT_LGCT: logging count

Number of samples to push to count every INS_LOG_BAT_LGIN

- Increment: 1

# INSNOTCH Parameters

## INS_NOTCH_ENABLE: Enable

*Note: This parameter is for advanced users*

Enable notch filter

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|

## INS_NOTCH_ATT: Attenuation

*Note: This parameter is for advanced users*

Notch attenuation in dB

- Range: 5 30

- Units: dB

## INS_NOTCH_FREQ: Frequency

*Note: This parameter is for advanced users*

Notch center frequency in Hz

- Range: 10 400

- Units: Hz

## INS_NOTCH_BW: Bandwidth

*Note: This parameter is for advanced users*

Notch bandwidth in Hz

- Range: 5 100

- Units: Hz

# LEAK Parameters

## LEAK1_PIN: Pin that leak detector is connected to

Pin that the leak detector is connected to

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
|50|Pixhawk Aux1|
|51|Pixhawk Aux2|
|52|Pixhawk Aux3|
|53|Pixhawk Aux4|
|54|Pixhawk Aux5|
|55|Pixhawk Aux6|
|13|Pixhawk 3.3ADC1|
|14|Pixhawk 3.3ADC2|
|15|Pixhawk 6.6ADC|

- RebootRequired: True

## LEAK1_LOGIC: Default reading of leak detector when dry

Default reading of leak detector when dry

|Value|Meaning|
|:---:|:---:|
|0|Low|
|1|High|

## LEAK2_PIN: Pin that leak detector is connected to

Pin that the leak detector is connected to

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
|50|Pixhawk Aux1|
|51|Pixhawk Aux2|
|52|Pixhawk Aux3|
|53|Pixhawk Aux4|
|54|Pixhawk Aux5|
|55|Pixhawk Aux6|
|13|Pixhawk 3.3ADC1|
|14|Pixhawk 3.3ADC2|
|15|Pixhawk 6.6ADC|

- RebootRequired: True

## LEAK2_LOGIC: Default reading of leak detector when dry

Default reading of leak detector when dry

|Value|Meaning|
|:---:|:---:|
|0|Low|
|1|High|

## LEAK3_PIN: Pin that leak detector is connected to

Pin that the leak detector is connected to

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
|50|Pixhawk Aux1|
|51|Pixhawk Aux2|
|52|Pixhawk Aux3|
|53|Pixhawk Aux4|
|54|Pixhawk Aux5|
|55|Pixhawk Aux6|
|13|Pixhawk 3.3ADC1|
|14|Pixhawk 3.3ADC2|
|15|Pixhawk 6.6ADC|

- RebootRequired: True

## LEAK3_LOGIC: Default reading of leak detector when dry

Default reading of leak detector when dry

|Value|Meaning|
|:---:|:---:|
|0|Low|
|1|High|

# LOG Parameters

## LOG_BACKEND_TYPE: AP_Logger Backend Storage type

Bitmap of what Logger backend types to enable. Block-based logging is available on SITL and boards with dataflash chips. Multiple backends can be selected.

|Value|Meaning|
|:---:|:---:|
|0|None|
|1|File|
|2|MAVLink|
|3|File and MAVLink|
|4|Block|
|6|Block and MAVLink|

- Bitmask: 0:File,1:MAVLink,2:Block

## LOG_FILE_BUFSIZE: Maximum AP_Logger File Backend buffer size (in kilobytes)

The AP_Logger_File backend uses a buffer to store data before writing to the block device.  Raising this value may reduce "gaps" in your SD card logging.  This buffer size may be reduced depending on available memory.  PixHawk requires at least 4 kilobytes.  Maximum value available here is 64 kilobytes.

## LOG_DISARMED: Enable logging while disarmed

If LOG_DISARMED is set to 1 then logging will be enabled while disarmed. This can make for very large logfiles but can help a lot when tracking down startup issues

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|

## LOG_REPLAY: Enable logging of information needed for Replay

If LOG_REPLAY is set to 1 then the EKF2 state estimator will log detailed information needed for diagnosing problems with the Kalman filter. It is suggested that you also raise LOG_FILE_BUFSIZE to give more buffer space for logging and use a high quality microSD card to ensure no sensor data is lost

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|

## LOG_FILE_DSRMROT: Stop logging to current file on disarm

When set, the current log file is closed when the vehicle is disarmed.  If LOG_DISARMED is set then a fresh log will be opened.

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|

## LOG_MAV_BUFSIZE: Maximum AP_Logger MAVLink Backend buffer size

*Note: This parameter is for advanced users*

Maximum amount of memory to allocate to AP_Logger-over-mavlink

- Units: kB

## LOG_FILE_TIMEOUT: Timeout before giving up on file writes

This controls the amount of time before failing writes to a log file cause the file to be closed and logging stopped.

- Units: s

# LOIT Parameters

## LOIT_ANG_MAX: Loiter Angle Max

*Note: This parameter is for advanced users*

Loiter maximum lean angle. Set to zero for 2/3 of PSC_ANGLE_MAX or ANGLE_MAX

- Units: deg

- Range: 0 45

- Increment: 1

## LOIT_SPEED: Loiter Horizontal Maximum Speed

Defines the maximum speed in cm/s which the aircraft will travel horizontally while in loiter mode

- Units: cm/s

- Range: 20 2000

- Increment: 50

## LOIT_ACC_MAX: Loiter maximum correction acceleration

*Note: This parameter is for advanced users*

Loiter maximum correction acceleration in cm/s/s.  Higher values cause the copter to correct position errors more aggressively.

- Units: cm/s/s

- Range: 100 981

- Increment: 1

## LOIT_BRK_ACCEL: Loiter braking acceleration

*Note: This parameter is for advanced users*

Loiter braking acceleration in cm/s/s. Higher values stop the copter more quickly when the stick is centered.

- Units: cm/s/s

- Range: 25 250

- Increment: 1

## LOIT_BRK_JERK: Loiter braking jerk

*Note: This parameter is for advanced users*

Loiter braking jerk in cm/s/s/s. Higher values will remove braking faster if the pilot moves the sticks during a braking maneuver.

- Units: cm/s/s/s

- Range: 500 5000

- Increment: 1

## LOIT_BRK_DELAY: Loiter brake start delay (in seconds)

*Note: This parameter is for advanced users*

Loiter brake start delay (in seconds)

- Units: s

- Range: 0 2

- Increment: 0.1

# MNT Parameters

## MNT_DEFLT_MODE: Mount default operating mode

Mount default operating mode on startup and after control is returned from autopilot

|Value|Meaning|
|:---:|:---:|
|0|Retracted|
|1|Neutral|
|2|MavLink Targeting|
|3|RC Targeting|
|4|GPS Point|

## MNT_RETRACT_X: Mount roll angle when in retracted position

Mount roll angle when in retracted position

- Units: deg

- Range: -180.00 179.99

- Increment: 1

## MNT_RETRACT_Y: Mount tilt/pitch angle when in retracted position

Mount tilt/pitch angle when in retracted position

- Units: deg

- Range: -180.00 179.99

- Increment: 1

## MNT_RETRACT_Z: Mount yaw/pan angle when in retracted position

Mount yaw/pan angle when in retracted position

- Units: deg

- Range: -180.00 179.99

- Increment: 1

## MNT_NEUTRAL_X: Mount roll angle when in neutral position

Mount roll angle when in neutral position

- Units: deg

- Range: -180.00 179.99

- Increment: 1

## MNT_NEUTRAL_Y: Mount tilt/pitch angle when in neutral position

Mount tilt/pitch angle when in neutral position

- Units: deg

- Range: -180.00 179.99

- Increment: 1

## MNT_NEUTRAL_Z: Mount pan/yaw angle when in neutral position

Mount pan/yaw angle when in neutral position

- Units: deg

- Range: -180.00 179.99

- Increment: 1

## MNT_STAB_ROLL: Stabilize mount's roll angle

enable roll stabilisation relative to Earth

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|

## MNT_STAB_TILT: Stabilize mount's pitch/tilt angle

enable tilt/pitch stabilisation relative to Earth

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|

## MNT_STAB_PAN: Stabilize mount pan/yaw angle

enable pan/yaw stabilisation relative to Earth

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|

## MNT_RC_IN_ROLL: roll RC input channel

0 for none, any other for the RC channel to be used to control roll movements

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|5|RC5|
|6|RC6|
|7|RC7|
|8|RC8|
|9|RC9|
|10|RC10|
|11|RC11|
|12|RC12|

## MNT_ANGMIN_ROL: Minimum roll angle

Minimum physical roll angular position of mount.

- Units: cdeg

- Range: -18000 17999

- Increment: 1

## MNT_ANGMAX_ROL: Maximum roll angle

Maximum physical roll angular position of the mount

- Units: cdeg

- Range: -18000 17999

- Increment: 1

## MNT_RC_IN_TILT: tilt (pitch) RC input channel

0 for none, any other for the RC channel to be used to control tilt (pitch) movements

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|5|RC5|
|6|RC6|
|7|RC7|
|8|RC8|
|9|RC9|
|10|RC10|
|11|RC11|
|12|RC12|

## MNT_ANGMIN_TIL: Minimum tilt angle

Minimum physical tilt (pitch) angular position of mount.

- Units: cdeg

- Range: -18000 17999

- Increment: 1

## MNT_ANGMAX_TIL: Maximum tilt angle

Maximum physical tilt (pitch) angular position of the mount

- Units: cdeg

- Range: -18000 17999

- Increment: 1

## MNT_RC_IN_PAN: pan (yaw) RC input channel

0 for none, any other for the RC channel to be used to control pan (yaw) movements

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|5|RC5|
|6|RC6|
|7|RC7|
|8|RC8|
|9|RC9|
|10|RC10|
|11|RC11|
|12|RC12|

## MNT_ANGMIN_PAN: Minimum pan angle

Minimum physical pan (yaw) angular position of mount.

- Units: cdeg

- Range: -18000 17999

- Increment: 1

## MNT_ANGMAX_PAN: Maximum pan angle

Maximum physical pan (yaw) angular position of the mount

- Units: cdeg

- Range: -18000 17999

- Increment: 1

## MNT_JSTICK_SPD: mount joystick speed

0 for position control, small for low speeds, 100 for max speed. A good general value is 10 which gives a movement speed of 3 degrees per second.

- Range: 0 100

- Increment: 1

## MNT_LEAD_RLL: Roll stabilization lead time

Causes the servo angle output to lead the current angle of the vehicle by some amount of time based on current angular rate, compensating for servo delay. Increase until the servo is responsive but doesn't overshoot. Does nothing with pan stabilization enabled.

- Units: s

- Range: 0.0 0.2

- Increment: .005

## MNT_LEAD_PTCH: Pitch stabilization lead time

Causes the servo angle output to lead the current angle of the vehicle by some amount of time based on current angular rate. Increase until the servo is responsive but doesn't overshoot. Does nothing with pan stabilization enabled.

- Units: s

- Range: 0.0 0.2

- Increment: .005

## MNT_TYPE: Mount Type

Mount Type (None, Servo or MAVLink)

|Value|Meaning|
|:---:|:---:|
|0|None|
| 1|Servo|
| 2|3DR Solo|
| 3|Alexmos Serial|
| 4|SToRM32 MAVLink|
| 5|SToRM32 Serial|

- RebootRequired: True

## MNT2_DEFLT_MODE: Mount default operating mode

Mount default operating mode on startup and after control is returned from autopilot

|Value|Meaning|
|:---:|:---:|
|0|Retracted|
|1|Neutral|
|2|MavLink Targeting|
|3|RC Targeting|
|4|GPS Point|

## MNT2_RETRACT_X: Mount2 roll angle when in retracted position

Mount2 roll angle when in retracted position

- Units: deg

- Range: -180.00 179.99

- Increment: 1

## MNT2_RETRACT_Y: Mount2 tilt/pitch angle when in retracted position

Mount2 tilt/pitch angle when in retracted position

- Units: deg

- Range: -180.00 179.99

- Increment: 1

## MNT2_RETRACT_Z: Mount2 yaw/pan angle when in retracted position

Mount2 yaw/pan angle when in retracted position

- Units: deg

- Range: -180.00 179.99

- Increment: 1

## MNT2_NEUTRAL_X: Mount2 roll angle when in neutral position

Mount2 roll angle when in neutral position

- Units: deg

- Range: -180.00 179.99

- Increment: 1

## MNT2_NEUTRAL_Y: Mount2 tilt/pitch angle when in neutral position

Mount2 tilt/pitch angle when in neutral position

- Units: deg

- Range: -180.00 179.99

- Increment: 1

## MNT2_NEUTRAL_Z: Mount2 pan/yaw angle when in neutral position

Mount2 pan/yaw angle when in neutral position

- Units: deg

- Range: -180.00 179.99

- Increment: 1

## MNT2_STAB_ROLL: Stabilize Mount2's roll angle

enable roll stabilisation relative to Earth

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|

## MNT2_STAB_TILT: Stabilize Mount2's pitch/tilt angle

enable tilt/pitch stabilisation relative to Earth

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|

## MNT2_STAB_PAN: Stabilize mount2 pan/yaw angle

enable pan/yaw stabilisation relative to Earth

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|

## MNT2_RC_IN_ROLL: Mount2's roll RC input channel

0 for none, any other for the RC channel to be used to control roll movements

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|5|RC5|
|6|RC6|
|7|RC7|
|8|RC8|
|9|RC9|
|10|RC10|
|11|RC11|
|12|RC12|

## MNT2_ANGMIN_ROL: Mount2's minimum roll angle

Mount2's minimum physical roll angular position

- Units: cdeg

- Range: -18000 17999

- Increment: 1

## MNT2_ANGMAX_ROL: Mount2's maximum roll angle

Mount2's maximum physical roll angular position

- Units: cdeg

- Range: -18000 17999

- Increment: 1

## MNT2_RC_IN_TILT: Mount2's tilt (pitch) RC input channel

0 for none, any other for the RC channel to be used to control tilt (pitch) movements

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|5|RC5|
|6|RC6|
|7|RC7|
|8|RC8|
|9|RC9|
|10|RC10|
|11|RC11|
|12|RC12|

## MNT2_ANGMIN_TIL: Mount2's minimum tilt angle

Mount2's minimum physical tilt (pitch) angular position

- Units: cdeg

- Range: -18000 17999

- Increment: 1

## MNT2_ANGMAX_TIL: Mount2's maximum tilt angle

Mount2's maximum physical tilt (pitch) angular position

- Units: cdeg

- Range: -18000 17999

- Increment: 1

## MNT2_RC_IN_PAN: Mount2's pan (yaw) RC input channel

0 for none, any other for the RC channel to be used to control pan (yaw) movements

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|5|RC5|
|6|RC6|
|7|RC7|
|8|RC8|
|9|RC9|
|10|RC10|
|11|RC11|
|12|RC12|

## MNT2_ANGMIN_PAN: Mount2's minimum pan angle

Mount2's minimum physical pan (yaw) angular position

- Units: cdeg

- Range: -18000 17999

- Increment: 1

## MNT2_ANGMAX_PAN: Mount2's maximum pan angle

MOunt2's maximum physical pan (yaw) angular position

- Units: cdeg

- Range: -18000 17999

- Increment: 1

## MNT2_LEAD_RLL: Mount2's Roll stabilization lead time

Causes the servo angle output to lead the current angle of the vehicle by some amount of time based on current angular rate, compensating for servo delay. Increase until the servo is responsive but doesn't overshoot. Does nothing with pan stabilization enabled.

- Units: s

- Range: 0.0 0.2

- Increment: .005

## MNT2_LEAD_PTCH: Mount2's Pitch stabilization lead time

Causes the servo angle output to lead the current angle of the vehicle by some amount of time based on current angular rate. Increase until the servo is responsive but doesn't overshoot. Does nothing with pan stabilization enabled.

- Units: s

- Range: 0.0 0.2

- Increment: .005

## MNT2_TYPE: Mount2 Type

Mount Type (None, Servo or MAVLink)

|Value|Meaning|
|:---:|:---:|
|0|None|
| 1|Servo|
| 2|3DR Solo|
| 3|Alexmos Serial|
| 4|SToRM32 MAVLink|
| 5|SToRM32 Serial|

# MOT Parameters

## MOT_1_DIRECTION: Motor normal or reverse

Used to change motor rotation directions without changing wires

|Value|Meaning|
|:---:|:---:|
|1|normal|
|-1|reverse|

## MOT_2_DIRECTION: Motor normal or reverse

Used to change motor rotation directions without changing wires

|Value|Meaning|
|:---:|:---:|
|1|normal|
|-1|reverse|

## MOT_3_DIRECTION: Motor normal or reverse

Used to change motor rotation directions without changing wires

|Value|Meaning|
|:---:|:---:|
|1|normal|
|-1|reverse|

## MOT_4_DIRECTION: Motor normal or reverse

Used to change motor rotation directions without changing wires

|Value|Meaning|
|:---:|:---:|
|1|normal|
|-1|reverse|

## MOT_5_DIRECTION: Motor normal or reverse

Used to change motor rotation directions without changing wires

|Value|Meaning|
|:---:|:---:|
|1|normal|
|-1|reverse|

## MOT_6_DIRECTION: Motor normal or reverse

Used to change motor rotation directions without changing wires

|Value|Meaning|
|:---:|:---:|
|1|normal|
|-1|reverse|

## MOT_7_DIRECTION: Motor normal or reverse

Used to change motor rotation directions without changing wires

|Value|Meaning|
|:---:|:---:|
|1|normal|
|-1|reverse|

## MOT_8_DIRECTION: Motor normal or reverse

Used to change motor rotation directions without changing wires

|Value|Meaning|
|:---:|:---:|
|1|normal|
|-1|reverse|

## MOT_FV_CPLNG_K: Forward/vertical to pitch decoupling factor

Used to decouple pitch from forward/vertical motion. 0 to disable, 1.2 normal

- Range: 0.0 1.5

- Increment: 0.1

## MOT_9_DIRECTION: Motor normal or reverse

Used to change motor rotation directions without changing wires

|Value|Meaning|
|:---:|:---:|
|1|normal|
|-1|reverse|

## MOT_10_DIRECTION: Motor normal or reverse

Used to change motor rotation directions without changing wires

|Value|Meaning|
|:---:|:---:|
|1|normal|
|-1|reverse|

## MOT_11_DIRECTION: Motor normal or reverse

Used to change motor rotation directions without changing wires

|Value|Meaning|
|:---:|:---:|
|1|normal|
|-1|reverse|

## MOT_12_DIRECTION: Motor normal or reverse

Used to change motor rotation directions without changing wires

|Value|Meaning|
|:---:|:---:|
|1|normal|
|-1|reverse|

## MOT_YAW_HEADROOM: Matrix Yaw Min

*Note: This parameter is for advanced users*

Yaw control is given at least this pwm in microseconds range

- Range: 0 500

- Units: PWM

## MOT_THST_EXPO: Thrust Curve Expo

*Note: This parameter is for advanced users*

Motor thrust curve exponent (from 0 for linear to 1.0 for second order curve)

- Range: 0.25 0.8

## MOT_SPIN_MAX: Motor Spin maximum

*Note: This parameter is for advanced users*

Point at which the thrust saturates expressed as a number from 0 to 1 in the entire output range

- Values: 0.9:Low, 0.95:Default, 1.0:High

## MOT_BAT_VOLT_MAX: Battery voltage compensation maximum voltage

*Note: This parameter is for advanced users*

Battery voltage compensation maximum voltage (voltage above this will have no additional scaling effect on thrust).  Recommend 4.4 * cell count, 0 = Disabled

- Range: 6 35

- Units: V

## MOT_BAT_VOLT_MIN: Battery voltage compensation minimum voltage

*Note: This parameter is for advanced users*

Battery voltage compensation minimum voltage (voltage below this will have no additional scaling effect on thrust).  Recommend 3.5 * cell count, 0 = Disabled

- Range: 6 35

- Units: V

## MOT_BAT_CURR_MAX: Motor Current Max

*Note: This parameter is for advanced users*

Maximum current over which maximum throttle is limited (0 = Disabled)

- Range: 0 200

- Units: A

## MOT_PWM_TYPE: Output PWM type

*Note: This parameter is for advanced users*

This selects the output PWM type, allowing for normal PWM continuous output, OneShot, brushed or DShot motor output

|Value|Meaning|
|:---:|:---:|
|0|Normal|
|1|OneShot|
|2|OneShot125|
|3|Brushed|
|4|DShot150|
|5|DShot300|
|6|DShot600|
|7|DShot1200|

- RebootRequired: True

## MOT_PWM_MIN: PWM output miniumum

*Note: This parameter is for advanced users*

This sets the min PWM output value in microseconds that will ever be output to the motors, 0 = use input RC3_MIN

- Units: PWM

- Range: 0 2000

## MOT_PWM_MAX: PWM output maximum

*Note: This parameter is for advanced users*

This sets the max PWM value in microseconds that will ever be output to the motors, 0 = use input RC3_MAX

- Units: PWM

- Range: 0 2000

## MOT_SPIN_MIN: Motor Spin minimum

*Note: This parameter is for advanced users*

Point at which the thrust starts expressed as a number from 0 to 1 in the entire output range.  Should be higher than MOT_SPIN_ARM.

- Values: 0.0:Low, 0.15:Default, 0.3:High

## MOT_SPIN_ARM: Motor Spin armed

*Note: This parameter is for advanced users*

Point at which the motors start to spin expressed as a number from 0 to 1 in the entire output range.  Should be lower than MOT_SPIN_MIN.

- Values: 0.0:Low, 0.1:Default, 0.2:High

## MOT_BAT_CURR_TC: Motor Current Max Time Constant

*Note: This parameter is for advanced users*

Time constant used to limit the maximum current

- Range: 0 10

- Units: s

## MOT_THST_HOVER: Thrust Hover Value

*Note: This parameter is for advanced users*

Motor thrust needed to hover expressed as a number from 0 to 1

- Range: 0.2 0.8

## MOT_HOVER_LEARN: Hover Value Learning

*Note: This parameter is for advanced users*

Enable/Disable automatic learning of hover throttle

|Value|Meaning|
|:---:|:---:|
|0|Disabled|

## MOT_SAFE_DISARM: Motor PWM output disabled when disarmed

*Note: This parameter is for advanced users*

Disables motor PWM output when disarmed

|Value|Meaning|
|:---:|:---:|
|0|PWM enabled while disarmed|
| 1|PWM disabled while disarmed|

## MOT_YAW_SV_ANGLE: Yaw Servo Max Lean Angle

Yaw servo's maximum lean angle

- Range: 5 80

- Units: deg

- Increment: 1

## MOT_SPOOL_TIME: Spool up time

*Note: This parameter is for advanced users*

Time in seconds to spool up the motors from zero to min throttle. 

- Range: 0 2

- Units: s

- Increment: 0.1

## MOT_BOOST_SCALE: Motor boost scale

*Note: This parameter is for advanced users*

Booster motor output scaling factor vs main throttle.  The output to the BoostThrottle servo will be the main throttle times this scaling factor. A higher scaling factor will put more of the load on the booster motor. A value of 1 will set the BoostThrottle equal to the main throttle.

- Range: 0 5

- Increment: 0.1

## MOT_BAT_IDX: Battery compensation index

*Note: This parameter is for advanced users*

Which battery monitor should be used for doing compensation

|Value|Meaning|
|:---:|:---:|
|0|First battery|
| 1|Second battery|

## MOT_SLEW_UP_TIME: Output slew time for increasing throttle

*Note: This parameter is for advanced users*

Time in seconds to slew output from zero to full.  For medium size copter such as a Solo, a value of 0.25 is a good starting point.  This is used to limit the rate at which output can change. Range is constrained between 0 and 0.5.

- Range: 0 .5

- Units: s

- Increment: 0.001

## MOT_SLEW_DN_TIME: Output slew time for decreasing throttle

*Note: This parameter is for advanced users*

Time in seconds to slew output from full to zero.  For medium size copter such as a Solo, a value of 0.275 is a good starting point.  This is used to limit the rate at which output can change.  Range is constrained between 0 and 0.5.

- Range: 0 .5

- Units: s

- Increment: 0.001

# NTF Parameters

## NTF_LED_BRIGHT: LED Brightness

*Note: This parameter is for advanced users*

Select the RGB LED brightness level. When USB is connected brightness will never be higher than low regardless of the setting.

|Value|Meaning|
|:---:|:---:|
|0|Off|
|1|Low|
|2|Medium|
|3|High|

## NTF_BUZZ_ENABLE: Buzzer enable

*Note: This parameter is for advanced users*

Enable or disable the buzzer.

|Value|Meaning|
|:---:|:---:|
|0|Disable|
|1|Enable|

## NTF_LED_OVERRIDE: Specifies colour source for the RGBLed

*Note: This parameter is for advanced users*

Specifies the source for the colours and brightness for the LED.  OutbackChallenge conforms to the MedicalExpress (https://uavchallenge.org/medical-express/) rules, essentially "Green" is disarmed (safe-to-approach), "Red" is armed (not safe-to-approach). Traffic light is a simplified color set, red when armed, yellow when the safety switch is not surpressing outputs (but disarmed), and green when outputs are surpressed and disarmed, the LED will blink faster if disarmed and failing arming checks.

|Value|Meaning|
|:---:|:---:|
|0|Standard|
|1|MAVLink|
|2|OutbackChallenge|
|3|TrafficLight|

## NTF_DISPLAY_TYPE: Type of on-board I2C display

*Note: This parameter is for advanced users*

This sets up the type of on-board I2C display. Disabled by default.

|Value|Meaning|
|:---:|:---:|
|0|Disable|
|1|ssd1306|
|2|sh1106|
|10|SITL|

## NTF_OREO_THEME: OreoLED Theme

*Note: This parameter is for advanced users*

Enable/Disable Solo Oreo LED driver, 0 to disable, 1 for Aircraft theme, 2 for Rover theme

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Aircraft|
|2|Rover|

## NTF_BUZZ_PIN: Buzzer pin

*Note: This parameter is for advanced users*

Enables to connect active buzzer to arbitrary pin. Requires 3-pin buzzer or additional MOSFET!

|Value|Meaning|
|:---:|:---:|
|0|Disabled|

## NTF_LED_TYPES: LED Driver Types

*Note: This parameter is for advanced users*

Controls what types of LEDs will be enabled

- Bitmask: 0:Build in LED, 1:Internal ToshibaLED, 2:External ToshibaLED, 3:External PCA9685, 4:Oreo LED, 5:UAVCAN, 6:NCP5623 External, 7:NCP5623 Internal, 8:NeoPixel

## NTF_BUZZ_ON_LVL: Buzzer-on pin logic level

*Note: This parameter is for advanced users*

Specifies pin level that indicates buzzer should play

|Value|Meaning|
|:---:|:---:|
|0|LowIsOn|
|1|HighIsOn|

## NTF_BUZZ_VOLUME: Buzzer volume

Enable or disable the buzzer.

- Range: 0 100

- Units: %

# PSC Parameters

## PSC_ACC_XY_FILT: XY Acceleration filter cutoff frequency

*Note: This parameter is for advanced users*

Lower values will slow the response of the navigation controller and reduce twitchiness

- Units: Hz

- Range: 0.5 5

- Increment: 0.1

## PSC_POSZ_P: Position (vertical) controller P gain

Position (vertical) controller P gain.  Converts the difference between the desired altitude and actual altitude into a climb or descent rate which is passed to the throttle rate controller

- Range: 1.000 3.000

## PSC_VELZ_P: Velocity (vertical) controller P gain

Velocity (vertical) controller P gain.  Converts the difference between desired vertical speed and actual speed into a desired acceleration that is passed to the throttle acceleration controller

- Range: 1.000 8.000

## PSC_ACCZ_P: Acceleration (vertical) controller P gain

Acceleration (vertical) controller P gain.  Converts the difference between desired vertical acceleration and actual acceleration into a motor output

- Range: 0.500 1.500

- Increment: 0.05

## PSC_ACCZ_I: Acceleration (vertical) controller I gain

Acceleration (vertical) controller I gain.  Corrects long-term difference in desired vertical acceleration and actual acceleration

- Range: 0.000 3.000

## PSC_ACCZ_IMAX: Acceleration (vertical) controller I gain maximum

Acceleration (vertical) controller I gain maximum.  Constrains the maximum pwm that the I term will generate

- Range: 0 1000

- Units: d%

## PSC_ACCZ_D: Acceleration (vertical) controller D gain

Acceleration (vertical) controller D gain.  Compensates for short-term change in desired vertical acceleration vs actual acceleration

- Range: 0.000 0.400

## PSC_ACCZ_FILT: Acceleration (vertical) controller filter

Filter applied to acceleration to reduce noise.  Lower values reduce noise but add delay.

- Range: 1.000 100.000

- Units: Hz

## PSC_POSXY_P: Position (horizonal) controller P gain

Position controller P gain.  Converts the distance (in the latitude direction) to the target location into a desired speed which is then passed to the loiter latitude rate controller

- Range: 0.500 2.000

## PSC_VELXY_P: Velocity (horizontal) P gain

*Note: This parameter is for advanced users*

Velocity (horizontal) P gain.  Converts the difference between desired velocity to a target acceleration

- Range: 0.1 6.0

- Increment: 0.1

## PSC_VELXY_I: Velocity (horizontal) I gain

*Note: This parameter is for advanced users*

Velocity (horizontal) I gain.  Corrects long-term difference in desired velocity to a target acceleration

- Range: 0.02 1.00

- Increment: 0.01

## PSC_VELXY_D: Velocity (horizontal) D gain

*Note: This parameter is for advanced users*

Velocity (horizontal) D gain.  Corrects short-term changes in velocity

- Range: 0.00 1.00

- Increment: 0.001

## PSC_VELXY_IMAX: Velocity (horizontal) integrator maximum

*Note: This parameter is for advanced users*

Velocity (horizontal) integrator maximum.  Constrains the target acceleration that the I gain will output

- Range: 0 4500

- Increment: 10

- Units: cm/s/s

## PSC_VELXY_FILT: Velocity (horizontal) input filter

*Note: This parameter is for advanced users*

Velocity (horizontal) input filter.  This filter (in hz) is applied to the input for P and I terms

- Range: 0 100

- Units: Hz

## PSC_VELXY_D_FILT: Velocity (horizontal) input filter

*Note: This parameter is for advanced users*

Velocity (horizontal) input filter.  This filter (in hz) is applied to the input for P and I terms

- Range: 0 100

- Units: Hz

## PSC_ANGLE_MAX: Position Control Angle Max

*Note: This parameter is for advanced users*

Maximum lean angle autopilot can request.  Set to zero to use ANGLE_MAX parameter value

- Units: deg

- Range: 0 45

- Increment: 1

# RC Parameters

## RC_OVERRIDE_TIME: RC override timeout

*Note: This parameter is for advanced users*

Timeout after which RC overrides will no longer be used, and RC input will resume, 0 will disable RC overrides, -1 will never timeout, and continue using overrides until they are disabled

- Range: 0.0 120.0

- Units: s

## RC_OPTIONS: RC options

*Note: This parameter is for advanced users*

RC input options

- Bitmask: 0:Ignore RC Receiver, 1:Ignore MAVLink Overrides, 2:Ignore Receiver Failsafe

# RCn Parameters

## RCn_MIN: RC min PWM

*Note: This parameter is for advanced users*

RC minimum PWM pulse width in microseconds. Typically 1000 is lower limit, 1500 is neutral and 2000 is upper limit.

- Units: PWM

- Range: 800 2200

- Increment: 1

## RCn_TRIM: RC trim PWM

*Note: This parameter is for advanced users*

RC trim (neutral) PWM pulse width in microseconds. Typically 1000 is lower limit, 1500 is neutral and 2000 is upper limit.

- Units: PWM

- Range: 800 2200

- Increment: 1

## RCn_MAX: RC max PWM

*Note: This parameter is for advanced users*

RC maximum PWM pulse width in microseconds. Typically 1000 is lower limit, 1500 is neutral and 2000 is upper limit.

- Units: PWM

- Range: 800 2200

- Increment: 1

## RCn_REVERSED: RC reversed

*Note: This parameter is for advanced users*

Reverse channel input. Set to 0 for normal operation. Set to 1 to reverse this input channel.

|Value|Meaning|
|:---:|:---:|
|0|Normal|
|1|Reversed|

## RCn_DZ: RC dead-zone

*Note: This parameter is for advanced users*

PWM dead zone in microseconds around trim or bottom

- Units: PWM

- Range: 0 200

## RCn_OPTION: RC input option

Function assigned to this RC channel

|Value|Meaning|
|:---:|:---:|
|0|Do Nothing|
| 4|ModeRTL|
| 9|Camera Trigger|
| 16|ModeAuto|
| 24|Auto Mission Reset|
| 28|Relay On/Off|
| 29|Landing Gear|
| 34|Relay2 On/Off|
| 30|Lost Plane Sound|
| 31|Motor Emergency Stop|
| 35|Relay3 On/Off|
| 36|Relay4 On/Off|
| 41|ArmDisarm|
| 43|InvertedFlight|
| 46|RC Override Enable|
| 51|ModeManual|
| 55|ModeGuided|
| 58|Clear Waypoints|
| 62|Compass Learn|
| 64|Reverse Throttle|
| 65|GPS Disable|
| 66|Relay5|
| 67|Relay6|
| 72|ModeCircle|
| 100|KillIMU1|
| 101|KillIMU2|

# RELAY Parameters

## RELAY_PIN: First Relay Pin

Digital pin number for first relay control. This is the pin used for camera control.

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
|49|BB Blue GP0 pin 4|
|50|AUXOUT1|
|51|AUXOUT2|
|52|AUXOUT3|
|53|AUXOUT4|
|54|AUXOUT5|
|55|AUXOUT6|
|57|BB Blue GP0 pin 3|
|113|BB Blue GP0 pin 6|
|116|BB Blue GP0 pin 5|

## RELAY_PIN2: Second Relay Pin

Digital pin number for 2nd relay control.

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
|49|BB Blue GP0 pin 4|
|50|AUXOUT1|
|51|AUXOUT2|
|52|AUXOUT3|
|53|AUXOUT4|
|54|AUXOUT5|
|55|AUXOUT6|
|57|BB Blue GP0 pin 3|
|113|BB Blue GP0 pin 6|
|116|BB Blue GP0 pin 5|

## RELAY_PIN3: Third Relay Pin

Digital pin number for 3rd relay control.

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
|49|BB Blue GP0 pin 4|
|50|AUXOUT1|
|51|AUXOUT2|
|52|AUXOUT3|
|53|AUXOUT4|
|54|AUXOUT5|
|55|AUXOUT6|
|57|BB Blue GP0 pin 3|
|113|BB Blue GP0 pin 6|
|116|BB Blue GP0 pin 5|

## RELAY_PIN4: Fourth Relay Pin

Digital pin number for 4th relay control.

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
|49|BB Blue GP0 pin 4|
|50|AUXOUT1|
|51|AUXOUT2|
|52|AUXOUT3|
|53|AUXOUT4|
|54|AUXOUT5|
|55|AUXOUT6|
|57|BB Blue GP0 pin 3|
|113|BB Blue GP0 pin 6|
|116|BB Blue GP0 pin 5|

## RELAY_DEFAULT: Default relay state

The state of the relay on boot.

|Value|Meaning|
|:---:|:---:|
|0|Off|
|1|On|
|2|NoChange|

## RELAY_PIN5: Fifth Relay Pin

Digital pin number for 5th relay control.

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
|49|BB Blue GP0 pin 4|
|50|AUXOUT1|
|51|AUXOUT2|
|52|AUXOUT3|
|53|AUXOUT4|
|54|AUXOUT5|
|55|AUXOUT6|
|57|BB Blue GP0 pin 3|
|113|BB Blue GP0 pin 6|
|116|BB Blue GP0 pin 5|

## RELAY_PIN6: Sixth Relay Pin

Digital pin number for 6th relay control.

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
|49|BB Blue GP0 pin 4|
|50|AUXOUT1|
|51|AUXOUT2|
|52|AUXOUT3|
|53|AUXOUT4|
|54|AUXOUT5|
|55|AUXOUT6|
|57|BB Blue GP0 pin 3|
|113|BB Blue GP0 pin 6|
|116|BB Blue GP0 pin 5|

# RNGFND1 Parameters

## RNGFND1_TYPE: Rangefinder type

What type of rangefinder device that is connected

|Value|Meaning|
|:---:|:---:|
|0|None|
|1|Analog|
|2|MaxbotixI2C|
|3|LidarLiteV2-I2C|
|5|PWM|
|6|BBB-PRU|
|7|LightWareI2C|
|8|LightWareSerial|
|9|Bebop|
|10|MAVLink|
|11|uLanding|
|12|LeddarOne|
|13|MaxbotixSerial|
|14|TeraRangerI2C|
|15|LidarLiteV3-I2C|
|16|VL53L0X|
|17|NMEA|
|18|WASP-LRF|
|19|BenewakeTF02|
|20|BenewakeTFmini|
|21|LidarLightV3HP|
|22|PWM|
|23|BlueRoboticsPing|
|24|UAVCAN|
|25|BenewakeTFMiniPlus|

## RNGFND1_PIN: Rangefinder pin

Analog pin that rangefinder is connected to. Set to 11 on PX4 for the analog 'airspeed' port. Set to 15 on the Pixhawk for the analog 'airspeed' port.

|Value|Meaning|
|:---:|:---:|
|-1|Not Used|
| 11|PX4-airspeed port|
| 15|Pixhawk-airspeed port|

## RNGFND1_SCALING: Rangefinder scaling

Scaling factor between rangefinder reading and distance. For the linear and inverted functions this is in meters per volt. For the hyperbolic function the units are meterVolts.

- Units: m/V

- Increment: 0.001

## RNGFND1_OFFSET: rangefinder offset

Offset in volts for zero distance for analog rangefinders. Offset added to distance in centimeters for PWM and I2C Lidars

- Units: V

- Increment: 0.001

## RNGFND1_FUNCTION: Rangefinder function

Control over what function is used to calculate distance. For a linear function, the distance is (voltage-offset)*scaling. For a inverted function the distance is (offset-voltage)*scaling. For a hyperbolic function the distance is scaling/(voltage-offset). The functions return the distance in meters.

|Value|Meaning|
|:---:|:---:|
|0|Linear|
|1|Inverted|
|2|Hyperbolic|

## RNGFND1_MIN_CM: Rangefinder minimum distance

Minimum distance in centimeters that rangefinder can reliably read

- Units: cm

- Increment: 1

## RNGFND1_MAX_CM: Rangefinder maximum distance

Maximum distance in centimeters that rangefinder can reliably read

- Units: cm

- Increment: 1

## RNGFND1_STOP_PIN: Rangefinder stop pin

Digital pin that enables/disables rangefinder measurement for the pwm rangefinder. A value of -1 means no pin. If this is set, then the pin is set to 1 to enable the rangefinder and set to 0 to disable it. This is used to enable powersaving when out of range.

|Value|Meaning|
|:---:|:---:|
|-1|Not Used|
|50|Pixhawk AUXOUT1|
|51|Pixhawk AUXOUT2|
|52|Pixhawk AUXOUT3|
|53|Pixhawk AUXOUT4|
|54|Pixhawk AUXOUT5|
|55|Pixhawk AUXOUT6|
|111|PX4 FMU Relay1|
|112|PX4 FMU Relay2|
|113|PX4IO Relay1|
|114|PX4IO Relay2|
|115|PX4IO ACC1|
|116|PX4IO ACC2|

## RNGFND1_RMETRIC: Ratiometric

This parameter sets whether an analog rangefinder is ratiometric. Most analog rangefinders are ratiometric, meaning that their output voltage is influenced by the supply voltage. Some analog rangefinders (such as the SF/02) have their own internal voltage regulators so they are not ratiometric.

|Value|Meaning|
|:---:|:---:|
|0|No|
|1|Yes|

## RNGFND1_PWRRNG: Powersave range

This parameter sets the estimated terrain distance in meters above which the sensor will be put into a power saving mode (if available). A value of zero means power saving is not enabled

- Units: m

- Range: 0 32767

## RNGFND1_GNDCLEAR: Distance (in cm) from the range finder to the ground

This parameter sets the expected range measurement(in cm) that the range finder should return when the vehicle is on the ground.

- Units: cm

- Range: 5 127

- Increment: 1

## RNGFND1_ADDR: Bus address of sensor

This sets the bus address of the sensor, where applicable. Used for the I2C and UAVCAN sensors to allow for multiple sensors on different addresses. A value of 0 disables the sensor.

- Range: 0 127

- Increment: 1

## RNGFND1_POS_X:  X position offset

*Note: This parameter is for advanced users*

X position of the first rangefinder in body frame. Positive X is forward of the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFND1_POS_Y: Y position offset

*Note: This parameter is for advanced users*

Y position of the first rangefinder in body frame. Positive Y is to the right of the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFND1_POS_Z: Z position offset

*Note: This parameter is for advanced users*

Z position of the first rangefinder in body frame. Positive Z is down from the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFND1_ORIENT: Rangefinder orientation

*Note: This parameter is for advanced users*

Orientation of rangefinder

|Value|Meaning|
|:---:|:---:|
|0|Forward|
| 1|Forward-Right|
| 2|Right|
| 3|Back-Right|
| 4|Back|
| 5|Back-Left|
| 6|Left|
| 7|Forward-Left|
| 24|Up|
| 25|Down|

# RNGFND1 Parameters

## RNGFND1_WSP_MAVG: Moving Average Range

*Note: This parameter is for advanced users*

Sets the number of historic range results to use for calculating the current range result. When MAVG is greater than 1, the current range result will be the current measured value averaged with the N-1 previous results

- Range: 0 255

## RNGFND1_WSP_MEDF: Moving Median Filter

*Note: This parameter is for advanced users*

Sets the window size for the real-time median filter. When MEDF is greater than 0 the median filter is active

- Range: 0 255

## RNGFND1_WSP_FRQ: Frequency

*Note: This parameter is for advanced users*

Sets the repetition frequency of the ranging operation in Hertz. Upon entering the desired frequency the system will calculate the nearest frequency that it can handle according to the resolution of internal timers.

- Range: 0 10000

## RNGFND1_WSP_AVG: Multi-pulse averages

*Note: This parameter is for advanced users*

Sets the number of pulses to be used in multi-pulse averaging mode. In this mode, a sequence of rapid fire ranges are taken and then averaged to improve the accuracy of the measurement

- Range: 0 255

## RNGFND1_WSP_THR: Sensitivity threshold

*Note: This parameter is for advanced users*

Sets the system sensitivity. Larger values of THR represent higher sensitivity. The system may limit the maximum value of THR to prevent excessive false alarm rates based on settings made at the factory. Set to -1 for automatic threshold adjustments

- Range: -1 255

## RNGFND1_WSP_BAUD: Baud rate

*Note: This parameter is for advanced users*

Desired baud rate

|Value|Meaning|
|:---:|:---:|
|0|Low Speed|
|1|High Speed|

# RNGFND2 Parameters

## RNGFND2_TYPE: Rangefinder type

What type of rangefinder device that is connected

|Value|Meaning|
|:---:|:---:|
|0|None|
|1|Analog|
|2|MaxbotixI2C|
|3|LidarLiteV2-I2C|
|5|PWM|
|6|BBB-PRU|
|7|LightWareI2C|
|8|LightWareSerial|
|9|Bebop|
|10|MAVLink|
|11|uLanding|
|12|LeddarOne|
|13|MaxbotixSerial|
|14|TeraRangerI2C|
|15|LidarLiteV3-I2C|
|16|VL53L0X|
|17|NMEA|
|18|WASP-LRF|
|19|BenewakeTF02|
|20|BenewakeTFmini|
|21|LidarLightV3HP|
|22|PWM|
|23|BlueRoboticsPing|
|24|UAVCAN|
|25|BenewakeTFMiniPlus|

## RNGFND2_PIN: Rangefinder pin

Analog pin that rangefinder is connected to. Set to 11 on PX4 for the analog 'airspeed' port. Set to 15 on the Pixhawk for the analog 'airspeed' port.

|Value|Meaning|
|:---:|:---:|
|-1|Not Used|
| 11|PX4-airspeed port|
| 15|Pixhawk-airspeed port|

## RNGFND2_SCALING: Rangefinder scaling

Scaling factor between rangefinder reading and distance. For the linear and inverted functions this is in meters per volt. For the hyperbolic function the units are meterVolts.

- Units: m/V

- Increment: 0.001

## RNGFND2_OFFSET: rangefinder offset

Offset in volts for zero distance for analog rangefinders. Offset added to distance in centimeters for PWM and I2C Lidars

- Units: V

- Increment: 0.001

## RNGFND2_FUNCTION: Rangefinder function

Control over what function is used to calculate distance. For a linear function, the distance is (voltage-offset)*scaling. For a inverted function the distance is (offset-voltage)*scaling. For a hyperbolic function the distance is scaling/(voltage-offset). The functions return the distance in meters.

|Value|Meaning|
|:---:|:---:|
|0|Linear|
|1|Inverted|
|2|Hyperbolic|

## RNGFND2_MIN_CM: Rangefinder minimum distance

Minimum distance in centimeters that rangefinder can reliably read

- Units: cm

- Increment: 1

## RNGFND2_MAX_CM: Rangefinder maximum distance

Maximum distance in centimeters that rangefinder can reliably read

- Units: cm

- Increment: 1

## RNGFND2_STOP_PIN: Rangefinder stop pin

Digital pin that enables/disables rangefinder measurement for the pwm rangefinder. A value of -1 means no pin. If this is set, then the pin is set to 1 to enable the rangefinder and set to 0 to disable it. This is used to enable powersaving when out of range.

|Value|Meaning|
|:---:|:---:|
|-1|Not Used|
|50|Pixhawk AUXOUT1|
|51|Pixhawk AUXOUT2|
|52|Pixhawk AUXOUT3|
|53|Pixhawk AUXOUT4|
|54|Pixhawk AUXOUT5|
|55|Pixhawk AUXOUT6|
|111|PX4 FMU Relay1|
|112|PX4 FMU Relay2|
|113|PX4IO Relay1|
|114|PX4IO Relay2|
|115|PX4IO ACC1|
|116|PX4IO ACC2|

## RNGFND2_RMETRIC: Ratiometric

This parameter sets whether an analog rangefinder is ratiometric. Most analog rangefinders are ratiometric, meaning that their output voltage is influenced by the supply voltage. Some analog rangefinders (such as the SF/02) have their own internal voltage regulators so they are not ratiometric.

|Value|Meaning|
|:---:|:---:|
|0|No|
|1|Yes|

## RNGFND2_PWRRNG: Powersave range

This parameter sets the estimated terrain distance in meters above which the sensor will be put into a power saving mode (if available). A value of zero means power saving is not enabled

- Units: m

- Range: 0 32767

## RNGFND2_GNDCLEAR: Distance (in cm) from the range finder to the ground

This parameter sets the expected range measurement(in cm) that the range finder should return when the vehicle is on the ground.

- Units: cm

- Range: 5 127

- Increment: 1

## RNGFND2_ADDR: Bus address of sensor

This sets the bus address of the sensor, where applicable. Used for the I2C and UAVCAN sensors to allow for multiple sensors on different addresses. A value of 0 disables the sensor.

- Range: 0 127

- Increment: 1

## RNGFND2_POS_X:  X position offset

*Note: This parameter is for advanced users*

X position of the first rangefinder in body frame. Positive X is forward of the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFND2_POS_Y: Y position offset

*Note: This parameter is for advanced users*

Y position of the first rangefinder in body frame. Positive Y is to the right of the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFND2_POS_Z: Z position offset

*Note: This parameter is for advanced users*

Z position of the first rangefinder in body frame. Positive Z is down from the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFND2_ORIENT: Rangefinder orientation

*Note: This parameter is for advanced users*

Orientation of rangefinder

|Value|Meaning|
|:---:|:---:|
|0|Forward|
| 1|Forward-Right|
| 2|Right|
| 3|Back-Right|
| 4|Back|
| 5|Back-Left|
| 6|Left|
| 7|Forward-Left|
| 24|Up|
| 25|Down|

# RNGFND2 Parameters

## RNGFND2_WSP_MAVG: Moving Average Range

*Note: This parameter is for advanced users*

Sets the number of historic range results to use for calculating the current range result. When MAVG is greater than 1, the current range result will be the current measured value averaged with the N-1 previous results

- Range: 0 255

## RNGFND2_WSP_MEDF: Moving Median Filter

*Note: This parameter is for advanced users*

Sets the window size for the real-time median filter. When MEDF is greater than 0 the median filter is active

- Range: 0 255

## RNGFND2_WSP_FRQ: Frequency

*Note: This parameter is for advanced users*

Sets the repetition frequency of the ranging operation in Hertz. Upon entering the desired frequency the system will calculate the nearest frequency that it can handle according to the resolution of internal timers.

- Range: 0 10000

## RNGFND2_WSP_AVG: Multi-pulse averages

*Note: This parameter is for advanced users*

Sets the number of pulses to be used in multi-pulse averaging mode. In this mode, a sequence of rapid fire ranges are taken and then averaged to improve the accuracy of the measurement

- Range: 0 255

## RNGFND2_WSP_THR: Sensitivity threshold

*Note: This parameter is for advanced users*

Sets the system sensitivity. Larger values of THR represent higher sensitivity. The system may limit the maximum value of THR to prevent excessive false alarm rates based on settings made at the factory. Set to -1 for automatic threshold adjustments

- Range: -1 255

## RNGFND2_WSP_BAUD: Baud rate

*Note: This parameter is for advanced users*

Desired baud rate

|Value|Meaning|
|:---:|:---:|
|0|Low Speed|
|1|High Speed|

# RNGFND3 Parameters

## RNGFND3_TYPE: Rangefinder type

What type of rangefinder device that is connected

|Value|Meaning|
|:---:|:---:|
|0|None|
|1|Analog|
|2|MaxbotixI2C|
|3|LidarLiteV2-I2C|
|5|PWM|
|6|BBB-PRU|
|7|LightWareI2C|
|8|LightWareSerial|
|9|Bebop|
|10|MAVLink|
|11|uLanding|
|12|LeddarOne|
|13|MaxbotixSerial|
|14|TeraRangerI2C|
|15|LidarLiteV3-I2C|
|16|VL53L0X|
|17|NMEA|
|18|WASP-LRF|
|19|BenewakeTF02|
|20|BenewakeTFmini|
|21|LidarLightV3HP|
|22|PWM|
|23|BlueRoboticsPing|
|24|UAVCAN|
|25|BenewakeTFMiniPlus|

## RNGFND3_PIN: Rangefinder pin

Analog pin that rangefinder is connected to. Set to 11 on PX4 for the analog 'airspeed' port. Set to 15 on the Pixhawk for the analog 'airspeed' port.

|Value|Meaning|
|:---:|:---:|
|-1|Not Used|
| 11|PX4-airspeed port|
| 15|Pixhawk-airspeed port|

## RNGFND3_SCALING: Rangefinder scaling

Scaling factor between rangefinder reading and distance. For the linear and inverted functions this is in meters per volt. For the hyperbolic function the units are meterVolts.

- Units: m/V

- Increment: 0.001

## RNGFND3_OFFSET: rangefinder offset

Offset in volts for zero distance for analog rangefinders. Offset added to distance in centimeters for PWM and I2C Lidars

- Units: V

- Increment: 0.001

## RNGFND3_FUNCTION: Rangefinder function

Control over what function is used to calculate distance. For a linear function, the distance is (voltage-offset)*scaling. For a inverted function the distance is (offset-voltage)*scaling. For a hyperbolic function the distance is scaling/(voltage-offset). The functions return the distance in meters.

|Value|Meaning|
|:---:|:---:|
|0|Linear|
|1|Inverted|
|2|Hyperbolic|

## RNGFND3_MIN_CM: Rangefinder minimum distance

Minimum distance in centimeters that rangefinder can reliably read

- Units: cm

- Increment: 1

## RNGFND3_MAX_CM: Rangefinder maximum distance

Maximum distance in centimeters that rangefinder can reliably read

- Units: cm

- Increment: 1

## RNGFND3_STOP_PIN: Rangefinder stop pin

Digital pin that enables/disables rangefinder measurement for the pwm rangefinder. A value of -1 means no pin. If this is set, then the pin is set to 1 to enable the rangefinder and set to 0 to disable it. This is used to enable powersaving when out of range.

|Value|Meaning|
|:---:|:---:|
|-1|Not Used|
|50|Pixhawk AUXOUT1|
|51|Pixhawk AUXOUT2|
|52|Pixhawk AUXOUT3|
|53|Pixhawk AUXOUT4|
|54|Pixhawk AUXOUT5|
|55|Pixhawk AUXOUT6|
|111|PX4 FMU Relay1|
|112|PX4 FMU Relay2|
|113|PX4IO Relay1|
|114|PX4IO Relay2|
|115|PX4IO ACC1|
|116|PX4IO ACC2|

## RNGFND3_RMETRIC: Ratiometric

This parameter sets whether an analog rangefinder is ratiometric. Most analog rangefinders are ratiometric, meaning that their output voltage is influenced by the supply voltage. Some analog rangefinders (such as the SF/02) have their own internal voltage regulators so they are not ratiometric.

|Value|Meaning|
|:---:|:---:|
|0|No|
|1|Yes|

## RNGFND3_PWRRNG: Powersave range

This parameter sets the estimated terrain distance in meters above which the sensor will be put into a power saving mode (if available). A value of zero means power saving is not enabled

- Units: m

- Range: 0 32767

## RNGFND3_GNDCLEAR: Distance (in cm) from the range finder to the ground

This parameter sets the expected range measurement(in cm) that the range finder should return when the vehicle is on the ground.

- Units: cm

- Range: 5 127

- Increment: 1

## RNGFND3_ADDR: Bus address of sensor

This sets the bus address of the sensor, where applicable. Used for the I2C and UAVCAN sensors to allow for multiple sensors on different addresses. A value of 0 disables the sensor.

- Range: 0 127

- Increment: 1

## RNGFND3_POS_X:  X position offset

*Note: This parameter is for advanced users*

X position of the first rangefinder in body frame. Positive X is forward of the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFND3_POS_Y: Y position offset

*Note: This parameter is for advanced users*

Y position of the first rangefinder in body frame. Positive Y is to the right of the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFND3_POS_Z: Z position offset

*Note: This parameter is for advanced users*

Z position of the first rangefinder in body frame. Positive Z is down from the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFND3_ORIENT: Rangefinder orientation

*Note: This parameter is for advanced users*

Orientation of rangefinder

|Value|Meaning|
|:---:|:---:|
|0|Forward|
| 1|Forward-Right|
| 2|Right|
| 3|Back-Right|
| 4|Back|
| 5|Back-Left|
| 6|Left|
| 7|Forward-Left|
| 24|Up|
| 25|Down|

# RNGFND3 Parameters

## RNGFND3_WSP_MAVG: Moving Average Range

*Note: This parameter is for advanced users*

Sets the number of historic range results to use for calculating the current range result. When MAVG is greater than 1, the current range result will be the current measured value averaged with the N-1 previous results

- Range: 0 255

## RNGFND3_WSP_MEDF: Moving Median Filter

*Note: This parameter is for advanced users*

Sets the window size for the real-time median filter. When MEDF is greater than 0 the median filter is active

- Range: 0 255

## RNGFND3_WSP_FRQ: Frequency

*Note: This parameter is for advanced users*

Sets the repetition frequency of the ranging operation in Hertz. Upon entering the desired frequency the system will calculate the nearest frequency that it can handle according to the resolution of internal timers.

- Range: 0 10000

## RNGFND3_WSP_AVG: Multi-pulse averages

*Note: This parameter is for advanced users*

Sets the number of pulses to be used in multi-pulse averaging mode. In this mode, a sequence of rapid fire ranges are taken and then averaged to improve the accuracy of the measurement

- Range: 0 255

## RNGFND3_WSP_THR: Sensitivity threshold

*Note: This parameter is for advanced users*

Sets the system sensitivity. Larger values of THR represent higher sensitivity. The system may limit the maximum value of THR to prevent excessive false alarm rates based on settings made at the factory. Set to -1 for automatic threshold adjustments

- Range: -1 255

## RNGFND3_WSP_BAUD: Baud rate

*Note: This parameter is for advanced users*

Desired baud rate

|Value|Meaning|
|:---:|:---:|
|0|Low Speed|
|1|High Speed|

# RNGFND4 Parameters

## RNGFND4_TYPE: Rangefinder type

What type of rangefinder device that is connected

|Value|Meaning|
|:---:|:---:|
|0|None|
|1|Analog|
|2|MaxbotixI2C|
|3|LidarLiteV2-I2C|
|5|PWM|
|6|BBB-PRU|
|7|LightWareI2C|
|8|LightWareSerial|
|9|Bebop|
|10|MAVLink|
|11|uLanding|
|12|LeddarOne|
|13|MaxbotixSerial|
|14|TeraRangerI2C|
|15|LidarLiteV3-I2C|
|16|VL53L0X|
|17|NMEA|
|18|WASP-LRF|
|19|BenewakeTF02|
|20|BenewakeTFmini|
|21|LidarLightV3HP|
|22|PWM|
|23|BlueRoboticsPing|
|24|UAVCAN|
|25|BenewakeTFMiniPlus|

## RNGFND4_PIN: Rangefinder pin

Analog pin that rangefinder is connected to. Set to 11 on PX4 for the analog 'airspeed' port. Set to 15 on the Pixhawk for the analog 'airspeed' port.

|Value|Meaning|
|:---:|:---:|
|-1|Not Used|
| 11|PX4-airspeed port|
| 15|Pixhawk-airspeed port|

## RNGFND4_SCALING: Rangefinder scaling

Scaling factor between rangefinder reading and distance. For the linear and inverted functions this is in meters per volt. For the hyperbolic function the units are meterVolts.

- Units: m/V

- Increment: 0.001

## RNGFND4_OFFSET: rangefinder offset

Offset in volts for zero distance for analog rangefinders. Offset added to distance in centimeters for PWM and I2C Lidars

- Units: V

- Increment: 0.001

## RNGFND4_FUNCTION: Rangefinder function

Control over what function is used to calculate distance. For a linear function, the distance is (voltage-offset)*scaling. For a inverted function the distance is (offset-voltage)*scaling. For a hyperbolic function the distance is scaling/(voltage-offset). The functions return the distance in meters.

|Value|Meaning|
|:---:|:---:|
|0|Linear|
|1|Inverted|
|2|Hyperbolic|

## RNGFND4_MIN_CM: Rangefinder minimum distance

Minimum distance in centimeters that rangefinder can reliably read

- Units: cm

- Increment: 1

## RNGFND4_MAX_CM: Rangefinder maximum distance

Maximum distance in centimeters that rangefinder can reliably read

- Units: cm

- Increment: 1

## RNGFND4_STOP_PIN: Rangefinder stop pin

Digital pin that enables/disables rangefinder measurement for the pwm rangefinder. A value of -1 means no pin. If this is set, then the pin is set to 1 to enable the rangefinder and set to 0 to disable it. This is used to enable powersaving when out of range.

|Value|Meaning|
|:---:|:---:|
|-1|Not Used|
|50|Pixhawk AUXOUT1|
|51|Pixhawk AUXOUT2|
|52|Pixhawk AUXOUT3|
|53|Pixhawk AUXOUT4|
|54|Pixhawk AUXOUT5|
|55|Pixhawk AUXOUT6|
|111|PX4 FMU Relay1|
|112|PX4 FMU Relay2|
|113|PX4IO Relay1|
|114|PX4IO Relay2|
|115|PX4IO ACC1|
|116|PX4IO ACC2|

## RNGFND4_RMETRIC: Ratiometric

This parameter sets whether an analog rangefinder is ratiometric. Most analog rangefinders are ratiometric, meaning that their output voltage is influenced by the supply voltage. Some analog rangefinders (such as the SF/02) have their own internal voltage regulators so they are not ratiometric.

|Value|Meaning|
|:---:|:---:|
|0|No|
|1|Yes|

## RNGFND4_PWRRNG: Powersave range

This parameter sets the estimated terrain distance in meters above which the sensor will be put into a power saving mode (if available). A value of zero means power saving is not enabled

- Units: m

- Range: 0 32767

## RNGFND4_GNDCLEAR: Distance (in cm) from the range finder to the ground

This parameter sets the expected range measurement(in cm) that the range finder should return when the vehicle is on the ground.

- Units: cm

- Range: 5 127

- Increment: 1

## RNGFND4_ADDR: Bus address of sensor

This sets the bus address of the sensor, where applicable. Used for the I2C and UAVCAN sensors to allow for multiple sensors on different addresses. A value of 0 disables the sensor.

- Range: 0 127

- Increment: 1

## RNGFND4_POS_X:  X position offset

*Note: This parameter is for advanced users*

X position of the first rangefinder in body frame. Positive X is forward of the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFND4_POS_Y: Y position offset

*Note: This parameter is for advanced users*

Y position of the first rangefinder in body frame. Positive Y is to the right of the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFND4_POS_Z: Z position offset

*Note: This parameter is for advanced users*

Z position of the first rangefinder in body frame. Positive Z is down from the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFND4_ORIENT: Rangefinder orientation

*Note: This parameter is for advanced users*

Orientation of rangefinder

|Value|Meaning|
|:---:|:---:|
|0|Forward|
| 1|Forward-Right|
| 2|Right|
| 3|Back-Right|
| 4|Back|
| 5|Back-Left|
| 6|Left|
| 7|Forward-Left|
| 24|Up|
| 25|Down|

# RNGFND4 Parameters

## RNGFND4_WSP_MAVG: Moving Average Range

*Note: This parameter is for advanced users*

Sets the number of historic range results to use for calculating the current range result. When MAVG is greater than 1, the current range result will be the current measured value averaged with the N-1 previous results

- Range: 0 255

## RNGFND4_WSP_MEDF: Moving Median Filter

*Note: This parameter is for advanced users*

Sets the window size for the real-time median filter. When MEDF is greater than 0 the median filter is active

- Range: 0 255

## RNGFND4_WSP_FRQ: Frequency

*Note: This parameter is for advanced users*

Sets the repetition frequency of the ranging operation in Hertz. Upon entering the desired frequency the system will calculate the nearest frequency that it can handle according to the resolution of internal timers.

- Range: 0 10000

## RNGFND4_WSP_AVG: Multi-pulse averages

*Note: This parameter is for advanced users*

Sets the number of pulses to be used in multi-pulse averaging mode. In this mode, a sequence of rapid fire ranges are taken and then averaged to improve the accuracy of the measurement

- Range: 0 255

## RNGFND4_WSP_THR: Sensitivity threshold

*Note: This parameter is for advanced users*

Sets the system sensitivity. Larger values of THR represent higher sensitivity. The system may limit the maximum value of THR to prevent excessive false alarm rates based on settings made at the factory. Set to -1 for automatic threshold adjustments

- Range: -1 255

## RNGFND4_WSP_BAUD: Baud rate

*Note: This parameter is for advanced users*

Desired baud rate

|Value|Meaning|
|:---:|:---:|
|0|Low Speed|
|1|High Speed|

# RNGFND5 Parameters

## RNGFND5_TYPE: Rangefinder type

What type of rangefinder device that is connected

|Value|Meaning|
|:---:|:---:|
|0|None|
|1|Analog|
|2|MaxbotixI2C|
|3|LidarLiteV2-I2C|
|5|PWM|
|6|BBB-PRU|
|7|LightWareI2C|
|8|LightWareSerial|
|9|Bebop|
|10|MAVLink|
|11|uLanding|
|12|LeddarOne|
|13|MaxbotixSerial|
|14|TeraRangerI2C|
|15|LidarLiteV3-I2C|
|16|VL53L0X|
|17|NMEA|
|18|WASP-LRF|
|19|BenewakeTF02|
|20|BenewakeTFmini|
|21|LidarLightV3HP|
|22|PWM|
|23|BlueRoboticsPing|
|24|UAVCAN|
|25|BenewakeTFMiniPlus|

## RNGFND5_PIN: Rangefinder pin

Analog pin that rangefinder is connected to. Set to 11 on PX4 for the analog 'airspeed' port. Set to 15 on the Pixhawk for the analog 'airspeed' port.

|Value|Meaning|
|:---:|:---:|
|-1|Not Used|
| 11|PX4-airspeed port|
| 15|Pixhawk-airspeed port|

## RNGFND5_SCALING: Rangefinder scaling

Scaling factor between rangefinder reading and distance. For the linear and inverted functions this is in meters per volt. For the hyperbolic function the units are meterVolts.

- Units: m/V

- Increment: 0.001

## RNGFND5_OFFSET: rangefinder offset

Offset in volts for zero distance for analog rangefinders. Offset added to distance in centimeters for PWM and I2C Lidars

- Units: V

- Increment: 0.001

## RNGFND5_FUNCTION: Rangefinder function

Control over what function is used to calculate distance. For a linear function, the distance is (voltage-offset)*scaling. For a inverted function the distance is (offset-voltage)*scaling. For a hyperbolic function the distance is scaling/(voltage-offset). The functions return the distance in meters.

|Value|Meaning|
|:---:|:---:|
|0|Linear|
|1|Inverted|
|2|Hyperbolic|

## RNGFND5_MIN_CM: Rangefinder minimum distance

Minimum distance in centimeters that rangefinder can reliably read

- Units: cm

- Increment: 1

## RNGFND5_MAX_CM: Rangefinder maximum distance

Maximum distance in centimeters that rangefinder can reliably read

- Units: cm

- Increment: 1

## RNGFND5_STOP_PIN: Rangefinder stop pin

Digital pin that enables/disables rangefinder measurement for the pwm rangefinder. A value of -1 means no pin. If this is set, then the pin is set to 1 to enable the rangefinder and set to 0 to disable it. This is used to enable powersaving when out of range.

|Value|Meaning|
|:---:|:---:|
|-1|Not Used|
|50|Pixhawk AUXOUT1|
|51|Pixhawk AUXOUT2|
|52|Pixhawk AUXOUT3|
|53|Pixhawk AUXOUT4|
|54|Pixhawk AUXOUT5|
|55|Pixhawk AUXOUT6|
|111|PX4 FMU Relay1|
|112|PX4 FMU Relay2|
|113|PX4IO Relay1|
|114|PX4IO Relay2|
|115|PX4IO ACC1|
|116|PX4IO ACC2|

## RNGFND5_RMETRIC: Ratiometric

This parameter sets whether an analog rangefinder is ratiometric. Most analog rangefinders are ratiometric, meaning that their output voltage is influenced by the supply voltage. Some analog rangefinders (such as the SF/02) have their own internal voltage regulators so they are not ratiometric.

|Value|Meaning|
|:---:|:---:|
|0|No|
|1|Yes|

## RNGFND5_PWRRNG: Powersave range

This parameter sets the estimated terrain distance in meters above which the sensor will be put into a power saving mode (if available). A value of zero means power saving is not enabled

- Units: m

- Range: 0 32767

## RNGFND5_GNDCLEAR: Distance (in cm) from the range finder to the ground

This parameter sets the expected range measurement(in cm) that the range finder should return when the vehicle is on the ground.

- Units: cm

- Range: 5 127

- Increment: 1

## RNGFND5_ADDR: Bus address of sensor

This sets the bus address of the sensor, where applicable. Used for the I2C and UAVCAN sensors to allow for multiple sensors on different addresses. A value of 0 disables the sensor.

- Range: 0 127

- Increment: 1

## RNGFND5_POS_X:  X position offset

*Note: This parameter is for advanced users*

X position of the first rangefinder in body frame. Positive X is forward of the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFND5_POS_Y: Y position offset

*Note: This parameter is for advanced users*

Y position of the first rangefinder in body frame. Positive Y is to the right of the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFND5_POS_Z: Z position offset

*Note: This parameter is for advanced users*

Z position of the first rangefinder in body frame. Positive Z is down from the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFND5_ORIENT: Rangefinder orientation

*Note: This parameter is for advanced users*

Orientation of rangefinder

|Value|Meaning|
|:---:|:---:|
|0|Forward|
| 1|Forward-Right|
| 2|Right|
| 3|Back-Right|
| 4|Back|
| 5|Back-Left|
| 6|Left|
| 7|Forward-Left|
| 24|Up|
| 25|Down|

# RNGFND5 Parameters

## RNGFND5_WSP_MAVG: Moving Average Range

*Note: This parameter is for advanced users*

Sets the number of historic range results to use for calculating the current range result. When MAVG is greater than 1, the current range result will be the current measured value averaged with the N-1 previous results

- Range: 0 255

## RNGFND5_WSP_MEDF: Moving Median Filter

*Note: This parameter is for advanced users*

Sets the window size for the real-time median filter. When MEDF is greater than 0 the median filter is active

- Range: 0 255

## RNGFND5_WSP_FRQ: Frequency

*Note: This parameter is for advanced users*

Sets the repetition frequency of the ranging operation in Hertz. Upon entering the desired frequency the system will calculate the nearest frequency that it can handle according to the resolution of internal timers.

- Range: 0 10000

## RNGFND5_WSP_AVG: Multi-pulse averages

*Note: This parameter is for advanced users*

Sets the number of pulses to be used in multi-pulse averaging mode. In this mode, a sequence of rapid fire ranges are taken and then averaged to improve the accuracy of the measurement

- Range: 0 255

## RNGFND5_WSP_THR: Sensitivity threshold

*Note: This parameter is for advanced users*

Sets the system sensitivity. Larger values of THR represent higher sensitivity. The system may limit the maximum value of THR to prevent excessive false alarm rates based on settings made at the factory. Set to -1 for automatic threshold adjustments

- Range: -1 255

## RNGFND5_WSP_BAUD: Baud rate

*Note: This parameter is for advanced users*

Desired baud rate

|Value|Meaning|
|:---:|:---:|
|0|Low Speed|
|1|High Speed|

# RNGFND6 Parameters

## RNGFND6_TYPE: Rangefinder type

What type of rangefinder device that is connected

|Value|Meaning|
|:---:|:---:|
|0|None|
|1|Analog|
|2|MaxbotixI2C|
|3|LidarLiteV2-I2C|
|5|PWM|
|6|BBB-PRU|
|7|LightWareI2C|
|8|LightWareSerial|
|9|Bebop|
|10|MAVLink|
|11|uLanding|
|12|LeddarOne|
|13|MaxbotixSerial|
|14|TeraRangerI2C|
|15|LidarLiteV3-I2C|
|16|VL53L0X|
|17|NMEA|
|18|WASP-LRF|
|19|BenewakeTF02|
|20|BenewakeTFmini|
|21|LidarLightV3HP|
|22|PWM|
|23|BlueRoboticsPing|
|24|UAVCAN|
|25|BenewakeTFMiniPlus|

## RNGFND6_PIN: Rangefinder pin

Analog pin that rangefinder is connected to. Set to 11 on PX4 for the analog 'airspeed' port. Set to 15 on the Pixhawk for the analog 'airspeed' port.

|Value|Meaning|
|:---:|:---:|
|-1|Not Used|
| 11|PX4-airspeed port|
| 15|Pixhawk-airspeed port|

## RNGFND6_SCALING: Rangefinder scaling

Scaling factor between rangefinder reading and distance. For the linear and inverted functions this is in meters per volt. For the hyperbolic function the units are meterVolts.

- Units: m/V

- Increment: 0.001

## RNGFND6_OFFSET: rangefinder offset

Offset in volts for zero distance for analog rangefinders. Offset added to distance in centimeters for PWM and I2C Lidars

- Units: V

- Increment: 0.001

## RNGFND6_FUNCTION: Rangefinder function

Control over what function is used to calculate distance. For a linear function, the distance is (voltage-offset)*scaling. For a inverted function the distance is (offset-voltage)*scaling. For a hyperbolic function the distance is scaling/(voltage-offset). The functions return the distance in meters.

|Value|Meaning|
|:---:|:---:|
|0|Linear|
|1|Inverted|
|2|Hyperbolic|

## RNGFND6_MIN_CM: Rangefinder minimum distance

Minimum distance in centimeters that rangefinder can reliably read

- Units: cm

- Increment: 1

## RNGFND6_MAX_CM: Rangefinder maximum distance

Maximum distance in centimeters that rangefinder can reliably read

- Units: cm

- Increment: 1

## RNGFND6_STOP_PIN: Rangefinder stop pin

Digital pin that enables/disables rangefinder measurement for the pwm rangefinder. A value of -1 means no pin. If this is set, then the pin is set to 1 to enable the rangefinder and set to 0 to disable it. This is used to enable powersaving when out of range.

|Value|Meaning|
|:---:|:---:|
|-1|Not Used|
|50|Pixhawk AUXOUT1|
|51|Pixhawk AUXOUT2|
|52|Pixhawk AUXOUT3|
|53|Pixhawk AUXOUT4|
|54|Pixhawk AUXOUT5|
|55|Pixhawk AUXOUT6|
|111|PX4 FMU Relay1|
|112|PX4 FMU Relay2|
|113|PX4IO Relay1|
|114|PX4IO Relay2|
|115|PX4IO ACC1|
|116|PX4IO ACC2|

## RNGFND6_RMETRIC: Ratiometric

This parameter sets whether an analog rangefinder is ratiometric. Most analog rangefinders are ratiometric, meaning that their output voltage is influenced by the supply voltage. Some analog rangefinders (such as the SF/02) have their own internal voltage regulators so they are not ratiometric.

|Value|Meaning|
|:---:|:---:|
|0|No|
|1|Yes|

## RNGFND6_PWRRNG: Powersave range

This parameter sets the estimated terrain distance in meters above which the sensor will be put into a power saving mode (if available). A value of zero means power saving is not enabled

- Units: m

- Range: 0 32767

## RNGFND6_GNDCLEAR: Distance (in cm) from the range finder to the ground

This parameter sets the expected range measurement(in cm) that the range finder should return when the vehicle is on the ground.

- Units: cm

- Range: 5 127

- Increment: 1

## RNGFND6_ADDR: Bus address of sensor

This sets the bus address of the sensor, where applicable. Used for the I2C and UAVCAN sensors to allow for multiple sensors on different addresses. A value of 0 disables the sensor.

- Range: 0 127

- Increment: 1

## RNGFND6_POS_X:  X position offset

*Note: This parameter is for advanced users*

X position of the first rangefinder in body frame. Positive X is forward of the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFND6_POS_Y: Y position offset

*Note: This parameter is for advanced users*

Y position of the first rangefinder in body frame. Positive Y is to the right of the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFND6_POS_Z: Z position offset

*Note: This parameter is for advanced users*

Z position of the first rangefinder in body frame. Positive Z is down from the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFND6_ORIENT: Rangefinder orientation

*Note: This parameter is for advanced users*

Orientation of rangefinder

|Value|Meaning|
|:---:|:---:|
|0|Forward|
| 1|Forward-Right|
| 2|Right|
| 3|Back-Right|
| 4|Back|
| 5|Back-Left|
| 6|Left|
| 7|Forward-Left|
| 24|Up|
| 25|Down|

# RNGFND6 Parameters

## RNGFND6_WSP_MAVG: Moving Average Range

*Note: This parameter is for advanced users*

Sets the number of historic range results to use for calculating the current range result. When MAVG is greater than 1, the current range result will be the current measured value averaged with the N-1 previous results

- Range: 0 255

## RNGFND6_WSP_MEDF: Moving Median Filter

*Note: This parameter is for advanced users*

Sets the window size for the real-time median filter. When MEDF is greater than 0 the median filter is active

- Range: 0 255

## RNGFND6_WSP_FRQ: Frequency

*Note: This parameter is for advanced users*

Sets the repetition frequency of the ranging operation in Hertz. Upon entering the desired frequency the system will calculate the nearest frequency that it can handle according to the resolution of internal timers.

- Range: 0 10000

## RNGFND6_WSP_AVG: Multi-pulse averages

*Note: This parameter is for advanced users*

Sets the number of pulses to be used in multi-pulse averaging mode. In this mode, a sequence of rapid fire ranges are taken and then averaged to improve the accuracy of the measurement

- Range: 0 255

## RNGFND6_WSP_THR: Sensitivity threshold

*Note: This parameter is for advanced users*

Sets the system sensitivity. Larger values of THR represent higher sensitivity. The system may limit the maximum value of THR to prevent excessive false alarm rates based on settings made at the factory. Set to -1 for automatic threshold adjustments

- Range: -1 255

## RNGFND6_WSP_BAUD: Baud rate

*Note: This parameter is for advanced users*

Desired baud rate

|Value|Meaning|
|:---:|:---:|
|0|Low Speed|
|1|High Speed|

# RNGFND7 Parameters

## RNGFND7_TYPE: Rangefinder type

What type of rangefinder device that is connected

|Value|Meaning|
|:---:|:---:|
|0|None|
|1|Analog|
|2|MaxbotixI2C|
|3|LidarLiteV2-I2C|
|5|PWM|
|6|BBB-PRU|
|7|LightWareI2C|
|8|LightWareSerial|
|9|Bebop|
|10|MAVLink|
|11|uLanding|
|12|LeddarOne|
|13|MaxbotixSerial|
|14|TeraRangerI2C|
|15|LidarLiteV3-I2C|
|16|VL53L0X|
|17|NMEA|
|18|WASP-LRF|
|19|BenewakeTF02|
|20|BenewakeTFmini|
|21|LidarLightV3HP|
|22|PWM|
|23|BlueRoboticsPing|
|24|UAVCAN|
|25|BenewakeTFMiniPlus|

## RNGFND7_PIN: Rangefinder pin

Analog pin that rangefinder is connected to. Set to 11 on PX4 for the analog 'airspeed' port. Set to 15 on the Pixhawk for the analog 'airspeed' port.

|Value|Meaning|
|:---:|:---:|
|-1|Not Used|
| 11|PX4-airspeed port|
| 15|Pixhawk-airspeed port|

## RNGFND7_SCALING: Rangefinder scaling

Scaling factor between rangefinder reading and distance. For the linear and inverted functions this is in meters per volt. For the hyperbolic function the units are meterVolts.

- Units: m/V

- Increment: 0.001

## RNGFND7_OFFSET: rangefinder offset

Offset in volts for zero distance for analog rangefinders. Offset added to distance in centimeters for PWM and I2C Lidars

- Units: V

- Increment: 0.001

## RNGFND7_FUNCTION: Rangefinder function

Control over what function is used to calculate distance. For a linear function, the distance is (voltage-offset)*scaling. For a inverted function the distance is (offset-voltage)*scaling. For a hyperbolic function the distance is scaling/(voltage-offset). The functions return the distance in meters.

|Value|Meaning|
|:---:|:---:|
|0|Linear|
|1|Inverted|
|2|Hyperbolic|

## RNGFND7_MIN_CM: Rangefinder minimum distance

Minimum distance in centimeters that rangefinder can reliably read

- Units: cm

- Increment: 1

## RNGFND7_MAX_CM: Rangefinder maximum distance

Maximum distance in centimeters that rangefinder can reliably read

- Units: cm

- Increment: 1

## RNGFND7_STOP_PIN: Rangefinder stop pin

Digital pin that enables/disables rangefinder measurement for the pwm rangefinder. A value of -1 means no pin. If this is set, then the pin is set to 1 to enable the rangefinder and set to 0 to disable it. This is used to enable powersaving when out of range.

|Value|Meaning|
|:---:|:---:|
|-1|Not Used|
|50|Pixhawk AUXOUT1|
|51|Pixhawk AUXOUT2|
|52|Pixhawk AUXOUT3|
|53|Pixhawk AUXOUT4|
|54|Pixhawk AUXOUT5|
|55|Pixhawk AUXOUT6|
|111|PX4 FMU Relay1|
|112|PX4 FMU Relay2|
|113|PX4IO Relay1|
|114|PX4IO Relay2|
|115|PX4IO ACC1|
|116|PX4IO ACC2|

## RNGFND7_RMETRIC: Ratiometric

This parameter sets whether an analog rangefinder is ratiometric. Most analog rangefinders are ratiometric, meaning that their output voltage is influenced by the supply voltage. Some analog rangefinders (such as the SF/02) have their own internal voltage regulators so they are not ratiometric.

|Value|Meaning|
|:---:|:---:|
|0|No|
|1|Yes|

## RNGFND7_PWRRNG: Powersave range

This parameter sets the estimated terrain distance in meters above which the sensor will be put into a power saving mode (if available). A value of zero means power saving is not enabled

- Units: m

- Range: 0 32767

## RNGFND7_GNDCLEAR: Distance (in cm) from the range finder to the ground

This parameter sets the expected range measurement(in cm) that the range finder should return when the vehicle is on the ground.

- Units: cm

- Range: 5 127

- Increment: 1

## RNGFND7_ADDR: Bus address of sensor

This sets the bus address of the sensor, where applicable. Used for the I2C and UAVCAN sensors to allow for multiple sensors on different addresses. A value of 0 disables the sensor.

- Range: 0 127

- Increment: 1

## RNGFND7_POS_X:  X position offset

*Note: This parameter is for advanced users*

X position of the first rangefinder in body frame. Positive X is forward of the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFND7_POS_Y: Y position offset

*Note: This parameter is for advanced users*

Y position of the first rangefinder in body frame. Positive Y is to the right of the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFND7_POS_Z: Z position offset

*Note: This parameter is for advanced users*

Z position of the first rangefinder in body frame. Positive Z is down from the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFND7_ORIENT: Rangefinder orientation

*Note: This parameter is for advanced users*

Orientation of rangefinder

|Value|Meaning|
|:---:|:---:|
|0|Forward|
| 1|Forward-Right|
| 2|Right|
| 3|Back-Right|
| 4|Back|
| 5|Back-Left|
| 6|Left|
| 7|Forward-Left|
| 24|Up|
| 25|Down|

# RNGFND7 Parameters

## RNGFND7_WSP_MAVG: Moving Average Range

*Note: This parameter is for advanced users*

Sets the number of historic range results to use for calculating the current range result. When MAVG is greater than 1, the current range result will be the current measured value averaged with the N-1 previous results

- Range: 0 255

## RNGFND7_WSP_MEDF: Moving Median Filter

*Note: This parameter is for advanced users*

Sets the window size for the real-time median filter. When MEDF is greater than 0 the median filter is active

- Range: 0 255

## RNGFND7_WSP_FRQ: Frequency

*Note: This parameter is for advanced users*

Sets the repetition frequency of the ranging operation in Hertz. Upon entering the desired frequency the system will calculate the nearest frequency that it can handle according to the resolution of internal timers.

- Range: 0 10000

## RNGFND7_WSP_AVG: Multi-pulse averages

*Note: This parameter is for advanced users*

Sets the number of pulses to be used in multi-pulse averaging mode. In this mode, a sequence of rapid fire ranges are taken and then averaged to improve the accuracy of the measurement

- Range: 0 255

## RNGFND7_WSP_THR: Sensitivity threshold

*Note: This parameter is for advanced users*

Sets the system sensitivity. Larger values of THR represent higher sensitivity. The system may limit the maximum value of THR to prevent excessive false alarm rates based on settings made at the factory. Set to -1 for automatic threshold adjustments

- Range: -1 255

## RNGFND7_WSP_BAUD: Baud rate

*Note: This parameter is for advanced users*

Desired baud rate

|Value|Meaning|
|:---:|:---:|
|0|Low Speed|
|1|High Speed|

# RNGFND8 Parameters

## RNGFND8_TYPE: Rangefinder type

What type of rangefinder device that is connected

|Value|Meaning|
|:---:|:---:|
|0|None|
|1|Analog|
|2|MaxbotixI2C|
|3|LidarLiteV2-I2C|
|5|PWM|
|6|BBB-PRU|
|7|LightWareI2C|
|8|LightWareSerial|
|9|Bebop|
|10|MAVLink|
|11|uLanding|
|12|LeddarOne|
|13|MaxbotixSerial|
|14|TeraRangerI2C|
|15|LidarLiteV3-I2C|
|16|VL53L0X|
|17|NMEA|
|18|WASP-LRF|
|19|BenewakeTF02|
|20|BenewakeTFmini|
|21|LidarLightV3HP|
|22|PWM|
|23|BlueRoboticsPing|
|24|UAVCAN|
|25|BenewakeTFMiniPlus|

## RNGFND8_PIN: Rangefinder pin

Analog pin that rangefinder is connected to. Set to 11 on PX4 for the analog 'airspeed' port. Set to 15 on the Pixhawk for the analog 'airspeed' port.

|Value|Meaning|
|:---:|:---:|
|-1|Not Used|
| 11|PX4-airspeed port|
| 15|Pixhawk-airspeed port|

## RNGFND8_SCALING: Rangefinder scaling

Scaling factor between rangefinder reading and distance. For the linear and inverted functions this is in meters per volt. For the hyperbolic function the units are meterVolts.

- Units: m/V

- Increment: 0.001

## RNGFND8_OFFSET: rangefinder offset

Offset in volts for zero distance for analog rangefinders. Offset added to distance in centimeters for PWM and I2C Lidars

- Units: V

- Increment: 0.001

## RNGFND8_FUNCTION: Rangefinder function

Control over what function is used to calculate distance. For a linear function, the distance is (voltage-offset)*scaling. For a inverted function the distance is (offset-voltage)*scaling. For a hyperbolic function the distance is scaling/(voltage-offset). The functions return the distance in meters.

|Value|Meaning|
|:---:|:---:|
|0|Linear|
|1|Inverted|
|2|Hyperbolic|

## RNGFND8_MIN_CM: Rangefinder minimum distance

Minimum distance in centimeters that rangefinder can reliably read

- Units: cm

- Increment: 1

## RNGFND8_MAX_CM: Rangefinder maximum distance

Maximum distance in centimeters that rangefinder can reliably read

- Units: cm

- Increment: 1

## RNGFND8_STOP_PIN: Rangefinder stop pin

Digital pin that enables/disables rangefinder measurement for the pwm rangefinder. A value of -1 means no pin. If this is set, then the pin is set to 1 to enable the rangefinder and set to 0 to disable it. This is used to enable powersaving when out of range.

|Value|Meaning|
|:---:|:---:|
|-1|Not Used|
|50|Pixhawk AUXOUT1|
|51|Pixhawk AUXOUT2|
|52|Pixhawk AUXOUT3|
|53|Pixhawk AUXOUT4|
|54|Pixhawk AUXOUT5|
|55|Pixhawk AUXOUT6|
|111|PX4 FMU Relay1|
|112|PX4 FMU Relay2|
|113|PX4IO Relay1|
|114|PX4IO Relay2|
|115|PX4IO ACC1|
|116|PX4IO ACC2|

## RNGFND8_RMETRIC: Ratiometric

This parameter sets whether an analog rangefinder is ratiometric. Most analog rangefinders are ratiometric, meaning that their output voltage is influenced by the supply voltage. Some analog rangefinders (such as the SF/02) have their own internal voltage regulators so they are not ratiometric.

|Value|Meaning|
|:---:|:---:|
|0|No|
|1|Yes|

## RNGFND8_PWRRNG: Powersave range

This parameter sets the estimated terrain distance in meters above which the sensor will be put into a power saving mode (if available). A value of zero means power saving is not enabled

- Units: m

- Range: 0 32767

## RNGFND8_GNDCLEAR: Distance (in cm) from the range finder to the ground

This parameter sets the expected range measurement(in cm) that the range finder should return when the vehicle is on the ground.

- Units: cm

- Range: 5 127

- Increment: 1

## RNGFND8_ADDR: Bus address of sensor

This sets the bus address of the sensor, where applicable. Used for the I2C and UAVCAN sensors to allow for multiple sensors on different addresses. A value of 0 disables the sensor.

- Range: 0 127

- Increment: 1

## RNGFND8_POS_X:  X position offset

*Note: This parameter is for advanced users*

X position of the first rangefinder in body frame. Positive X is forward of the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFND8_POS_Y: Y position offset

*Note: This parameter is for advanced users*

Y position of the first rangefinder in body frame. Positive Y is to the right of the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFND8_POS_Z: Z position offset

*Note: This parameter is for advanced users*

Z position of the first rangefinder in body frame. Positive Z is down from the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFND8_ORIENT: Rangefinder orientation

*Note: This parameter is for advanced users*

Orientation of rangefinder

|Value|Meaning|
|:---:|:---:|
|0|Forward|
| 1|Forward-Right|
| 2|Right|
| 3|Back-Right|
| 4|Back|
| 5|Back-Left|
| 6|Left|
| 7|Forward-Left|
| 24|Up|
| 25|Down|

# RNGFND8 Parameters

## RNGFND8_WSP_MAVG: Moving Average Range

*Note: This parameter is for advanced users*

Sets the number of historic range results to use for calculating the current range result. When MAVG is greater than 1, the current range result will be the current measured value averaged with the N-1 previous results

- Range: 0 255

## RNGFND8_WSP_MEDF: Moving Median Filter

*Note: This parameter is for advanced users*

Sets the window size for the real-time median filter. When MEDF is greater than 0 the median filter is active

- Range: 0 255

## RNGFND8_WSP_FRQ: Frequency

*Note: This parameter is for advanced users*

Sets the repetition frequency of the ranging operation in Hertz. Upon entering the desired frequency the system will calculate the nearest frequency that it can handle according to the resolution of internal timers.

- Range: 0 10000

## RNGFND8_WSP_AVG: Multi-pulse averages

*Note: This parameter is for advanced users*

Sets the number of pulses to be used in multi-pulse averaging mode. In this mode, a sequence of rapid fire ranges are taken and then averaged to improve the accuracy of the measurement

- Range: 0 255

## RNGFND8_WSP_THR: Sensitivity threshold

*Note: This parameter is for advanced users*

Sets the system sensitivity. Larger values of THR represent higher sensitivity. The system may limit the maximum value of THR to prevent excessive false alarm rates based on settings made at the factory. Set to -1 for automatic threshold adjustments

- Range: -1 255

## RNGFND8_WSP_BAUD: Baud rate

*Note: This parameter is for advanced users*

Desired baud rate

|Value|Meaning|
|:---:|:---:|
|0|Low Speed|
|1|High Speed|

# RNGFND9 Parameters

## RNGFND9_TYPE: Rangefinder type

What type of rangefinder device that is connected

|Value|Meaning|
|:---:|:---:|
|0|None|
|1|Analog|
|2|MaxbotixI2C|
|3|LidarLiteV2-I2C|
|5|PWM|
|6|BBB-PRU|
|7|LightWareI2C|
|8|LightWareSerial|
|9|Bebop|
|10|MAVLink|
|11|uLanding|
|12|LeddarOne|
|13|MaxbotixSerial|
|14|TeraRangerI2C|
|15|LidarLiteV3-I2C|
|16|VL53L0X|
|17|NMEA|
|18|WASP-LRF|
|19|BenewakeTF02|
|20|BenewakeTFmini|
|21|LidarLightV3HP|
|22|PWM|
|23|BlueRoboticsPing|
|24|UAVCAN|
|25|BenewakeTFMiniPlus|

## RNGFND9_PIN: Rangefinder pin

Analog pin that rangefinder is connected to. Set to 11 on PX4 for the analog 'airspeed' port. Set to 15 on the Pixhawk for the analog 'airspeed' port.

|Value|Meaning|
|:---:|:---:|
|-1|Not Used|
| 11|PX4-airspeed port|
| 15|Pixhawk-airspeed port|

## RNGFND9_SCALING: Rangefinder scaling

Scaling factor between rangefinder reading and distance. For the linear and inverted functions this is in meters per volt. For the hyperbolic function the units are meterVolts.

- Units: m/V

- Increment: 0.001

## RNGFND9_OFFSET: rangefinder offset

Offset in volts for zero distance for analog rangefinders. Offset added to distance in centimeters for PWM and I2C Lidars

- Units: V

- Increment: 0.001

## RNGFND9_FUNCTION: Rangefinder function

Control over what function is used to calculate distance. For a linear function, the distance is (voltage-offset)*scaling. For a inverted function the distance is (offset-voltage)*scaling. For a hyperbolic function the distance is scaling/(voltage-offset). The functions return the distance in meters.

|Value|Meaning|
|:---:|:---:|
|0|Linear|
|1|Inverted|
|2|Hyperbolic|

## RNGFND9_MIN_CM: Rangefinder minimum distance

Minimum distance in centimeters that rangefinder can reliably read

- Units: cm

- Increment: 1

## RNGFND9_MAX_CM: Rangefinder maximum distance

Maximum distance in centimeters that rangefinder can reliably read

- Units: cm

- Increment: 1

## RNGFND9_STOP_PIN: Rangefinder stop pin

Digital pin that enables/disables rangefinder measurement for the pwm rangefinder. A value of -1 means no pin. If this is set, then the pin is set to 1 to enable the rangefinder and set to 0 to disable it. This is used to enable powersaving when out of range.

|Value|Meaning|
|:---:|:---:|
|-1|Not Used|
|50|Pixhawk AUXOUT1|
|51|Pixhawk AUXOUT2|
|52|Pixhawk AUXOUT3|
|53|Pixhawk AUXOUT4|
|54|Pixhawk AUXOUT5|
|55|Pixhawk AUXOUT6|
|111|PX4 FMU Relay1|
|112|PX4 FMU Relay2|
|113|PX4IO Relay1|
|114|PX4IO Relay2|
|115|PX4IO ACC1|
|116|PX4IO ACC2|

## RNGFND9_RMETRIC: Ratiometric

This parameter sets whether an analog rangefinder is ratiometric. Most analog rangefinders are ratiometric, meaning that their output voltage is influenced by the supply voltage. Some analog rangefinders (such as the SF/02) have their own internal voltage regulators so they are not ratiometric.

|Value|Meaning|
|:---:|:---:|
|0|No|
|1|Yes|

## RNGFND9_PWRRNG: Powersave range

This parameter sets the estimated terrain distance in meters above which the sensor will be put into a power saving mode (if available). A value of zero means power saving is not enabled

- Units: m

- Range: 0 32767

## RNGFND9_GNDCLEAR: Distance (in cm) from the range finder to the ground

This parameter sets the expected range measurement(in cm) that the range finder should return when the vehicle is on the ground.

- Units: cm

- Range: 5 127

- Increment: 1

## RNGFND9_ADDR: Bus address of sensor

This sets the bus address of the sensor, where applicable. Used for the I2C and UAVCAN sensors to allow for multiple sensors on different addresses. A value of 0 disables the sensor.

- Range: 0 127

- Increment: 1

## RNGFND9_POS_X:  X position offset

*Note: This parameter is for advanced users*

X position of the first rangefinder in body frame. Positive X is forward of the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFND9_POS_Y: Y position offset

*Note: This parameter is for advanced users*

Y position of the first rangefinder in body frame. Positive Y is to the right of the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFND9_POS_Z: Z position offset

*Note: This parameter is for advanced users*

Z position of the first rangefinder in body frame. Positive Z is down from the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFND9_ORIENT: Rangefinder orientation

*Note: This parameter is for advanced users*

Orientation of rangefinder

|Value|Meaning|
|:---:|:---:|
|0|Forward|
| 1|Forward-Right|
| 2|Right|
| 3|Back-Right|
| 4|Back|
| 5|Back-Left|
| 6|Left|
| 7|Forward-Left|
| 24|Up|
| 25|Down|

# RNGFND9 Parameters

## RNGFND9_WSP_MAVG: Moving Average Range

*Note: This parameter is for advanced users*

Sets the number of historic range results to use for calculating the current range result. When MAVG is greater than 1, the current range result will be the current measured value averaged with the N-1 previous results

- Range: 0 255

## RNGFND9_WSP_MEDF: Moving Median Filter

*Note: This parameter is for advanced users*

Sets the window size for the real-time median filter. When MEDF is greater than 0 the median filter is active

- Range: 0 255

## RNGFND9_WSP_FRQ: Frequency

*Note: This parameter is for advanced users*

Sets the repetition frequency of the ranging operation in Hertz. Upon entering the desired frequency the system will calculate the nearest frequency that it can handle according to the resolution of internal timers.

- Range: 0 10000

## RNGFND9_WSP_AVG: Multi-pulse averages

*Note: This parameter is for advanced users*

Sets the number of pulses to be used in multi-pulse averaging mode. In this mode, a sequence of rapid fire ranges are taken and then averaged to improve the accuracy of the measurement

- Range: 0 255

## RNGFND9_WSP_THR: Sensitivity threshold

*Note: This parameter is for advanced users*

Sets the system sensitivity. Larger values of THR represent higher sensitivity. The system may limit the maximum value of THR to prevent excessive false alarm rates based on settings made at the factory. Set to -1 for automatic threshold adjustments

- Range: -1 255

## RNGFND9_WSP_BAUD: Baud rate

*Note: This parameter is for advanced users*

Desired baud rate

|Value|Meaning|
|:---:|:---:|
|0|Low Speed|
|1|High Speed|

# RNGFNDA Parameters

## RNGFNDA_TYPE: Rangefinder type

What type of rangefinder device that is connected

|Value|Meaning|
|:---:|:---:|
|0|None|
|1|Analog|
|2|MaxbotixI2C|
|3|LidarLiteV2-I2C|
|5|PWM|
|6|BBB-PRU|
|7|LightWareI2C|
|8|LightWareSerial|
|9|Bebop|
|10|MAVLink|
|11|uLanding|
|12|LeddarOne|
|13|MaxbotixSerial|
|14|TeraRangerI2C|
|15|LidarLiteV3-I2C|
|16|VL53L0X|
|17|NMEA|
|18|WASP-LRF|
|19|BenewakeTF02|
|20|BenewakeTFmini|
|21|LidarLightV3HP|
|22|PWM|
|23|BlueRoboticsPing|
|24|UAVCAN|
|25|BenewakeTFMiniPlus|

## RNGFNDA_PIN: Rangefinder pin

Analog pin that rangefinder is connected to. Set to 11 on PX4 for the analog 'airspeed' port. Set to 15 on the Pixhawk for the analog 'airspeed' port.

|Value|Meaning|
|:---:|:---:|
|-1|Not Used|
| 11|PX4-airspeed port|
| 15|Pixhawk-airspeed port|

## RNGFNDA_SCALING: Rangefinder scaling

Scaling factor between rangefinder reading and distance. For the linear and inverted functions this is in meters per volt. For the hyperbolic function the units are meterVolts.

- Units: m/V

- Increment: 0.001

## RNGFNDA_OFFSET: rangefinder offset

Offset in volts for zero distance for analog rangefinders. Offset added to distance in centimeters for PWM and I2C Lidars

- Units: V

- Increment: 0.001

## RNGFNDA_FUNCTION: Rangefinder function

Control over what function is used to calculate distance. For a linear function, the distance is (voltage-offset)*scaling. For a inverted function the distance is (offset-voltage)*scaling. For a hyperbolic function the distance is scaling/(voltage-offset). The functions return the distance in meters.

|Value|Meaning|
|:---:|:---:|
|0|Linear|
|1|Inverted|
|2|Hyperbolic|

## RNGFNDA_MIN_CM: Rangefinder minimum distance

Minimum distance in centimeters that rangefinder can reliably read

- Units: cm

- Increment: 1

## RNGFNDA_MAX_CM: Rangefinder maximum distance

Maximum distance in centimeters that rangefinder can reliably read

- Units: cm

- Increment: 1

## RNGFNDA_STOP_PIN: Rangefinder stop pin

Digital pin that enables/disables rangefinder measurement for the pwm rangefinder. A value of -1 means no pin. If this is set, then the pin is set to 1 to enable the rangefinder and set to 0 to disable it. This is used to enable powersaving when out of range.

|Value|Meaning|
|:---:|:---:|
|-1|Not Used|
|50|Pixhawk AUXOUT1|
|51|Pixhawk AUXOUT2|
|52|Pixhawk AUXOUT3|
|53|Pixhawk AUXOUT4|
|54|Pixhawk AUXOUT5|
|55|Pixhawk AUXOUT6|
|111|PX4 FMU Relay1|
|112|PX4 FMU Relay2|
|113|PX4IO Relay1|
|114|PX4IO Relay2|
|115|PX4IO ACC1|
|116|PX4IO ACC2|

## RNGFNDA_RMETRIC: Ratiometric

This parameter sets whether an analog rangefinder is ratiometric. Most analog rangefinders are ratiometric, meaning that their output voltage is influenced by the supply voltage. Some analog rangefinders (such as the SF/02) have their own internal voltage regulators so they are not ratiometric.

|Value|Meaning|
|:---:|:---:|
|0|No|
|1|Yes|

## RNGFNDA_PWRRNG: Powersave range

This parameter sets the estimated terrain distance in meters above which the sensor will be put into a power saving mode (if available). A value of zero means power saving is not enabled

- Units: m

- Range: 0 32767

## RNGFNDA_GNDCLEAR: Distance (in cm) from the range finder to the ground

This parameter sets the expected range measurement(in cm) that the range finder should return when the vehicle is on the ground.

- Units: cm

- Range: 5 127

- Increment: 1

## RNGFNDA_ADDR: Bus address of sensor

This sets the bus address of the sensor, where applicable. Used for the I2C and UAVCAN sensors to allow for multiple sensors on different addresses. A value of 0 disables the sensor.

- Range: 0 127

- Increment: 1

## RNGFNDA_POS_X:  X position offset

*Note: This parameter is for advanced users*

X position of the first rangefinder in body frame. Positive X is forward of the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFNDA_POS_Y: Y position offset

*Note: This parameter is for advanced users*

Y position of the first rangefinder in body frame. Positive Y is to the right of the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFNDA_POS_Z: Z position offset

*Note: This parameter is for advanced users*

Z position of the first rangefinder in body frame. Positive Z is down from the origin. Use the zero range datum point if supplied.

- Units: m

## RNGFNDA_ORIENT: Rangefinder orientation

*Note: This parameter is for advanced users*

Orientation of rangefinder

|Value|Meaning|
|:---:|:---:|
|0|Forward|
| 1|Forward-Right|
| 2|Right|
| 3|Back-Right|
| 4|Back|
| 5|Back-Left|
| 6|Left|
| 7|Forward-Left|
| 24|Up|
| 25|Down|

# RNGFNDA Parameters

## RNGFNDA_WSP_MAVG: Moving Average Range

*Note: This parameter is for advanced users*

Sets the number of historic range results to use for calculating the current range result. When MAVG is greater than 1, the current range result will be the current measured value averaged with the N-1 previous results

- Range: 0 255

## RNGFNDA_WSP_MEDF: Moving Median Filter

*Note: This parameter is for advanced users*

Sets the window size for the real-time median filter. When MEDF is greater than 0 the median filter is active

- Range: 0 255

## RNGFNDA_WSP_FRQ: Frequency

*Note: This parameter is for advanced users*

Sets the repetition frequency of the ranging operation in Hertz. Upon entering the desired frequency the system will calculate the nearest frequency that it can handle according to the resolution of internal timers.

- Range: 0 10000

## RNGFNDA_WSP_AVG: Multi-pulse averages

*Note: This parameter is for advanced users*

Sets the number of pulses to be used in multi-pulse averaging mode. In this mode, a sequence of rapid fire ranges are taken and then averaged to improve the accuracy of the measurement

- Range: 0 255

## RNGFNDA_WSP_THR: Sensitivity threshold

*Note: This parameter is for advanced users*

Sets the system sensitivity. Larger values of THR represent higher sensitivity. The system may limit the maximum value of THR to prevent excessive false alarm rates based on settings made at the factory. Set to -1 for automatic threshold adjustments

- Range: -1 255

## RNGFNDA_WSP_BAUD: Baud rate

*Note: This parameter is for advanced users*

Desired baud rate

|Value|Meaning|
|:---:|:---:|
|0|Low Speed|
|1|High Speed|

# SCHED Parameters

## SCHED_DEBUG: Scheduler debug level

*Note: This parameter is for advanced users*

Set to non-zero to enable scheduler debug messages. When set to show "Slips" the scheduler will display a message whenever a scheduled task is delayed due to too much CPU load. When set to ShowOverruns the scheduled will display a message whenever a task takes longer than the limit promised in the task table.

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|2|ShowSlips|
|3|ShowOverruns|

## SCHED_LOOP_RATE: Scheduling main loop rate

*Note: This parameter is for advanced users*

This controls the rate of the main control loop in Hz. This should only be changed by developers. This only takes effect on restart. Values over 400 are considered highly experimental.

|Value|Meaning|
|:---:|:---:|
|50|50Hz|
|100|100Hz|
|200|200Hz|
|250|250Hz|
|300|300Hz|
|400|400Hz|

- RebootRequired: True

# SCR Parameters

## SCR_ENABLE: Enable Scripting

*Note: This parameter is for advanced users*

Controls if scripting is enabled

|Value|Meaning|
|:---:|:---:|
|0|None|
|1|Lua Scripts|

- RebootRequired: True

## SCR_VM_I_COUNT: Scripting Virtual Machine Instruction Count

*Note: This parameter is for advanced users*

The number virtual machine instructions that can be run before considering a script to have taken an excessive amount of time

- Range: 1000 1000000

- Increment: 10000

## SCR_HEAP_SIZE: Scripting Heap Size

*Note: This parameter is for advanced users*

Amount of memory available for scripting

- Range: 1024 1048576

- Increment: 1024

- RebootRequired: True

# SERIAL Parameters

## SERIAL0_BAUD: Serial0 baud rate

The baud rate used on the USB console. Most stm32-based boards can support rates of up to 1500. If you setup a rate you cannot support and then can't connect to your board you should load a firmware from a different vehicle type. That will reset all your parameters to defaults.

|Value|Meaning|
|:---:|:---:|
|1|1200|
|2|2400|
|4|4800|
|9|9600|
|19|19200|
|38|38400|
|57|57600|
|111|111100|
|115|115200|
|256|256000|
|460|460800|
|500|500000|
|921|921600|
|1500|1500000|

## SERIAL0_PROTOCOL: Console protocol selection

Control what protocol to use on the console. 

|Value|Meaning|
|:---:|:---:|
|1|MAVlink1|
| 2|MAVLink2|

- RebootRequired: True

## SERIAL1_PROTOCOL: Telem1 protocol selection

Control what protocol to use on the Telem1 port. Note that the Frsky options require external converter hardware. See the wiki for details.

|Value|Meaning|
|:---:|:---:|
|-1|None|
| 1|MAVLink1|
| 2|MAVLink2|
| 3|Frsky D|
| 4|Frsky SPort|
| 5|GPS|
| 7|Alexmos Gimbal Serial|
| 8|SToRM32 Gimbal Serial|
| 9|Rangefinder|
| 10|FrSky SPort Passthrough (OpenTX)|
| 11|Lidar360|
| 13|Beacon|
| 14|Volz servo out|
| 15|SBus servo out|
| 16|ESC Telemetry|
| 17|Devo Telemetry|
| 18|OpticalFlow|
| 19|RobotisServo|
| 20|NMEA Output|
| 21|WindVane|
| 22|SLCAN|
| 23|RCIN|

- RebootRequired: True

## SERIAL1_BAUD: Telem1 Baud Rate

The baud rate used on the Telem1 port. Most stm32-based boards can support rates of up to 1500. If you setup a rate you cannot support and then can't connect to your board you should load a firmware from a different vehicle type. That will reset all your parameters to defaults.

|Value|Meaning|
|:---:|:---:|
|1|1200|
|2|2400|
|4|4800|
|9|9600|
|19|19200|
|38|38400|
|57|57600|
|111|111100|
|115|115200|
|256|256000|
|500|500000|
|921|921600|
|1500|1500000|

## SERIAL2_PROTOCOL: Telemetry 2 protocol selection

Control what protocol to use on the Telem2 port. Note that the Frsky options require external converter hardware. See the wiki for details.

|Value|Meaning|
|:---:|:---:|
|-1|None|
| 1|MAVLink1|
| 2|MAVLink2|
| 3|Frsky D|
| 4|Frsky SPort|
| 5|GPS|
| 7|Alexmos Gimbal Serial|
| 8|SToRM32 Gimbal Serial|
| 9|Rangefinder|
| 10|FrSky SPort Passthrough (OpenTX)|
| 11|Lidar360|
| 13|Beacon|
| 14|Volz servo out|
| 15|SBus servo out|
| 16|ESC Telemetry|
| 17|Devo Telemetry|
| 18|OpticalFlow|
| 19|RobotisServo|
| 20|NMEA Output|
| 21|WindVane|
| 22|SLCAN|
| 23|RCIN|

- RebootRequired: True

## SERIAL2_BAUD: Telemetry 2 Baud Rate

The baud rate of the Telem2 port. Most stm32-based boards can support rates of up to 1500. If you setup a rate you cannot support and then can't connect to your board you should load a firmware from a different vehicle type. That will reset all your parameters to defaults.

|Value|Meaning|
|:---:|:---:|
|1|1200|
|2|2400|
|4|4800|
|9|9600|
|19|19200|
|38|38400|
|57|57600|
|111|111100|
|115|115200|
|256|256000|
|500|500000|
|921|921600|
|1500|1500000|

## SERIAL3_PROTOCOL: Serial 3 (GPS) protocol selection

Control what protocol Serial 3 (GPS) should be used for. Note that the Frsky options require external converter hardware. See the wiki for details.

|Value|Meaning|
|:---:|:---:|
|-1|None|
| 1|MAVLink1|
| 2|MAVLink2|
| 3|Frsky D|
| 4|Frsky SPort|
| 5|GPS|
| 7|Alexmos Gimbal Serial|
| 8|SToRM32 Gimbal Serial|
| 9|Rangefinder|
| 10|FrSky SPort Passthrough (OpenTX)|
| 11|Lidar360|
| 13|Beacon|
| 14|Volz servo out|
| 15|SBus servo out|
| 16|ESC Telemetry|
| 17|Devo Telemetry|
| 18|OpticalFlow|
| 19|RobotisServo|
| 20|NMEA Output|
| 21|WindVane|
| 22|SLCAN|
| 23|RCIN|

- RebootRequired: True

## SERIAL3_BAUD: Serial 3 (GPS) Baud Rate

The baud rate used for the Serial 3 (GPS). Most stm32-based boards can support rates of up to 1500. If you setup a rate you cannot support and then can't connect to your board you should load a firmware from a different vehicle type. That will reset all your parameters to defaults.

|Value|Meaning|
|:---:|:---:|
|1|1200|
|2|2400|
|4|4800|
|9|9600|
|19|19200|
|38|38400|
|57|57600|
|111|111100|
|115|115200|
|256|256000|
|500|500000|
|921|921600|
|1500|1500000|

## SERIAL4_PROTOCOL: Serial4 protocol selection

Control what protocol Serial4 port should be used for. Note that the Frsky options require external converter hardware. See the wiki for details.

|Value|Meaning|
|:---:|:---:|
|-1|None|
| 1|MAVLink1|
| 2|MAVLink2|
| 3|Frsky D|
| 4|Frsky SPort|
| 5|GPS|
| 7|Alexmos Gimbal Serial|
| 8|SToRM32 Gimbal Serial|
| 9|Rangefinder|
| 10|FrSky SPort Passthrough (OpenTX)|
| 11|Lidar360|
| 13|Beacon|
| 14|Volz servo out|
| 15|SBus servo out|
| 16|ESC Telemetry|
| 17|Devo Telemetry|
| 18|OpticalFlow|
| 19|RobotisServo|
| 20|NMEA Output|
| 21|WindVane|
| 22|SLCAN|
| 23|RCIN|

- RebootRequired: True

## SERIAL4_BAUD: Serial 4 Baud Rate

The baud rate used for Serial4. Most stm32-based boards can support rates of up to 1500. If you setup a rate you cannot support and then can't connect to your board you should load a firmware from a different vehicle type. That will reset all your parameters to defaults.

|Value|Meaning|
|:---:|:---:|
|1|1200|
|2|2400|
|4|4800|
|9|9600|
|19|19200|
|38|38400|
|57|57600|
|111|111100|
|115|115200|
|256|256000|
|500|500000|
|921|921600|
|1500|1500000|

## SERIAL5_PROTOCOL: Serial5 protocol selection

Control what protocol Serial5 port should be used for. Note that the Frsky options require external converter hardware. See the wiki for details.

|Value|Meaning|
|:---:|:---:|
|-1|None|
| 1|MAVLink1|
| 2|MAVLink2|
| 3|Frsky D|
| 4|Frsky SPort|
| 5|GPS|
| 7|Alexmos Gimbal Serial|
| 8|SToRM32 Gimbal Serial|
| 9|Rangefinder|
| 10|FrSky SPort Passthrough (OpenTX)|
| 11|Lidar360|
| 13|Beacon|
| 14|Volz servo out|
| 15|SBus servo out|
| 16|ESC Telemetry|
| 17|Devo Telemetry|
| 18|OpticalFlow|
| 19|RobotisServo|
| 20|NMEA Output|
| 21|WindVane|
| 22|SLCAN|
| 23|RCIN|

- RebootRequired: True

## SERIAL5_BAUD: Serial 5 Baud Rate

The baud rate used for Serial5. Most stm32-based boards can support rates of up to 1500. If you setup a rate you cannot support and then can't connect to your board you should load a firmware from a different vehicle type. That will reset all your parameters to defaults.

|Value|Meaning|
|:---:|:---:|
|1|1200|
|2|2400|
|4|4800|
|9|9600|
|19|19200|
|38|38400|
|57|57600|
|111|111100|
|115|115200|
|256|256000|
|500|500000|
|921|921600|
|1500|1500000|

## SERIAL6_PROTOCOL: Serial6 protocol selection

Control what protocol Serial6 port should be used for. Note that the Frsky options require external converter hardware. See the wiki for details.

|Value|Meaning|
|:---:|:---:|
|-1|None|
| 1|MAVLink1|
| 2|MAVLink2|
| 3|Frsky D|
| 4|Frsky SPort|
| 5|GPS|
| 7|Alexmos Gimbal Serial|
| 8|SToRM32 Gimbal Serial|
| 9|Rangefinder|
| 10|FrSky SPort Passthrough (OpenTX)|
| 11|Lidar360|
| 13|Beacon|
| 14|Volz servo out|
| 15|SBus servo out|
| 16|ESC Telemetry|
| 17|Devo Telemetry|
| 18|OpticalFlow|
| 19|RobotisServo|
| 20|NMEA Output|
| 21|WindVane|
| 22|SLCAN|
| 23|RCIN|

- RebootRequired: True

## SERIAL6_BAUD: Serial 6 Baud Rate

The baud rate used for Serial6. Most stm32-based boards can support rates of up to 1500. If you setup a rate you cannot support and then can't connect to your board you should load a firmware from a different vehicle type. That will reset all your parameters to defaults.

|Value|Meaning|
|:---:|:---:|
|1|1200|
|2|2400|
|4|4800|
|9|9600|
|19|19200|
|38|38400|
|57|57600|
|111|111100|
|115|115200|
|256|256000|
|500|500000|
|921|921600|
|1500|1500000|

## SERIAL1_OPTIONS: Telem1 options

*Note: This parameter is for advanced users*

Control over UART options. The InvertRX option controls invert of the receive pin. The InvertTX option controls invert of the transmit pin. The HalfDuplex option controls half-duplex (onewire) mode, where both transmit and receive is done on the transmit wire. The Swap option allows the RX and TX pins to be swapped on STM32F7 based boards.

- Bitmask: 0:InvertRX, 1:InvertTX, 2:HalfDuplex, 4:Swap

- RebootRequired: True

## SERIAL2_OPTIONS: Telem2 options

*Note: This parameter is for advanced users*

Control over UART options. The InvertRX option controls invert of the receive pin. The InvertTX option controls invert of the transmit pin. The HalfDuplex option controls half-duplex (onewire) mode, where both transmit and receive is done on the transmit wire.

- Bitmask: 0:InvertRX, 1:InvertTX, 2:HalfDuplex, 4:Swap

- RebootRequired: True

## SERIAL3_OPTIONS: Serial3 options

*Note: This parameter is for advanced users*

Control over UART options. The InvertRX option controls invert of the receive pin. The InvertTX option controls invert of the transmit pin. The HalfDuplex option controls half-duplex (onewire) mode, where both transmit and receive is done on the transmit wire.

- Bitmask: 0:InvertRX, 1:InvertTX, 2:HalfDuplex, 4:Swap

- RebootRequired: True

## SERIAL4_OPTIONS: Serial4 options

*Note: This parameter is for advanced users*

Control over UART options. The InvertRX option controls invert of the receive pin. The InvertTX option controls invert of the transmit pin. The HalfDuplex option controls half-duplex (onewire) mode, where both transmit and receive is done on the transmit wire.

- Bitmask: 0:InvertRX, 1:InvertTX, 2:HalfDuplex, 4:Swap

- RebootRequired: True

## SERIAL5_OPTIONS: Serial5 options

*Note: This parameter is for advanced users*

Control over UART options. The InvertRX option controls invert of the receive pin. The InvertTX option controls invert of the transmit pin. The HalfDuplex option controls half-duplex (onewire) mode, where both transmit and receive is done on the transmit wire.

- Bitmask: 0:InvertRX, 1:InvertTX, 2:HalfDuplex, 4:Swap

- RebootRequired: True

## SERIAL6_OPTIONS: Serial6 options

*Note: This parameter is for advanced users*

Control over UART options. The InvertRX option controls invert of the receive pin. The InvertTX option controls invert of the transmit pin. The HalfDuplex option controls half-duplex (onewire) mode, where both transmit and receive is done on the transmit wire.

- Bitmask: 0:InvertRX, 1:InvertTX, 2:HalfDuplex, 4:Swap

- RebootRequired: True

## SERIAL_PASS1: Serial passthru first port

*Note: This parameter is for advanced users*

This sets one side of pass-through between two serial ports. Once both sides are set then all data received on either port will be passed to the other port

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
|0|Serial0|
|1|Serial1|
|2|Serial2|
|3|Serial3|
|4|Serial4|
|5|Serial5|
|6|Serial6|

## SERIAL_PASS2: Serial passthru second port

*Note: This parameter is for advanced users*

This sets one side of pass-through between two serial ports. Once both sides are set then all data received on either port will be passed to the other port

|Value|Meaning|
|:---:|:---:|
|-1|Disabled|
|0|Serial0|
|1|Serial1|
|2|Serial2|
|3|Serial3|
|4|Serial4|
|5|Serial5|
|6|Serial6|

## SERIAL_PASSTIMO: Serial passthru timeout

*Note: This parameter is for advanced users*

This sets a timeout for serial pass-through in seconds. When the pass-through is enabled by setting the SERIAL_PASS1 and SERIAL_PASS2 parameters then it remains in effect until no data comes from the first port for SERIAL_PASSTIMO seconds. This allows the port to revent to its normal usage (such as MAVLink connection to a GCS) when it is no longer needed. A value of 0 means no timeout.

- Range: 0 120

- Units: s

## SERIAL7_PROTOCOL: Serial7 protocol selection

Control what protocol Serial7 port should be used for. Note that the Frsky options require external converter hardware. See the wiki for details.

|Value|Meaning|
|:---:|:---:|
|-1|None|
| 1|MAVLink1|
| 2|MAVLink2|
| 3|Frsky D|
| 4|Frsky SPort|
| 5|GPS|
| 7|Alexmos Gimbal Serial|
| 8|SToRM32 Gimbal Serial|
| 9|Rangefinder|
| 10|FrSky SPort Passthrough (OpenTX)|
| 11|Lidar360|
| 13|Beacon|
| 14|Volz servo out|
| 15|SBus servo out|
| 16|ESC Telemetry|
| 17|Devo Telemetry|
| 18|OpticalFlow|
| 19|RobotisServo|
| 20|NMEA Output|
| 21|WindVane|
| 22|SLCAN|
| 23|RCIN|

- RebootRequired: True

## SERIAL7_BAUD: Serial 7 Baud Rate

The baud rate used for Serial7. Most stm32-based boards can support rates of up to 1500. If you setup a rate you cannot support and then can't connect to your board you should load a firmware from a different vehicle type. That will reset all your parameters to defaults.

|Value|Meaning|
|:---:|:---:|
|1|1200|
|2|2400|
|4|4800|
|9|9600|
|19|19200|
|38|38400|
|57|57600|
|111|111100|
|115|115200|
|256|256000|
|500|500000|
|921|921600|
|1500|1500000|

## SERIAL7_OPTIONS: Serial7 options

*Note: This parameter is for advanced users*

Control over UART options. The InvertRX option controls invert of the receive pin. The InvertTX option controls invert of the transmit pin. The HalfDuplex option controls half-duplex (onewire) mode, where both transmit and receive is done on the transmit wire.

- Bitmask: 0:InvertRX, 1:InvertTX, 2:HalfDuplex, 4:Swap

- RebootRequired: True

# SERVO Parameters

## SERVO_AUTO_TRIM: Automatic servo trim

*Note: This parameter is for advanced users*

This enables automatic servo trim in flight. Servos will be trimed in stabilized flight modes when the aircraft is close to level. Changes to servo trim will be saved every 10 seconds and will persist between flights.

|Value|Meaning|
|:---:|:---:|
|0|Disable|
|1|Enable|

## SERVO_RATE: Servo default output rate

*Note: This parameter is for advanced users*

This sets the default output rate in Hz for all outputs.

- Range: 25 400

- Units: Hz

# SERVOn Parameters

## SERVOn_MIN: Minimum PWM

minimum PWM pulse width in microseconds. Typically 1000 is lower limit, 1500 is neutral and 2000 is upper limit.

- Units: PWM

- Range: 500 2200

- Increment: 1

## SERVOn_MAX: Maximum PWM

maximum PWM pulse width in microseconds. Typically 1000 is lower limit, 1500 is neutral and 2000 is upper limit.

- Units: PWM

- Range: 800 2200

- Increment: 1

## SERVOn_TRIM: Trim PWM

Trim PWM pulse width in microseconds. Typically 1000 is lower limit, 1500 is neutral and 2000 is upper limit.

- Units: PWM

- Range: 800 2200

- Increment: 1

## SERVOn_REVERSED: Servo reverse

Reverse servo operation. Set to 0 for normal operation. Set to 1 to reverse this output channel.

|Value|Meaning|
|:---:|:---:|
|0|Normal|
|1|Reversed|

## SERVOn_FUNCTION: Servo output function

Function assigned to this servo. Seeing this to Disabled(0) will setup this output for control by auto missions or MAVLink servo set commands. any other value will enable the corresponding function

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|RCPassThru|
|2|Flap|
|3|Flap_auto|
|4|Aileron|
|6|mount_pan|
|7|mount_tilt|
|8|mount_roll|
|9|mount_open|
|10|camera_trigger|
|11|release|
|12|mount2_pan|
|13|mount2_tilt|
|14|mount2_roll|
|15|mount2_open|
|16|DifferentialSpoilerLeft1|
|17|DifferentialSpoilerRight1|
|19|Elevator|
|21|Rudder|
|24|FlaperonLeft|
|25|FlaperonRight|
|26|GroundSteering|
|27|Parachute|
|28|EPM|
|29|LandingGear|
|30|EngineRunEnable|
|31|HeliRSC|
|32|HeliTailRSC|
|33|Motor1|
|34|Motor2|
|35|Motor3|
|36|Motor4|
|37|Motor5|
|38|Motor6|
|39|Motor7|
|40|Motor8|
|41|MotorTilt|
|51|RCIN1|
|52|RCIN2|
|53|RCIN3|
|54|RCIN4|
|55|RCIN5|
|56|RCIN6|
|57|RCIN7|
|58|RCIN8|
|59|RCIN9|
|60|RCIN10|
|61|RCIN11|
|62|RCIN12|
|63|RCIN13|
|64|RCIN14|
|65|RCIN15|
|66|RCIN16|
|67|Ignition|
|68|Choke|
|69|Starter|
|70|Throttle|
|71|TrackerYaw|
|72|TrackerPitch|
|73|ThrottleLeft|
|74|ThrottleRight|
|75|tiltMotorLeft|
|76|tiltMotorRight|
|77|ElevonLeft|
|78|ElevonRight|
|79|VTailLeft|
|80|VTailRight|
|81|BoostThrottle|
|82|Motor9|
|83|Motor10|
|84|Motor11|
|85|Motor12|
|86|DifferentialSpoilerLeft2|
|87|DifferentialSpoilerRight2|
|88|Winch|
|89|Main Sail|
|90|Camera ISO|
|91|Camera Focus|
|92|Camera Shutter Speed|
|94|Script 1|
|95|Script 2|
|96|Script 3|
|97|Script 4|
|98|Script 5|
|99|Script 6|
|100|Script 7|
|101|Script 8|
|102|Script 9|
|103|Script 10|
|104|Script 11|
|105|Script 12|
|106|Script 13|
|107|Script 14|
|108|Script 15|
|109|Script 16|

# SERVOBLH Parameters

## SERVO_BLH_MASK: BLHeli Channel Bitmask

*Note: This parameter is for advanced users*

Enable of BLHeli pass-thru servo protocol support to specific channels. This mask is in addition to motors enabled using SERVO_BLH_AUTO (if any)

- Bitmask: 0:Channel1,1:Channel2,2:Channel3,3:Channel4,4:Channel5,5:Channel6,6:Channel7,7:Channel8,8:Channel9,9:Channel10,10:Channel11,11:Channel12,12:Channel13,13:Channel14,14:Channel15,15:Channel16

## SERVO_BLH_AUTO: BLHeli auto-enable for multicopter motors

If set to 1 this auto-enables BLHeli pass-thru support for all multicopter motors

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|

## SERVO_BLH_TEST: BLHeli internal interface test

*Note: This parameter is for advanced users*

Setting SERVO_BLH_TEST to a motor number enables an internal test of the BLHeli ESC protocol to the corresponding ESC. The debug output is displayed on the USB console.

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|TestMotor1|
|2|TestMotor2|
|3|TestMotor3|
|4|TestMotor4|
|5|TestMotor5|
|6|TestMotor6|
|7|TestMotor7|
|8|TestMotor8|

## SERVO_BLH_TMOUT: BLHeli protocol timeout

This sets the inactivity timeout for the BLHeli protocol in seconds. If no packets are received in this time normal MAVLink operations are resumed. A value of 0 means no timeout

- Units: s

- Range: 0 300

## SERVO_BLH_TRATE: BLHeli telemetry rate

This sets the rate in Hz for requesting telemetry from ESCs. It is the rate per ESC. Setting to zero disables telemetry requests

- Units: Hz

- Range: 0 500

## SERVO_BLH_DEBUG: BLHeli debug level

When set to 1 this enabled verbose debugging output over MAVLink when the blheli protocol is active. This can be used to diagnose failures.

|Value|Meaning|
|:---:|:---:|
|0|Disabled|
|1|Enabled|

## SERVO_BLH_OTYPE: BLHeli output type override

*Note: This parameter is for advanced users*

When set to a non-zero value this overrides the output type for the output channels given by SERVO_BLH_MASK. This can be used to enable DShot on outputs that are not part of the multicopter motors group.

|Value|Meaning|
|:---:|:---:|
|0|None|
|1|OneShot|
|2|OneShot125|
|3|Brushed|
|4|DShot150|
|5|DShot300|
|6|DShot600|
|7|DShot1200|

## SERVO_BLH_PORT: Control port

*Note: This parameter is for advanced users*

This sets the telemetry port to use for blheli pass-thru

|Value|Meaning|
|:---:|:---:|
|0|Console|
|1|Telem1|
|2|Telem2|
|3|Telem3|
|4|Telem4|
|5|Telem5|

## SERVO_BLH_POLES: BLHeli Motor Poles

*Note: This parameter is for advanced users*

This allows calculation of true RPM from ESC's eRPM. The default is 14.

- Range: 1 127

## SERVO_BLH_REMASK: BLHeli bitmask of reversible channels

*Note: This parameter is for advanced users*

Mask of channels which are reversible. This is used for ESCs which have been configured in '3D' mode, allowing for the motor to spin in either direction

- Bitmask: 0:Channel1,1:Channel2,2:Channel3,3:Channel4,4:Channel5,5:Channel6,6:Channel7,7:Channel8,8:Channel9,9:Channel10,10:Channel11,11:Channel12,12:Channel13,13:Channel14,14:Channel15,15:Channel16

# SERVOROB Parameters

## SERVO_ROB_POSMIN: Robotis servo position min

Position minimum at servo min value. This should be within the position control range of the servos, normally 0 to 4095

- Range: 0 4095

## SERVO_ROB_POSMAX: Robotis servo position max

Position maximum at servo max value. This should be within the position control range of the servos, normally 0 to 4095

- Range: 0 4095

# SERVOSBUS Parameters

## SERVO_SBUS_RATE: SBUS default output rate

*Note: This parameter is for advanced users*

This sets the SBUS output frame rate in Hz.

- Range: 25 250

- Units: Hz

# SERVOVOLZ Parameters

## SERVO_VOLZ_MASK: Channel Bitmask

Enable of volz servo protocol to specific channels

- Bitmask: 0:Channel1,1:Channel2,2:Channel3,3:Channel4,4:Channel5,5:Channel6,6:Channel7,7:Channel8,8:Channel9,9:Channel10,10:Channel11,11:Channel12,12:Channel13,13:Channel14,14:Channel15,15:Channel16

# SRn Parameters

## SRn_RAW_SENS: Raw sensor stream rate

*Note: This parameter is for advanced users*

Stream rate of RAW_IMU, SCALED_IMU2, SCALED_PRESSURE, and SENSOR_OFFSETS to ground station

- Units: Hz

- Range: 0 10

- Increment: 1

## SRn_EXT_STAT: Extended status stream rate to ground station

*Note: This parameter is for advanced users*

Stream rate of SYS_STATUS, MEMINFO, MISSION_CURRENT, GPS_RAW_INT, NAV_CONTROLLER_OUTPUT, and LIMITS_STATUS to ground station

- Units: Hz

- Range: 0 10

- Increment: 1

## SRn_RC_CHAN: RC Channel stream rate to ground station

*Note: This parameter is for advanced users*

Stream rate of SERVO_OUTPUT_RAW and RC_CHANNELS_RAW to ground station

- Units: Hz

- Range: 0 10

- Increment: 1

## SRn_POSITION: Position stream rate to ground station

*Note: This parameter is for advanced users*

Stream rate of GLOBAL_POSITION_INT to ground station

- Units: Hz

- Range: 0 10

- Increment: 1

## SRn_EXTRA1: Extra data type 1 stream rate to ground station

*Note: This parameter is for advanced users*

Stream rate of ATTITUDE and SIMSTATE (SITL only) to ground station

- Units: Hz

- Range: 0 10

- Increment: 1

## SRn_EXTRA2: Extra data type 2 stream rate to ground station

*Note: This parameter is for advanced users*

Stream rate of VFR_HUD to ground station

- Units: Hz

- Range: 0 10

- Increment: 1

## SRn_EXTRA3: Extra data type 3 stream rate to ground station

*Note: This parameter is for advanced users*

Stream rate of AHRS, HWSTATUS, and SYSTEM_TIME to ground station

- Units: Hz

- Range: 0 10

- Increment: 1

## SRn_PARAMS: Parameter stream rate to ground station

*Note: This parameter is for advanced users*

Stream rate of PARAM_VALUE to ground station

- Units: Hz

- Range: 0 10

- Increment: 1
