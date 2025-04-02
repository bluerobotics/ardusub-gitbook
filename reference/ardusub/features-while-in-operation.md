{% include "../../archive-notice.html" %}

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

Gain settings can be adjusted through the *[JS_GAIN](/developers/full-parameter-list.md#jsgaindefault-default-gain-at-boot)* parameter settings.

## Pitch/Roll Control

{% include "roll-pitch-control.md" %}
