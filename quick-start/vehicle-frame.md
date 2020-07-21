# Building a Vehicle Frame

## Frame Selection

The first step in building an ArduSub vehicle is to pick a vehicle "frame" from which to mount and orient thrusters. Some frames use less thrusters, while others have better manueverability (strafe, pitch/roll stability).

ArduSub includes a high-level motor library that can configure motors in any configuration. This library is used to implement a number of supported frame configurations. 

All configurations are shown from **top-down view**. Green thrusters indicate counter-clockwise propellers and blue thrusters indicate clockwise propellers (or vice-versa). The numbers next to each thruster correspond to the numbered main output on the [autopilot board](/introduction/hardware-options/required-hardware/autopilot.html) when the ESC signal wires are plugged in.

Currently supported are:

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
			<p><strong>Vectored ROV w/ Four Vertical Thrusters</strong>, an 8-thruster configuration with 6-DOF control and heavy-lifting capacity. Used for the <a href="https://bluerobotics.com/introducing-bluerov2-heavy/"><em>BlueROV2 Heavy</em></a>. (Frame: <code>vectored6dof</code>)</p>
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
		<td align="center">
			<img src="/images/simplerov-5.png" class="img-responsive img-center" style="max-height:250px;">
			<p><strong>ROV</strong> with a lateral thruster and side-by-side vertical thrusters. (Frame: <code>simplerov</code>)</p>
		</td>
	</tr>
</table>

### Custom Frame

If the vehicle thruster configuration a user wishes to build is not one of the pre-build frames, then a custom frame may be configured in using this documentation: [Making a Custom Configuration](http://www.ardusub.com/developers/developers.html#making-a-custom-configuration)

## Component Selection

The minumum required electronic components can be found in the [Hardware Options: Required Hardware](/introduction/hardware-options/required-hardware.html) section of this documentation book.

Vehicle frames are commonly built out of corrosion resitant material such as HDPE and aluminum.

## Wiring and Connections

The exact wiring configuration depends on the vehicle configuration and the hardware used. The following are the standard channel assignments. Please see the "Frame Selection" for standard thruster numbering.

The MAIN and AUX output numbers reference the Pixhawk 1 PWM outputs.

<img src="/images/quick-start/quick-start-pixhawk-outputs.png" class="img-responsive img-center" style="max-height:600px;">

| PWM Channel | Connection  |
|------------:|:------------|
| MAIN OUT Channel 1   | Thruster #1 |
| MAIN OUT Channel 2   | Thruster #2 |
| MAIN OUT Channel 3   | Thruster #3 |
| MAIN OUT Channel 4   | Thruster #4 (if used) |
| MAIN OUT Channel 5   | Thruster #5 (if used) |
| MAIN OUT Channel 6   | Thruster #6 (if used) |
| MAIN OUT Channel 7   | Thruster #7 (if used) |
| MAIN OUT Channel 8   | Thruster #8 (if used) |
| User Configurable (MAIN or AUX) | LED Lights  |
| User Configurable (MAIN or AUX) | Camera Tilt Servo |

The hardware also has other input/output ports including I<sup>2</sup>C and serial ports. These are the recommended connections for those ports.

| Port                    | Connection                             |
|------------------------:|:---------------------------------------|
| I<sup>2</sup>C          | Pressure sensor (MS58XX)               |
| USB Serial Port         | Companion computer (if used)           |
| Power Port              | Power Module                           |

## Reference Frames

If the idea of deciding on which components to use is too daunting for first time builders, Blue Robotics sells the [BlueROV2](https://bluerobotics.com/store/rov/bluerov2/) which may be used as a semi-complete "reference frame" from which to understand the ArduSub control system. Components can be reused and reconfigured for custom frame designs.
