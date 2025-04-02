{% include "../archive-notice.html" %}

# Configuring Outputs

The Pixhawk has 14 servo output channels which are configured via the [SERVOn_* parameters](/operators-manual/full-parameter-list.html#servon-parameters) and the [BRD_PWM_COUNT](/operators-manual/full-parameter-list.html#brdpwmcount-auxiliary-pin-config) parameter.

| Pixhawk Label | Servo Channel |
|---:|:---|
| Main 1 | 1 |
| Main 2 | 2 |
| Main 3 | 3 |
| Main 4 | 4 |
| Main 5 | 5 |
| Main 6 | 6 |
| Main 7 | 7 |
| Main 8 | 8 |
| Aux 1 | 9 |
| Aux 2 | 10 |
| Aux 3 | 11 |
| Aux 4 | 12 |
| Aux 5 | 13 |
| Aux 6 | 14 |


The Pixhawk has 6 'auxiliary' outputs that can be configured as either general purpose input/output or PWM output.

The auxiliary pins are configured at boot according to the [BRD_PWM_COUNT](/operators-manual/full-parameter-list.html#brdpwmcount-auxiliary-pin-config) parameter.

| BRD_PWM_COUNT <td colspan=6> <b> Aux pin configuration 
|---:|:---|
|               | 1 | 2 | 3 | 4 | 5 | 6 |
|       0       | GPIO | GPIO | GPIO | GPIO | GPIO | GPIO |
|       2       | PWM | PWM | GPIO | GPIO | GPIO | GPIO |
|   (default) 4 | PWM | PWM | PWM | PWM | GPIO | GPIO |
|       6       | PWM | PWM | PWM | PWM | PWM | PWM |


# Controlling Servos

An output must be configured as PWM via the BRD_PWM_COUNT parameter to operate a servo.

The servos can be operated via the mavlink command DO_SET_SERVO. This command can be used to set the output of any servo channel that is not configured as a motor output. This command can conflict with other functions operating on the servo channel like pan/tilt mounts or lights. In order to avoid conflicts, the corresponding [SERVOn_FUNCTION](/operators-manual/full-parameter-list.html#servonfunction-servo-output-function) parameter should be set to Disabled (0).

Up to three servos can also be operated via [joystick button functions](/operators-manual/full-parameter-list.html#btnn-parameters). The joystick button functions for \*__servo_\_**n** will control the output on the Aux **n** pin (these cannot be remapped like the relay outputs).

| Joystick button function | Aux channel operated |
|---:|:---|
| *servo_1* | Aux 1 |
| *servo_2* | Aux 2 |
| *servo_3* | Aux 3 |

# Controlling Relays

ArduSub supports control of up to 4 relays. An output must be configured as GPIO via the BRD_PWM_COUNT parameter to operate a relay. The output pin must also be selected for the corresponding [RELAY_PIN](/operators-manual/full-parameter-list.html#relaypin-first-relay-pin) parameter. 

The relays can be operated via the mavlink command DO_SET_RELAY.

Up to three relays can also be operated via [joystick button functions](/operators-manual/full-parameter-list.html#btnn-parameters).


