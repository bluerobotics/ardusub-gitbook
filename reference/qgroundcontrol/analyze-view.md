{% include "../../archive-notice.html" %}

# Analyze View

## Log Download Page

The Log Download page  is used to manage dataflash log files from the connected vehicle. These vehicle log files are stored on the SD card inserted in the autopilot.

<img src="/images/reference/reference-qgc-analyze-log-download.png" class="img-responsive img-center" style="max-height:600px;">

Available actions:

* **Refresh**: Retrieve the list of available vehicle dataflash logs on the vehicle.
* **Download**: Download the selected log file. May take a few minutes if it is a large file.
* **Erase All**: Erases all log files on the vehicle.
* **Cancel**: Cancels log file download.

## Geotag Images [Does not work for Ardusub]

This feature is not available for ArduSub, PX4 only.

## Mavlink Console [Does not work for ArduSub]

This feature is not available for ArduSub, PX4 only.

## Mavlink Inspector

The MAVLink Inspector provides real-time information and charting of MAVLink traffic received by QGroundControl.

> **Note** This feature is intended primarily for **autopilot developers/vehicle creators**. Additional information on its use can be found [here](https://docs.qgroundcontrol.com/en/analyze_view/mavlink_inspector.html).

<img src="/images/reference/reference-qgc-analyze-mavlink-inspector.png" class="img-responsive img-center" style="max-height:600px;">
