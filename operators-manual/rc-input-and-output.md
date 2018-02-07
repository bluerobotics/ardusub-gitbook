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
| 7 | Reserved |
| 8 | Camera Tilt |
| 9 | Lights 1 Level |
| 10 | Lights 2 Level |
| 11 | Video Switch |

## RC Outputs

On the Pixhawk, there are 8 main outputs and 6 auxiliary outputs. The main outputs are updated at 200Hz by default (configured via the [*RC_SPEED*](/operators-manual/full-parameter-list.md#rcspeed-esc-update-speed) parameter), and the auxiliary outputs are always updated at 50Hz. It is important not to connect analog servos to the main outputs, because the very fast update rate can cause the servo to burn itself out.

By default, aux outputs 5 and 6 (SERVO13 and SERVO14) are reserved as GPIO pins to be used for relays, and will not output a pwm signal for other functions. This is configured with the [*BRD_PWM_COUNT*](/operators-manual/full-parameter-list.md#brdpwmcount-auxiliary-pin-config) parameter, which determines how many of the auxiliary outputs to configure as PWM outputs (default is 4).