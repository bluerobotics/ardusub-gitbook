# Features While in Operation

## Joystick Button Functions

The ArduSub firmware comes with the button setup shown below as a default:

<img src="/images/reference/reference-operational-joystick-defaults.png" class="img-responsive img-center" style="max-height:600px;">

Buttons may be reassigned though the following steps:
1. Go to Vehicle Setup View then select “[Joystick](/reference/ardusub/joystick-setup-page.md)”.
2. The “[Button Assignment](/reference/ardusub/joystick-setup-page.md#button-assignment)” tab shows what all the buttons are currently set to control.
3. Press the button that you are interested in changing. The button number will light up.
4. Select what you would like the button to do from the dropdown to the right of the button number.

## Flight Modes

* In **Manual Mode** the vehicle will only output motor controls based on the pilot input from the joysticks. There is no feedback stabilization, heading holding, or depth holding.
* In **Stabilize Mode** the vehicle will stabilize roll to level and it will maintain heading when not commanded to turn. The vertical control is left entirely to the pilot.
* In **Depth Hold Mode** the vehicle will hold depth unless you command it to dive/ascend. It will also stabilize roll to level and maintain heading when not commanded to turn.

## Pilot Input Gain

The Pilot Input Gain controls how much power is available for thruster control.

Gain settings can be adjusted through the *[JS_GAIN](/operators-manual/full-parameter-list.html#jsgaindefault-default-gain-at-boot)* parameter settings.

## Pitch/Roll Control

[Presently](https://github.com/ArduPilot/ardupilot/issues/9808) (due to legacy/inheritance reasons), there is no convenient way to control the roll and pitch of and ArduSub vehicle with QGroundControl. The available solution is to use the roll_pitch_toggle joystick button function. When this button is pushed, the forward and lateral joystick axes toggle between controlling the forward and lateral motion of the vehicle and controlling the roll and pitch of the vehicle.

The roll and pitch input behaves differently in different flight modes. See the [flight mode documentation](/operators-manual/flight-modes) for more information about how the different flight modes operate.

- MANUAL: The roll and pitch input control the **rotation rate** of the vehicle. As long as the joystick input is deflected, the vehicle will continue to rotate. A centered joystick input commands a rotation rate of zero.
- ACRO: This functions like MANUAL, but the rate of rotation is precisely controlled and stabilized.
- STABILIZE: The roll and pitch input control the **desired angle** of the vehicle attitude. When the joystick input is centered, the vehicle will stabilize a level attitude. When the joystick input is deflected, the vehicle will stabilize the deflected angle. There are two parameters that control the maximum angle of vehicle deflection: the pilot input gain (which scales the input), and the ANGLE_MAX parameter (which controls the maximum angle that the vehicle will deflect in stabilize mode). For example, if the ANGLE_MAX parameter is 80 degrees, and the input gain is 50%, when the the roll or pitch joystick input is completely deflected, the vehicle will deflect 40 degrees ( 0.5 * 80 ). Press the roll_pitch_toggle joystick button while the vehicle is deflected to lock the current deflection angle and return to controlling forward and lateral motion. To clear the roll and pitch input command, switch to MANUAL mode, or press the roll_pitch_toggle button.
- DEPTH HOLD: This functions like STABILIZE mode, but only small angles are tolerated. The vehicle will misbehave at larger angles. Roll and pitch input should be avoided in DEPTH HOLD mode until it is [properly supported](https://github.com/ArduPilot/ardupilot/issues/9823).

## Notifications
