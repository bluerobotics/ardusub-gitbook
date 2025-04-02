{% include "../archive-notice.html" %}

# RC input and output

ArduSub is designed around two independent concepts of *RC Input* and *RC Output*. RC Input is an array of control channels representing pilot inputs like forward and yaw commands. RC Output is an array of channels representing the pulse widths to write to individual servo output pins. Although ArduSub does not support the use of RC receivers, the logic is the same and is applied to joystick inputs instead. Joystick input and RC Input are synonymous in ArduSub.

## RC Inputs

These are the default channel mappings for RC input:

| Channel | Meaning |
|---:|:---|
| 1 | Pitch |
| 2 | Roll |
| 3 | Throttle |
| 4 | Yaw |
| 5 | Forward |
| 6 | Lateral |
| 7 | Camera Pan |
| 8 | Camera Tilt* |
| 9 | Lights 1 Level |
| 10 | Lights 2 Level |
| 11 | Video Switch |

\****Note:*** RC Input Camera Tilt control is not standard servo-style control. Specifying a 'PWM' value sets the **speed for a sweep from the current tilt angle to the min/max camera angle**. The input difference from the midpoint (1500) sets the speed, e.g. a 1900 input sweeps to the max camera angle twice as fast as 1700.

## RC Outputs

On the Pixhawk, there are 8 main outputs and 6 auxiliary outputs. The main outputs are updated at 200Hz by default (configured via the [*RC_SPEED*](/developers/full-parameter-list.md#rcspeed-esc-update-speed) parameter), and the auxiliary outputs are always updated at 50Hz. It is important not to connect analog servos to the main outputs, because the very fast update rate can cause the servo to burn itself out.

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


The Pixhawk 6 'auxiliary' outputs can be configured as either general purpose input/output or PWM output.
By default, aux outputs 5 and 6 (SERVO13 and SERVO14) are reserved as GPIO pins to be used for relays, and will not output a pwm signal for other functions. This is configured with the [*BRD_PWM_COUNT*](/developers/full-parameter-list.md#brdpwmcount-auxiliary-pin-config) parameter at boot, which determines how many of the auxiliary outputs to configure as PWM outputs (default is 4).


| BRD_PWM_COUNT <td colspan=6> <b> Aux pin configuration
|---:|:---|
|               | 1 | 2 | 3 | 4 | 5 | 6 |
|       0       | GPIO | GPIO | GPIO | GPIO | GPIO | GPIO |
|       2       | PWM | PWM | GPIO | GPIO | GPIO | GPIO |
|   **(default) 4** | **PWM** | **PWM** | **PWM** | **PWM** | **GPIO** | **GPIO** |
|       6       | PWM | PWM | PWM | PWM | PWM | PWM |


# Controlling Servos

An output must be configured as PWM via the BRD_PWM_COUNT parameter to operate a servo.

The servos can be operated via the mavlink command DO_SET_SERVO. This command can be used to set the output of any servo channel that is not configured as a motor output. This command can conflict with other functions operating on the servo channel like pan/tilt mounts or lights. In order to avoid conflicts, the corresponding [SERVOn_FUNCTION](/developers/full-parameter-list.html#servonfunction-servo-output-function) parameter should be set to Disabled (0).

Up to three servos can also be operated via [joystick button functions](/developers/full-parameter-list.html#btnn-parameters). The joystick button functions for \*__servo_\_**n** will control the output on the Aux **n** pin (these cannot be remapped like the relay outputs).

| Joystick button function | Aux channel operated |
|---:|:---|
| *servo_1* | Aux 1 |
| *servo_2* | Aux 2 |
| *servo_3* | Aux 3 |

# Controlling Relays

ArduSub supports control of up to 4 relays. An output must be configured as GPIO via the [*BRD_PWM_COUNT*](/developers/full-parameter-list.md#brdpwmcount-auxiliary-pin-config) parameter to operate a relay. The output pin must also be selected for the corresponding [RELAY_PIN](/developers/full-parameter-list.html#relaypin-first-relay-pin) parameter.

The relays can be operated via the mavlink command DO_SET_RELAY.

Up to three relays can also be operated via [joystick button functions](/developers/full-parameter-list.html#btnn-parameters).
