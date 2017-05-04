# Raspberry Pi Setup

This page explains how to set up a Raspberry Pi for use with ArduSub.

## Easy Setup With Disk Image

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

## Setup From Scratch

These instructions are provided for those who wish to set everything up themselves.

### Install Raspbian and Set IP Address

Start with Jessie-Lite image downloaded from [raspberrypi.org](https://www.raspberrypi.org/downloads/raspbian/) and follow their instructions to install it to an SD card.

1. Modify the file `/boot/cmdline.txt` to have "ip=192.168.2.2" to the end of the line. It will look something like this (all one line):

		dwc_otg.lpm_enable=0 console=serial0,115200 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait ip=192.168.2.2

2. Create a new, empty file `/boot/ssh` (no extension) to enable ssh.
3. Insert the SD card into the Raspberry Pi, connect the Ethernet directly to your computer (through a tether interface board if desired), and power it up.

### Connect to the Raspberry Pi

The host computer needs to be configured with a static ip address of 192.168.2.1 on the ethernet interface. Please see the main [host computer setup](/initial-setup/#host-computer-setup) sections for details.

All of the remaining setup is completed on the command line. You must connect to the Raspberry Pi via SSH, using a client program like PuTTY or the Mac Terminal. The default password is `raspberry`.

	ssh pi@192.168.2.2

### Connect to the Internet

The Raspberry Pi will require an internet connection to download and install the necessary software. If you are on a Mac and have set up [Internet sharing](/initial-setup/#mac), you are good to go. Otherwise, setup the WiFi connection on the Raspberry Pi as shown below.

#### WiFi

Edit `/etc/wpa_supplicant/wpa_supplicant.conf` on the Raspberry Pi by running:

	sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

Add the following to the end of the file:

	network={
	ssid="yournetworkname"
	psk="yournetworkpassword"
	}

Save your changes with CTRL+O, and close the editor with CTRL+X. Then restart the wireless interface:

	sudo ifdown wlan0
	sudo ifup wlan0

Check your Internet connection:

	ping ardusub.com

### Command Line Setup

First, run `raspi-config` to expand the filesystem and enable the camera.

1. Run `sudo raspi-config` on the command line.
2. Choose "Expand Filesystem", then "Ok"
3. Choose "Enable Camera", then "Yes", then "Ok" (The option "Enable Camera" can be found under "Interfacing Options" if it is not available in the main menu).
4. Choose "Finish" and "Yes" to rebooting.

Next, update the current software and install the prerequisites needed by running the setup script in the Blue Robotics [companion repository](https://github.com/bluerobotics/companion). Start by downloading the script on the Raspberry Pi:

	wget https://raw.githubusercontent.com/bluerobotics/companion/master/RPI2/Raspbian/setup.sh

Make the script executable

	chmod +x setup.sh

Run the script

	./setup.sh

It may take 90 minutes for all of the software to be installed and set up. When the script completes, reboot the Raspberry Pi:

	sudo shutdown now -r

When the Raspberry Pi reboots, it will automatically start streaming video if the camera is connected and will automatically connect to the Pixhawk, if connected. If you have issues at this point, try running the setup script again, in case a package was unable to be retreived the first time.

## Advanced

### Reentering Mavproxy and Video Processes

The `mavproxy` and video processes are started in "screen" sessions so that they can be reentered to view output and any errors that may have occurred. To reenter the sessions, open and SSH terminal to the Raspberry Pi and run the following commands:

	sudo screen -r video

	sudo screen -r mavproxy

To quit the process, press Ctrl-C. To exit without stopping the process, press Ctrl-A, then D to "detach" from the session.

### Backing Up Disk Image

On Mac or Linux, first find out the disk number of the SD card using `diskutil`.

	diskutil list

Find the SD card in the output. On Mac it will be something like `/dev/disk2` and on Linux it will be something like '/dev/sdb'.

*On Mac:*

	sudo dd bs=4m if=/dev/disk2 | gzip > raspbian-ardusub.img.gz

*On Linux:*

	sudo dd bs=4M if=/dev/sdb | gzip > raspbian-ardusub.img.gz

Press Ctrl-T to check on status while this is happening. It can take quite a while. 

To restore the image, see the simple setup instructions above.

### Flashing Pixhawk Through SSH

With an Ethernet tether and companion computer, it is possible to flash the Pixhawk firmware through the companion computer - no need to directly access the Pixhawk.

#### Flashing with Latest Build From the Internet

*These instructions are in alpha test phase! Use with care and patience.*

*Note: The default password for the Raspberry Pi is `raspberry`*

To use these instructions, your companion computer will have to be connected to the Internet. Please see the [Internet setup instructions](/raspi-setup/#connect-to-the-internet) to set that up.

First make sure your companion computer has the most recent scripts. Execute this command from the host computer:

	ssh pi@192.168.2.2 "git --work-tree=/home/pi/companion --git-dir=/home/pi/companion/.git pull origin master"

Next, run the firmware updater script:
 
	ssh pi@192.168.2.2 "/home/pi/companion/RPI2/Raspbian/flash_px4.py --frame=vectored"

While the flashing command is running, you will see the script try to start the Pixhawk's bootloader multiple times. The output will look like this:

	if the board does not respond, unplug and re-plug the USB connector.
	attempting reboot on /dev/ttyACM0...

Eventually it should catch and reflash the board.

#### Flashing With a .px4 File

These instructions assume you already have a firmware file (ArduSub-v2.px4) from the [firmware repository](http://firmware.ardusub.com/Sub/stable/v3.4/) or that you [compiled yourself](/developers/). Run the commands from the section above to update your `companion` code to the most recent version and then run the following command to update the firmware:

	ssh pi@192.168.2.2 "/home/pi/companion/RPI2/Raspbian/flash_px4.py --stdin" < ArduSub-v2.px4

<p style="font-size:10px; text-align:center">
Sponsored by <a href="http://www.bluerobotics.com/">Blue Robotics</a>. Code released under the <a href="https://github.com/bluerobotics/ardusub/blob/master/COPYING.txt">GPLv3 License</a>. Documentation released under the <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC-NC-SA 4.0</a>.
<a href="https://github.com/bluerobotics/ardusub-docs/issues/">Submit a Documentation GitHub Issue here</a> to report any errors, suggestions, or missing information in this documentation.<br />
<a href="https://github.com/bluerobotics/ardusub/issues/">Submit an ArduSub GitHub Issue here</a> to report issues with the ArduSub software.
</p>