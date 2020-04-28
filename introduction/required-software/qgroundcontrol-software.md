# QGroundControl Software


QGroundControl is the Graphical User Interface (GUI) which provides control and setup functionality for PX4 or ArduPilot powered vehicles. It provides easy and straightforward usage for beginners, while still delivering high end feature support for experienced users.
Key Features:
Full setup/configuration of ArduPilot and PX4 Pro powered vehicles.
Flight support for vehicles running PX4 and ArduPilot (or any other autopilot that communicates using the MAVLink protocol).
Mission planning for autonomous flight.
Flight map display showing vehicle position, flight track, waypoints and vehicle instruments.
Video streaming with instrument display overlays.
Support for managing multiple vehicles.
QGC runs on Windows, OS X, Linux platforms, iOS and Android devices.

QGC is designed to provide a single codebase that can run across multiple OS platforms as well as multiple device sizes and styles.

The QGC user interface is implemented using [Qt QML](http://doc.qt.io/qt-5/qtqml-index.html). QML provides for hardware acceleration which is a key feature on lower powered devices such as tablets or phones. QML also provides features which allows us to more easily create a single user interface which can adapt itself to differing screen sizes and resolution.


## Versioning

There are two versions of QGroundControl software:

* Stable (4.0.X): The recommended build for most users.
* Daily (Development HEAD | Git Revision | Date | Time): Development build, updated frequently. These builds are for development purposes only and not recommended for regular use.

## What Version is Installed?

To find out what firmware version is installed on your autopilot, navigate to the Summary tab of the Vehicle Setup page. The firmware version will be listed under the Frame section.

## Release History

QGroundControl release history is available [here](https://docs.qgroundcontrol.com/en/releases/release_notes.html).
