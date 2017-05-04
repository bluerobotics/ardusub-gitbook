---
layout: default
title: "Joystick"
permalink: /joystick/
nav:
- Joystick: joystick
- Overview: overview
- Axis Setup: axis-setup
- Button Functions: button-functions
- Behind the Scenes: behind-the-scenes
---

# Failsafes

## Button Functions

### mode_

Push to switch to the cooresponding flight mode

### Camera Tilt

### Lights

### Relay

### Servo

### Trim

        k_none                  = 0,            ///< disabled
        k_shift                 = 1,            ///< "shift" buttons to allow more functions
        k_arm_toggle            = 2,            ///< arm/disarm vehicle toggle
        k_arm                   = 3,            ///< arm vehicle
        k_disarm                = 4,            ///< disarm vehicle

        k_mode_manual           = 5,            ///< enter enter manual mode
        k_mode_stabilize        = 6,            ///< enter stabilize mode
        k_mode_depth_hold       = 7,            ///< enter depth hold mode
        k_mode_poshold          = 8,            ///< enter poshold mode
        k_mode_auto             = 9,            ///< enter auto mode
        k_mode_circle           = 10,           ///< enter circle mode
        k_mode_guided           = 11,           ///< enter guided mode
        k_mode_acro             = 12,           ///< enter acro mode

        // 12-20 reserved for future mode functions
        k_mount_center          = 21,           ///< move mount to center
        k_mount_tilt_up         = 22,           ///< tilt mount up
        k_mount_tilt_down       = 23,           ///< tilt mount down
        k_camera_trigger        = 24,           ///< trigger camera shutter
        k_camera_source_toggle  = 25,           ///< toggle camera source
        k_mount_pan_right       = 26,           ///< pan mount right
        k_mount_pan_left        = 27,           ///< pan mount left
        // 26-30 reserved for future camera functions
        k_lights1_cycle         = 31,           ///< lights 1 cycle
        k_lights1_brighter      = 32,           ///< lights 1 up
        k_lights1_dimmer        = 33,           ///< lights 1 down
        k_lights2_cycle         = 34,           ///< lights 2 cycle
        k_lights2_brighter      = 35,           ///< lights 2 up
        k_lights2_dimmer        = 36,           ///< lights 2 down
        // 37-40 reserved for future light functions
        k_gain_toggle           = 41,           ///< toggle different gain settings
        k_gain_inc              = 42,           ///< increase control gain
        k_gain_dec              = 43,           ///< decrease control gain
        k_trim_roll_inc         = 44,           ///< increase roll trim
        k_trim_roll_dec         = 45,           ///< decrease roll trim
        k_trim_pitch_inc        = 46,           ///< increase pitch trim
        k_trim_pitch_dec        = 47,           ///< decrease pitch trim
        k_input_hold_toggle     = 48,           ///< toggle input hold (trim to current controls)
        k_roll_pitch_toggle     = 49,           ///< adjust roll/pitch input instead of forward/lateral

        // 50 reserved for future function

        k_relay_1_on            = 51,           ///< trigger relay on
        k_relay_1_off           = 52,           ///< trigger relay off
        k_relay_1_toggle        = 53,           ///< trigger relay toggle
        k_relay_2_on            = 54,           ///< trigger relay on
        k_relay_2_off           = 55,           ///< trigger relay off
        k_relay_2_toggle        = 56,           ///< trigger relay toggle

### Servo

#### increase

Increase servo output by 50 pwm.

#### decrease

Decrease servo output by 50 pwm.

#### min

Set servo output to the configured minimum pwm according to SERVO**N**_MIN.

#### max

Set servo output to the configured maximum pwm according to SERVO**N**_MAX

#### center

Set servo output to the configured center according to SERVO**N**_TRIM

### Custom

These are reserved for developer use, and do not do anything by default.

## Internal Temperature

This is triggered when the internal temperature of the water tight enclosure (WTE) exceeds the threshold set in the FS_TEMP_MAX parameter.

## Leak

This is triggered when a configured *Leak Detector* detects a leak.

## Ground Control Station HEARTBEAT

Triggered when a heartbeat from the ground control station hasn't been received for more than 

## Pilot Input (ArduSub 3.5 and later)

Triggered when pilot manual control input has not been received since the amount of time specified by the FS_PILOT_TIMEOUT parameter.

## Sensors (ArduSub 3.5 and later)

Triggered when a sensor failure prevents the current flight mode to proceed. The autopilot will switch into *MANUAL* mode when triggered. This failsafe is not configurable.

## Battery (ArduSub 3.5 and later)

Triggered when the battery voltage drops below XXX or the remaining capacity drops below xxx.

## EKF (ArduSub 3.5 and later)


## Crash (ArduSub 3.5 and later)


<p style="font-size:10px; text-align:center">
Sponsored by <a href="http://www.bluerobotics.com/">Blue Robotics</a>. Code released under the <a href="https://github.com/bluerobotics/ardusub/blob/master/COPYING.txt">GPLv3 License</a>. Documentation released under the <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC-NC-SA 4.0</a>.<br />
<a href="https://github.com/bluerobotics/ardusub-docs/issues/">Submit a Documentation GitHub Issue here</a> to report any errors, suggestions, or missing information in this documentation.<br />
<a href="https://github.com/bluerobotics/ardusub/issues/">Submit an ArduSub GitHub Issue here</a> to report issues with the ArduSub software.
</p>