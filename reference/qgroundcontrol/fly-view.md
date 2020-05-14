# Fly View

The Fly View is used to control and monitor the vehicle when diving.

You can use it to:
* Display video, mission, telemetry, and other information for the current vehicle.
* Control the vehicle and accessories with a connected joystick.
* Switch between a video view and map view (if an underwater positioning system is used).


## UI Overview
The screenshot above shows the main elements of the fly view:

* **[Fly Toolbar](/reference/qgroundcontrol/main-toolbar.md):** Key status information (warning messages, battery, joystick status), and vehicle state (Flight mode, Armed/Disarmed status).
    * Select the sensor indicators to view more detail.
    * Press the Flight mode text (e.g. "Manual") to select a new mode or press an assigned joystick button. Not every mode may be available.
    * Press the Armed/Disarmed text to toggle the armed state or press an assigned joystick button.

* **Video:** Displays live video from the vehicle when connected to the [Companion Computer](/introduction/hardware-options/required-hardware/companion-computer.md).
    * A [Telemetry Overlay](https://github.com/bluerobotics/ardusub-gitbook/blob/ArduSub-Docs-Overhaul/reference/qgroundcontrol/other-features.md#video-overlay) is automatically generated as a subtitle file when a video is recorded.

* **Map/Switcher:** Displays the position of a connected vehicle when using an underwater positioning system.
    * Click on the element to toggle the video or map views in the primary or secondary windows. 
    * You can drag the map to move it around (the map automatically re-centres after a certain amount of time).
    * The switcher can be hidden by clicking on the **"<<<"** icon.
    * The switcher can be expanded by clicking and dragging the upper right corner.
    * The switcher can be popped out by clicking on the upper left icon when video is in the secondary window element.

* **Instrument Panel**: A multi-page widget that displays vehicle information including: telemetry, camera, video, system health, and vibration.

* **Confirmation Slider**: Context sensitive slider to confirm requested actions. Slide to start operation. Press X to cancel.

## Instrument Panel

The instrument panel is a multi-page widget that displays information about the current vehicle, including: telemetry, camera, video, system health, and vibration information.

The default page displays vehicle telemetry - use the drop down menu in the right corner to select the other pages.

### Values

The values page shows telemetry information; by default the altitude (relative to the home location) and the ground speed.

You can configure what information is display by pressing the small gear icon on the top left of the panel. Each value can be displayed in normal or "large" size (large size shows just one value per row in the page, while normal shows 2).

### Camera

The camera page is used to configure and control the camera. For a camera connected directly to the Flight Controller the only available option is camera triggering:

When connected to camera that supports the MAVLink Camera Protocol you can additionally configure and use other camera services that it makes available. For example, if your camera supports video mode you will be able to switch between still image capture and video mode, and start/stop recording.

Advanced settings can be changed via the gear icon at the top left of the page.

### Video Stream

The video page is used to enable/disable video streaming. When enabled, you can start/stop the video stream, enable a grid overlay, change how the image fits the screen, and record the video locally with QGC.

### Health

The health page shows you the health of the systems within your vehicle. QGroundControl will switch to this page automatically if any systems change to unhealthy.

### Vibration

The vibration page shows current vibration levels and clip counts.

## Actions/Tasks

The vibration page shows current vibration levels and clip counts.

### Arm

Arming a vehicle starts the motors in preparation for takeoff.
To arm the vehicle, select Disarmed in the Fly Toolbar and then use the confirmation sider.

### Disarm

Disarming the vehicle stops the motors (making the vehicle safe). To disarm the vehicle select Armed in the Fly Toolbar when the vehicle is landed.

## Replay Telemetry Data

