# Companion Web Interface

The Companion computer hosts a useful web-interface with different pages for accessing parameters and functionalities associated with Companion. When a Companion computer is connected to a ground computer, a user can access the web-interface on [192.168.2.2:2770](http://192.168.2.2:2770). Users can access Network, System, Camera and Routing pages alongside a number of other user friendly options as described below.

## Companion Header

The web interface header displays the Companion software version. It provides navigation links to the main configuration pages available in the web interface, options to restart and shutdown the Companion computer, and a switch to enable advanced options on the current page (if available).

<img src="/images/companionversion.png" class="img-responsive img-center" style="max-width:750px" />

## Network

The web interface by default opens at the [Network](http://192.168.2.2:2770/network) page. This page allows users to:

- Configure WiFi
- Check WiFi and Internet Status 
- Configure Ethernet IP address
- Test the network for Uploads and Downloads
- Ethernet network configuration (advanced): The Ethernet interface can be configured as DHCP Server, DHCP Client or Manual (static) mode.
  - Manual: Manual: The interface is configured with a static IP address. This is the default configuration. The default IP address is 192.168.2.2.
  - DHCP Server: The interface is configured as a DHCP server on the 192.168.2.x subnet. The interface IP address will be 192.168.2.2 in this mode.
  - DHCP Client: This is useful for connecting to a router.

<img src="/images/Network.png" class="img-responsive img-center" style="max-width:750px" />

## System

The [System](http://192.168.2.2:2770/system) page provides the following functionalities and features:

- Update software on Companion
- Display Companion computer hardware status parameters and detailed status of processes.

<img src="/images/system1.png" class="img-responsive img-center" style="max-width:750px" />

- Display current ArduSub firmware version on the autopilot
- Download, Update, or Restore pixhawk firmware
- Download a system log for the web interface

<img src="/images/system2.png" class="img-responsive img-center" style="max-width:750px" />

## Camera

The [Camera](http://192.168.2.2:2770/camera) page allows the user to view and make changes to:
 
- Detailed camera settings including Brightness, Contrast, Hue, Sharpness, etc. among others
- Video Streaming settings including selecting a video device, format and frame size

<img src="/images/camera.png" class="img-responsive img-center" style="max-width:750px" />

## Routing

The [Routing](http://192.168.2.2:2770/routing) page can be used to route serial communications between serial devices and network ports. It can be used to create one-to-one, and one-to-many connections. The configuration on this page is persistent and loaded at boot. The configuration is stored in the file `~/routing.conf`.

> **Note:** This program is written in python and is not optimized or well-suited for high-bandwidth applications. The maximum recommended baudrate is 115200. If high bandwidth routing is required, standard linux tools like `tty`, `socat` and `netcat` should be used instead.

<img src="/images/companion-routing/routing-setup.png" class="img-responsive img-center" style="max-width:750px" />

To use the companion routing tool:

- create one or more endpoints with your desired configuration
- add connections between the endpoints as you want
- remove connections by clicking the 'broken link' button next to the configuration
- remove endpoints by clicking the 'trash can' button next to the configuration

<img src="/images/companion-routing/configuration.png" class="img-responsive img-center" style="max-width:750px" />

### Endpoints

An endpoint can be a serial port or a network port. Create an endpoint by entering the desired port settings, and click 'create link'.

**Serial Endpoints**

Select one of the available serial ports from the drop down list, and choose the baudrate to use. The serial port must not be in use by another program! Click 'Add Serial Endpoint' to create the communication endpoint.

<img src="/images/companion-routing/serial-endpoint.png" class="img-responsive img-center" style="max-width:750px" />

**UDP Endpoints**

Enter the ip address and UDP port to use. If the ip address is '0.0.0.0', it will bind the local port as a server. All other ip addresses will result in a client connection. Click 'Add UDP Endpoint' to create the communication endpoint.

<img src="/images/companion-routing/udp-endpoint.png" class="img-responsive img-center" style="max-width:750px" />

### Routes

Endpoints can be connected bidirectionally (typical), or with a one way connection. To begin routing communications between endpoints, choose the endpoints that you wish to connect, the direction to route communications, and click 'connect'.

<img src="/images/companion-routing/create-routes.png" class="img-responsive img-center" style="max-width:750px" />


## Other Pages:

Apart from the four pages that can be accessed via direct links, Companion web interface also provides a few other pages for interacting with some more features.

### MAVProxy

[MAVProxy](http://192.168.2.2:2770/mavproxy) page allows the user to:

- Adjust the MAVProxy settings
- Restart or Restore MAVProxy

<img src="/images/mavproxy.png" class="img-responsive img-center" style="max-width:750px" />

### Git

[Git](http://192.168.2.2:2770/git) page is used for:

- Displaying the current head
- Adding remote repositories
- Updating the system to development branches

<img src="/images/git.png" class="img-responsive img-center" style="max-width:750px" />

### Waterlinked

[Waterlinked](http://192.168.2.2:2770/waterlinked) page can be used to: 

- Setup waterlinked underwater GPS driver
- Restart driver

<img src="/images/waterlinked.png" class="img-responsive img-center" style="max-width:750px" />

### Terminal over browser

[Terminal](http://192.168.2.2:8088) page can be used to:

- Interact with the Companion from a web browser using terminal. (Useful for those who do not use Ubuntu/Linux)

<img src="/images/terminal.png" class="img-responsive img-center" style="max-width:750px" />

### File System Access

[File Manager](http://192.168.2.2:7777) page can be used to:
 
- View, Download, delete, move, rename, or archive the files on the Companion computer directly from the web browser

<img src="/images/files.png" class="img-responsive img-center" style="max-width:750px" />


<p style="font-size:10px; text-align:center">
Sponsored by <a href="http://www.bluerobotics.com/">Blue Robotics</a>. Code released under the <a href="https://github.com/bluerobotics/ardusub/blob/master/COPYING.txt">GPLv3 License</a>. Documentation released under the <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC-NC-SA 4.0</a>.<br />
<a href="https://github.com/bluerobotics/ardusub-docs/issues/">Submit a Documentation GitHub Issue here</a> to report any errors, suggestions, or missing information in this documentation.<br />
<a href="https://github.com/bluerobotics/ardusub/issues/">Submit an ArduSub GitHub Issue here</a> to report issues with the ArduSub software.
</p>
