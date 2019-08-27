# Developers

## How to Get the Code

ArduSub is hosted and maintained on [github](https://github.com/ardupilot/ardupilot.git). You need to clone the repository to have full code access including submodules.

```sh
    git clone https://github.com/ardupilot/ardupilot.git
    cd ardupilot
    git submodule update --init --recursive
```

## Compiling

Before compiling ArduSub, first checkout the 3.6 (soon-to-be stable) version:

```
git fetch --tags
git checkout Sub-3.6
git submodule update --init --recursive
```

To set up your build environment, follow these instructions:

- [Mac Instructions](http://ardupilot.org/dev/docs/building-setup-mac.html)
- [Linux Instructions](http://ardupilot.org/dev/docs/building-setup-linux.html)
- [Windows Instructions](http://ardupilot.org/dev/docs/building-setup-windows.html)

> **Note:** Skip the clone instructions in the links above, as they could cause you to use __master__ instead of __Sub-3.6__ and lead the install scripts to install a different set of tools.

### Python Version (Linux only)
ArduSub 3.6 still requires Python 2 to build. If your System defaults to Python 3 (check your version by running `python --version` in terminal), you need a workaround so that Ardupilot uses Python 2 to build.

Make a dummy folder at your home:

    mkdir ~/bin

And then add Symlinks to Python2 in there:

    ln -s /usr/bin/python2 ~/bin/python
    ln -s /usr/bin/python2-config ~/bin/python-config

Doing this, you have a dummy folder with Python2 binaries. Now you can make a terminal session look for Python in this folder first with

    export PATH=~/bin:$PATH

> **Note:** Master branch currently works fine with Python 3, but since all Ardupilot development is done on it, it is more prone to eventual issues which can take some time to be cleared.

### MAKE (deprecated)
To compile the ArduSub branch with make, it's necessary to be inside the root folder of ArduPilot to use it.
The make command uses the following format:

	make [board type]

For example, to build for the Pixhawk 1:

	make Pixhawk1

The available board types can be seen by entering `make list_boards`.

### WAF
Waf is a global build system for ArduPilot repository, it's necessary to be inside the root folder of ArduPilot to use it.
You can check how to use waf with:

	./waf --help

To configure waf to build ArduSub for Pixhawk 1:

	./waf configure --board Pixhawk1

And to compile:

	./waf build sub

The firmware file will be created at `ardupilot/build/Pixhawk1/bin/ardusub.apj`

#### Uploading Locally

This only works with a direct USB connection to the Pixhawk, and to upload the code:

**waf**: Use `--upload` with the vehicle type (only works after configuring and building with `waf` before).

	./waf --upload sub

### Uploading Remotely

With an Ethernet tether and companion computer, it is possible to flash the Pixhawk firmware through the companion computer - no need to directly access the Pixhawk.

#### Flashing Via Web Interface

Navigate to [192.168.2.2:2770/system](http://192.168.2.2:2770/system) in your browser. Under the 'Pixhawk Firmware Update' section, click 'Browse' and select the firmware file (.apj) saved on your computer. Click 'Upload' and wait for the flashing process to complete.

## Running

The code begins running immediately once uploaded. For Linux-based autopilots, it must be launched or started with launch script. Please see the documentation for your respective autopilot.

## Making a Custom Configuration

One of the biggest additions to the ArduSub code is a six degree-of-freedom motor library that allows a wide variety of motor configurations to be set up easily. The motors libraries for each configuration are built on a set of higher-level motor classes as follows:

    AP_Motors
        |---- AP_MotorsMulticopter
                       |---- AP_MotorsMatrix
                                    |---- AP_Motors6DOF

To add a new motor configuration, you will need to add your custom motor setup to [AP_Motors6DOF.cpp](https://github.com/bluerobotics/ardusub/blob/master/libraries/AP_Motors/AP_Motors6DOF.cpp). Find the following line, and add your frame configuration there. The frame is configured at boot according to the FRAME_CONFIG parameter. You will need to change this parameter to CUSTOM to use your custom frame.

    case AS_MOTORS_CUSTOM_FRAME:
        // Put your custom motor setup here

The behavior of each motor will be defined by its assigned contributions to each of the 6 degrees of freedom in AP_Motors6DOF.cpp. You can use the other frame configurations as a reference guide to defining your own custom configuration. Here is the BlueROV1 frame configuration as an example:

| Motor # | Roll Factor | Pitch Factor | Yaw Factor | Throttle Factor | Forward Factor | Lateral Factor |
| ------- | ----------- | ------------ | ---------- | --------------- | -------------- | -------------- |
| 1       | 0           | 0            | -1.0       | 0               | 1.0            | 0              |
| 2       | 0           | 0            | 1.0        | 0               | 1.0            | 0              |
| 3       | -0.5        | 0.5          | 0          | 0.45            | 0              | 0              |
| 4       | 0.5         | 0.5          | 0          | 0.45            | 0              | 0              |
| 5       | 0           | -1.0         | 0          | 1.0             | 0              | 0              |
| 6       | -0.25       | 0            | 0          | 0               | 0              | 1.0            |

<img src="/images/bluerov-frame.png" class="img-responsive img-center" style="max-height:250px;">

## Troubleshooting

1. If something goes wrong while compiling:
    1. Check the [compiling](#compiling) section to set up your environment.
    2. ArduSub is only compatible with GCC 6. Be sure that "gcc-arm-none-eabi 6" is your "PATH" env with: `echo $PATH | grep gcc-arm-none-eabi`.
        1. It's also possible to add custom paths for the compiler with `export PATH=/your_path/gcc-arm-none-eabi-6-2017-q2-update/bin/:$PATH`. Run `./waf configure --board Pixhawk1` again if compiling with [WAF](#waf).

<p style="font-size:10px; text-align:center">
Sponsored by <a href="http://www.bluerobotics.com/">Blue Robotics</a>. Code released under the <a href="https://github.com/bluerobotics/ardusub/blob/master/COPYING.txt">GPLv3 License</a>. Documentation released under the <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC-NC-SA 4.0</a>.<br />
<a href="https://github.com/bluerobotics/ardusub-gitbook/issues/">Submit a Documentation GitHub Issue here</a> to report any errors, suggestions, or missing information in this documentation.<br />
<a href="https://github.com/bluerobotics/ardusub/issues/">Submit an ArduSub GitHub Issue here</a> to report issues with the ArduSub software.
</p>
