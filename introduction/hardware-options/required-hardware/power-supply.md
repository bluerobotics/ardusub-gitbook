{% include "../../../archive-notice.html" %}

# Power Supply

A stable power supply and power distribution system is an integral part of any underwater vehicle. The power supply needs to be able to power all the onboard electronics and keep up with the current draw of the thrusters.

The working voltage is usually tied to the maximum voltage rating of the thrusters. Voltage regulators step down higher voltages into lower ones to power the electronics.

# Battery Power

For safety reasons, it is recommended to design an underwater vehicle to operate on battery power. Lithium type batteries are a popular choice due to their high storage capacity in a compact form factor. When selecting a battery for a new vehicle, here are a few important considerations:

- **Voltage:** Lithium batteries often specify their nominal pack voltage as well as a corresponding **"S"** rating indicating the number of 3.7V cells in wired in **S**eries inside the battery. The voltage of your battery needs to be matched to the ratings of your ESCs and thrusters.

    * For example, [Blue Robotics Basic ESCs](https://bluerobotics.com/store/thrusters/speed-controllers/besc30-r3/) support 2S through 6S (7-26V) batteries, however the [T200 Thruster](https://bluerobotics.com/store/thrusters/t100-t200-thrusters/t200-thruster-r2-rp/) is only rated for a maximum of 20V. Therefore, the the maximum recommended battery to use in this system is a 4S battery as a fully charged battery is 16.8V.

- **Capacity** Batteries usually specify their capacity in units of mAh, the larger this number, the more energy the battery will store, and the longer you can run your ROV.

- **Current Rating:** Batteries usually specify a **C** rating for **C**urrent. In order to calculate the rated current in Amps, multiply the capacity of the battery in Ah (mAh/1000) times the **C** rating. For example, a 10000 mAh (10 Ah) battery with a 10C rating is rated for 100 Amps. As a general rule of thumb, your battery should be rated for a continuous current draw of 15 Amps times the number of thrusters.

A battery will also need its own [watertight enclosure (WTE)](https://bluerobotics.com/product-category/watertight-enclosures/) unless space is allocated inside the main electronics enclosure.

<img src="/images/hardware/battery.jpg" class="img-responsive img-center" style="max-height:600px;">

These batteries are known to fit inside a 3" inner diameter (WTE):
* [Blue Robotics Lithium-ion Battery (14.8V, 18Ah)](https://bluerobotics.com/store/comm-control-power/powersupplies-batteries/battery-li-4s-18ah-r3/)
* [Blue Robotics Lithium-ion Battery (14.8V, 15.6Ah)](https://bluerobotics.com/store/comm-control-power/powersupplies-batteries/battery-li-4s-15-6ah/)
* [Turnigy Li-po (14.8V, 10Ah) (Hobby King)](https://hobbyking.com/en_us/turnigy-high-capacity-10000mah-4s-12c-multi-rotor-lipo-pack-w-xt90.html)



# Power Over Tether (High Voltage)

**With the inherent danger of high voltage around water, the ArduSub developers highly discourage users from making their own high voltage power supplies.**

If a power over tether solution is required, then Blue Robotics sells the [Outland Technology Power Supply (OTPS) for the BlueROV2](https://bluerobotics.com/store/comm-control-power/powersupplies-batteries/otps1kw/). Although the OTPS system was resigned to replace the battery enclosure on the BlueROV2, it can be adapted for other vehicle projects.

<img src="/images/hardware/otps.jpg" class="img-responsive img-center" style="max-height:600px;">

# Voltage Regulators

Depending on the electronics used, the primary voltage of the vehicle will most likely need to be stepped down and regulated more more sensitive electronics such as Companion Computers and autopilots. 

The following regulators have been tested to provide adequate power:

* [Blue Robotics 5V 6A Power Supply](https://bluerobotics.com/store/comm-control-power/elec-packages/bec-5v6a-r1/)
