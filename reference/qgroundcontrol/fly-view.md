{% include "../../archive-notice.html" %}

# Fly View

The Fly View is used to control and monitor the vehicle when diving.

You can use it to:
* Display video, telemetry, and other information for the current vehicle.
* Control the vehicle and accessories with a connected joystick.
* Switch between a video view and map view (if an underwater positioning system is used).

<img src="/images/reference/reference-qgc-fly-annotated.png" class="img-responsive img-center" style="max-height:600px;">

## UI Overview
The screenshot above shows the main elements of the fly view:

* **[Fly Toolbar](/reference/qgroundcontrol/main-toolbar.md):** Key status information (warning messages, battery, joystick status), and vehicle state (Flight mode, Armed/Disarmed status).
    * Select the sensor indicators (joystick, battery, etc.) to view more detail.
    * Press the Flight Mode text (e.g. "Manual") to select a new mode or press an assigned joystick button. Not every mode may be available.
    * Press the Armed/Disarmed text to toggle the armed state or press an assigned joystick button. A confirmation slider will appear.

* **Video:** Displays live video from the vehicle when connected to the [Companion Computer](/introduction/hardware-options/required-hardware/companion-computer.md).
    * Video can be recorded on the topside computer with the [Video Steam](/reference/qgroundcontrol/fly-view.md#video-stream) instrument page.
    * A [Telemetry Overlay](https://github.com/bluerobotics/ardusub-gitbook/blob/ArduSub-Docs-Overhaul/reference/qgroundcontrol/other-features.md#video-overlay) is automatically generated as a subtitle file when a video is recorded.

* **Map/Switcher:** Displays the position of a connected vehicle when using an underwater positioning system.
    * Click on the element to toggle the video or map views in the primary or secondary windows. 
    * You can drag the map to move it around (the map automatically re-centres after a certain amount of time).
    * The switcher can be hidden by clicking on the **"<<<"** icon.
    * The switcher can be expanded by clicking and dragging the upper right corner.
    * The switcher can be popped out by clicking on the upper left icon when video is in the secondary window element.
    
* **Attitude and Compass Indicators**: Visual instruments which show the vehicle's attitude (pitch and roll orientation) and compass heading.

* **Instrument Panel**: A multi-page widget that displays vehicle information including: telemetry, camera, video, system health, and vibration.

## Instrument Panel

The instrument panel is a multi-page widget that displays information about the current vehicle, including: telemetry, camera, video, system health, and vibration information.

The default page displays vehicle telemetry - use the drop down menu in the right corner to select the other pages.

### Values

The values page shows telemetry information; by default the altitude (relative to the home location) and the ground speed.

<img src="/images/reference/reference-qgc-fly-instruments-values.png" class="img-responsive img-center" style="max-height:600px;">

You can configure what information is display by pressing the small gear icon on the top left of the panel. Each value can be displayed in normal or "large" size (large size shows just one value per row in the page, while normal shows 2).

<img src="/images/reference/reference-qgc-fly-instruments-values-configure.png" class="img-responsive img-center" style="max-height:600px;">

### Camera

This functionality is not built into ArduSub, please use [Companion's Camera Settings Page](/reference/companion/camera.md) to change camera settings.

<img src="/images/reference/reference-qgc-fly-instruments-camera.png" class="img-responsive img-center" style="max-height:600px;">

### Video Stream

The video page is used to enable/disable video streaming. When enabled, you can start/stop the video stream, enable a grid overlay, change how the image fits the screen, and record the video locally with QGC.

<img src="/images/reference/reference-qgc-fly-instruments-video-stream.png" class="img-responsive img-center" style="max-height:600px;">

### Health

The health page shows you the health of the systems within your vehicle. QGroundControl will switch to this page automatically if any systems change to unhealthy.

### Vibration

The vibration page shows current vibration levels and clip counts.

<img src="/images/reference/reference-qgc-fly-instruments-vibration.png" class="img-responsive img-center" style="max-height:600px;">

## Actions/Tasks

### Arm

Arming a vehicle unlocks the drive thrusters and allows for maneuvering.

>**Note** It is recommended to only arm the vehicle when in the MANUAL flight mode to prevent inadvertent thruster activation. The vehicle will attempt to stabilize itself in other flight modes.

The vehicle may be armed in two ways:
1. Press an assigned [joystick button](/reference/ardusub/joystick-setup-page.md#button-assignment). 
2. Select the DISARMED button in the Fly Toolbar and then use the confirmation sider.

### Disarm

Disarming the vehicle disengages the thrusters (making the vehicle safe to handle).

The vehicle may be disarmed in two ways:
1. Press an assigned [joystick button](/reference/ardusub/joystick-setup-page.md#button-assignment).
2. Select the ARMED button in the Fly Toolbar and then use the confirmation sider.
