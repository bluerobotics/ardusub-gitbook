# Electronic Speed Controls (ESCs)

ArduSub is designed to work with brushless and brushed Electronic Speed Controls (ESCs) to control motors and thrusters. A corresponding ESC will need to be used for a similar motor type. For example if a brushless thruster is used, then a brushless ESC will be needed.

ArduPilot does not currently support controlling both brushed and brushless motors at the same time.

The minumim requirements for an ESC of either type are:

* Bi-directional control - they operate in forward and reverse (most ESCS for UAVs and hobby drones only operate in one direction)
* Controlled by a PWM input where:
    * 1900 us is full forward
    * 1500 us is stopped
    * 1100 us is full reverse

# Brushless ESCs

/images/introduction/hardware/hardware-besc.png

The following brushless ESCs are supported for use with ArduSub:

* [Blue Robotics Basic ESC](https://bluerobotics.com/store/thrusters/speed-controllers/besc30-r3/)

# Brushed ESCs

The following brushed ESCs are supported for use with ArduSub:
