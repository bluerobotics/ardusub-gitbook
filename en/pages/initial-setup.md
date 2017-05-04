# Initial Setup

First-time setup of the autopilot includes downloading and installing the QGroundControl, mounting the controller to the vehicle, connecting it to the tether, power, and motors, and then performing initial configuration and calibration.

## Wiring and Connections

The exact wiring configuration depends on the vehicle configuration and the hardware used. The following are the standard channel assignments. Please see the [frame configurations](/introduction/#supported-frames) for standard thruster numbering.

| PWM Channel | Connection  |
|------------:|:------------|
| Channel 1   | Thruster #1 |
| Channel 2   | Thruster #2 |
| Channel 3   | Thruster #3 |
| Channel 4   | Thruster #4 (if used) |
| Channel 5   | Thruster #5 (if used) |
| Channel 6   | Thruster #6 (if used) |
| Channel 7   | Thruster #7 (if used) |
| Channel 8   | Thruster #8 (if used) |
| User Configurable | LED Lights  |
| User Configurable | Camera Tilt Servo |

The hardware also has other input/output ports including I<sup>2</sup>C and serial ports. These are the recommended connections for those ports.

| Port                    | Connection                             |
|------------------------:|:---------------------------------------|
| I<sup>2</sup>C          | Pressure sensor (MS58XX)               |
| Telem1 Serial Port      | Tether (if using serial)               |
| USB Serial Port         | Companion computer (if used)           |
| Power Port              | Power Module                           |

## Install QGroundControl

Download the latest stable version of [QGroundControl](http://qgroundcontrol.com/downloads/).

## Setup Raspberry Pi

If using the *Advanced Electronics Package*, a Raspberry Pi computer is used as a *companion computer* with the Pixhawk. The computer handles video streaming and relaying communications to the surface through an Ethernet connection.

For information on how to set up the Raspberry Pi for use with ArduSub, see the [Raspberry Pi Setup Page](/raspi-setup/).

## Loading Firmware on Pixhawk

Compiled firmware is now available and can be downloaded from [firmware.ardusub.com](http://firmware.ardusub.com/Sub/stable/v3.4/). Firmware is only available for the following hardware right now:

* Pixhawk (px-v2)

Please see the [Developer section](/developers/) for instructions on how to compile from source.

### Loading Through Raspberry Pi

If you're using the Raspberry Pi companion computer and an Ethernet tether, it's usually most convenient to flash the *ArduSub* firmware to the Pixhawk through the Raspberry Pi. Please note that the [Raspberry Pi must be already set up](#setup-raspberry-pi) and then you can follow the [instructions to flash through Raspberry Pi](/raspi-setup/#flashing-pixhawk-through-ssh).

### Loading Through QGroundControl

Install the most recent daily build of [QGroundControl](#install-qgroundcontrol) and navigate to the *Firmware* tab of the settings page.

<img src="/images/qgc/firmware-1.png" class="img-responsive img-center" />

Plug in the Pixhawk to the computer's USB port. Once detected, QGroundControl will show a firmware selection box on the right. Choose "ArduPilot Flight Stack" and then check the "Advanced Settings" checkbox. From the dropdown box that appears, choose "Custom firmware file...".

<img src="/images/qgc/firmware-2.png" class="img-responsive img-center" />

Press "OK" at the top right and you will be prompted to select the firmware file (which will probably be named "ArduSub-v2.px4"). Make sure you download the most recent [stable firmware](http://firmware.ardusub.com/Sub/stable/v3.4/) and choose it here.

The firmware will upload the Pixhawk and you'll see the following printout and success message.

<img src="/images/qgc/firmware-3.png" class="img-responsive img-center" />

## Host Computer Setup

Just a few small setup items are required on the host computer. Please see the details here depending on which tether interface is being used.

### Install FTDI Drivers (Serial/Fathom-S Tether Interface Only)

Mac and Linux computers usually have the FTDI drivers installed already. For Windows computers, the driver will probably have to be installed. [Sparkfun has a great tutorial](https://learn.sparkfun.com/tutorials/how-to-install-ftdi-drivers/all) on installing the drivers properly.

Once installed, the Fathom-S Tether Interface will appear as a serial port on the computer.

### Set Up Internet Sharing (Ethernet/Fathom-X Tether Interface Only)

In an Ethernet-based setup, the Raspberry Pi defaults to the IP address of 192.168.2.2. The **host computer must be set up with an IP address of 192.168.2.1** in order to receive communications and video. See instructions below:

#### Windows

1. Go to *Control Panel > Network and Internet > Network Connections* and right click on the Ethernet adapter, then choose *Properties*.
2. In the properties dialog, choose *Internet Protocol Version 4 (TCP/IPv4)*, then click *Properties*.
<img src="/images/qgc/win/windows-properties-window.png" class="img-responsive img-center" style="max-width:600px" />
3. In the next dialog, enter *192.168.2.1* as the computer's IP address. Enter *255.255.255.0* for the subnet mask.
<img src="/images/qgc/win/windows-ipv4-settings.png" class="img-responsive img-center" style="max-width:500px" />

#### Linux

To be completed

#### Mac

1. From System Prefrences, go to Network Settings and set IP for Ethernet to Manual, the address to 192.168.2.1, and the subnet mask to 255.255.255.0.
2. From System Prefrences, go to Sharing and click "Internet Sharing". Choose "Wi-Fi" for the source and your Ethernet port or adapter for the destination.

## Connect QGC to Controller

The controller can be connected to QGC through several different methods depending on the hardware used.

### Serial Port Connection

If using a serial port, simply connect the port to the computer and open QGC. The controller should automatically connect to QGC and onboard data will be downloaded.

### Ethernet Connection with Companion Computer

If an Ethernet connection is used, then a *companion computer* must be used to relay communications between the Pixhawk autopilot and the surface computer. The Pixhawk is connected to the *companion computer* via USB.

Please see the [Raspberry Pi Setup](/raspi-setup/) page for more details on setting up the *companion computer*.

### Ethernet Connection with Linux Autopilot (Navio, BBBmini, etc.)

For Linux based autopilots, the network connection is launched when the ArduSub code is started. For examples, please see the documentation for your respective autopilot.

## Sensor Calibration

Once the controller is connected to QGC for the first time, we must calibrate the accelerometers, compass, and joystick.

1. Go to the settings tab in QGC and select the red *Sensors* tab on the left sidebar.
2. Choose your autopilot orientation:
	- `None` for level orientation (such as the BlueROV1)
	- `Roll90` for the BlueROV2
3. Click on *Accelerometers* and follow the instructions.
4. Click on *Compass* and follow the instructions.
5. When completed, the *Sensors* tab will no longer be red.

## Important Parameters to Set

There are a few parameters that must be set before the Pixhawk will output to the thrusters, lights, and servos. We'll also disable the failsafes. These will be enabled in the future but are currently not suited for *ArduSub*.

Find the Parameters tab on the settings page and change the following settings:

| Parameter         | Value to Set         |
|------------------:|:---------------------|
| ARMING_CHECK      | Disabled             |
| BRD_SAFETYENABLE  | Disabled             |


You **have to power cycle the system** after setting these parameters to get them to work.

## Joystick/Gamepad Calibration

The first time you use a new joystick or gamepad in QGroundControl, you will be asked to calibrate it. This allows QGC to detect which axis is which and what the range of each axis is.

**Important *ArduSub*-specific Instructions:** The calibration process is a little confusing for *ArduSub*. This will be fixed in upcoming versions of QGC, but for now, you must follow this process.

1. Click "Calibrate" on the joystick page, then click "Next".
2. **We want to calibrate the joysticks in the opposite way that QGC asks us to do it**. When asked to move each axis, move the following sticks:
- Throttle: right stick up/down
- Yaw: right stick right/left
- Roll: left stick right/left
- Pitch: left stick up/down

## Button Setup

*ArduSub* provides a number of parameters to map controller buttons to various functions. This setup is required as there are no defaults configured.

We recommend the button assignments shown in the image below:

<img src="/images/controller.png" class="img-responsive img-center" />

Each button can be assigned to one primary function and one alternate "shift" function. If the "shift" functions are used, then a "shift" button must be assigned. This works like the shift key on your keyboard, altering the functionality of other buttons while pressed.

You can assign the buttons to various functions on the *Joystick* settings tab. Pressing each button will light up the button number and then the desired function can be chosen. See the image below for an example set (on a Mac). Note that the button numbering is different between controllers and operating systems so this won't necessarily be the same as your setup.

<img src="/images/qgc/button-setup-1.png" class="img-responsive img-center" />

Note, if using a Logitech gamepad, pressing the "mode" button causes the left joystick and the button pad to switch places. Make sure the light next to "mode" is *not* illuminated. Also note that to use an Xbox controller or Logitech gamepad in "X-input" mode, you must install an X-input driver. We recommend [360Controller](https://github.com/360Controller/360Controller/releases).

## Setup Voltage and Current Measurement

On the *Power* tab choose the appropriate setup. If using the standard 3DR Power Module, choose *Analog Voltage and Current*, the appropriate battery capacity, and the *Power Module 90A*. The battery capacity depends on the battery that you are using on your ROV and should be entered in *mAh*.

<img src="/images/qgc/power-setup-1.png" class="img-responsive img-center" />

## Flight Mode Setup

There are several flight modes available: *Manual*, *Stabilize*, and *DepthHold*. On the *Flight Modes* tab, set the first flight mode (the default) to *Manual* and set the second and third to *Stabilize* and *DepthHold*. The remaining flight modes can be left on *Stabilize* or any other setting.

<img src="/images/qgc/flight-mode-setup-1.png" class="img-responsive img-center" />

Remember, when you set up the joystick above, you added buttons to change flight modes. These flight modes can be entered by pressing one of those buttons or by selecting the desired mode from the toolbar in QGroundControl.

## Camera Tilt Setup (if used)

Select the *Camera* tab. The "Gimbal Tilt" settings are used for the camera tilt. Choose whichever channel the servo is plugged into for "Output channel" and *RC8* for "Input channel". Valid output channels are any of the unused motor outputs (RC1-RC8), and Aux outputs 1-4 (RC9-RC12). Select *Servo* for the "Type" under "Gimbal Settings" on the right.

<img src="/images/qgc/camera-tilt-setup-1.png" class="img-responsive img-center" />

Is desired, you can check the *Stabilize* box, which will enable auto-stabilization of the camera based on the vehicle pitch angle. We generally leave this unchecked.

## Lights Setup

The lights feature is currently setup to support lights that use a standard servo PWM signal for control. This is done by connecting the *RCIN9* input, which contains the light control signal, to the appropriate output. To do this, please find the parameter `RCx_FUNCTION`, where `x` is the output channel that corresponds to the lights, and set it to `RCIN9`.

For example, if the lights are connected to output channel 7, then set `RC7_FUNCTION` to `RCIN9` as shown below.

<img src="/images/qgc/lights-setup-1.png" class="img-responsive img-center" />

Note, this setup only works with lights that are controllable with a servo PWM pulse, such as the Blue Robotics *Lumen* Lights.

## Configuring Motor Directions

Due to clockwise and counterclockwise propellers, as well as wiring, the motor directions will have to be tested and corrected during initial setup. *ArduSub* includes a set of parameters for this purpose. The parameters are called `MOT_1_DIRECTION` for motors 1-8 and valid values are *normal* or *reverse*.

Make sure you complete all above steps before completing this step. We generally follow this process to check motor rotation directions:

1. Set the flight mode to "Manual"
2. Arm vehicle
3. Move the "forward" joystick forward and verify that the thrusters that produce some forward thrust are operating in the correct direction and blowing out the back of the vehicle
4. Move the "vertical" joystick upwards and verify that the thrusters that produce some vertical thrust are operating in the correct direction and blowing air downwards

Provided that the correct frame configuration was chosen during compilation, you should not need to perform any more validation than that.

<p style="font-size:10px; text-align:center">
Sponsored by <a href="http://www.bluerobotics.com/">Blue Robotics</a>. Code released under the <a href="https://github.com/bluerobotics/ardusub/blob/master/COPYING.txt">GPLv3 License</a>. Documentation released under the <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC-NC-SA 4.0</a>.<br />
<a href="https://github.com/bluerobotics/ardusub-docs/issues/">Submit a Documentation GitHub Issue here</a> to report any errors, suggestions, or missing information in this documentation.<br />
<a href="https://github.com/bluerobotics/ardusub/issues/">Submit an ArduSub GitHub Issue here</a> to report issues with the ArduSub software.
</p>
