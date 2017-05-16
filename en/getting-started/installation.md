# Installation

## QGroundControl

Download and install QGroundControl using one of the links below.

* [Windows](https://s3-us-west-2.amazonaws.com/qgroundcontrol/builds/master/QGroundControl-installer.exe)
* [OS X](https://s3-us-west-2.amazonaws.com/qgroundcontrol/builds/master/QGroundControl.dmg)
* Linux
  * [AppImage](https://s3-us-west-2.amazonaws.com/qgroundcontrol/builds/master/QGroundControl.AppImage)
  * [Compressed Archive](https://s3-us-west-2.amazonaws.com/qgroundcontrol/builds/master/QGroundControl.tar.bz2)
* [Android](https://play.google.com/store/apps/details?id=org.mavlink.qgroundcontrolbeta&rdid=org.mavlink.qgroundcontrolbeta)

## ArduSub

Open QGroundControl and navigate to the *Firmware* tab of the *Vehicle Setup* page.

<img src="/images/qgc/firmware-1.png" class="img-responsive img-center" />

Plug in the Pixhawk to the computer's USB port. Once detected, QGroundControl will show a firmware selection box on the right. Choose "ArduPilot Flight Stack", then select ArduSub from the dropdown list.

<img src="/images/qgc/firmware-2.png" class="img-responsive img-center" />

Press "OK" at the top right. The firmware will upload the Pixhawk and you'll see the following printout and success message.

<img src="/images/qgc/firmware-3.png" class="img-responsive img-center" />

## Raspberry Pi

The Raspberry Pi operating system and supporting software is installed by restoring a pre-configured `.img` file to the Raspberry Pi SD Card. Download the image file [here](http://img.ardusub.com/2017-01-12-ardusub-raspbian.img.zip), then transfer the image to your SD card using the instructions below.

### Windows

Follow the instructions provided on [raspberrypi.org](https://www.raspberrypi.org/documentation/installation/installing-images/windows.md)

### Mac and Linux

Insert the SD card in a card reader, open a terminal, and run the following command to find the disk identifier of the SD card.

On Mac:

    diskutil list

On Linux:

    sudo fdisk -l

You can find the disk identifier in the output. It will look something like `/dev/disk2` on Mac and `/dev/sdb` or `/dev/mmcblk0` on Linux. Verify the disk identifier of the SD card by checking the disk size listed. If you are still unsure, try running the command with and without the SD card connected to the computer to see which disk identifier appears and disappears in the output. You need to start by unmounting all partitions on that disk. Run the following command using the top level disk identifier for your SD card, *not* an identifier for one of the partitions on the SD card. (Partition identifiers look like `/dev/disk1s1` on Mac or `/dev/sdb1`, `/dev/mmcblk0p1` on Linux)

On Mac:

    diskutil unmountDisk /dev/diskX

On Linux (add ?* to unmount all partitions):

    umount /dev/sdX?*

To write the disk image to the SD card, use the following command. On Mac, change `/dev/diskX` to `/dev/rdiskX` for faster transfers. On Linux, replace `bs=1m` with `bs=1M`. Make sure that the identifier after `of=` is your SD card!:

    sudo dd bs=1m if=~/Downloads/ardusub-raspbian.img of=/dev/rdiskX

Note that the location and name of `ardusub-raspbian.img` might be slightly different depending on where you downloaded it. Once complete, you can eject the SD card and install it on the Raspberry Pi. That's it!