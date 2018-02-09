# GPS Positioning

The ROV autopilot is capable of utilizing an external positioning system to perform autonomous maneuvers like station keeping, 'click to go here', transects, and pre-planned waypoint missions. All GPS/positioning functionality in ArduSub is IN DEVELOPMENT. The [position-enabled](operators-manual/flight-modes.html#position-enabled-modes) flight modes are not considered stable. However, a positioning system may be integrated in order to display the position of the vehicle on the Ground Control Station map. This can be done without making use of the position-enabled flight modes, and this sort of operation is considered stable.

## Forwarding NMEA data to companion

 The first step to using ArduSub with a positioning system is to get the positioning system data into the autopilot. The Companion computer in the ROV listens for NMEA data on udp port 27000. You can forward NMEA data to this port, and the ROV will automatically use that for it's gps position. The NMEA data can come from a USBL or other positioning system, or from an application that is synthesizing a GPS position using computer vision, motion capture, or other means. A useful application for bridging NMEA data between a COM port on the surface computer and the udp port on the ROV is the [NMEA Router](http://arundale.com/docs/ais/nmearouter.html) by Neal Arundale.

The positioning system must report the number of satellites, and the satellites must be greater than 6 for the autopilot to accept the position as a valid lock. When a valid position and lock is detected by the autopilot, the main LED on the autopilot will change from blue to green.

On a pi terminal, enter the command `screen -r nmearx` to see if the data is correctly making it's way into the ROV system. Enter `ctrl+A`, then `d` to 'detach' from the screen and return to the pi terminal.

## Autopilot configuration

There is some configuration that needs to be done on the autopilot in order for the absolute positioning to perform correctly. These parameters need to be set:
- GPS_TYPE = MAV(14) (This is done automatically by the same application that listens for data on port 27000)
- EK2_GPS_TYPE = 2D Position(2) (We don't want to use the 3D position, we get very good depth measurements from the pressure sensor)

The Autopilot and the positioning system need to agree on where North is. Turn the vehicle until the autopilot indicates that it is facing north, and check that the positioning system reports the same heading. If the positioning system does not provide a heading estimate for the vehicle, move the vehicle forward towards North, and make sure that the positioning system reflects this accurately.

If the two systems do not agree on North:
- Calibrate the compass on the autopilot
- Verify the magnetic heading of the autopilot, change the [COMPASS_DEC](operators-manual/full-parameter-list.html#compassdec-compass-declination) parameter if neccessary
- Offset the positioning system heading to match the autopilot heading. If this is not possible offset the autopilot heading with the COMPASS_DEC parameter to match the positioning system heading

The autopilot navigation filter needs to be tuned to the characteristics of the positioning system. Many factors can affect the tuning requirements including: Accuracy/precision of the positioning system, position update frequency, position update delay behind inertial measurements, etc. The navigation filter parameters can be found [here](operators-manual/full-parameter-list.html#ek2-parameters).

If the position-enabled flight modes are to be used, the autopilot position controller needs to be tuned. In QGC, check the 'Show advanced settings' option in the _General_ tab of the _Application Setup_ menu, and restart the application. There will be a _Tuning_ tab on the _Vehicle Setup_ page that can be used to facilitate tuning the position controller. The parameters of interest are those with 'XY' in the name in the 'Position Controller' section.

<p style="font-size:10px; text-align:center">
Sponsored by <a href="http://www.bluerobotics.com/">Blue Robotics</a>. Code released under the <a href="https://github.com/bluerobotics/ardusub/blob/master/COPYING.txt">GPLv3 License</a>. Documentation released under the <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC-NC-SA 4.0</a>.<br />
<a href="https://github.com/bluerobotics/ardusub-docs/issues/">Submit a Documentation GitHub Issue here</a> to report any errors, suggestions, or missing information in this documentation.<br />
<a href="https://github.com/bluerobotics/ardusub/issues/">Submit an ArduSub GitHub Issue here</a> to report issues with the ArduSub software.
</p>
