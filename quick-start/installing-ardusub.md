# Installing ArduSub

ArduSub is the firmware binary which resides on the flash memory of the autopilot board. 

It may be installed (or updated) in one of two ways:
1. Connecting it to a Companion Computer and pressing the appropriate button.
2. Directly connecting the board to a Topside Computer with QGroundControl.

## With a Companion Computer (Automatic Installation)

To load ArduSub onto an autopilot board:

1. Plug a _fully charged_ battery into the vehicle and connect the tether to the topside computer.

2. Navigate to [192.168.2.2:2770/network](192.168.2.2:2770/network) in an internet browser (Chrome, Edge, Firefox, etc.) and ensure that the vehicle has access to a WiFi network. If you do not see a webpage at this address, verify the network settings are correct. Troubleshooting steps can be found [here](/troubleshooting/troubleshooting.html).

3. Navigate to [192.168.2.2:2770/system](192.168.2.2:2770/system). Click the button under the 'Pixhawk Firmware Update' section that says 'Stable'.

4. Wait for the update process to complete, and you are finished!


## Without a Companion Computer (Manual Installation)

Open QGroundControl and navigate to the *Firmware* tab of the *Vehicle Setup* page.

<img src="/images/qgc/firmware-1.png" class="img-responsive img-center" />

Plug in the Pixhawk to the computer's USB port. Once detected, QGroundControl will show a firmware selection box on the right. Choose **"ArduPilot Flight Stack"**, then select **"ChibiOS"**, **"Sub"**, and (assuming you are using a Pixhawk) **"Pixhawk1"** from the dropdown list.

<img src="/images/qgc/firmware-2.png" class="img-responsive img-center" />

Press "OK" at the top right. The firmware will upload the Pixhawk and you'll see the following printout and success message. The Pixhawk should start running and get detected by QGroundControl right away.

<img src="/images/qgc/firmware-3.png" class="img-responsive img-center" />

# Frame Selection

# Completing Calibrations

## Joystick/Gamepad Calibration

Some joysticks require calibration before you can enable them for use with QGroundControl. If your joystick requires calibration, the <strong>Joystick</strong> tab on the <strong>Vehicle Settings</strong> page will be red, and you should follow these steps to calibrate your joystick. If your joystick does not require calibration, the <strong>Joystick</strong> tab will not be red, and you can skip this step!

1. Go to the <strong>Vehicle Settings</strong> page in QGroundControl, then click on the red <strong>Joystick</strong> tab in the sidebar on the left.

2. Ensure the 'TX Mode' selection is set to 3.

3. Click "Calibrate", then click "Next".
 
4. Follow the step-by-step instructions, move the sticks as indicated in the diagram in QGroundControl.

When completed, the <strong>Joystick</strong> tab will no longer be red, and the <strong>Enabled</strong> checkbox on the Joystick page should be checked.

## Button Setup

<p>The default button setup for the BlueROV2 is as shown in the image below:</p>

[guide_image src="/wp-content/uploads/2019/03/joystick-defaults.png" caption=""]

<p>The button functions may be reconfigured in the <strong>Joystick</strong> tab on the <strong>Vehicle Settings</strong> page.</p>

## Sensor Calibration

<p>1. Go to the <strong>Vehicle Settings</strong> page (Gears icon) in QGroundControl and select the red <strong>Sensors</strong> tab in the sidebar on the left.</p>
<p>2. Click on the <strong>Accelerometers</strong> and follow the instructions.</p>
<ul>
	<li>Choose <em>Roll90</em> for the <strong>Autopilot Orientation</strong> selection.</li>
</ul>
<p>3. Click on <strong>Compass</strong> and follow the instructions.</p>
<p>4. Click on <strong>Calibrate Pressure</strong> and wait for the calibration to complete.</p>

<p>When completed, the <em>Sensors</em> tab will no longer be red.</p>

[guide_image src="/wp-content/uploads/2016/06/BlueROV2_Sensor_Calibration_Complete.png" caption=""]

## Configure Motor Directions

<p><strong>The direction that the motors will spin depends on how the vehicle and motors were assembled, so each motor's forward/reverse direction must be configured in software.</strong></p>

<p>To begin, navigate to the Vehicle Settings page in QGroundControl and select the Motors tab in the sidebar on the left, then proceed with the <strong>automatic</strong> (recommended) or <strong>manual</strong> configuration.</p>

[guide_warning]Be sure to keep all body parts and clothing clear of thrusters while the BlueROV2 is armed.[/guide_warning]

[guide_warning]<strong>DO NOT</strong> run thrusters for longer than 30 seconds in air or you will wear out the plastic bearings.[/guide_warning]

### Automatic Configuration

<p>1. Adjust the vehicle's buoyancy to be neutral or slightly <strong>positive</strong>.</p> 

<p>2. Place the vehicle in water with enough room for it to move around slightly without bumping into walls or the bottom. Make sure the vehicle has a bit of slack in the tether so that it can move freely.</p>

<p>3. Click the <strong>Auto-Detect Directions</strong> button, and wait while the vehicle does it's motor direction detection routine.

<p>4. The results of the routine will appear as the routine progresses, and success or failure will be indicated. If the routine failed, you may try again, or configure the motor directions <strong>manually</strong>.

[guide_image src="/wp-content/uploads/2016/06/autodetect-motors.png" caption=""]


### Manual Configuration

<p>1. Go to the Vehicle Settings page in QGroundControl and select the <em>Motors</em> tab in the sidebar on the left.</p>
<p>2. Read and understand the instructions on the setup page.</p>
<p>3. Arm the BlueROV2 by clicking the switch on the page.</p>
<p>4. One at a time, move each slider, and make sure that the motor that spins is pushing air as described in the instructions on the Motor Setup page. If a motor is spinning in the wrong direction, click the corresponding checkbox under the 'Reverse Motor Direction' section to correct the motor rotation.</p>
<p>5. When you are finished with the setup, disarm the ROV by clicking the switch.</p>

[guide_image src="/wp-content/uploads/2019/03/brov2-standard-motor-directions.png" caption=""]
   
## Voltage and Current Measurement Setup

<p>
In the <strong>Power</strong> tab of the QGroundControl Vehicle Setup page, select “Blue Robotics Power Sense Module R2” for the Power Sensor.
</p>

<p><img src="/wp-content/uploads/2018/10/reference-ardusub-power-psmr2.png" width="800" class="img-responsive img-center" /></p>

## SOS Leak Sensor Setup

<p>In the Safety tab, select "Pixhawk Aux6" as the leak detector pin, and set the Logic when dry to "Low."</p>

[guide_image src="/wp-content/uploads/2016/11/SOS_Leak_Sensor_Setup_in_QGC_Edited.png" caption=""]
