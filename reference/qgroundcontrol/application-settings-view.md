# Application Settings View

The _Application Settings View_ is used to configure the settings for the QGroundControl application (rather than a specific vehicle). You do not have to have a vehicle connected to change these values.

You can switch between the various pages by clicking the buttons in the left-sidebar.

<img src="/images/reference/reference-qgc-application-settings.png" class="img-responsive img-center" style="max-height:600px;">

## Pages

The following pages are available for configuration:

* **[General Settings](/reference/qgroundcontrol/application-settings-view.md#general-settings-page)**
* **[Comm Links](/reference/qgroundcontrol/application-settings-view.md#comm-links-page)**
* **[Offline Maps](/reference/qgroundcontrol/application-settings-view.md#offline-maps)**
* **[Mavlink](/reference/qgroundcontrol/application-settings-view.md#mavlink)**
* **[Console](l/reference/qgroundcontrol/application-settings-view.md#console)**

### General Settings Page

The main application configuration settings. These are used to specify: display units, autoconnection devices, video display and storage, etc.

#### Units
<img src="/images/reference/reference-qgc-application-settings-general-units.png" class="img-responsive img-center" style="max-height:600px;">

The settings are:
* **Distance:** Meters | Feet
* **Area:** SquareMetres | SquareFeet | SquareKilometers | Hectares | Acres |SquareMiles
* **Speed:** Metres/second | Feet/second | Miles/hour | Kilometres/hour | Knots
* **Temperature:** Celsius | Fahrenheit

##### Miscellaneous

<img src="/images/reference/reference-qgc-application-settings-general-misc.png" class="img-responsive img-center" style="max-height:600px;">

The settings are:
* **Language:** System (System Language) | Bulgarian, Chinese, etc...
* **Color Scheme:** Indoor (Dark) | Outdoor (Light)
* **Map Provider:** Google | Mapbox | Bing | Airmap | VWorld | Eniro | Statkart
* **Map Type:** Road | Hybrid | Satellite
* **Stream GCS Position:** Never | Always | When in Follow Me Flight Mode.
* **UI Scaling:** UI scale percentage (affects fonts, icons, button sizes, layout etc.)
* **Mute all audio output:** Turns off all audio output.
* **Check for Internet Connection:** Uncheck to allow maps to be used in China/places where map tile downloads are likely to fail (stops the map-tile engine continually rechecking for an Internet connection).
* **Autoload Missions:** If enabled, automatically upload a plan to the vehicle on connection.
    * The plan file must be named AutoLoad#.plan, where the # is replaced with the vehicle id.
    * The plan file must be located in the Application Load/Save Path.
* **Clear all settings on next start:** Resets all settings to the default (including this one) when QGroundControl restarts.
* **Announce battery lower than:** Battery level at which QGroundControl will start low battery announcements.
* **Application Load/Save Path:** Default location for loading/saving application files, including: parameters, telemetry logs, and mission plans.

#### Data Persistence

<img src="/images/reference/reference-qgc-application-settings-general-data-persistence.png" class="img-responsive img-center" style="max-height:600px;">

The settings are:
* **Disable all data persistence:** Check to prevent any data being saved or cached: logs, map tiles etc. This setting disables the telemetry logs section.

#### Telemetry Logs

<img src="/images/reference/reference-qgc-application-settings-general-telemetry-logs.png" class="img-responsive img-center" style="max-height:600px;">

The settings are:
* **Save log after each flight:** Telemetry logs (.tlog) automatically saved to the Application Load/Save Path (above) after flight.
* **Save logs even if vehicle was not armed:** Logs when a vehicle connects to QGroundControl. Stops logging when the last vehicle disconnects.
* **[CSV Logging:](https://docs.qgroundcontrol.com/en/SettingsView/csv.html)** Log subset of telemetry data to a CSV file.

#### Fly View

<img src="/images/reference/reference-qgc-application-settings-general-fly-view.png" class="img-responsive img-center" style="max-height:600px;">

The settings are:
* **Use Preflight Checklist:** Enable pre-flight checklist in Fly toolbar.
* **Enforce Preflight Checklist:** Checklist completion is a pre-condition for arming.
* **Keep Map Centered on Vehicle:** Forces map to center on the currently selected vehicle.
* **Show Telemetry Log Replay Status Bar:** Display status bar for Replaying Flight Data.
* **Virtual Joystick:** Enable virtual joysticks (Does NOT work for ArduSub, PX4 only)
* **Use Vertical Instrument Panel:** Align instrument panel vertically rather than horizontally (default).
* **Show additional heading indicators on Compass:** Adds additional indicators to the compass rose:
    * Blue arrow: course over ground.
    * White house: direction back to home.
    * Green line: Direction to next waypoint.
* **Lock Compass Nose-Up:** Check to rotate the compass rose (default is to rotate the vehicle inside the compass indicateor, North Up).
* **Guided Minimum Altitude:** Minimum value for guided actions altitude slider.
* **Guided Maximum Altitude:** Minimum value for guided actions altitude slider.
* **Go To Location Max Distance:** The maximum distance that a Go To location can be set from the current vehicle location (in guided mode).

#### Plan View

<img src="/images/reference/reference-qgc-application-settings-general-plan-view.png" class="img-responsive img-center" style="max-height:600px;">

#### Autoconnect Devices

<img src="/images/reference/reference-qgc-application-settings-general-autoconnect.png" class="img-responsive img-center" style="max-height:600px;">

#### RTK GPS

<img src="/images/reference/reference-qgc-application-settings-general-rtk.png" class="img-responsive img-center" style="max-height:600px;">

#### ADSB Server

<img src="/images/reference/reference-qgc-application-settings-general-adsb.png" class="img-responsive img-center" style="max-height:600px;">

#### Video

<img src="/images/reference/reference-qgc-application-settings-general-video.png" class="img-responsive img-center" style="max-height:600px;">

#### Video Recording

<img src="/images/reference/reference-qgc-application-settings-general-video-recording.png" class="img-responsive img-center" style="max-height:600px;">

#### Brand Image

<img src="/images/reference/reference-qgc-application-settings-general-brand-image.png" class="img-responsive img-center" style="max-height:600px;">

### Comm Links Page

Allows you to manually create communication links and connect to them. Keep in mind that normally this is not needed since QGroundControl will automatically connect to the most common devices.

<img src="/images/reference/reference-qgc-application-settings-comm-links.png" class="img-responsive img-center" style="max-height:600px;">

<img src="/images/reference/reference-qgc-application-settings-comm-links-udp.png" class="img-responsive img-center" style="max-height:600px;">

### Offline Maps

Allows you to cache maps for use while you have no Internet connection.

<img src="/images/reference/reference-qgc-application-settings-general-offline-maps.png" class="img-responsive img-center" style="max-height:600px;">

### Mavlink

Settings associated with the MAVLink connection to a vehicle.

<img src="/images/reference/reference-qgc-application-settings-mavlink.png" class="img-responsive img-center" style="max-height:600px;">

### Console

Used to capture application logs for help with diagnosing application problems.

<img src="/images/reference/reference-qgc-application-settings-console.png" class="img-responsive img-center" style="max-height:600px;">
