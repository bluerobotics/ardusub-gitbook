{% include "../../../archive-notice.html" %}

# Grippers and Manipulators

A gripper is a useful tool for picking up small objects, attaching recovery lines, or freeing a snagged tether. Other manipulators may be useful in cleaning, inspection, or repair tasks.

Ardusub has the ability to natively control grippers through assigning joystick buttons and servo outputs for grippers that use Pulse Width Modulation (PWM) for control.

Other grippers often have their own control software and interface for assigning control functions. In this case, it is recommended to use grippers with RS485 for control (instead of RS232) as they can use a spare twisted wire pair in the tether for data transmission instead of needing to write custom software for the [Companion Computer](/introduction/hardware-options/required-hardware/companion-computer.md).

# Supported Grippers and Manipulators

<img src="/images/hardware/gripper.jpg" class="img-responsive img-center" style="max-height:600px;">

The following grippers have been used on ArduSub vehicles:

* [Blue Robotics Newton Subsea Gripper](https://bluerobotics.com/store/rov/bluerov2-accessories/newton-gripper-asm-r2-rp/) (PWM output from autopilot)
* [Blueprint Lab Series Grippers](https://blueprintlab.com/products/grabbers/) (RS485 through the tether)
