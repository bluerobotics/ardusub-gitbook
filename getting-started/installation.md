# Installation

## QGroundControl

Download and install QGroundControl using one of the links below.

- [Windows](https://s3.amazonaws.com/downloads.bluerobotics.com/QGC/QGroundControl-installer.exe)
- [Mac](https://s3.amazonaws.com/downloads.bluerobotics.com/QGC/QGroundControl.dmg)
- [Linux](https://s3.amazonaws.com/downloads.bluerobotics.com/QGC/QGroundControl.AppImage)

## ArduSub

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

The *Companion Computer* is assigned a static IP address of 192.168.2.2, and it expects the surface computer to have an IP address of 192.168.2.1. The network configuration on the surface computer needs to be set up before it can communicate with the ROV. Choose your operating system below to display the appropriate network setup instructions.

<div align="center">
	<div style="display:inline-block" >
	<button type="button" onclick="{ document.getElementById('windowsDiv').style.display = 'block'; document.getElementById('macDiv').style.display = 'none'; document.getElementById('linuxDiv').style.display = 'none'; }">Windows</a>
	</div>
	<div style="display:inline-block">
	<button type="button" class="btn btn-primary" onclick="{ document.getElementById('macDiv').style.display = 'block'; document.getElementById('windowsDiv').style.display = 'none'; document.getElementById('linuxDiv').style.display = 'none'; }">Mac</a>
	</div>
	<div style="display:inline-block">
	<button type="button" class="btn btn-primary" onclick="{ document.getElementById('linuxDiv').style.display = 'block'; document.getElementById('macDiv').style.display = 'none'; document.getElementById('windowsDiv').style.display = 'none'; }">Linux</a>
	</div>
</div>
<div id="windowsDiv" style="display:none">

	<h1 id="windows">Windows 10</h1>
	<ol>
	<li><p>Go to <em>Control Panel</em> &gt; <em>Network and Sharing Center</em> and then choose &quot;Change adapter settings&quot;.</p>
	<p> <img src="../images/windows-setup/network-and-sharing-center-annotated.png" class="img-responsive img-center" style="max-width:800px"></p>
	</li>
	<li><p>Right click on the Ethernet adapter, then choose <em>Properties</em>.</p>
	<p> <img src="../images/windows-setup/network-connections-annotated.png" class="img-responsive img-center" style="max-width:800px"></p>
	</li>
	<li><p>In the properties dialog, choose <em>Internet Protocol Version 4 (TCP/IPv4)</em>, then click <em>Properties</em>.</p>
	<p> <img src="../images/windows-setup/internet-protocol-version-4-annotated.png" class="img-responsive img-center" style="max-width:800px"></p>
	</li>
	<li><p>Select &quot;Use the following IP address&quot; And enter 192.168.2.1 for the IP address and 255.255.255.0 for the Subnet mask. Then select OK.</p>
	<p> <img src="../images/windows-setup/static-ip-annotated.png" class="img-responsive img-center" style="max-width:800px"></p>
	</li>
	</ol>
	<p><strong>Firewall</strong></p>
	<ol>
	<li><p>Go to <em>Control Panel</em> &gt; <em>Windows Firewall</em> and then select &quot;Allow an app or feature through Windows Firewall&quot;.</p>
	</li>
	<li><p>Select &quot;Change Settings&quot; and then select &quot;Open source ground control app provided by QGroundControl dev team&quot; or &quot;QGroundControl&quot;.</p>
	<p> <img src="../images/windows-setup/windows-firewall-annotated.png" class="img-responsive img-center" style="max-width:800px"></p>
	</li>
	</ol>

</div>
<div id="macDiv" style="display:none">

	<h1 id="mac">Mac</h1>
	<ol>
	<li><p>Go to <em>System Preferences</em> &gt; <em>Network</em></p>
	</li>
	<li><p>If your computer has an Ethernet port, select Ethernet from the options on the left side. If you had to get a USB to Ethernet adapter, plug it in now then select it.</p>
	</li>
	<li><p>Select the dropdown next to &quot;Configure IPv4&quot; and then select &quot;Manually&quot;</p>
	</li>
	<li><p>Enter 192.168.2.1 for the IP Address and 255.255.255.0 for the Subnet Mask and then select apply.</p>
	<p> <img src="../images/mac-setup/mac-network-settings-annotated.png" class="img-responsive img-center" style="max-width:800px"></p>
	</li>
	</ol>

</div>
<div id="linuxDiv" style="display:none">

	<h1 id="linux">Linux</h1>
	<ol>
	<li><p>Click the Network Icon in the toolbar at the top of the screen, and click &quot;Edit Connections...&quot;</p>
	<p> <img src="../images/linux-setup/LinuxStep1.png" class="img-responsive img-center" style="max-width:800px"></p>
	</li>
	<li><p>Click &quot;Add&quot;</p>
	<p> <img src="../images/linux-setup/LinuxStep2.png" class="img-responsive img-center" style="max-width:800px"></p>
	</li>
	<li><p>Select &quot;Ethernet&quot; for the connection type and click &quot;Create...&quot;</p>
	<p> <img src="../images/linux-setup/LinuxStep3.png" class="img-responsive img-center" style="max-width:800px"></p>
	</li>
	<li><p>From the &quot;Device MAC Address&quot; dropdown, select the ethernet interface you want to use. If you are using the built in ethernet card on your computer, there will be only one choice. If you are using a USB to Ethernet adapter, find out which interface corresponds to the adapter by looking at the options before and after plugging the adapter into the computer.</p>
	<p> <img src="../images/linux-setup/LinuxStep4.png" class="img-responsive img-center" style="max-width:800px"></p>
	</li>
	<li><p>Click the &quot;IPv4 Settings&quot; tab, and from the &quot;Method&quot; dropdown menu, select &quot;Manual&quot;. Click &quot;Add&quot;, and enter 192.168.2.1 for the Address, 255.255.255.0 for the Netmask and 0.0.0.0 for the Gateway. Click &quot;Save...&quot; to complete the setup.</p>
	<p> <img src="../images/linux-setup/LinuxStep5.png" class="img-responsive img-center" style="max-width:800px"></p>
	</li>
	</ol>

</div>