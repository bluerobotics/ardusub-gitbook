# Import mavutil
from pymavlink import mavutil
import time

# Wait for server connection
def wait_conn(master):
    msg = None
    while not msg:
        master.mav.ping_send(
            time.time(), # Unix time
            0, # Ping number
            0, # Request ping of all systems
            0 # Request ping of all components
        )
        msg = master.recv_match()
        time.sleep(0.5)

# Connect to the default listening port for
# mavproxy on Blue Robotics companion computer
master = mavutil.mavlink_connection('udpout:localhost:9000')

# Send a ping to start connection and wait for any reply.
wait_conn(master)

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