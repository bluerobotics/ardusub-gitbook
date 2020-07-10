# Installing ArduSub

ArduSub is the firmware binary which resides on the flash memory of the autopilot board. 

It may be installed (or updated) in one of two ways:
1. Connecting it to a Companion Computer and pressing the appropriate button.
2. Directly connecting the board to a Topside Computer with QGroundControl.

## With a Companion Computer (Automatic Installation)

To load ArduSub onto an autopilot board:

1. Navigate to [192.168.2.2:2770/network](192.168.2.2:2770/network) and ensure that the ROV has an internet connection.

2. Navigate to [192.168.2.2:2770/system](192.168.2.2:2770/system). Click the button under the 'Pixhawk Firmware Update' section that says 'Stable'.

3. Wait for the update process to complete, and you are finished!


## Without a Companion Computer (Manual Installation)

Open QGroundControl and navigate to the *Firmware* tab of the *Vehicle Setup* page.

<img src="/images/qgc/firmware-1.png" class="img-responsive img-center" />

Plug in the Pixhawk to the computer's USB port. Once detected, QGroundControl will show a firmware selection box on the right. Choose **"ArduPilot Flight Stack"**, then select **"ChibiOS"**, **"Sub"**, and (assuming you are using a Pixhawk) **"Pixhawk1"** from the dropdown list.

<img src="/images/qgc/firmware-2.png" class="img-responsive img-center" />

Press "OK" at the top right. The firmware will upload the Pixhawk and you'll see the following printout and success message. The Pixhawk should start running and get detected by QGroundControl right away.

<img src="/images/qgc/firmware-3.png" class="img-responsive img-center" />
