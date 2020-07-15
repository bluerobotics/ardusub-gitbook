# Installing ArduSub

ArduSub is the firmware binary which resides on the flash memory of the autopilot board. 

It may be installed (or updated) in one of two ways:
1. Connecting it to a Companion Computer and pressing the appropriate button.
2. Directly connecting the board to a Topside Computer with QGroundControl.

## With a Companion Computer (Automatic Installation)

To load ArduSub onto an autopilot board:

1. Plug a *fully charged* battery into the vehicle and connect the tether to the topside computer.

2. Navigate to [192.168.2.2:2770/network](192.168.2.2:2770/network) in an internet browser (Chrome, Edge, Firefox, etc.) and ensure that the vehicle has access to a WiFi network. If you do not see a webpage at this address, verify the network settings are correct. Troubleshooting steps can be found [here](/troubleshooting/troubleshooting.html).

3. Navigate to [192.168.2.2:2770/system](192.168.2.2:2770/system). Click the button under the *Pixhawk Firmware Update* section that says **Stable**.

4. Wait for the update process to complete, and you are finished!


## Without a Companion Computer (Manual Installation)

Open QGroundControl and navigate to the *Vehicle Setup View* then *Firmware* page.

<img src="/images/qgc/firmware-1.png" class="img-responsive img-center" />

Plug in the Pixhawk to the computer's USB port. Once detected, QGroundControl will show a firmware selection box on the right. Choose **"ArduPilot Flight Stack"**, then select **"ChibiOS"**, **"Sub"**, and (assuming you are using a Pixhawk) **"Pixhawk1"** from the dropdown list.

<img src="/images/qgc/firmware-2.png" class="img-responsive img-center" />

Press "OK" at the top right. The firmware will upload the Pixhawk and you'll see the following printout and success message. The Pixhawk should start running and get detected by QGroundControl right away.

<img src="/images/qgc/firmware-3.png" class="img-responsive img-center" />

# Frame Selection

1. Go to **Vehicle Setup View** then select the **[Frame Setup Page](/reference/ardusub/frame-setup-page.md)**.
2. Click on the corresponding vehicle frame that was originally picked out in the "[Building a Vehicle Frame](/quick-start/vehicle-frame.md)" section of this documentation.
3. Reboot the vehicle or autopilot for the frame selection to be saved and loaded on the next start.

<img src="/images/reference/reference-ardusub-frame.png" class="img-responsive img-center" style="max-height:600px;">

# Completing Calibrations

Before an ArduSub vehicle may be used, several calibration and setup steps must be completed for it to function correctly.

## Joystick/Gamepad Calibration

Some joysticks require calibration before they can be enabled for use with QGroundControl. If a joystick requires calibration, the **Joystick** tab on the **Vehicle Settings View** will be red, and these steps should be followed to calibrate the joystick. If the joystick does not require calibration, the **Joystick** tab will not be red, and this step can be skipped!

1. Go to the **Vehicle Settings View** in QGroundControl, then click on the red **Joystick** tab in the sidebar on the left.
2. Ensure the 'TX Mode' selection is set to 3.
3. Click "Calibrate", then click "Next".
4. Follow the step-by-step instructions, move the sticks as indicated in the diagram in QGroundControl.

When completed, the **Joystick** tab will no longer be red, and the *Enabled* checkbox on the Joystick page should be checked.

## Button Setup

The default button setup for ArduSub is as shown in the image below:

<img src="/images/reference/reference-operational-joystick-defaults.png" class="img-responsive img-center" style="max-height:600px;">

The button functions may be reconfigured in the **Joystick** page.

## Sensor Calibration

1. Go to the **Vehicle Settings View** and select the red **Sensors** tab in the sidebar on the left.
2. Click on the **Accelerometers** and follow the instructions.
* Choose <em>Roll90</em> for the **Autopilot Orientation** selection.
3. Click on **Compass** and follow the instructions.
4. Click on **Calibrate Pressure** and wait for the calibration to complete.

When completed, the **Sensors** tab will no longer be red.

<img src="/images/quick-start/quick-start-sensor-calibration-complete.png" class="img-responsive img-center" style="max-height:600px;">

## Configure Motor Directions

**The direction that the motors will spin depends on how the vehicle and motors were assembled, so each motor's forward/reverse direction must be configured in software.**

To begin, navigate to the **Vehicle Settings View** and select the **Motors** tab in the sidebar on the left, then proceed with the **automatic** (recommended) or **manual** configuration.</p>

> **Warning** Be sure to keep all body parts and clothing clear of thrusters while the vehicle is armed.

> **Warning** **DO NOT** run thrusters for longer than 30 seconds in air or you will wear out the plastic bearings.

### Automatic Configuration

1. Adjust the vehicle's buoyancy to be neutral or slightly **positive**.

2. Place the vehicle in water with enough room for it to move around slightly without bumping into walls or the bottom. Make sure the vehicle has a bit of slack in the tether so that it can move freely.

3. Click the <strong>Auto-Detect Directions</strong> button, and wait while the vehicle does it's motor direction detection routine.

4. The results of the routine will appear as the routine progresses, and success or failure will be indicated. If the routine failed, you may try again, or configure the motor directions **manually**.

<img src="/images/quick-start/quick-start-autodetect-motors.png" class="img-responsive img-center" style="max-height:600px;">


### Manual Configuration

1. Go to the Vehicle Settings page in QGroundControl and select the **Motors** tab in the sidebar on the left.
2. Read and understand the instructions on the setup page.
3. Arm the BlueROV2 by clicking the switch on the page.
4. One at a time, move each slider, and make sure that the motor that spins is pushing air as described in the instructions on the Motor Setup page. If a motor is spinning in the wrong direction, click the corresponding checkbox under the 'Reverse Motor Direction' section to correct the motor rotation.
5. When you are finished with the setup, disarm the ROV by clicking the switch.

<img src="/images/quick-start/quick-start-manual-motor-directions.png" class="img-responsive img-center" style="max-height:600px;">
   
## Voltage and Current Measurement Setup

In the **Power** tab of the QGroundControl Vehicle Setup page, select “Blue Robotics Power Sense Module R2” for the Power Sensor.

<img src="/images/reference/reference-ardusub-power-psmr2.png" class="img-responsive img-center" style="max-height:600px;">

## SOS Leak Sensor Setup

<p>In the Safety tab, select "Pixhawk Aux6" as the leak detector pin, and set the Logic when dry to "Low."</p>

<img src="/images/quick-start/quick-start-leak-sensor.png" class="img-responsive img-center" style="max-height:600px;">
