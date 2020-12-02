# DVL integration (BETA)

The DVL integration with ArduSub is in a BETA stage and is currently unsupported for normal use. This document is provided to instruct beta testers and developers how to test the BETA stage integration. There is no guarantee that the DVL integration will work for any particular application.

## Supported DVLs

The Waterlinked A50 DVL (link) is the only supported DVL at the moment in the beta integration.

### A50 DVL configuration

needs to be on ethernet, anything else..

## Companion Software

A beta version of the companion software is required to use the DVL integration.

### Installing beta companion software

(pictures)

### DVL configuration in Companion

(pictures)

## ArduSub Firmware

The DVL data is sent by the VISUAL_ODOMETRY mavlink message. This message is supported in ArduSub 4.1-beta and onward. The ArduSub 4.1-beta firmware is recommended for testing with DVL.

## Installing the ArduSub beta firmware

Click 'beta' under the update pixhawk section in the system page. (link, picture)

## PIDs and Other Important Parameters

These parameters must be configured to the recommended values for DVL integration to perform correctly:

SR0_Protocol

others....
