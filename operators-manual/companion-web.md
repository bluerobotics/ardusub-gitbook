#Companion Web Interface

The companion computer hosts a useful web-interface with different pages for accessing parameters and functionalities associated with companion. When a companion computer is connected to a ground computer, a user can access the web-interface on [192.168.2.2:2770](http://192.168.2.2:2770). Users can access Network, System, Camera and Routing pages alongside a number of other user friendly options as described below. 

##Companion Header

The header on Companion Web Interface now displays the companion software version. It also features a toggle switch that enables advanced options on the network page. 

[Header Image]

##Network

The web interface by default opens at the [Network](http://192.168.2.2:2770/network) page. This page allows users to:

- Configure WiFi
- Check WiFi and Internet Status 
- Configure Ethernet IP address
- Test the network for Uploads and Downloads
- Change companion network configuration settings in advanced mode. There are three network configuration options available.
  - Manual: In this configuration, companion has a static IP(192.168.2.2) and this is the default network configuration mode with a fresh companion image.
  - DHCP Server: In this configuration, companion acts as a server and assigns an IP address to any device connected to it on the same network. The IP address of companion is set to static IP(192.168.2.2) in this mode.
  - DHCP Client: In this configuration, companion acts as a client and gets an IP address from any active DHCP server on the network. In this mode, companion does not have any fixed IP address pre-assigned to it.
 
[Image for advanced options]

<img src="/images/network-setup.png" class="img-responsive img-center" style="max-width:750px" />

##System

The [System](http://192.168.2.2:2770/system) page provides the following functionalities and features:

- Display companion computer hardware status parameters
- Give detailed information about status of processes running on companion. Shows basic error debugging information for most common issues.
- Display companion software version
- Display ArduSub version information
- Download system/webui logs for additional information and error identification
- Update software on companion
- Download, Update, or Restore pixhawk firmware

<img src="/images/system-setup.png" class="img-responsive img-center" style="max-width:750px" />

##Camera

The [Camera](http://192.168.2.2:2770/camera) page allows the user to view and make changes to:
 
- Detailed camera settings including Brightness, Contrast, Hue, Sharpness, etc. among others
- Video Streaming settings including selecting a video device, format and frame size

<img src="/images/camera-setup.png" class="img-responsive img-center" style="max-width:750px" />

##Routing

The [Routing](http://192.168.2.2:2770/routing) page can be used to configure Serial and UDP endpoints as well as to create routes. 

<img src="/images/routing-setup.png" class="img-responsive img-center" style="max-width:750px" />

##Other Pages:

Apart from the four pages that can be accessed via direct links, companion web interface also provides a few other pages for interacting with some more features.

###MAVProxy

[MAVProxy](http://192.168.2.2:2770/mavproxy) page allows the user to:

- Adjust the MAVProxy settings
- Restart or Restore MAVProxy

<img src="/images/mavproxy-setup.png" class="img-responsive img-center" style="max-width:750px" />

###Git

[Git](http://192.168.2.2:2770/git) page is used for:

- Displaying the current head
- Adding remote repositories

<img src="/images/git-setup.png" class="img-responsive img-center" style="max-width:750px" />

###Waterlinked

[Waterlinked](http://192.168.2.2:2770/waterlinked) page can be used to: 

- Setup waterlinked underwater GPS driver
- Restart driver

<img src="/images/waterlinked-setup.png" class="img-responsive img-center" style="max-width:750px" />

###Terminal over browser

[Terminal](http://192.168.2.2:8088) page can be used to:

- Interact with the companion from a web browser using terminal. (Useful for those who do not use Ubuntu/Linux)

<img src="/images/terminal.png" class="img-responsive img-center" style="max-width:750px" />

###File System Access

[File Manager](http://192.168.2.2:7777) page can be used to:
 
- View, Download, delete, move, rename, or archive the files on a companion computer directly from the web browser.

<img src="/images/files.png" class="img-responsive img-center" style="max-width:750px" />


<p style="font-size:10px; text-align:center">
Sponsored by <a href="http://www.bluerobotics.com/">Blue Robotics</a>. Code released under the <a href="https://github.com/bluerobotics/ardusub/blob/master/COPYING.txt">GPLv3 License</a>. Documentation released under the <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC-NC-SA 4.0</a>.<br />
<a href="https://github.com/bluerobotics/ardusub-docs/issues/">Submit a Documentation GitHub Issue here</a> to report any errors, suggestions, or missing information in this documentation.<br />
<a href="https://github.com/bluerobotics/ardusub/issues/">Submit an ArduSub GitHub Issue here</a> to report issues with the ArduSub software.
</p>
