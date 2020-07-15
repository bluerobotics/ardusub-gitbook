# ArduSub Autopilot Firmware

The ArduSub firmware is a binary file that is loaded on to the internal memory of a compatible [autopilot](/introduction/hardware-options/required-hardware/autopilot.md) board. The firmware contains the necessary logic processes to control the specified vehicle type, Sub in this case. Some autopilots (eg. Pixhawk) have an SD card that is used to store data logs. Note that the autopilot firmware is NOT located on the SD card.

No software programming is required to operate ArduSub, settings are changed through user configurable parameters when connected to [QGroundControl](/introduction/required-software/qgroundcontrol-software.md).

<img src="/images/software/ardusub.png" class="img-responsive img-center" style="max-height:600px;">

The [ArduPilot project](https://ardupilot.org/) supports multiple vehicle types, and each one has it's own firmware file. You must make sure that you have programmed the autopilot with the *ArduSub* firmware to use ArduSub. The other vehicle firmware types of the ArduPilot family are:
* [ArduCopter](https://ardupilot.org/copter/index.html)
* [ArduPlane](https://ardupilot.org/plane/index.html)
* [ArduRover](https://ardupilot.org/rover/index.html) (also for boats!)

## Versioning

There are three versions of ArduSub firmware:

* Stable (4.0.X): The recommended build for most users. The versions for these builds are do not have a suffix, just a number.
* Beta (4.0.X-beta): The most recent beta release, this is for users who wish to help test new features before they go into a stable release. The versions for these builds are suffixed with -beta.
* Development (4.1.X-dev): Development build, updated frequently. This build should only be used in practice by developers and advanced users. The versions for these builds are suffixed with -dev.

Precompiled ArduSub binaries are available [here](https://firmware.ardupilot.org/Sub/). 

> **Note** Binaries are provided for many different autopilot boards, but only the Pixhawk 1 (PX4-v2) is thoroughly tested and supported. More information on the binary file types can be found [here](https://ardupilot.org/dev/docs/pre-built-binaries.html).

## What Version is Installed?

To find out what firmware version is installed on your autopilot, navigate to the _Vehicle Setup_ view and then the _Summary_ tab. The firmware version will be listed under the Frame section.

<img src="/images/software/ardusub-version.png" class="img-responsive img-center" style="max-height:600px;">

## Release History

ArduSub release history is available [here](https://raw.githubusercontent.com/ArduPilot/ardupilot/master/ArduSub/ReleaseNotes.txt).
