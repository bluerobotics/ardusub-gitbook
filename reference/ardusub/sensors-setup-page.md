# Sensors Setup Page

The Sensors Setup page allows users to calibrate the vehicle's accelerometer, compass, pressure sensor.

Available sensors are displayed as a list of buttons beside the sidebar. Sensors marked with green are already calibrated, while sensors marked with red require calibration prior to operation. Sensors with no color marks are simple calibrations that are optional.

<img src="/images/reference/reference-ardusub-sensors.png" class="img-responsive img-center" style="max-height:600px;">

## Accelerometer Calibration

<img src="/images/reference/reference-ardusub-sensors-accelerometer.png" class="img-responsive img-center" style="max-height:600px;">

To calibrate the flight controller accelerometers the vehicle will need to be placed and held in a number of orientations.

The calibration steps are:

1. Click the **Accelerometer** sensor button.
2. Click OK to start the calibration.
3. Position the vehicle based on text instructions in the center display. 
4. Click the Next button to capture each position.

## Compass Calibration

<img src="/images/reference/reference-ardusub-sensors-compass.png" class="img-responsive img-center" style="max-height:600px;">

You need to rotate the vehicle randomly around all axes until the progress bar fills all the way to the right and the calibration completes. When the calibration completes you will get the following results:

<img src="/images/reference/reference-ardusub-sensors-compass-complete.png" class="img-responsive img-center" style="max-height:600px;">

## Level Horizon

If the horizon (as shown in the HUD) is not level after completing accelerometer calibration you can calibrate the level horizon for your vehicle. You will be asked to place the vehicle in a level orientation while it captures the information.

Place the vehicle in its level flight orientation on a level surface:
For planes this is the position during level flight (planes tend to have their wings slightly pitched up!)
For copters this is the hover position.
Click OK to start the calibration.

## Calibrate Pressure

This calibration set's the altitude to zero at the current pressure.
To perform Pressure calibration:
Click the Calibrate Pressure button and then Ok.

The calibration result is immediately displayed.
