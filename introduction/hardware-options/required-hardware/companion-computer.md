# Companion Computer

Companion Computers are usually small single board computers (SBCs) which can be connected to an autopilot board and communicate using the [MAVLink protocol](https://ardupilot.org/dev/docs/mavlink-basics.html). A Companion Computer will take in MAVLink telemetry from the [autopilot](/introduction/hardware-options/required-hardware/autopilot.md) and can route or process the telemetry data. 

The Companion Computer has two major functions within the ArduSub control system:

* Streaming HD video to the [Topside Computer](/introduction/hardware-options/required-hardware/topside-computer.md)
* Relaying communications between the autopilot and the Topside Computer via Ethernet communications

The Companion Computer must be running the [ArduSub Companion Computer Software](https://github.com/bluerobotics/companion) to function correctly with ArduSub. 

# Supported Hardware

Only the [Raspberry Pi 3 Model B](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/) is supported for use with the Companion Computer Software.

<img src="/images/hardware/RPi3B.png" class="img-responsive img-center" style="max-height:600px;">

# Unsupported Hardware

The following single board computers are <b>not</b> supported with the current ArduSub Companion software image:

* Raspberry Pi Zero
* Raspberry Pi Zero W
* Raspberry Pi 1 Model B+
* Raspberry Pi 1 Model A+
* Raspberry Pi 2 Model B
* Raspberry Pi 3 Model B+
* Raspberry Pi 3 Model A+
* Raspberry Pi 4 Model B
* Any other SBC

# References

The ArduPilot documentation has more reading material about Companion Computers, but those software images are not compatible with the ArduSub system.

* [ArduPilot: Companion Computers](https://ardupilot.org/dev/docs/companion-computers.html)
