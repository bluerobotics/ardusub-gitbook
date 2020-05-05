# Companion Computer Software

The Companion Computer software image is a modified version of [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) that is written onto a microSD card and installed in the [Companion Computer](/introduction/hardware-options/required-hardware/companion-computer.md). 

Companion software performs the following functions:
* Relays communications between the autopilot and QGroundControl via Ethernet communications
* Streams HD video to QGroundControl.
* Allows interfacing of additional peripherals (sensors and sonars) with compatible drivers.

<img src="/images/introduction/software/software-companion.png" class="img-responsive img-center" style="max-height:600px;">

## What Version is Installed?

To find out what software version is installed on a Companion Computer, open a web browser (Chrome, Firefox, Edge, etc) and navigate to [http://192.168.2.2:2770/](http://192.168.2.2:2770/). The software version will be listed in the top header section.

<img src="/images/introduction/software/software-companion-version.png" class="img-responsive img-center" style="max-height:600px;">

## Release History

Companion release history is available [here](https://github.com/bluerobotics/companion/blob/master/release-notes.txt).
