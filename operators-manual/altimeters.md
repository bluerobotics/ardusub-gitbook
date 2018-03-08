# Altimeters

Ardusub supports the use of an altimeter or range measurement input. If the range measurement is downward facing (altimeter), then the altimeter will be used to assist depth hold. When the altimeter measurement is valid, depth hold mode will automatically begin following the altimeter measurement and hold a distance above the bottom, as opposed to a distance from the surface when the pressure sensor is used.

# Parameters

The altimeter is configured in ArduSub as a 'rangefinder', and the relevant parameters are in the RNGFND_ group. ArduSub will will only use the altimeter measurement to assist depth hold mode if the measurement is in the valid range specified by the RNGFND_MIN and RNGFND_MAX parameters. ArduSub will always report the altimeter measurement to the groundstation, regardless of whether or not it is being used or is valid. The rangefinder distance can be displayed in QGC by clicking the small gear near the telemetry values, and selecting APMSubInfo.rangefinder for display. If you want the altimeter to be used for depth hold, specify the minimum and maximum valid measurements according to the range where you want the altimeter to be used. This can be the full range that the hardware is capable of, or a smaller range within those capabilities. If you do not want the altimeter to be used for depth hold mode, set both the minimum and maximum parameters to 0.

These are the relevant parameters for configuration:

- RNGFND_TYPE: The type of rangefinder to be used. Ardusub currently only supports MAVLink rangefinder input. Changes to this parameter require a reboot to take effect.
- RNGFND_MIN: The minimum valid measurement to be used for depth hold assist
- RNGFND_MAX: The maximum valid measurement to be used for depth hold assist
- RNGFND_GAIN: Gain to control how quickly the vehicle will respond to changes in the rangefinder measurement. Higher values = faster reaction. 
