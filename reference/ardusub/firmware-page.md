# Firmware Page

The Firmware Page allows ArduSub firmware to be downloaded from the internet and directly installed onto Pixhawk-family flight-controller boards. By default QGC will install the current stable version of the selected autopilot, but you can also choose to install beta builds, daily builds, or custom firmware files.

QGroundControl can also install the firmware for SiK Radios and PX4 Flow devices.

Loading Firmware is currently not available on tablet or phone versions of QGroundControl.

Connect Device for Firmware Update
Before you start installing Firmware all USB connections to you vehicle must be disconnected (both direct or through a telemetry radio). The vehicle must not be powered by a battery.

2. Plug in the Pixhawk to the computer's USB port. Once detected, QGroundControl will show a firmware selection box on the right. 
3. Choose **"ArduPilot Flight Stack"**, then select **"ChibiOS"**, **"Sub"**, and (assuming you are using a Pixhawk) **"Pixhawk1"** from the dropdown list.

<img src="/images/qgc/firmware-2.png" class="img-responsive img-center" />

4. Press "OK" at the top right. 
5. The firmware will upload the Pixhawk and you'll see the following printout and success message. The Pixhawk will reboot and then will automatically connect with QGroundControl.

<img src="/images/qgc/firmware-3.png" class="img-responsive img-center" />
