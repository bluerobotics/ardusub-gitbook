# Pymavlink

ArduSub communicates with a protocol called MAVLink. Pymavlink is a python implementation of the MAVLink protocol. With pymavlink, it is possible to create a python script to read sensor data and send commands to an ArduSub vehicle.

Please reference the pymavlink [repository](https://github.com/ArduPilot/pymavlink) and [chat](https://gitter.im/ArduPilot/pymavlink) for further information.

# Safety

The autopilot employs a some failsafe mechanisms to keep you and your equipement safe, as well as to prevent your ROV from running away from you during experiments.

All system components that communicate via MAVLink are expected to send a HEARTBEAT message at a constant rate of at least 1 Hz. If the autopilot does not receive a heartbeat from your application after this interval, it will trigger a [failsafe](/operators-manual/failsafes.html).

When the autopilot is being commanded to move via RC_CHANNELS_RAW or MANUAL_CONTROL messages, the messages must be sent at a constant rate like the HEARTBEAT message. Otherwise, the autopilot will execute a failsafe if it has not received an updated command after a timeout period.

## Recommendation

Pymavlink is currently a Python 2 package. It is recommended to install and use it with Python 2.

However Python 3 support is in development. The following instructions assume you are using Python 2 and a Debian-based \(like Ubuntu\) installation.

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

```bash
python
import pymavlink
pymavlink.__doc__
```

This should return some information about pymavlink:

```bash
Python MAVLink library - see http://www.qgroundcontrol.org/mavlink/mavproxy_startpage
```

# Examples

Pymavlink has 3 types of messages:
* `command_long_send`: To create a raw package
* `<message_name>_send`: To send simple mavlink messages
* `mavutil`: Functions to abstract some MAVLink messages

### Connect

There is 3 types of udp connections for `mavlink_connection`:
* **udpout**: It outputs data to a specified address:port (client).
* **udpbcast**: Is the same thing as `udpout`, but will scan for a valid server.
    * With `192.168.1.255` ip, it will scan for `*.1.1` to `*.1.255`.
* **udpin**: It binds to a specific port in address:port (server), it's necessary to receive data from clients (**udpout**) before starting to send any data.
* **udp**: It exist for legacy reasons, works as **udpin**.

##### Autopilot \(E.g: Pixhawk\) connected to the computer via serial

```py
# Import mavutil
from pymavlink import mavutil

# Create the connection
# Need to provide the serial port and baudrate
master = mavutil.mavlink_connection(
            '/dev/ttyACM0',
            baud=115200)

# Restart the ArduSub board !
master.reboot_autopilot()
```

##### Run pyMavlink on the surface computer

```py
import time
# Import mavutil
from pymavlink import mavutil

# Create the connection
#  If using a companion computer
#  the default connection is available
#  at ip 192.168.2.1 and the port 14550
# Note: The connection is done with 'udpin' and not 'udpout'.
#  You can check in http:192.168.2.2:2770/mavproxy that the communication made for 14550
#  uses a 'udpbcast' (client) and not 'udpin' (server).
#  If you want to use QGroundControl in parallel with your python script,
#  it's possible to add a new output port in http:192.168.2.2:2770/mavproxy as a new line.
#  E.g: --out udpbcast:192.168.2.255:yourport
master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')

# Get some information !
while True:
    try:
        print(master.recv_match().to_dict())
    except:
        pass
    time.sleep(0.1)
'''
Output:
{'mavpackettype': 'AHRS2', 'roll': -0.11364290863275528, 'pitch': -0.02841472253203392, 'yaw': 2.0993032455444336, 'altitude': 0.0, 'lat': 0, 'lng': 0}
{'mavpackettype': 'AHRS3', 'roll': 0.025831475853919983, 'pitch': 0.006112074479460716, 'yaw': 2.1514968872070312, 'altitude': 0.0, 'lat': 0, 'lng': 0, 'v1': 0.0, 'v2': 0.0, 'v3': 0.0, 'v4': 0.0}
{'mavpackettype': 'VFR_HUD', 'airspeed': 0.0, 'groundspeed': 0.0, 'heading': 123, 'throttle': 0, 'alt': 3.129999876022339, 'climb': 3.2699999809265137}
{'mavpackettype': 'AHRS', 'omegaIx': 0.0014122836291790009, 'omegaIy': -0.022567369043827057, 'omegaIz': 0.02394154854118824, 'accel_weight': 0.0, 'renorm_val': 0.0, 'error_rp': 0.08894175291061401, 'error_yaw': 0.0990816056728363}
{'mavpackettype': 'HWSTATUS', 'Vcc': 4651, 'I2Cerr': 0}
{'mavpackettype': 'SYSTEM_TIME', 'time_unix_usec': 0, 'time_boot_ms': 75191}
{'mavpackettype': 'EKF_STATUS_REPORT', 'flags': 0, 'velocity_variance': 0.0, 'pos_horiz_variance': 0.000695356575306505, 'pos_vert_variance': 0.20162872970104218, 'compass_variance': 0.0037216085474938154, 'terrain_alt_variance': 0.04920071363449097}
{'mavpackettype': 'VIBRATION', 'time_usec': 75191474, 'vibration_x': 0.03712763264775276, 'vibration_y': 0.03271860256791115, 'vibration_z': 0.05147671326994896, 'clipping_0': 0, 'clipping_1': 0, 'clipping_2': 0}
{'mavpackettype': 'RAW_IMU', 'time_usec': 75430490, 'xacc': 6, 'yacc': -27, 'zacc': -1123, 'xgyro': -1, 'ygyro': 22, 'zgyro': -23, 'xmag': -353, 'ymag': -532, 'zmag': 257}
{'mavpackettype': 'SCALED_IMU2', 'time_boot_ms': 75430, 'xacc': 39, 'yacc': 38, 'zacc': -980, 'xgyro': -45, 'ygyro': -65, 'zgyro': -13, 'xmag': 0, 'ymag': 0, 'zmag': 0}

'''
```

##### Change flight mode

```py
# Import mavutil
from pymavlink import mavutil

# Create the connection
master = mavutil.mavlink_connection('udp:0.0.0.0:14550')
# Wait a heartbeat before sending commands
master.wait_heartbeat()

# Choose a mode
mode = 'STABILIZE'

# Check if mode is available
if mode not in master.mode_mapping():
    print('Unknown mode : {}'.format(mode))
    print('Try:', list(master.mode_mapping().keys()))
    exit(1)

# Get mode ID
mode_id = master.mode_mapping()[mode]
# Set new mode
# master.mav.command_long_send(
#    master.target_system, master.target_component,
#    mavutil.mavlink.MAV_CMD_DO_SET_MODE, 0,
#    0, mode_id, 0, 0, 0, 0, 0) or:
# master.set_mode(mode_id) or:
master.mav.set_mode_send(
    master.target_system,
    mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
    mode_id)

# Check ACK
ack = False
while not ack:
    # Wait for ACK command
    ack_msg = master.recv_match(type='COMMAND_ACK', blocking=True)
    ack_msg = ack_msg.to_dict()

    # Check if command in the same in `set_mode`
    if ack_msg['command'] != mavutil.mavlink.MAVLINK_MSG_ID_SET_MODE:
        continue

    # Print the ACK result !
    print(mavutil.mavlink.enums['MAV_RESULT'][ack_msg['result']].description)
    break
```

##### Arm/Disarm the vehicle

```py
# Import mavutil
from pymavlink import mavutil

# Create the connection
master = mavutil.mavlink_connection('udp:0.0.0.0:14550')
# Wait a heartbeat before sending commands
master.wait_heartbeat()

# http://mavlink.org/messages/common#MAV_CMD_COMPONENT_ARM_DISARM

# Arm
# master.arducopter_arm() or:
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    1, 0, 0, 0, 0, 0, 0)

# Disarm
# master.arducopter_disarm() or:
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    0, 0, 0, 0, 0, 0, 0)
```

##### Send RC \(Joystick\)

```py
# Import mavutil
from pymavlink import mavutil

# Create the connection
master = mavutil.mavlink_connection('udp:0.0.0.0:14550')
# Wait a heartbeat before sending commands
master.wait_heartbeat()

# Create a function to send RC values
# More information about Joystick channels
# here: https://www.ardusub.com/operators-manual/rc-input-and-output.html#rc-inputs
def set_rc_channel_pwm(id, pwm=1500):
    """ Set RC channel pwm value
    Args:
        id (TYPE): Channel ID
        pwm (int, optional): Channel pwm value 1100-1900
    """
    if id < 1:
        print("Channel does not exist.")
        return

    # We only have 8 channels
    #http://mavlink.org/messages/common#RC_CHANNELS_OVERRIDE
    if id < 9:
        rc_channel_values = [65535 for _ in range(8)]
        rc_channel_values[id - 1] = pwm
        master.mav.rc_channels_override_send(
            master.target_system,                # target_system
            master.target_component,             # target_component
            *rc_channel_values)                  # RC channel list, in microseconds.

# Set some roll
set_rc_channel_pwm(2, 1600)

# Set some yaw
set_rc_channel_pwm(4, 1600)

# The camera pwm value is the servo speed
# and not the servo position
# Set camera tilt to 45º with full speed
set_rc_channel_pwm(8, 1900)
```

#### Send Manual Control
```py
# Import mavutil
from pymavlink import mavutil

# Create the connection
master = mavutil.mavlink_connection('udp:0.0.0.0:14550')
# Wait a heartbeat before sending commands
master.wait_heartbeat()

# Send a positive x value, negative y, negative z,
# positive rotation and no button.
# http://mavlink.org/messages/common#MANUAL_CONTROL
# Warning: Because of some legacy workaround, z will work between [0-1000]
# where 0 is full reverse, 500 is no output and 1000 is full throttle.
# x,y and r will be between [-1000 and 1000].
master.mav.manual_control_send(
    master.target_system,
    500,
    -500,
    250,
    500,
    0)

# To active button 0 (first button), 3 (fourth button) and 7 (eighth button)
# It's possible to check and configure this buttons in the Joystick menu of QGC
buttons = 1 + 1 << 3 + 1 << 7
master.mav.manual_control_send(
    master.target_system,
    0,
    0,
    0,
    0,
    buttons)
```

#### Send GPS position

```py
# Import mavutil
from pymavlink import mavutil
import time

# Create the connection
master = mavutil.mavlink_connection('udp:0.0.0.0:14550')
# Wait a heartbeat before sending commands
master.wait_heartbeat()

# GPS_TYPE need to be MAV
while True:
    time.sleep(0.2)
    master.mav.gps_input_send(
        0,          #Timestamp (micros since boot or Unix epoch)
        0,          #ID of the GPS for multiple GPS inputs
        8|16|32,    #Flags indicating which fields to ignore (see GPS_INPUT_IGNORE_FLAGS enum). All other fields must be provided.
        0,          #GPS time (milliseconds from start of GPS week)
        0,          #GPS week number
        3,          #0-1: no fix, 2: 2D fix, 3: 3D fix. 4: 3D with DGPS. 5: 3D with RTK
        0,          #Latitude (WGS84), in degrees * 1E7
        0,          #Longitude (WGS84), in degrees * 1E7
        0,          #Altitude (AMSL, not WGS84), in m (positive for up)
        1,          #GPS HDOP horizontal dilution of position in m
        1,          #GPS VDOP vertical dilution of position in m
        0,          #GPS velocity in m/s in NORTH direction in earth-fixed NED frame
        0,          #GPS velocity in m/s in EAST direction in earth-fixed NED frame
        0,          #GPS velocity in m/s in DOWN direction in earth-fixed NED frame
        0,          #GPS speed accuracy in m/s
        0,          #GPS horizontal accuracy in m
        0,          #GPS vertical accuracy in m
        7           #Number of satellites visible.
    )

```

##### Receive data and filter by message type

```py
# Import mavutil
from pymavlink import mavutil

# Create the connection
# From topside computer
master = mavutil.mavlink_connection('udp:0.0.0.0:14550')


while True:
    msg = master.recv_match()
    if not msg:
        continue
    if msg.get_type() == 'HEARTBEAT':
        print("\n\n*****Got message: %s*****" % msg.get_type())
        print("Message: %s" % msg)
        print("\nAs dictionary: %s" % msg.to_dict())
        # Armed = MAV_STATE_STANDBY (4), Disarmed = MAV_STATE_ACTIVE (3)
        print("\nSystem status: %s" % msg.system_status)
```

##### Send rangefinder/computer vision distance measurement to the autopilot

```py
# Import mavutil
from pymavlink import mavutil
import time

# Connect to the default listening port for
# mavproxy on Blue Robotics companion computer
# This endpoint is created with the 
# '--out udpin:localhost:9000' option with MAVProxy
master = mavutil.mavlink_connection('udpout:localhost:9000')

# Configure the autopilot to use mavlink rangefinder, the autopilot
# will need to be rebooted after this to use the updated setting
master.mav.param_set_send(
    1,
    1,
    "RNGFND_TYPE",
    10, # "MAVLink"
    mavutil.mavlink.MAV_PARAM_TYPE_INT8)
    
min = 10 # minimum valid measurement that the autopilot should use
max = 40 # maximum valid measurement that the autopilot should use
distance = 20 # You will need to supply the distance measurement
type = mavutil.mavlink.MAV_DISTANCE_SENSOR_UNKNOWN
id = 1
orientation = mavutil.mavlink.MAV_SENSOR_ROTATION_PITCH_270 # downward facing
covariance = 0

tstart = time.time()
while True:
    time.sleep(0.5)
    master.mav.distance_sensor_send(
        (time.time() - tstart) * 1000,
        min,
        max,
        distance,
        type,
        id,
        orientation,
        covariance)
```
