{% include "../../archive-notice.html" %}

# Camera Mount Setup Page

The Camera Mount Setup Page allows for the configuration of an installed camera pan/tilt/roll mount.

On ROVs, the standard is for just a tilt mount as the vehicle can normally rotate easily. However, if pan and roll servos are installed, there are additional configuration options to set up these axis'.

<img src="/images/reference/reference-ardusub-camera.png" class="img-responsive img-center" style="max-height:600px;">

The options allow for:
**Output Channel**: Select the appropriate output channel from the autopilot that the servo is plugged into.
**Servo Reverse**: Reverses the mount movement.
**Stabilize**: Enables auto-stabilization of the camera based on the vehicle pitch angle.
**Servo PWM limits**: Limits the PWM signal output to the servo. 1100 is the minimum, 1900 is the maximum. 
**Gimbal angle limits**: Limits the degrees of rotation.

## Gimbal Settings

These settings allow for different types of gimbals to be used.

<img src="/images/reference/reference-ardusub-camera-gimbal-settings.png" class="img-responsive img-center" style="max-height:600px;">

**Type**: None | Servo (Default) | 3DR Solo | Alexmos Serial | SToRM32 MAVLink | SToRM32 Serial

**Default Mode**: Retracted | Neutral | MAVLink Targeting | RC Targeting (Default) | GPS Point
