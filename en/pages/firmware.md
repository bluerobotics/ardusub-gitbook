# Firmware

## Overview

There are three different types of firmware:

 - Stable (3.4): The recommended build for most users.
 - Beta (3.5-rc1): A pre-release of a stable build, used for testing and bugfixes before officially labeling a build as stable. The versions for the these builds are suffixed with *-rcx*, where rc stands for release candidate, and x is a number that is incremented as the beta is updated.
 - Development (3.6-dev): Development build, updated frequently. This build should only be used in practice by developers and advanced users. The versions for these builds are suffixed with *-dev*.

The latest stable release of ArduSub is 3.4, and it is recommended to use QGroundControl stable release 3.1.3 with version of ArduSub. Versions of ArduSub later after 3.4 require a recent daily build of QGroundControl to operate.

## What Version is Installed?

To find out what firmware version is installed on your autopilot, [refresh your parameters](/configuring/#parameters). When the parameters are refreshed, the autopilot sends its software version information via STATUSTEXT messages. You can view these messages by clicking the *Messages* icon in QGroundControl. The *Messages* icon looks like a megaphone, or a warning sign if there are pending warnings. Here, you can see that the ArduSub version is *V3.5-rc1*.

<img src="/images/firmware/statustext-version.png" class="img-responsive img-center" style="max-height:600px;">

## Updating

It is **highly recommended** to [save your parameters](/configuring/#saving-and-loading) to a file before updating your firmware. To update your firmware using QGroundControl, go to the *Vehicle Setup Page* and click the *Firmware* tab, then plug your autopilot into the computer with a USB cable. Click ArduPilot flight stack, and choose your desired version to load. Beta and Development options are available after clicking the *Advanced settings* checkbox. *Stable* is not yet available through QGC for ArduSub. After you have selected your desired version, click *Ok* and wait for the upload to complete.

<img src="/images/firmware/qgc-upgrade.png" class="img-responsive img-center" style="max-height:600px;">

<p style="font-size:10px; text-align:center">
Sponsored by <a href="http://www.bluerobotics.com/">Blue Robotics</a>. Code released under the <a href="https://github.com/bluerobotics/ardusub/blob/master/COPYING.txt">GPLv3 License</a>. Documentation released under the <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC-NC-SA 4.0</a>.
<a href="https://github.com/bluerobotics/ardusub-docs/issues/">Submit a Documentation GitHub Issue here</a> to report any errors, suggestions, or missing information in this documentation.<br />
<a href="https://github.com/bluerobotics/ardusub/issues/">Submit an ArduSub GitHub Issue here</a> to report issues with the ArduSub software.
</p>