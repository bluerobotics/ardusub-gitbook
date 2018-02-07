---
layout: default
title: "Logging"
permalink: /logging/
nav:
- Logging: logging
---

# Logging

There are two types of logs that can be used to diagnose problems while running ArduSub, or to retrieve data for post-processing.

## Telemetry logs

Telemetry logs store received MAVLink messages. MAVProxy and QGroundControl save telemetry logs locally in a **.tlog** file. Telemetry logs are the preferred way of diagnosing most problems.

Once connected to the autopilot, MAVProxy will save all telemetry to a file called 'mav.tlog'. The mav.tlog file is saved under the same path from which MAVProxy was run. By default, QGroundControl only begins logging telemetry after the vehicle has been armed. QGroundControl can be configured to log telemetry while the autopilot is disarmed by clicking the 'Q' icon in the menu bar, then selecting the 'General' tab. Select the option to save logs 'even if vehicle was not armed' in order to log telemetry while disarmed. In order to save a telemetry log from QGroundControl, you *MUST* click save when prompted after disconnecting from the vehicle, or after quitting the application. *Note* recent versions of QGroundControl allow you to configure a directory to automatically save all telemetry logs, these versions will not prompt to save.

<img src="/images/log-disarmed-qgc.png" class="img-responsive img-center" style="max-height:400px;">

## DataFlash logs

DataFlash logs are saved by the Autopilot directly to on-board memory (SD card in the case of the Pixhawk), regardless of a telemetry connection. These logs are saved in a **.bin** file. DataFlash logs are capable of logging data at a much faster rate than telemetry logs. The DataFlash logs are named and saved in ascending order. If GPS is available, the logs will be dated according to the GPS timestamp. DataFlash log files can be opened and inspected with MAVProxy, APM Planner 2 or Mission Planner.

By default, a new dataflah log file is created when the vehicle is initially armed, and logging is performed only while the vehicle is armed. The *LOG_DISARMED* parameter can be set to 'Enabled' in order to begin a DataFlash log as soon as the autopilot is booted, even before arming. With *LOG_DISARMED* enabled, logging will be performed whether the vehicle is armed or disarmed, until the vehicle is powered down.

<img src="/images/log-disarmed.png" class="img-responsive img-center" style="max-height:400px;">

## Downloading

DataFlash logs can be retrieved in two ways:

1. Remove the Micro SD card from the Pixhawk and plug it into your computer to view and transfer the logs using a file explorer like a regular USB drive.

2. Download the logs remotely via QGroundControl or MAVProxy.

	- Log downloading via QGroundControl

		Click the Analyze icon at the top of the window. The icon looks like a magnifying glass over a document.

		Click the 'Refresh' button to view available logs.

		Select the log you would like to download, and click 'Download'.

		Multiple logs can be downloaded by highlighting the desired logs before clicking 'Download'.

		<img src="/images/log-download.png" class="img-responsive img-center" style="max-height:400px;">

	- Log downloading via MAVProxy

		While connected to the autopilot via MAVProxy, type 'log list' in the MAVProxy console to list the available DataFlash logs onboard the autopilot.

		Type 'log download X' to download log number X

		While the log is downloading, you can type 'log status' to view the status of the download, or 'log cancel' to cancel the download.
		
<p style="font-size:10px; text-align:center">
Sponsored by <a href="http://www.bluerobotics.com/">Blue Robotics</a>. Code released under the <a href="https://github.com/bluerobotics/ardusub/blob/master/COPYING.txt">GPLv3 License</a>. Documentation released under the <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC-NC-SA 4.0</a>.<br />
<a href="https://github.com/bluerobotics/ardusub-docs/issues/">Submit a Documentation GitHub Issue here</a> to report any errors, suggestions, or missing information in this documentation.<br />
<a href="https://github.com/bluerobotics/ardusub/issues/">Submit an ArduSub GitHub Issue here</a> to report issues with the ArduSub software.
</p>
