# Features

ArduSub has many features including:
- Built-in support for several vehicle frame options and motor configurations (custom configurations are possible too)
- High extensibility in software and hardware for customization
- Attitude and Heading Reference System (AHRS) and Inertial Navigation Filter (EKF)
- Extensive user-configurable parameter system
- Well developed ground control station software for piloting and configuration
- Compatibility with many development tools targeting MAVLink-enabled vehicles
- Sensor and data logging
- **No Programming Required**

## Supported Frames

ArduSub includes a high-level motor library that can configure motors in any configuration. This library is used to implement a number of supported frame configurations. All configurations are shown from **top-down view**. Green thrusters indicate counter-clockwise propellers and blue thrusters indicate clockwise propellers (or vice-versa). Currently supported are:

<table>
	<tr>
		<td align="center">
			<img src="/images/bluerov-frame.png" class="img-responsive img-center" style="max-height:250px;">
			<p><strong>BlueROV1 Configuration</strong> with 6-DOF thruster positioning. (Frame: <code>bluerov</code>)</p>
		</td>
		<td align="center">
			<img src="/images/vectored-frame.png" class="img-responsive img-center" style="max-height:250px;">
			<p><strong>Vectored ROV</strong> with side-by-side vertical thrusters. Used for the <a href="http://bluerov2.com"><em>BlueROV2</em></a>. (Frame: <code>vectored</code>)</p>
		</td>
		<td align="center">
			<img src="/images/vectored6dof-frame.png" class="img-responsive img-center" style="max-height:250px;">
			<p><strong>Vectored ROV w/ Four Vertical Thrusters</strong>, an 8-thruster configuration with 6-DOF control and heavy-lifting capacity. (Frame: <code>vectored6dof</code>)</p>
		</td>
	</tr>
	<tr>
		<td align="center">
			<img src="/images/simplerov-3.png" class="img-responsive img-center" style="max-height:250px;">
			<p><strong>ROV</strong> with a single vertical thruster. (Frame: <code>simplerov</code>)</p>
		</td>
		<td align="center">
			<img src="/images/simplerov-4.png" class="img-responsive img-center" style="max-height:250px;">
			<p><strong>ROV</strong> with side-by-side vertical thrusters. (Frame: <code>simplerov</code>)</p>
		</td>
	</tr>
</table>

## Supported Hardware

The ArduPilot project has support for a great variety of hardware platforms. ArduSub firmware is provided for many of these platforms, but **only the Pixhawk 1 is fully tested and supported**.

These are platforms that have been reported to work with ArduSub:

- Pixhawk
- Pixhawk 2
- Pixhawk Mini

Please let us know if you have tested ArduSub on another platform!

## Capabilities

- **Feedback control and stability:** Based on a multicopter autopilot system, the ArduSub controller has accurate feedback control to actively maintain orientation.
- **Depth hold:** Using pressure-based depth sensors, the ArduSub controller can maintain depth within a few centimeters.
- **Heading hold:** By default, the ArduSub automatically maintains its heading when not commanded to turn.
- **Camera Tilt:** Camera tilt control with servo or gimbal motors through the joystick or gamepad controller.
- **Light Control:** Control of subsea lighting through the joystick or gamepad controller.

## Extensibility

In addition to the standard onboard sensors (IMU, compass), the ArduSub controller directly supports a number of external sensors including:

- Pressure/depth sensors for measurement and auto depth-hold ([example](https://www.bluerobotics.com/store/electronics/bar30-sensor-r1/))
- GPS for position at the surface (does not work underwater)

Other sensors, and in particular high-bandwidth and specialized sensors, are integrated as *Companion* sensors, attached to the companion computer and running alongside *ArduSub* and sharing communication pathways. This allows rapid integration of new and unique payloads and allows you to use the manufacturer's user interface to control the sensor.

Sensor integration is still in the early phase, but will eventually include sensors such as:

- Depth sounders
- Scanning sonars
- Conductivity sensors
