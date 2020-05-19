# Main Toolbar

The main menu/tool bar provides access to the different application views, and high level status information for the connected vehicle. The menu is the same in all views except for "Plan View" (which has a single icon to take you back to "Fly" view).

<img src="/images/reference/reference-qgc-toolbar.png" class="img-responsive img-center" style="max-height:600px;">

## View Selection Icons

The following icons are used to switch between the main _Views_. These are displayed even if no vehicle is connected.

<img src="/images/reference/reference-qgc-toolbar-application-settings.png" class="img-responsive img-left" style="max-height:600px;"> **[Application Settings View](/reference/qgroundcontrol/application-settings-view.md)**: Configure the QGroundControl application.

<img src="/images/reference/reference-qgc-toolbar-vehicle-setup.png" class="img-responsive img-left" style="max-height:600px;"> **[Vehicle Setup View](/reference/qgroundcontrol/vehicle-setup-view.md)**: Configure and tune your vehicle.

<img src="/images/reference/reference-qgc-toolbar-plan.png" class="img-responsive img-left" style="max-height:600px;"> **[Plan View](/reference/qgroundcontrol/plan-view.md)**: Create autonomous missions. **[Not functional with ArduSub 4.0.1]**

<img src="/images/reference/reference-qgc-toolbar-fly.png" class="img-responsive img-left" style="max-height:600px;"> **[Fly View](/reference/qgroundcontrol/fly-view.md)**: Control and monitor your ArduSub vehicle, including streaming video.

<img src="/images/reference/reference-qgc-toolbar-analyze.png" class="img-responsive img-left" style="max-height:600px;"> **[Analyze View](/reference/qgroundcontrol/analyze-view.md)**: Download logs, and access the MAVLink console.

## Status Icons

Status icons are displayed when QGroundControl is connected to a vehicle. These show the high level status of the vehicle, and can be clicked to see more detailed information.

<img src="/images/reference/reference-qgc-toolbar-vehicle-messages.png" class="img-responsive img-left" style="max-height:600px;"> **Vehicle Messages**: Click to show a dropdown of messages from the vehicle. This will change to a Yield sign if there are critical messages.

<img src="/images/reference/reference-qgc-toolbar-battery.png" class="img-responsive img-left" style="max-height:600px;"> **Battery**: Current battery voltage. A [Power Sensing Module](/introduction/hardware-options/required-hardware/power-sensing-module.md) will need to be [properly configured](/reference/ardusub/power-setup-page.md) to display the correct voltage.

<img src="/images/reference/reference-qgc-toolbar-joystick.png" class="img-responsive img-left" style="max-height:600px;"> **Joystick Status**: Click to show the joystick status. The icon will be red if no joystick is connected and/or it is not enabled. After a joystick is [calibrated and enabled](/reference/ardusub/joystick-setup-page.md#calibration-procedures), the icon will turn white.

<img src="/images/reference/reference-qgc-toolbar-flight-mode.png" class="img-responsive img-left" style="max-height:600px;"> **Flight Mode**: Current flight mode. Click or press an assigned button to change flight mode.

<img src="/images/reference/reference-qgc-toolbar-arming-status.png" class="img-responsive img-left" style="max-height:600px;"> **Arming Status**: This dropdown shows the arming status of the vehicle. 

   * **Disarmed** means control to the ESCs has been disabled and cannot be activated inadvertently. 
    
   * **Armed** means the ESCs are enabled and moving the joystick will cause the thrusters to spin in the corresponding direction.

## Brand Image

This can be changed in the [General Settings](/reference/qgroundcontrol/application-settings-view.md#brand-image) of the _Application Settings View_.

