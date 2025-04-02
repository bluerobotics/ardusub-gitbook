{% include "../../archive-notice.html" %}

# MAVLink REST API

Starting from companion 0.0.19, a MAVLink REST API ([http://192.168.2.2:4777/mavlink](http://192.168.2.2:4777/mavlink)) endpoint is available.
It provides access to the last MAVLink messages sent by the vehicle in [json format](https://www.json.org).

The json contains the same structure defined by the [MAVLink protocol standard](https://mavlink.io/en/messages/common.html),
where each **field** exists and can be accessible.
Besides the MAVLink specification, each message contains an structure called `message_information`,
that provides the time, frequency and counter of such message.

It's possible to access:
- All messages available in [/mavlink](http://192.168.2.2:4777/mavlink)
- Specific messages via subpath, E.g: [/mavlink/HEARTBEAT](http://192.168.2.2:4777/mavlink/HEARTBEAT) or [/mavlink/ATTITUDE](http://192.168.2.2:4777/mavlink/ATTITUDE).
- Single fields via nested subpath, E.g: [/mavlink/HEARTBEAT/mavtype/type](http://192.168.2.2:4777/mavlink/HEARTBEAT/mavtype/type) or or [/mavlink/ATTITUDE/pitch](http://192.168.2.2:4777/mavlink/ATTITUDE/pitch).

You can check the following json as a minimal example of what you can find from the main path `/mavlink`:
```json
{
  "ATTITUDE": {
    "message_information": {
      "counter": 680870,
      "frequency": 9.998090744018556,
      "time": {
        "first_message": "2020-02-05T23:51:19.189911121+00:00",
        "last_message": "2020-02-06T18:46:19.301620958+00:00"
      }
    },
    "pitch": -0.24140535295009613,
    "pitchspeed": -0.002207340206950903,
    "roll": -0.21160905063152313,
    "rollspeed": -0.00044677406549453735,
    "time_boot_ms": 68104588,
    "type": "ATTITUDE",
    "yaw": -1.3117148876190186,
    "yawspeed": 0.0022055506706237793
  },
  "DISTANCE_SENSOR": {
    "covariance": 0,
    "current_distance": 0,
    "id": 0,
    "mavtype": {
      "type": "MAV_DISTANCE_SENSOR_UNKNOWN"
    },
    "max_distance": 700,
    "message_information": {
      "counter": 1,
      "frequency": null,
      "time": {
        "first_message": "2020-02-05T23:51:19.245754158+00:00",
        "last_message": "2020-02-05T23:51:19.245778012+00:00"
      }
    },
    "min_distance": 20,
    "orientation": {
      "type": "MAV_SENSOR_ROTATION_PITCH_270"
    },
    "time_boot_ms": 4482,
    "type": "DISTANCE_SENSOR"
  },
  "HEARTBEAT": {
    "autopilot": {
      "type": "MAV_AUTOPILOT_ARDUPILOTMEGA"
    },
    "base_mode": {
      "bits": 81
    },
    "custom_mode": 19,
    "mavlink_version": 3,
    "mavtype": {
      "type": "MAV_TYPE_SUBMARINE"
    },
    "message_information": {
      "counter": 68101,
      "frequency": 1.0000146627426147,
      "time": {
        "first_message": "2020-02-05T23:51:18.970019298+00:00",
        "last_message": "2020-02-06T18:46:18.978841566+00:00"
      }
    },
    "system_status": {
      "type": "MAV_STATE_CRITICAL"
    },
    "type": "HEARTBEAT"
  },
  "POWER_STATUS": {
    "Vcc": 5000,
    "Vservo": 0,
    "flags": {
      "bits": 0
    },
    "message_information": {
      "counter": 680870,
      "frequency": 9.998090744018556,
      "time": {
        "first_message": "2020-02-05T23:51:19.199533151+00:00",
        "last_message": "2020-02-06T18:46:19.311397896+00:00"
      }
    },
    "type": "POWER_STATUS"
  },
  "RAW_IMU": {
    "message_information": {
      "counter": 680871,
      "frequency": 9.998106002807615,
      "time": {
        "first_message": "2020-02-05T23:51:19.099038934+00:00",
        "last_message": "2020-02-06T18:46:19.325582710+00:00"
      }
    },
    "time_usec": 3680079699,
    "type": "RAW_IMU",
    "xacc": -237,
    "xgyro": -42,
    "xmag": 150,
    "yacc": 204,
    "ygyro": -1,
    "ymag": 67,
    "zacc": -920,
    "zgyro": 37,
    "zmag": 461
  },
  "RC_CHANNELS": {
    "chan10_raw": 1100,
    "chan11_raw": 1100,
    "chan12_raw": 0,
    "chan13_raw": 0,
    "chan14_raw": 0,
    "chan15_raw": 0,
    "chan16_raw": 0,
    "chan17_raw": 0,
    "chan18_raw": 0,
    "chan1_raw": 1500,
    "chan2_raw": 1500,
    "chan3_raw": 1500,
    "chan4_raw": 1500,
    "chan5_raw": 1500,
    "chan6_raw": 1500,
    "chan7_raw": 1500,
    "chan8_raw": 1500,
    "chan9_raw": 1100,
    "chancount": 0,
    "message_information": {
      "counter": 680870,
      "frequency": 9.998090744018556,
      "time": {
        "first_message": "2020-02-05T23:51:19.220836357+00:00",
        "last_message": "2020-02-06T18:46:19.323932621+00:00"
      }
    },
    "rssi": 0,
    "time_boot_ms": 68104589,
    "type": "RC_CHANNELS"
  },
  "SCALED_PRESSURE": {
    "message_information": {
      "counter": 680870,
      "frequency": 9.998090744018556,
      "time": {
        "first_message": "2020-02-05T23:51:19.228165860+00:00",
        "last_message": "2020-02-06T18:46:19.327375453+00:00"
      }
    },
    "press_abs": 1240.5726318359375,
    "press_diff": 0.0,
    "temperature": 19203,
    "time_boot_ms": 68104592,
    "type": "SCALED_PRESSURE"
  },
  "SERVO_OUTPUT_RAW": {
    "message_information": {
      "counter": 680870,
      "frequency": 9.998090744018556,
      "time": {
        "first_message": "2020-02-05T23:51:19.216933118+00:00",
        "last_message": "2020-02-06T18:46:19.321753267+00:00"
      }
    },
    "port": 0,
    "servo1_raw": 1500,
    "servo2_raw": 1500,
    "servo3_raw": 1500,
    "servo4_raw": 1500,
    "servo5_raw": 1500,
    "servo6_raw": 1500,
    "servo7_raw": 0,
    "servo8_raw": 0,
    "time_usec": 3680079638,
    "type": "SERVO_OUTPUT_RAW"
  }
}
```
