# Installation

## QGroundControl

Download QGroundControl

## ArduSub

Connect the Pixhawk to your computer with a USB cable.

## Raspberry Pi

With the simple method, you restore a `.img` file to the Raspberry Pi SD Card. This provides the operating system and everything already set up for running ArduSub. You can download the most recent disk image here:

<i class="fa fa-download" aria-hidden="true"></i> [Latest Ardusub-Raspbian Image](http://img.ardusub.com/2017-01-12-ardusub-raspbian.img.zip) *(1.6 GB, Updated 2017-01-12)*

*(Raspbian Jessie Lite 2016-11-25 w/ ArduSub Companion Computer Setup)*

To load the image to your SD card, use the following instructions.

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

If the image is still compressed, you can combine the decompression and writing in one command:

    gunzip --stdout ardusub-raspbian.img.gz | sudo dd bs=1m of=/dev/rdiskX

Note that the location and name of `ardusub-raspbian.img` might be slightly different depending on where you downloaded it. Once complete, you can eject the SD card and install it on the Raspberry Pi. That's it!