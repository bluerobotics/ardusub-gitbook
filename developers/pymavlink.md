# Pymavlink

ArduSub communicates with a protocol called MAVLink. Pymavlink is a python implementation of the MAVLink protocol. With pymavlink, it is possible to create a python script to read sensor data and send commands to an ArduSub vehicle.

Please reference the pymavlink [repository](https://github.com/ArduPilot/pymavlink) and [chat](https://gitter.im/ArduPilot/pymavlink) for further information.

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

### Connect

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

##### Autopilot \(E.g: Pixhawk\) connected to the computer via UDP

```py
# Import mavutil
from pymavlink import mavutil

# Create the connection
#  If using a companion computer
#  the default connection is available
#  at ip 192.168.2.1 and the port 14550
master = mavutil.mavlink_connection('udp:192.168.2.1:14550')

# Get some information !
while True:
    try:
        print(master.recv_match().to_dict())
    except:
        pass
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
master.set_mode(mode_id)
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

# Arm
master.arducopter_arm()

# Disarm
master.arducopter_disarm()
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
    rc_channel_values = [65535 for _ in range(8)]
    rc_channel_values[id] = pwm
    #http://mavlink.org/messages/common#RC_CHANNELS_OVERRIDE
    master.mav.rc_channels_override_send(
        master.target_system,                # target_system
        master.target_component,             # target_component
        *rc_channel_values)                  # RC channel list, in microseconds.

# Set some forward command !
set_rc_channel_pwm(4, 1600)

# Set camera tilt to 45º
set_rc_channel_pwm(7, 1900)

# set lights 1 in maximum state
set_rc_channel_pwm(8, 1900)

# set lights 2 in medium state
set_rc_channel_pwm(9, 1600)
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
    if msg == None:
        continue
    if msg.get_type() == 'HEARTBEAT':
        print("\n\n*****Got message: %s*****" % msg.get_type())
        print("Message: %s" % msg)
        print("\nAs dictionary: %s" % msg.to_dict())
        # Armed = MAV_STATE_STANDBY (4), Disarmed = MAV_STATE_ACTIVE (3)
        print("\nSystem status: %s" % msg.system_status)
```

