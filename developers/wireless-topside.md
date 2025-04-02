{% include "../archive-notice.html" %}

# Wireless Topside Connection

These instructions assume that you have already set up your ROV to the surface computer via the tether and static IP of 192.168.2.1 on the surface computer, according to the directions in the [Network Setup](/quick-start/installing-companion.md#network-setup) section. These instructions were compiled using the [TP-LINK TL-WR802N](http://www.tp-link.com/us/products/details/cat-5506_TL-WR802N.html) router.

To begin, power on the ROV, and connect via Ethernet. Open a web browser and navigate to [192.168.2.2:8088](http://192.168.2.2:8088). Click the 'Open Terminal' button in the upper right corner. Enter this command to remove the Raspberry Pi's static IP assignment on the Ethernet interface:

`sudo sed -i 's/ip=192.168.2.2//' /boot/cmdline.txt`

<img src="/images/wireless-topside/1.png" class="img-responsive img-center" style="max-height:400px;" align="middle">

Disconnect power from the ROV.

Now we need to set up the router. We will start by resetting the router to the factory defaults. Connect power to the router, and hold down the 'Reset' button for 15 seconds. Disconnect power from the router, and power it on again.

Connect the surface computer to the router's wireless network, using the network name and password printed on the label on the side of the router. After you have connected to the router's wireless network, open a web browser and navigate to [192.168.0.1](http://192.168.0.1). Enter the default username (admin) and password (admin).

In the _Operation Mode_ menu, choose the 'Access Point' option and save the settings and reboot the router.

<img src="/images/wireless-topside/2.png" class="img-responsive img-center" style="max-height:400px;" align="middle">

After the router reboots, reconnect the surface computer to the router's wireless network. Open a web browser and navigate to [192.168.0.254](http://192.168.0.254) and log into the router again.

In the _Network_ menu, set the Type to 'Static IP' and set the IP Address to 192.168.2.3. Then save the settings and reboot the router. Disconnect power from the router.

<img src="/images/wireless-topside/3.png" class="img-responsive img-center" style="max-height:400px;" align="middle">

Next, remove the static IP assignment from the surface computer, and configure the Ethernet interface as a DHCP client (this is the default 'automatic' configuration).

Connect the router to the tether with an Ethernet patch cable and connect power to the router. Power on the ROV. Connect the surface computer to the router's wireless network. Open a web browser and navigate to [192.168.2.3](http://192.168.2.3) and log into the router again.

In the _DHCP_ menu, go to the _DHCP Client List_ sub-menu. Write down the MAC Addresses for the surface computer and the Raspberry Pi.

<img src="/images/wireless-topside/4.png" class="img-responsive img-center" style="max-height:400px;" align="middle">

Go to the _Address Reservation_ sub-menu, and reserve 192.168.2.1 for the MAC of the surface computer and 192.168.2.2 for the MAC of the Raspberry Pi. Disconnect then reconnect power to the router.

<img src="/images/wireless-topside/5.png" class="img-responsive img-center" style="max-height:400px;" align="middle">

Connect the surface computer to the router's wireless network. Open QGroundControl, and it will connect to the ROV wirelessly!
