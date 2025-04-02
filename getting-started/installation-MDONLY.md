{% include "../archive-notice.html" %}

<script src="https://npmcdn.com/tether@1.2.4/dist/js/tether.min.js"></script>
<script src="../js/jquery.min.js"></script>
<script src="../js/bootstrap.js"></script>

# Installation

## QGroundControl

Download and install QGroundControl using one of the links below.

- [Windows](https://s3.amazonaws.com/downloads.bluerobotics.com/QGC/latest/QGroundControl-installer.exe)
- [Mac](https://s3.amazonaws.com/downloads.bluerobotics.com/QGC/latest/QGroundControl.dmg)
- [Linux](https://s3.amazonaws.com/downloads.bluerobotics.com/QGC/latest/QGroundControl.AppImage)

## ArduSub

>**Note** It is **highly recommended** to [save your parameters](/operators-manual/parameters.md#saving-and-loading) to a file before updating your firmware.

Open QGroundControl and navigate to the *Firmware* tab of the *Vehicle Setup* page.

<img src="/images/qgc/firmware-1.png" class="img-responsive img-center" />

Plug in the Pixhawk to the computer's USB port. Once detected, QGroundControl will show a firmware selection box on the right. Choose "ArduPilot Flight Stack", then select ArduSub from the dropdown list.

<img src="/images/qgc/firmware-2.png" class="img-responsive img-center" />

Press "OK" at the top right. The firmware will upload the Pixhawk and you'll see the following printout and success message.

<img src="/images/qgc/firmware-3.png" class="img-responsive img-center" />

## Raspberry Pi

The Raspberry Pi operating system and supporting software is installed by restoring a pre-configured `.img` file to the Raspberry Pi SD Card. The Raspberry Pi is referred to as the *Companion Computer*, and the software that runs on it is referred to collectively as the *Companion Software*.

1. Insert a microSD card with at least 4GB capacity into your computer with a card reader
1. Download the Raspberry Pi image [here](https://s3.amazonaws.com/downloads.bluerobotics.com/Pi/stable/ardusub-raspbian.img.zip)
1. While the Raspberry Pi image downloads, download and install [Etcher](https://etcher.io/). Make sure you select the correct download for your Operating System!
1. Open Etcher, select the Raspberry Pi image file (no need to extract beforehand) and your SD card, click 'Flash' and wait for it to complete
<img src="/images/etcher.png" width="690" height="351">
1. Eject the SD card, and place it back into the Raspberry Pi

## Network Setup

The *Companion Computer* is assigned a static IP address of 192.168.2.2, and it expects the surface computer to have an IP address of 192.168.2.1. The network configuration on the surface computer needs to be set up before it can communicate with the ROV.

# Windows

1. Go to _Control Panel_ > _Network and Sharing Center_ and then choose "Change adapter settings".

	<img src="/images/windows-setup/network-and-sharing-center-annotated.png" class="img-responsive img-center" style="max-width:800px" />

2. Right click on the Ethernet adapter, then choose _Properties_.

	<img src="/images/windows-setup/network-connections-annotated.png" class="img-responsive img-center" style="max-width:800px" />

3. In the properties dialog, choose _Internet Protocol Version 4 (TCP/IPv4)_, then click _Properties_.

	<img src="/images/windows-setup/internet-protocol-version-4-annotated.png" class="img-responsive img-center" style="max-width:800px" />

4. Select "Use the following IP address" And enter 192.168.2.1 for the IP address and 255.255.255.0 for the Subnet mask. Then select OK.

	<img src="/images/windows-setup/static-ip-annotated.png" class="img-responsive img-center" style="max-width:800px" />

**Firewall**

1. Go to _Control Panel_ > _Windows Firewall_ and then select "Allow an app or feature through Windows Firewall".

2. Select "Change Settings" and then select "Open source ground control app provided by QGroundControl dev team" or "QGroundControl".

	<img src="/images/windows-setup/windows-firewall-annotated.png" class="img-responsive img-center" style="max-width:800px" />

# Mac

1. Go to _System Preferences_ > _Network_

2. If your computer has an Ethernet port, select Ethernet from the options on the left side. If you had to get a USB to Ethernet adapter, plug it in now then select it.

3. Select the dropdown next to "Configure IPv4" and then select "Manually"

4. Enter 192.168.2.1 for the IP Address and 255.255.255.0 for the Subnet Mask and then select apply.

	<img src="/images/mac-setup/mac-network-settings-annotated.png" class="img-responsive img-center" style="max-width:800px" />

# Linux

1. Click the Network Icon in the toolbar at the top of the screen, and click "Edit Connections..."

	<img src="/images/linux-setup/LinuxStep1.png" class="img-responsive img-center" style="max-width:800px" />

2. Click "Add"

	<img src="/images/linux-setup/LinuxStep2.png" class="img-responsive img-center" style="max-width:800px" />

3. Select "Ethernet" for the connection type and click "Create..."

	<img src="/images/linux-setup/LinuxStep3.png" class="img-responsive img-center" style="max-width:800px" />

4. From the "Device MAC Address" dropdown, select the ethernet interface you want to use. If you are using the built in ethernet card on your computer, there will be only one choice. If you are using a USB to Ethernet adapter, find out which interface corresponds to the adapter by looking at the options before and after plugging the adapter into the computer.

	<img src="/images/linux-setup/LinuxStep4.png" class="img-responsive img-center" style="max-width:800px" />

5. Click the "IPv4 Settings" tab, and from the "Method" dropdown menu, select "Manual". Click "Add", and enter 192.168.2.1 for the Address, 255.255.255.0 for the Netmask and 0.0.0.0 for the Gateway. Click "Save..." to complete the setup.

	<img src="/images/linux-setup/LinuxStep5.png" class="img-responsive img-center" style="max-width:800px" />
