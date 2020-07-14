# Getting Ready for Your First Dive 
Before putting the BlueROV2 in the water, there are a few things that you need to do.

Your first dive should be in a body of water that is shallow, still, and clear. We recommend a pool or a test tank. Testing in a more controlled environment will provide a good opportunity to check that the ROV is ballasted correctly. It will also allow you to confirm that your controller is set up correctly and your ROV is behaving how you expect it to.

## Connecting Your Batteries 
To get ready for your first dive, you need to start by connecting a charged battery using the same process as shown in the Swapping Batteries section.

## Setting up Your Topside Control 
To set up your topside control follow the instructions on the Software Setup page.

## Controller Functions 
The BlueROV2 comes with the button setup shown below as a default:


If you do not like the button settings, you can change the button setup in QGroundControl.

1. Go to Settings then select “Joystick”.

2. Under “Button actions:” QGroundControl shows what all buttons are currently set to control.

3. Press the button that you are interested in changing. The button number will light up.

4. Select what you would like the button to do from the dropdown to the right of the button number.

### Dive Modes 
In Manual Mode the BlueROV2 will only output motor controls based on the pilot input from the joysticks. There is no feedback stabilization, heading holding, or depth holding.
In Stabilize Mode the BlueROV2 will stabilize roll to level and it will maintain heading when not commanded to turn. The vertical control is left entirely to the pilot.
In Depth Hold Mode the BlueROV2 will hold depth unless you command it to dive/ascend. It will also stabilize roll to level and maintain heading when not commanded to turn.
Pre-Dive Chec

# Pre-Dive Checklist
Put the ROV on the ground and make sure that people are clear of the thrusters.
Check to make sure the camera tilt function and lights work. If they do not, please see the [Troubleshooting](#troubleshooting) section.
Put the ROV in Manual Mode.
Arm the ROV.
Press the forward/reverse stick forward to check that the vectored thrusters are spinning freely.
Press the ascend/descend stick forward to check that the vertical thrusters are spinning freely.
Disarm the ROV.
Launch.

# All Launches 
Do not launch the ROV near swimmers or divers.
Do not release the ROV prior to it touching the water. If necessary, use the tether to lower it down. When lowereing the ROV, keep the dome away from any hard or sharp objects.
Do not launch in water that is too shallow to freely drive the ROV.
Keep the ROV away from boats that do not know that the ROV is in the water.
Do not arm until the ROV is in the water and the launcher is clear of the ROV.
## Boat Launch 
Keep the ROV and tether clear of the boat’s propellers or jets.
Make sure that the captain of the boat knows that the ROV is about to be launched.
## Shore Launch 
Do not launch the ROV in heavy surf.
You may need to walk the ROV into the water to get to a point where the water is deep enough to drive the ROV.

# Operation 
## Tether Management 
When diving the BlueROV2 the tether will require some active management. Here are some guidelines for good tether management:

Keep the tether away from propellers or jets if you are operating on a boat.
Keep the tether and ROV away from other boats that are not aware that it is in the water.
Keep the tether away from sharp objects such as coral, rocks, etc.
Do not deploy too much tether. Excess tether in the water will add drag to the ROV and opportunity for the tether to get caught on something.
Do not deploy the tether over sharp edges or rough ground.
Do not step on the tether.

## Driving Guidelines 
Do not drive into a sandy bottom. If you do drive into a sandy bottom, stop driving the vehicle and allow it to float up to prevent sand from getting into the vertical thrusters.
Drive smoothly and on low gain when possible to maximize battery life.
Do not touch coral with the ROV to prevent damage to the coral.
Avoid driving into seaweed when possible. Seaweed can get sucked into and stop the thrusters from spinning.
When diving, it is helpful to follow down a chain or a line to give a frame of reference.

## Battery Monitoring 
Be sure to occasionally glance at the battery voltage in the instrument panel.
It is recommended to recover the ROV once the battery reaches 12.5V to avoid discharging below 12.0V, which can permanently damage a 4S battery or shorten its lifespan.

# Recovery 
Disarm the BlueROV2 prior to attempting to recover it.

## Powered Recovery 
Typically, you will be recovering the BlueROV2 when it is under power.

The ROV pilot should find the tether and follow it back to the launching area.
While the pilot is driving back pull in the tether slack. Clean debris off of the tether and inspect for cuts or nicks while pulling in.
When the ROV arrives back to the launching location, disarm the ROV.
Pick up the ROV directly if practical, or pull the ROV up using the tether. Avoid sharp or hard object while lifting the ROV by the tether; allow space for the ROV to swing.
Remove the vent plug from the battery enclosure vent penetrator.
Disconnect the battery.
## Unpowered Recovery 
If the ROV loses power or connection to QGroundControl while diving, you should do the following:

Pull the tether in at a moderate pace. Don’t try to pull it in as fast as possible.
