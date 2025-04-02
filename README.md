# ⚠️  ARCHIVE NOTICE ⚠️

This documentation is being split up, and transferred to other sites:

- ArduSub is being moved to the [ArduPilot wiki](https://ardupilot.org/sub) ([GitHub](https://github.com/ArduPilot/ardupilot_wiki/tree/master/sub))
- The Blue Robotics Companion Software has been replaced by [BlueOS](https://blueos.cloud/docs) ([GitHub](https://github.com/bluerobotics/BlueOS-docs))
- Control Station Software (GCS) documentation can be found at
    - [QGroundControl](https://docs.qgroundcontrol.com/Stable_V4.3/en/qgc-user-guide/) ([GitHub](https://github.com/mavlink/qgroundcontrol/tree/master/docs))
    - [Cockpit](https://blueos.cloud/cockpit/docs/) ([GitHub](https://github.com/bluerobotics/Cockpit-docs))

---

# Overview

> **Note** The information in this guide applies to ArduSub V3.5 and up. If you are running an older version, you should [update](/quick-start/installing-ardusub.md).

## ArduSub and the ArduPilot Project

The ArduSub project is a fully-featured open-source solution for remotely operated underwater vehicles (ROVs) and autonomous underwater vehicles (AUVs). ArduSub is a part of the [ArduPilot project](http://ardupilot.org/), and was originally derived from the ArduCopter code. ArduSub has extensive capabilities out of the box including feedback stability control, depth and heading hold, and autonomous navigation.

ArduSub is designed to be safe, feature-rich, open-ended, and easy to use even for novice users.

ArduSub works seamlessly with Ground Control Station software that can monitor vehicle telemetry and perform powerful mission planning activities. It also benefits from other parts of the ArduPilot platform, including simulators, log analysis tools, and higher level APIs for vehicle management and control.

ArduSub is on the leading edge of marine robotics and intended for anyone who wants to operate a vehicle below the water's surface. There is support for many different ROV configurations, and adding a custom design is simple.

## About this Book

This book is an on-going work in progress to document the ArduSub software as well as supporting software and hardware. The documentation in this book is based on the most recent software available at the time of writing. In some cases, features or options documented here may be only available in developmental versions of the software. The authoring of this book and the ArduSub project are sponsored by [Blue Robotics](https://bluerobotics.com).

## License

- The ArduSub and ArduPilot code are released under the [GPLv3](https://raw.githubusercontent.com/ArduPilot/ardupilot/master/COPYING.txt) License.
- This book is released under the [CC-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) License.
