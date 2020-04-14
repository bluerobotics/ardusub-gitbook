# Sonars

# Echosounders and Altimeters 

A useful type of sonar is an echosounder, also known as an altimeter when installed on an underwater vehicle. An altimeter is a single-beam sonar which gets a range measurement from the bottom of the ROV to the seabed. This is useful in low visibility situations where the distance to the bottom is unknown.

In addition to getting a distance reading, echosounders can provide the full echo response (echo strength versus time) which can be plotted like the display of a fishfinder sonar. This is useful for locating targets or obstructions beneath the vehicle.

## Supported Echosounders/Altimeters

* [Blue Robotics Ping Sonar Altimeter and Echosounder](https://bluerobotics.com/store/sensors-sonars-cameras/sonar/ping-sonar-r2-rp/) (USB connection to Companion Computer)

# Scanning Imaging Sonars

Mechanically scanning sonars are useful tools for navigation, and acoustically imaging targets in a top-down 2-dimensional representation. If you are new to scanning sonars, Blue Robotics has written an introductory guide which illustrates the key concepts and can help with image recognition: [Understanding and Using Scanning Sonars](https://bluerobotics.com/learn/understanding-and-using-scanning-sonars/).

## Supported Scanning Sonars

Only the Blue Robotics Ping360 Scanning Sonar is fully integrated with the ArduSub system and has advanced features such as heading rotation and a direct connection to the Companion Computer.

* [Blue Robotics Ping360 Scanning Imaging Sonar](https://bluerobotics.com/store/sensors-sonars-cameras/sonar/ping360-sonar-r1-rp/) (USB or RS485: [Changing Communications Interface](https://bluerobotics.com/learn/changing-communications-interface-on-the-ping360/))

The following scanning sonars have been installed on ArduSub vehicles:
* [Tritech Micron Sonar](https://www.tritech.co.uk/product/small-rov-mechanical-sector-scanning-sonar-tritech-micron) (RS485 connection through tether)
* [Imagenex 852 Ultra-Miniature Imaging](https://imagenex.com/products/852-ultra-miniature-imaging) (RS485 connection through tether)

# Multibeam Sonars

Multibeam imaging sonars are similar to mechanically scanning sonars in that they acoustically image targets in a top-down 2-dimensional representation. However, with multiple sonar beams the refresh rate is much righer and presenting a real-time image of what is in front of the vehicle.

The following multibeam sonars have been installed on ArduSub vehicles:
 * [blueprint subsea Oculus Series Multibeam Sonars](https://www.blueprintsubsea.com/oculus/) (Ethernet)
 * [Tritech International Gemini 720im Multibeam Sonar](https://www.tritech.co.uk/product/gemini-720im) (Ethernet or RS485 connection through tether)
 * [Tritech International Gemini 720ik Multibeam Sonar](https://www.tritech.co.uk/product/gemini-720ik) (Ethernet)
 
 
# Profiling Sonars

Profiling sonars are 1-dimensional echosounders with a rotating head that are able to get accurate acoustic range data to create a "profile" of the surrounding environment. These types of sonars are useful for inspecting material buildup in pipes.

The following profiling sonars have been installed on ArduSub vehicles:
* [Imagenex 831L Pipe Profiling Sonar](https://imagenex.com/products/831l-pipe-profiling)
* [Imagenex 881A Profiling Sonar](https://imagenex.com/products/881a-profiling)
