# Thrusters

Thrusters are necessary to maneuver an underwater vehicle around. The number and orientation of thrusters on a vehicle determines the number of degrees of freedom (DoF) a vehicle may maneuver in.

The maximum current draw of the power supply on the vehicle is an  important consideration when choosing what type and how many thrusters to mount on a vehicle. The maximum current draw at the intended voltage should be totaled up for all the thrusters. If this exceeds the current rating of the power supply, either lower the supply voltage or remove thrusters.

Although brushless or brushed thrusters may be used with ArduSub, they may not be mixed, and the thruster type needs to be paired to an appropriate [Electronic Speed Control (ESC)](/introduction/hardware-options/required-hardware/escs.md).

# Brushless Thrusters

Brushless thrusters are a good choice for propulsion as they do not have brushes that must be protected and wear out. 

## Recommended Brushless Thrusters

<img src="/images/introduction/hardware/hardware-t200.jpg" class="img-responsive img-center" style="max-height:600px;">

The following brushless thrusters have been test and recommended for use:

* [Blue Robotics T200 Thruster](https://bluerobotics.com/store/thrusters/t100-t200-thrusters/t200-thruster/)

# Brushed Thrusters

Brushed thrusters are generally cheaper than brushless types, but must be internally sealed with either an oil compensating system or have shaft seals.

Partially disasembled bilge pump motors with propellers have been used in the past for a shallow water sealed thruster unit.

Brushed thrusters must use an appropriate [brushed ESC](/introduction/hardware-options/required-hardware/escs.md#brushed-escs).
