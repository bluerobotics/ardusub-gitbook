# Power Sensing Module

A power sensing module provides analog current and voltage sensing to an autopilot onboard the vehicle. ArduSub supports various modules in the firmware and when properly set, QGroundControl will give visual indications of battery level and current consumption.

# Recommended Power Sensing Modules

<img src="/images/introduction/hardware/hardware-psm.png" class="img-responsive img-center" style="max-height:600px;">

The following power sensing modules have been tested and recommended for use:

* [Blue Robotics Power Sense Module](https://bluerobotics.com/store/comm-control-power/elec-packages/psm-asm-r2-rp/)
    * Does not provide power to the autopilot, voltage and current sensing only.
* [Mauch HS Series Power Module](https://www.mauch-electronic.com/hs-sensor-product)
    * Requires an additional [4-14S Hybrid BEC](https://www.mauch-electronic.com/4-14s-hyb-bec) to power the board.
    
# Not Recommended Power Sensing Modules

The following modules have been tested ant **not** recommended for use:

* [mRobotics Classic Power Module (BEC) 4S LIPOs](https://store.mrobotics.io/product-p/classic-bec10-mr.htm)
    * Issue: For unknown reasons, will short circuit and send 12V to the autopilot, damaging both the power module and autopilot.

# Other Power Sensing Modules

ArduPilot has a list of other power sensing modules, but these have not been tested or verified:

* [Battery Monitors (aka Power Monitors/Modules)](https://ardupilot.org/copter/docs/common-powermodule-landingpage.html)
