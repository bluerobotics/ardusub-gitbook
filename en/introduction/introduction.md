# Introduction

ArduSub is an advanced open-source ROV/AUV control system.

## Overview

ArduSub is a complete open-source controller solution for subsea vehicles, offering both remotely operated control (via a number of intelligent dive modes) and execution of fully autonomous missions.

As part of the [DroneCode Software Platform](https://www.dronecode.org/dronecode-software-platform) it works seamlessly with Ground Control Station software that can monitor vehicle telemetry and perform powerful mission planning activities. It also benefits from other parts of the DroneCode platform, including simulators, log analysis tools, and higher level APIs for vehicle management and control.

ArduSub is on the cutting edge of marine robotics and intended for those people who want to try advanced technology, cutting edge software, and new capabilities. It can be used on many different types of subsea vehicles including several configurations of ROVs.

<img src="/images/ardusub-overview-diagram.png" class="img-responsive" />

## Key Features

- **Feedback control and stability:** Based on a multicopter autopilot system, the ArduSub controller has accurate feedback control to actively maintain orientation.
- **Depth hold:** Using pressure-based depth sensors, the ArduSub controller can maintain depth within a few centimeters.
- **Heading hold:** By default, the ArduSub automatically maintains its heading when not commanded to turn.
- **Camera Tilt:** Camera tilt control with servo or gimbal motors through the joystick or gamepad controller.
- **Light Control:** Control of subsea lighting through the joystick or gamepad controller.
- **No Programming Required:** The ArduSub controller works for a variety of ROV configurations without the need for any custom programming. Most parameters can be changed easily through the ground control station.

## What You'll Need

There are numerous potential combinations of hardware and vehicles compatible with the ArduSub controller. Here's a short summary list:

- [Supported ROV](#supported-frames) with thrusters and speed controllers
- Autopilot controller like the 3DR PixHawk
- Tether for communication via serial or Ethernet
- Laptop computer with QGroundControl installed
- USB gamepad or joystick controller ([example](http://www.amazon.com/Logitech-940-000110-Gamepad-F310/dp/B003VAHYQY))
- Pressure sensor for depth measurement ([example](https://www.bluerobotics.com/store/electronics/bar30-sensor-r1/))

### ROV

ArduSub is compatible with many different ROV frames. [Please see here](#supported-frames) for a list of actively supported frames.

### Hardware Controller

With [DroneCode](http://dronecode.org) compatibility, the ArduSub controller is usable with many different hardware options. It is primarily developed and supported on the **PixHawk** from 3D Robotics, but supports other hardware as well:

- **PixHawk** from 3D Robotics
- **PixRacer*** from AUAV
- **Navio+/Navio2** from Emlid
- **Erle Brain, PXFmini*** from Erle Robotics
- **BBBmini** shield for BeagleBone Black

*These options have 8 or less PWM outputs and may not support all ArduSub frame types

### Tether and Tether Interfaces

ArduSub is compatible with both serial and Ethernet based communication interfaces. The hardware autopilot used must support the option that you choose. The Pixhawk only supported a serial connection but can be connect to Ethernet through a companion computer. Other autopilots support Ethernet natively.

There are several available tether interface boards that work well with ArduSub:

* Blue Robotics *Fathom-S Tether Interface* provides analog video and a serial port for direct communication with the autopilot.
* Blue Robotics *Fathom-X Tether Interface* provides an Ethernet connection and requires a device with Ethernet support. 
* Direct Ethernet Connection can also be used and also requires a device with Ethernet support.

### Topside and Ground Control Station

The ArduSub software is designed primarily to interface through QGroundControl (QGC), an open-source, cross-platform user interface for drones of all types. The interface connects to the ArduSub controller through the tether and displays vehicle status information and allows parameters and settings to be updated.

Most importantly, QGC interfaces with the joystick or gamepad controller used to command the vehicle. It is compatible with most USB joysticks. There are several recommended joysticks:

- **Xbox 360 / Xbox One Controller** with wireless USB connection
- **Logitech 310** (wired) and **Logitech 710** (wireless) gamepads

If using an Ethernet-based tether option and computer-based autopilot, then streaming video can be displayed directly in QGC.

## Supported Frames

ArduSub includes a high-level motor library that can configure motors in any configuration. This library is used to implement a number of supported frame configurations. All configurations are shown from **top-down view**. Green thrusters indicate counter-clockwise propellers and blue thrusters indicate clockwise propellers (or vice-versa). Currently supported are:

<div class="row">
	<div class="col-md-4">
		<img src="/images/bluerov-frame.png" class="img-responsive img-center" style="max-height:250px;">
		<p class="text-center"><strong>BlueROV1 Configuration</strong> with 6-DOF thruster positioning. (Frame: <code>bluerov</code>)</p>
	</div>
	<div class="col-md-4">
		<img src="/images/vectored-frame.png" class="img-responsive img-center" style="max-height:250px;">
		<p class="text-center"><strong>Vectored ROV</strong> with side-by-side vertical thrusters. Used for the <a href="http://bluerov2.com"><em>BlueROV2</em></a>. (Frame: <code>vectored</code>)</p>
	</div>
	<div class="col-md-4">
		<img src="/images/vectored6dof-frame.png" class="img-responsive img-center" style="max-height:250px;">
		<p class="text-center"><strong>Vectored ROV w/ Four Vertical Thrusters</strong>, an 8-thruster configuration with 6-DOF control and heavy-lifting capacity. (Frame: <code>vectored6dof</code>)</p>
	</div>	
</div>

<div class="row">
	<div class="col-md-4">
		<img src="/images/simplerov-3.png" class="img-responsive img-center" style="max-height:250px;">
		<p class="text-center"><strong>ROV</strong> with a single vertical thruster. (Frame: <code>simplerov</code>)</p>
	</div>
	<div class="col-md-4">
		<img src="/images/simplerov-4.png" class="img-responsive img-center" style="max-height:250px;">
		<p class="text-center"><strong>ROV</strong> with side-by-side vertical thrusters. (Frame: <code>simplerov</code>)</p>
	</div>
</div>

As of ArduSub 3.5, the frame is configured at boot according to the FRAME_CONFIG parameter. Common frames can be selected using the Frame Setup menu in QGC (3.1 or later). Other frames (like custom) can be selected directly from the parameter editor. If you change your frame, you will need to reboot for changes to take effect.

[Please see here](/developers/#making-a-custom-configuration) if you would like to add your own configuration.

## Sensors and Actuators

In addition to the standard onboard sensors (IMU, compass), the ArduSub controller directly supports a number of external sensors including:

- Pressure/depth sensors for measurement and auto depth-hold ([example](https://www.bluerobotics.com/store/electronics/bar30-sensor-r1/))
- GPS for position at the surface (does not work underwater)

Other sensors, and in particular high-bandwidth and specialized sensors, are integrated as *Companion* sensors, attached to the companion computer and running alongside *ArduSub* and sharing communication pathways. This allows rapid integration of new and unique payloads and allows you to use the manufacturer's user interface to control the sensor.

Sensor integration is still in the early phase, but will eventually include sensors such as:

- Depth sounders
- Scanning sonars
- Conductivity sensors

The controller can command dimmable lights and can be configured to control standard servos as well for additional functionality.

## Applications

ArduSub provides the functionality needed for a wide variety of applications from simple observation-class ROVs to sophisticated research-class ROVs. Here's a short list of applications that ArduSub-powered ROVs can be used for:

- Observation and exploration
- Wreck discovery and documenting
- Photography and videography
- Boat and equipment inspection
- Biological sampling and surveying
- Underwater retrieval
- Academic and research projects
- ROV and AUV competitions

<p style="font-size:10px; text-align:center">
Sponsored by <a href="http://www.bluerobotics.com/">Blue Robotics</a>. Code released under the <a href="https://github.com/bluerobotics/ardusub/blob/master/COPYING.txt">GPLv3 License</a>. Documentation released under the <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC-NC-SA 4.0</a>.<br />
<a href="https://github.com/bluerobotics/ardusub-docs/issues/">Submit a Documentation GitHub Issue here</a> to report any errors, suggestions, or missing information in this documentation.<br />
<a href="https://github.com/bluerobotics/ardusub/issues/">Submit an ArduSub GitHub Issue here</a> to report issues with the ArduSub software.
</p>