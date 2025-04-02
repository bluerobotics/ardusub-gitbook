{% include "../archive-notice.html" %}

# Required Software

The ArduSub control system is made up of three major software components:

* [ArduSub Autopilot Firmware](/introduction/required-software/ardusub-autopilot-firmware.md): ArduSub firmware is the autopilot software responsible for processing pilot input and controlling the ROV. ArduSub is the 'brains' of the ROV.

* [Companion Computer Software](/introduction/required-software/companion-computer-software.md): Companion Computer software relays communications between the autopilot and QGroundControl via Ethernet communications. The Companion software also streams HD video to QGroundControl.

* [QGroundControl Software](/introduction/required-software/qgroundcontrol-software.md): QGroundControl is the user interface for operating the ROV.

Here is a diagram of what software piece is loaded onto which hardware component and their basic connections:

<img src="/images/software/overall.png" class="img-responsive img-center" style="max-height:600px;">

Here is a technical block diagram of the main software components and their interactions:

{% include "software-components-miro-board.md" %}
