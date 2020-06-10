# Pymavlink

ArduSub communicates with a protocol called MAVLink. Pymavlink is a python implementation of the MAVLink protocol. With pymavlink, it is possible to create a python script to read sensor data and send commands to an ArduSub vehicle.

Please reference the pymavlink [repository](https://github.com/ArduPilot/pymavlink) and [chat](https://gitter.im/ArduPilot/pymavlink) for further information.

# Safety

The autopilot employs a some failsafe mechanisms to keep you and your equipement safe, as well as to prevent your ROV from running away from you during experiments.

All system components that communicate via MAVLink are expected to send a HEARTBEAT message at a constant rate of at least 1 Hz. If the autopilot does not receive a heartbeat from your application after this interval, it will trigger a [failsafe](/operators-manual/failsafes.html).

When the autopilot is being commanded to move via RC_CHANNELS_RAW or MANUAL_CONTROL messages, the messages must be sent at a constant rate like the HEARTBEAT message. Otherwise, the autopilot will execute a failsafe if it has not received an updated command after a timeout period.

## Installation

#### Ubuntu 16.04

```sh
# Update list of available packages
apt update

# Install some dependencies
apt install python python-pip python-future

# Install mavproxy module and everything else needed
pip install mavproxy
```

##### Test installation
You can test your installation with python interactive shell.

```bash
python
import pymavlink
print(pymavlink.__doc__)
```
Output:
```bash
Python MAVLink library - see http://www.qgroundcontrol.org/mavlink/mavproxy_startpage
```

Note that `pymavlink.__doc__` will show some information about the package.
This is a record of this example running in python interactive shell:

[![asciicast](https://asciinema.org/a/237333.svg)](https://asciinema.org/a/237333)


# Examples

Pymavlink has 3 types of messages:
* `command_long_send`: To create a raw package
* `<message_name>_send`: To send simple mavlink messages
* `mavutil`: Functions to abstract some MAVLink messages

### Connect

There are 3 types of udp connections for `mavlink_connection`:
* **udpout**: Outputs data to a specified address:port (client).
* **udpbcast**: Broadcasts and locks to the first client to respond (does not handle multiple clients properly)
    * Using the IP `192.168.1.255` all devices from  `192.168.1.1` to `192.168.1.255` will receive the data.
* **udpin**: Binds to a specific port in address:port (server), it's necessary to receive data from clients (**udpout**) before starting to send any data.
* **udp**: Exists for legacy reasons, works as **udpin**.

##### Autopilot \(E.g: Pixhawk\) connected to the computer via serial

[include](pymavlink/serial_connection.py)

##### Run pyMavlink on the surface computer

[include](pymavlink/udp_connection.py)

##### Run pyMavlink on the companion computer

[include](pymavlink/companion_computer.py)

##### Change flight mode

[include](pymavlink/change_flight_mode.py)

##### Arm/Disarm the vehicle

[include](pymavlink/arm_disarm.py)

##### Send RC \(Joystick\)

[include](pymavlink/rc_joystick.py)

#### Send Manual Control

[include](pymavlink/manual_control.py)

#### Control Camera Gimbal

[include](pymavlink/camera_gimbal.py)

#### Read all parameters

[include](pymavlink/read_params.py)

#### Read and write parameters

[include](pymavlink/read_write_params.py)

#### Send GPS position

[include](pymavlink/send_gps.py)

##### Receive data and filter by message type

[include](pymavlink/filter_messages.py)

##### Send rangefinder/computer vision distance measurement to the autopilot

[include](pymavlink/send_rangefinder_vision.py)