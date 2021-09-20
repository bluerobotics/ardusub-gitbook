* [Autopilot](/introduction/hardware-options/required-hardware/autopilot.md): The autopilot board/flight controller board processes the pilot input and sensor data, and controls the motors, lights, servos, and relays on the vehicle. It runs the [ArduSub firmware](/introduction/required-software/ardusub-autopilot-firmware.md).

* [Companion Computer](/introduction/hardware-options/required-hardware/companion-computer.md): The Companion Computer streams video to the [Topside Computer](/introduction/hardware-options/required-hardware/topside-computer.md), and relays [MAVLink](https://ardupilot.org/dev/docs/mavlink-basics.html) communications between the autopilot and the Topside Computer via Ethernet.

* [Topside Computer](/introduction/hardware-options/required-hardware/topside-computer.md): The topside computer is where the live video feed and telemetry information are received and displayed. It accepts operator input from a joystick to allow controlling the connected vehicle.

* [Joystick](/introduction/hardware-options/required-hardware/joystick.md): A joystick allows the operator to control the vehicle, using stick control movements and button presses.

* [Camera](/introduction/hardware-options/required-hardware/camera.md): The camera allows the pilot to see and record from the vehicle's point of view. If paired with a [Camera Tilt Mount](/introduction/hardware-options/recommended-extras/camera-gimbal.md) or other gimbal it can be moved during operation.

* [Electronic Speed Controls (ESCs)](/introduction/hardware-options/required-hardware/escs.md): ESCs are used to control the speed/thrust of motors and [thrusters](/introduction/hardware-options/required-hardware/thrusters.md).

* [Thrusters](/introduction/hardware-options/required-hardware/thrusters.md): Thrusters are necessary to maneuver an underwater vehicle around. The number and orientation of thrusters on a vehicle determines the number of degrees of freedom (DoF) it may maneuver in.

* [Power Sensing Module](/introduction/hardware-options/required-hardware/power-sensing-module.md): A power sensing module provides analog current and voltage sensing to an autopilot onboard the vehicle. It's used to measure battery level, and how much power the vehicle is using.

* [Power Supply](/introduction/hardware-options/required-hardware/power-supply.md): The power supply and distribution system powers all the onboard electronics, including the high current draw of the thrusters. A regulator converts the main supplied power (from a battery or otherwise) into appropriate voltages for the more sensitive electronics - it must ensure a steady supply to avoid the computers restarting and losing control of the vehicle.

* [Tether](/introduction/hardware-options/required-hardware/tether.md): A tether is a length of cable which connects the Companion Computer to the Topside Computer. It allows low latency high-bandwidth communication to a vehicle in water, which other technologies are poorly suited to.
