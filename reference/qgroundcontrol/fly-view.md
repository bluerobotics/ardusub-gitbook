# Fly View

The Fly View is used to control and monitor the vehicle when diving.

You can use it to:
* Display video, mission, telemetry, and other information for the current vehicle.
* Control the vehicle and accessories with a connected joystick.
* Switch between a video view and map view (if an underwater positioning system is used).


## UI Overview
The screenshot above shows the main elements of the fly view:
Map: Displays the positions of all connected vehicles and the mission for the current vehicle.
You can drag the map to move it around (the map automatically re-centres after a certain amount of time).
Once flying, you can click on the map to set a Go to or Orbit at location.
Fly Toolbar: Key status information for sensors (GPS, battery, RC control), and vehicle state (Flight mode, Armed/Disarmed status).
Select the sensor indicators to view more detail.
Press the Flight mode text (e.g. "Hold") to select a new mode. Not every mode may be available.
Press the Armed/Disarmed text to toggle the armed state. If flying you can press this text to Emergency Stop.
Fly tools: You can use these to:
Toggle between takeoff/land.
Pause/restart the current operation (e.g. landing, or the mission).
Safety return (also known as RTL or Return).
The Action button offers other appropriate options for the current state (these overlay the Confirmation Slider). Actions include changing the altitude or continuing a mission.
Enable the preflight checklist (tool option disabled by default).
Instrument Panel: A multi-page widget that displays vehicle information including: telemetry, camera, video, system health, and vibration.
Video/Switcher: Toggle between video or map in a window.
Press the element to switch Video and Map to foreground.
QGroundControl supports RTP and RTSP video streaming over your vehicles UDP connection. It also support directly connected UVC device support. QGC video support is further discussed in the Video README.
A Telemetry Overlay is automatically generated as a subtitle file
Confirmation Slider: Context sensitive slider to confirm requested actions. Slide to start operation. Press X to cancel.

## Display Video

When video streaming is enabled, QGroundControl will display the video stream for the currently selected vehicle in the "video switcher window" at the bottom left of the map. You can press the switcher anywhere to toggle Video and Map to foreground (below we show the video in the foreground).

You can further configure video display using controls on the switcher:
Resize the switcher by dragging the icon in the to right corner.
Hide the switcher by pressing the toggle icon in the lower left.
Detach the video switcher window by pressing on the icon in its top left corner (once detached, you can move and resize the window just like any other in your OS). If you close the detached window the switcher will re-lock to the QGC Fly view.

## Instrument Panel

The instrument panel is a multi-page widget that displays information about the current vehicle, including: telemetry, camera, video, system health, and vibration information.
The default page displays vehicle telemetry - use the drop down menu on the to right to select the other options.

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

