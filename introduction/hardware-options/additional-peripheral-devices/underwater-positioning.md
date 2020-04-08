# Underwater Positioning and GPS

A positioning system is a useful addition to an ArduSub vehicle either for displaying numerical location coordinates or the position of the vehicle on a map in QGroundControl. 

> **Note** The [autopilot]() has the capability of utilizing an external positioning system to perform autonomous maneuvers like station keeping, 'click to go here', transects, and pre-planned waypoint missions, however this is IN DEVELOPMENT. The position-enabled flight modes are considered stable and **do not work** as of the latest firmware release. This page will be updated when functionality is added.

## GPS Module

ArduSub maintains the same [GPS module drivers](https://ardupilot.org/copter/docs/common-positioning-landing-page.html) as the rest of the ArduPilot family of firmwares, so a compatible GPS module may be directly connected to the GPS port on the autopilot. Positioning information will only be available when the vehicle is on the surface and the module is out of the water. The module will not be able to obtain a fix if it is underwater due to high frequency radio waves unable to penetrate the water medium.

Acoustic positioning systems are the only reliable way of providing positioning information underwater.

# SBL Positioning Systems

A short baseline acoustic positioning system 

<iframe width="300" height="225" src="https://www.youtube.com/embed/NpAClMNhno0" frameborder="0" allowfullscreen></iframe>

## Supported SBL Systems

* [Water Linked Underwater GPS Explorer Kit](https://waterlinked.com/underwater-gps/)

# USBL Positioning Systems
