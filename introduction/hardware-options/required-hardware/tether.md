# Tether

A tether is a length of cable which connects the [Companion Computer](/introduction/hardware-options/required-hardware/companion-computer.md) to the [Topside Computer](/introduction/hardware-options/required-hardware/topside-computer.md). Radio frequency (RF) waves do not travel far through water and acoustic modems have limited bandwidth, so a tether is a critical component to connect the vehicle to a surface computer.

# Requirements

The Companion Computer communicates by 10/100 Base Ethernet. Therefore, a standard [Cat 5 cable](https://en.wikipedia.org/wiki/Category_5_cable) may be used to connect to the vehicle and topside computer. The maximum transmission length of Cat5 cable is around 100m.

<img src="/images/hardware/tether.png" class="img-responsive img-center" style="max-height:600px;">

# Tether Interfaces

Although optional and not necessary for basic functionality, tether interfaces increase the **range** and **reliability** of Ethernet communications.

## Interfaces for Copper Twisted Wire Pairs

Interface boards which use the [Homeplug AV](https://en.wikipedia.org/wiki/HomePlug#HomePlug_AV) standard provide a robust high-speed, long-distance Ethernet connection over a single pair of wires. These boards enable HD video and high-bandwidth data over 300m+ tether lengths.

<img src="/images/hardware/fathomx.png" class="img-responsive img-center" style="max-height:600px;">

The following interface boards are supported:
* [Blue Robotics Fathom-X Tether Interface Board Set](https://bluerobotics.com/store/comm-control-power/tether-interface/fathom-x-r1/)

## Interfaces for Fiber Optic Cable

With communications being Ethernet based, fiber optic cables may also be used with Ethernet-to-Fiber converters installed inside the ROV and topside.

The following fiber optic interface boards have been known to work: 
* [DeltaROV Subsea Fiber to Ethernet Communication Kit](http://www.deltarov.com/new/product/drov-subsea-fiber-to-ethernet-communication-kit/)
