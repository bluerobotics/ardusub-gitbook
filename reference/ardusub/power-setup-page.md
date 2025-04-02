{% include "../../archive-notice.html" %}

# Power Setup Page
The Power Setup page is used to configure power sensing module parameters.

<img src="/images/reference/reference-ardusub-power-other.png" class="img-responsive img-center" style="max-height:600px;">

## Battery Voltage/Current Calibration
Enter data for your battery/power module from its data sheet: number of cells, full voltage per cell, empty voltage per cell. If provided, also enter voltage divider and amps-per-volt information.

QGroundControl can be used to calculate appropriate voltage divider and amps-per-volt values from measurements:

1. Measure the voltage from the battery using a multimeter.
2. Click Calculate next to the Voltage divider field. On the prompt that appears:
    * Enter the measured voltage.
    * Click Calculate to generate a new voltage-divider value.
    * Click Close to save the value into the main form.
3. Measure the current from the battery.
4. Click Calculate next to the Amps per volt field. On the prompt that appears:
    * Enter the measured current.
    * Click Calculate to generate a new amps per volt value.
    * Click Close to save the value into the main form.

## Blue Robotics Power Sense Module R2

QGC has a profile for the BlueRobotics Power Sense Module R2, which can be selected from the dropdown menu.

<img src="/images/reference/reference-ardusub-power-psmr2.png" class="img-responsive img-center" style="max-height:600px;">
