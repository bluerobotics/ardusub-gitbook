# Grippers and Manipulators

A gripper is a useful tool for picking up small objects, attaching recovery lines, or freeing a snagged tether.

Ardusub has the ability to natively control grippers through assigning joystick buttons and servo outputs for grippers that use Pulse Width Modulation (PWM) for control.

Other grippers often have their own control software and interface for assigning control functions. In this case, it is recommended to use Grippers for RS485 for control as they can use a spare twisted wire pair in the tether for data transmission instead of needing to write custom software for the [Companion Computer]().

# Supported Grippers and Manipulators

* [Blue Robotics Newton Subsea Gripper](https://bluerobotics.com/store/rov/bluerov2-accessories/newton-gripper-asm-r1-rp/) (Through autopilot PWM output)
* [Blueprint Lab Series Grippers](https://blueprintlab.com/products/rotating-grabber/) (RS485 through the tether)
