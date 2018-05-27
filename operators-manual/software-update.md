# Updating Software

## QGroundControl

QGroundControl software release notes are [here](https://raw.githubusercontent.com/bluerobotics/qgroundcontrol/3.2.4/BlueRobotics-Revision-Notes.txt). To update QGroundControl, simply download and install the latest stable version of QGC (BlueRobotics flavor) from one of the links below:

[Windows](https://s3.amazonaws.com/downloads.bluerobotics.com/QGC/QGroundControl-installer.exe)

[Mac](https://s3.amazonaws.com/downloads.bluerobotics.com/QGC/QGroundControl.dmg)

[Linux](https://s3.amazonaws.com/downloads.bluerobotics.com/QGC/QGroundControl.AppImage)

## Companion

Companion software release notes are [here](https://raw.githubusercontent.com/bluerobotics/companion/master/release-notes.txt). To perform a companion update update:

- Plug a _fully charged_ battery into the ROV and connect the tether to your computer.
- Navigate to [192.168.2.2:2770/network](http://192.168.2.2:2770/network) in your browser and ensure that the ROV has access to a WiFi network. If you do not see a webpage at this address, you need to perform the update according to the instructions [here](http://discuss.bluerobotics.com/t/software-updates/1128).
- Navigate to [192.168.2.2:2770/system](http://192.168.2.2:2770/system). Click the button that says 'Update companion'. If you do not see this button, then the companion software is up to date.
- The update process will take between 5 and 20 minutes depending on the Internet connection speed. Wait for the update process to complete.
- When it completes, refresh your browser. The companion version should be updated, and the update available message should no longer appear.
- If the update fails (usually due to a loss of internet connectivity), you will be warned that the ROV will reboot and to leave the battery plugged in. At this point, once you are able to refresh the webpage, it is safe to either power down the ROV or attempt the update again.

## ArduSub

ArduSub software release notes are [here](https://raw.githubusercontent.com/ArduPilot/ardupilot/master/ArduSub/ReleaseNotes.txt). An autopilot can be updated with the latest firmware via a connected companion computer or by connecting the autopilot directly to a computer via usb.

### Via QGC

To update an autopilot via QGC, the autopilot must be connected directly to the computer running QGC by a USB cable. Open QGC, go to the _Vehicle Setup_ page (click the gears icon), then go to the _Firmware_ tab and follow the instructions.

### Via Companion

An autopilot installed on a vehicle can be updated remotely via the companion computer web interface:

- Power on your ROV and connect it to your computer
- Navigate to [192.168.2.2:2770/network](http://192.168.2.2:2770/network) and ensure that the ROV has an internet connection
- Navigate to [192.168.2.2:2770/system](http://192.168.2.2:2770/system). Click the button under the 'Pixhawk Firmware Update' section that says 'Stable'.
- Wait for the update process to complete, and you are finished!

<p style="font-size:10px; text-align:center">
Sponsored by <a href="http://www.bluerobotics.com/">Blue Robotics</a>. Code released under the <a href="https://github.com/bluerobotics/ardusub/blob/master/COPYING.txt">GPLv3 License</a>. Documentation released under the <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC-NC-SA 4.0</a>.<br />
<a href="https://github.com/bluerobotics/ardusub-docs/issues/">Submit a Documentation GitHub Issue here</a> to report any errors, suggestions, or missing information in this documentation.<br />
<a href="https://github.com/bluerobotics/ardusub/issues/">Submit an ArduSub GitHub Issue here</a> to report issues with the ArduSub software.
</p>