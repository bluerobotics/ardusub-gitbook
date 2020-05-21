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

## Mavlink Console [Does not work for ArduSub]

## Mavlink Inspector

The MAVLink Inspector provides real-time information and charting of MAVLink traffic received by QGroundControl.

The inspector lists all received messages for the current vehicle, along with their source component id and update frequency. You can drill down into individual messages to get the message id, source component id, and the values of all the individual fields. You can also chart field values in real time, selecting multiple fields from multiple messages to display on one of two charts.

To use the MAVLink Inspector:
Select Analyze | MAVLink Inspector.
The view will start populating with messages as they are received.
Select a message to see its fields and their (dynamically updating) value:
Add fields to charts by enabling the adjacent checkboxes (plot 1 is displayed below plot 2).
Fields can be added to only one chart.
A chart can have multiple fields, and fields from multiple messages (these are listed above each chart). Messages containing fields that are being charted are highlighted with an asterisk.
The Scale and Range are set to sensible values, but can be modified if needed.
