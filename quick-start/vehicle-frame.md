# Building a Vehicle Frame

## Frame Selection


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

