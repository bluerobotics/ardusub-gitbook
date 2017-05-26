# Installation

## QGroundControl

Download and install QGroundControl using one of the links below.

* [Windows](https://s3-us-west-2.amazonaws.com/qgroundcontrol/builds/master/QGroundControl-installer.exe)
* [OS X](https://s3-us-west-2.amazonaws.com/qgroundcontrol/builds/master/QGroundControl.dmg)
* Linux
  * [AppImage](https://s3-us-west-2.amazonaws.com/qgroundcontrol/builds/master/QGroundControl.AppImage)
  * [Compressed Archive](https://s3-us-west-2.amazonaws.com/qgroundcontrol/builds/master/QGroundControl.tar.bz2)

## ArduSub

Open QGroundControl and navigate to the *Firmware* tab of the *Vehicle Setup* page.

<img src="/images/qgc/firmware-1.png" class="img-responsive img-center" />

Plug in the Pixhawk to the computer's USB port. Once detected, QGroundControl will show a firmware selection box on the right. Choose "ArduPilot Flight Stack", then select ArduSub from the dropdown list.

<img src="/images/qgc/firmware-2.png" class="img-responsive img-center" />

Press "OK" at the top right. The firmware will upload the Pixhawk and you'll see the following printout and success message.

<img src="/images/qgc/firmware-3.png" class="img-responsive img-center" />

## Raspberry Pi

The Raspberry Pi operating system and supporting software is installed by restoring a pre-configured `.img` file to the Raspberry Pi SD Card.

1. Insert a microSD card with at least 4GB capacity into your computer with a card reader
1. Download the Raspberry Pi image [here](https://s3.amazonaws.com/downloads.bluerobotics.com/Pi/stable/ardusub-raspbian.img.zip)
1. While the Raspberry Pi image downloads, download and install [Etcher](https://etcher.io/). Make sure you select the correct download for your Operating System!
1. Open Etcher, select the Raspberry Pi image file (no need to extract beforehand) and your SD card, click 'Flash' and wait for it to complete.
<img src="/images/etcher.png" width="690" height="351">
1. Eject the SD card, and place it back into the Raspberry Pi.