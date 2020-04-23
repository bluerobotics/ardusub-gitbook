# Underwater Positioning and GPS

A positioning system is a useful addition to an ArduSub vehicle either for displaying numerical location coordinates or the position of the vehicle on a map in QGroundControl. 

Below is an example of a Water Linked Underwater GPS System being used to locate a shipwreck:

<iframe width="300" height="225" src="https://www.youtube.com/embed/NpAClMNhno0" frameborder="0" allowfullscreen></iframe>

> **Note** The [autopilot]() has the capability of utilizing an external positioning system to perform autonomous maneuvers like station keeping, 'click to go here', transects, and pre-planned waypoint missions, however this is IN DEVELOPMENT. The position-enabled flight modes are considered stable and **do not work** as of the latest firmware release. This page will be updated when functionality is added.

## GPS Module

ArduSub maintains the same [GPS module drivers](https://ardupilot.org/copter/docs/common-positioning-landing-page.html) as the rest of the ArduPilot family of firmwares, so a compatible GPS module may be directly connected to the GPS port on the autopilot. Positioning information will only be available when the vehicle is on the surface and the module is out of the water. The module will not be able to obtain a fix if it is underwater due to high frequency radio waves unable to penetrate the water medium.

Acoustic positioning systems are the only reliable way of providing positioning information underwater.

# SBL Positioning Systems

A [short baseline (SBL) acoustic positioning system](https://en.wikipedia.org/wiki/Short_baseline_acoustic_positioning_system) uses an acoustic transmitter on the vehicle to transmit timed acoustic pulses. These pulses are received by a series of multiple receivers on the surface in an arraged geometric pattern. The "time of flight" is calculated to when each receiver records the acoustic pulse and then a consolidated position for the underwater vehicle can be plotted.

SBL systems can produce better positioning accuracy in highly reflective environments due to the adjustable receiver locations.

<img src="/images/introduction/hardware/hardware-SBL-WL.png" class="img-responsive img-center" style="max-height:600px;">

## Supported SBL Systems

* [Water Linked Underwater GPS Explorer Kit](https://waterlinked.com/underwater-gps/)

# USBL Positioning Systems

An [ultra-short baseline acoustic positioning system](https://en.wikipedia.org/wiki/Ultra-short_baseline) is similar to SBL system where and acoustic pulse is transmitted from a tranciever on the vehicle and then recieved by a receiver on the surface. Instead of simply calculating time of flight, range and bearing are calculated by USBLs.

USBLs are more compact than SBL systems where are the receivers transducers are fixed in one tranciever head.

<img src="/images/introduction/hardware/hardware-USBL-CS.png" class="img-responsive img-center" style="max-height:600px;">

## Supported USBL Systems

* [Cerulean Sonar ROV Locator](https://ceruleansonar.com/products/usbl-rov-locator?variant=16138964107330)
