# Joystick Button Functions

Joystick buttons can be configured to perform different functions. Each button may be assigned a regular function and a shift function. To use shift functions, a button must be assigned the special *shift* function. The shift button will then act like a shift key on a keyboard; when held, it modifies the other buttons to execute their assigned shift functions. The available button functions are described below.

### General

- none: Do nothing, button is disabled
- shift: When held, act as a shift modifier for other buttons
- arm_toggle: Toggle the armed state of the vehicle
- arm: Arm the vehicle
- disarm: Disarm the vehicle
- gain_toggle: Toggle between minimum and maximum pilot input gain sensitivity
- gain_inc: Increase pilot input gain/sensitivity
- gain_dec: Decrease pilot input gain/sensitivity
- trim_roll_inc: Trim level target roll to the right
- trim_roll_dec: Trim level target roll to the left
- trim_pitch_inc: Trim level target pitch forward
- trim_pitch_dec: Trim level target pitch backward
- input_hold_toggle: Toggle holding current joystick axis inputs (cruise control on/off)
- roll_pitch_toggle: Toggle between roll/pitch and forward/lateral control on joystick input

### Mode Selection

These button functions will command a switch to the corresponding flight mode. Please note that the advanced modes are in development and are not recommended for general use.

** Standard Modes **
- mode_manual
- mode_stabilize
- mode_depth_hold

** Advanced Modes **
- mode_poshold
- mode_auto
- mode_circle
- mode_guided
- mode_acro

### Camera Control

- mount_center: Sets RC Input channel 8 pwm to the value configured by the *CAM_TILT_CENTER* parameter
- mount_tilt_up: Increase RC Input channel 8 pwm by the amount configured by the *JS_CAM_TILT_STEP* parameter
- mount_tilt_down: Decrease RC Input channel 8 pwm by the amount configured by the *JS_CAM_TILT_STEP* parameter
- camera_trigger: Trigger cameras shutter **NOT IMPLEMENTED**
- camera_source_toggle: Toggle video source, toggles RC Input channel 10 between 1100 and 1900 pwm
- mount_pan_right: Pan mount right **NOT IMPLEMENTED**
- mount_pan_left: Pan mount left **NOT IMPLEMENTED**

### Lights Control

- lights1_cycle: Increase or decrease RC Input channel 9 pwm by the amount configured by the *JS_LIGHTS_STEP* parameter, switches between increasing and increasing when output limits are reached
- lights1_brighter: Increase RC Input channel 9 pwm by the amount configured by the *JS_LIGHTS_STEP* parameter
- lights1_dimmer: Decrease RC Input channel 9 pwm by the amount configured by the *JS_LIGHTS_STEP* parameter

- lights2_cycle: Increase or decrease RC Input channel 10 pwm by the amount configured by the *JS_LIGHTS_STEP* parameter, switches between increasing and increasing when output limits are reached
- lights2_brighter: Increase RC Input channel 10 pwm by the amount configured by the *JS_LIGHTS_STEP* parameter
- lights2_dimmer: Decrease RC Input channel 10 pwm by the amount configured by the *JS_LIGHTS_STEP* parameter

### Relay Control

- relay_1_on: Sets the pin configured by the *RELAY_PIN* parameter to output HIGH
- relay_1_off: Sets the pin configured by the *RELAY_PIN* parameter to output LOW
- relay_1_toggle: Toggles the state of the pin configured by the *RELAY_PIN* parameter

- relay_2_on: Sets the pin configured by the *RELAY_PIN2* parameter to output HIGH
- relay_2_off: Sets the pin configured by the *RELAY_PIN2* parameter to output LOW
- relay_2_toggle: Toggles the state of the pin configured by the *RELAY_PIN2* parameter

- relay_3_on: Sets the pin configured by the *RELAY_PIN3* parameter to output HIGH
- relay_3_off: Sets the pin configured by the *RELAY_PIN3* parameter to output LOW
- relay_3_toggle: Toggles the state of the pin configured by the *RELAY_PIN3* parameter

### Servo Control

- servo_1_inc: Increase *Aux1* servo output by 50 pwm
- servo_1_dec: Decrease *Aux1* servo output by 50 pwm
- servo_1_min: Set *Aux1* servo output to the configured minimum pwm according to SERVO9_MIN
- servo_1_max: Set *Aux1* servo output to the configured maximum pwm according to SERVO9_MAX
- servo_1_center: Set *Aux1* servo output to the configured center according to SERVO9_TRIM

- servo_2_inc: Increase *Aux2* servo output by 50 pwm
- servo_2_dec: Decrease *Aux2* servo output by 50 pwm
- servo_2_min: Set *Aux2* servo output to the configured minimum pwm according to SERVO10_MIN
- servo_2_max: Set *Aux2* servo output to the configured maximum pwm according to SERVO10_MAX
- servo_2_center: Set *Aux2* servo output to the configured center according to SERVO10_TRIM

- servo_3_inc: Increase *Aux3* servo output by 50 pwm
- servo_3_dec: Decrease *Aux3* servo output by 50 pwm
- servo_3_min: Set *Aux3* servo output to the configured minimum pwm according to SERVO11_MIN
- servo_3_max: Set *Aux3* servo output to the configured maximum pwm according to SERVO11_MAX
- servo_3_center: Set *Aux3* servo output to the configured center according to SERVO11_TRIM


### Custom

These are reserved for developer use, and do not do anything by default

- custom_1
- custom_2
- custom_3
- custom_4
- custom_5
- custom_6

<p style="font-size:10px; text-align:center">
Sponsored by <a href="http://www.bluerobotics.com/">Blue Robotics</a>. Code released under the <a href="https://github.com/bluerobotics/ardusub/blob/master/COPYING.txt">GPLv3 License</a>. Documentation released under the <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC-NC-SA 4.0</a>.<br />
<a href="https://github.com/bluerobotics/ardusub-docs/issues/">Submit a Documentation GitHub Issue here</a> to report any errors, suggestions, or missing information in this documentation.<br />
<a href="https://github.com/bluerobotics/ardusub/issues/">Submit an ArduSub GitHub Issue here</a> to report issues with the ArduSub software.
</p>

### ArduSub default button configuration
This is the default configuration of the joystick buttons in ArduSub.

|  Normal function | Shift function |
|:----------------:|:--------------:|
|       none       |      none      |
|    mode_manual   |      none      |
|  mode_depth_hold |      none      |
|  mode_stabilize  |      none      |
|      disarm      |      none      |
|       shift      |      none      |
|        arm       |      none      |
|   mount_center   |      none      |
|  input_hold_set  |      none      |
|  mount_tilt_down |      none      |
|   mount_tilt_up  |      none      |
|     gain_inc     | trim_pitch_dec |
|     gain_dec     | trim_pitch_inc |
|  lights1_dimmer  |  trim_roll_dec |
| lights1_brighter |  trim_roll_inc |
|       none       |      none      |

For more information, it's possible to check the ArduSub [joystick source code](https://github.com/ArduPilot/ardupilot/blob/master/ArduSub/joystick.cpp#L649).
