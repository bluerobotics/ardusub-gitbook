{% include "../archive-notice.html" %}

# ArduSub Firmware

## Versioning

There are three flavors of ArduSub firmware:

- Stable (4.0): The recommended build for most users.
- Development (4.1-dev): Development build, updated frequently. This build should only be used in practice by developers and advanced users. The versions for these builds are suffixed with *-dev*.

Precompiled ArduSub binaries are available [here](https://firmware.us.ardupilot.org/Sub/). **Note** Binaries are provided for many platforms, but only the Pixhawk 1 (PX4-v2 platform) is thoroughly tested and supported.

## Release History

ArduSub release history is available [here](https://raw.githubusercontent.com/ArduPilot/ardupilot/master/ArduSub/ReleaseNotes.txt).

## What Version is Installed?

To find out what firmware version is installed on your autopilot, navigate to the *Summary* tab of the *Vehicle Setup* page. The firmware version will be listed under the *Frame* section.

<img src="/images/qgc/firmware-version.png" class="img-responsive img-center" style="max-height:600px;">

## Updating

It is **highly recommended** to [save your parameters](/operators-manual/parameters.md#saving-and-loading) to a file before updating your firmware. To update your firmware using QGroundControl, go to the *Vehicle Setup Page* and click the *Firmware* tab, then plug your autopilot into the computer with a USB cable. Choose 'ArduPilot Flight Stack', then choose your desired version to load. Beta and Development options are available after clicking the *Advanced settings* checkbox. 

<img src="/images/firmware/qgc-upgrade.png" class="img-responsive img-center" style="max-height:600px;">

<p style="font-size:10px; text-align:center">
Sponsored by <a href="http://www.bluerobotics.com/">Blue Robotics</a>. Code released under the <a href="https://github.com/bluerobotics/ardusub/blob/master/COPYING.txt">GPLv3 License</a>. Documentation released under the <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC-NC-SA 4.0</a>.<br />
<a href="https://github.com/bluerobotics/ardusub-gitbook/issues/">Submit a Documentation GitHub Issue here</a> to report any errors, suggestions, or missing information in this documentation.<br />
<a href="https://github.com/bluerobotics/ardusub/issues/">Submit an ArduSub GitHub Issue here</a> to report issues with the ArduSub software.
</p>
