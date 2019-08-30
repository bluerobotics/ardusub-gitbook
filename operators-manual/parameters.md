# Parameters

Parameters are the user configurable settings for the autopilot. They are stored on internal memory on the autopilot, and are loaded when the autopilot boots up. Most of the configuration in the *Vehicle Setup* page in QGroundControl takes place by changing parameter values on the autopilot behind the scenes. Some parameters require a reboot to take effect, but most do not.

## Saving and Loading

The entire set of parameters on the autopilot can be saved to a text file. Parameters can also be loaded from a text file, overwriting the current parameters on the autopilot. The parameter file reflects all of the settings that the user can adjust in the autopilot. This makes it a very useful tool for troubleshooting, and it is important to save and share a parameter file with the community if you need support with setting up or operating.

To save or load parameters using QGroundControl, go to the *Vehicle Setup Page*, and click the *Parameters* tab. Click the *Tools* dropdown menu in the upper right hand corner and select *Save to file* or *Load from file*.

#### Refreshing

Some of the parameters are dynamic and will change under certain circumstances or after different events. In order to reload the current parameter values on the autopilot click *Refresh*.

#### Resetting

The entire set of parameters can be erased and reset to the default values that are configured in the autopilot firmware by clicking *Reset all to defaults* (ArduSub V3.5+ only).

<img src="/images/configuring/save-parameters.png" class="img-responsive img-center" style="max-height:600px;">

## Parameter Files

These files have the recommended parameters for ArduSub, making it easy to setup and update parameters on your vehicle. These parameters will not adjust your accelerometer calibration, compass calibration, or motor directions, but will change joystick button setup, PID controller values, lights and other peripheral configurations, and all other parameters.

<p style="font-size:10px; text-align:center">
Sponsored by <a href="http://www.bluerobotics.com/">Blue Robotics</a>. Code released under the <a href="https://github.com/bluerobotics/ardusub/blob/master/COPYING.txt">GPLv3 License</a>. Documentation released under the <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">CC-NC-SA 4.0</a>.<br />
<a href="https://github.com/bluerobotics/ardusub-gitbook/issues/">Submit a Documentation GitHub Issue here</a> to report any errors, suggestions, or missing information in this documentation.<br />
<a href="https://github.com/bluerobotics/ardusub/issues/">Submit an ArduSub GitHub Issue here</a> to report issues with the ArduSub software.
</p>
