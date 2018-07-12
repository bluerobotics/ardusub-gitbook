# S.I.T.L (Software In The Loop)

SITL is a simulator that allows you to run ArduSub without any hardware. It is a build of the autopilot code using an ordinary C++ compiler, giving you a native executable that allows you to test the behaviour of the vehicle.

## Installation
To configure and run SITL for the first time in your computer, take a look in [**Running SITL**](http://ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html) ArduPilot documentation.

## Running ArduSub SITL

This part assumes that you have already set up SITL on your machine.
First is necessary to be inside ArduSub folder.
```sh
cd ardupilot/ArduSub
```
To execute SITL with `sim_vehicle.py`.
```sh
sim_vehicle.py -L RATBeach --out=udp:0.0.0.0:14550 --map --console
```
After that, ArduSub SITL will compile and start to run, you'll be able to connect it with QGroundControl and control it.

<img src="/images/sitl_ardusub_qgc.png" class="img-responsive img-center" style="max-height:400px;">

For more information about `sim_vehicle.py` and the options available, check:
```sh
sim_vehicle.py --help
```

### Running ArduSub SITL with Gazebo

To run ArduSub SITL with Gazebo, it's necessary to:
1. [Install Gazebo-7 or Gazebo-8](http://gazebosim.org/tutorials?tut=install_ubuntu)
2. Install [freebuoyancy_gazebo](https://github.com/bluerobotics/freebuoyancy_gazebo#install) plugin for buoyancy simulation.
3. Install [ardupilot_gazebo/add_link](https://github.com/patrickelectric/ardupilot_gazebo/tree/add_link#usage-) plugin for ardupilot-gazebo communication. *add_link* is a branch that provides actuation over sdf links, after the `git clone`, it's necessary to run `git checkout add_link`.
3. Run BlueRov2 Gazebo model
    1. Download bluerov_ros_playground
        ```bash
        git clone https://github.com/patrickelectric/bluerov_ros_playground
        ```

    2. Run Gazebo model
        ```bash
        cd bluerov_ros_playground
        source gazebo.sh
        gazebo worlds/underwater.world -u
        # Start the simulation
        ```

4. Execute ArduPilot SITL
    ```bash
    sim_vehicle.py -f gazebo-bluerov2 -L RATBeach --out=udp:0.0.0.0:14550 --console
    ```

The console will start to display the output if the connection was successful.

<img src="/images/gazebo_sitl.gif" class="img-responsive img-center" style="max-height:400px;">
