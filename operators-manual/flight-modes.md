# Flight Modes

ArduSub supports several different flight modes, some of which are only available when certain sensors are present. ArduSub always operates in exactly one flight mode at any given time. ArduSub always boots in *Manual* mode.

## Manual

*Manual* mode passes the pilot inputs directly to the motors, with no stabilization. ArduSub always boots in *Manual* mode.

## Stabilize

*Stabilize* mode is like *Manual* mode, with heading and attitude stabilization.

## Depth Hold

*Depth Hold* is like *Stabilize* mode with the addition of depth stabilization when the pilot throttle input is zero. A depth sensor is required to use depth hold mode.

## Acro

*Acro* (Acrobatic) mode performs angular rate stabilization.

# Position Enabled Modes

> **Warning** These modes are still in development and are not considered stable. These functions are NOT SUPPORTED for normal use/operation.

<span></span>
> **GPS** These modes require an [underwater positioning system](https://en.wikipedia.org/wiki/Underwater_acoustic_positioning_system). A GPS antenna will not work under water.

## Position Hold

*Position Hold* mode will stabilize the vehicle's absolute position, attitude, and heading when the pilot control inputs are neutral. The vehicle can be maneuvered and repositioned by the pilot.

> **Warning** This mode is not supported!

## Auto

*Auto* mode executes the mission stored on the autopilot autonomously. Pilot control inputs are ignored in most cases. The vehicle may be disarmed, or the mode can be changed to abort the mission.

> **Warning** This mode is not supported!

## Circle

*Circle* mode navigates in circles with the front of the vehicle facing the center point.

> **Warning** This mode is not supported!

## Guided

*Guided* mode allows the vehicle's target position to be set dynamically by a ground control station or companion computer. This allows 'Click to Navigate Here' interactions with a map.

> **Warning** This mode is not supported!

<p style="font-size:10px; text-align:center">
Sponsored by <a href="http://www.bluerobotics.com/">Blue Robotics</a>. Code released under the <a href="https://github.com/bluerobotics/ardusub/blob/master/COPYING.txt">GPLv3 License</a>. Documentation released under the <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC-NC-SA 4.0</a>.<br />
<a href="https://github.com/bluerobotics/ardusub-gitbook/issues/">Submit a Documentation GitHub Issue here</a> to report any errors, suggestions, or missing information in this documentation.<br />
<a href="https://github.com/bluerobotics/ardusub/issues/">Submit an ArduSub GitHub Issue here</a> to report issues with the ArduSub software.
</p>
