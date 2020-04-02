# Tether

A tether is a length of cable which connects the [Companion Computer]() to the [Topside Computer](). Radio frequency (RF) waves don’t travel far through water and acoustic modems have limited bandwidth, so a tether is a critical component to connect the vehicle to a surface computer.

# Requirments

The Companion Computer communicates by 10/100 Base Ethernet. Therefore, a standard [Cat 5 cable](https://en.wikipedia.org/wiki/Category_5_cable) may be used to connect to the vehicle and topside computer. The maximum transmission length of Cat5 cable is around 100m.

# Tether Interfaces

Although optional and not necessary for basic functionality, tether interfaces increase the **range** and **reliability** of Ethernet communications.

## Interfaces for Copper Twisted Wire Pairs


Interface boards which use the [Homeplug AV](https://en.wikipedia.org/wiki/HomePlug#HomePlug_AV) standard provide a robust high-speed, long-distance Ethernet connection over a single pair of wires. These boards enable HD video and high-bandwidth data over 300m+ tether lengths.

The following interface boards are supported:
* [Blue Robotics Fathom-X Tether Interface Board Set](https://bluerobotics.com/store/comm-control-power/tether-interface/fathom-x-r1/)
* [Blue Link Dual Ethernet Plus Serial Multiplexer (DEPS MUX)](https://blue-linked.com/bluerov2-store/ols/products/deps-mux)

## Interfaces for Fiber Optic Cable
