# Camera

The Companion Computer software contains a series of drivers which will stream HD video from the vehicle to the Ground Control Station (GCS) at the surface. Only one camera may be connected to the Companion at a time. Support for multiple camera streams is planned, but not implemented at this time.

# Supported Cameras

## USB Cameras

Most modern USB cameras are compatible with the Companion software as long as they have the following specifications:

* H.264 Output
* 1080p resolution (4k cameras are not supported)

The following USB cameras have been tested to work:

* [Blue Robotics Low-Light HD USB Camera](https://www.bluerobotics.com/store/electronics/cam-usb-low-light-r1/)

## Camera Serial Interface (CSI) Cameras

With a Camera Serial Interface (CSI) input on the Raspberry Pi, this type of camera may be used with the Companion software. A Raspberry Pi camera module came pre-installed on the BlueROV2 until mid-2017 when it was replaced by the Low-Light HD USB Camera.

The following CSI cameras have been tested to work:

* [Raspberry Pi Camera Module v2](https://www.raspberrypi.org/products/camera-module-v2/)

## Ethernet Cameras

Although no Ethernet cameras have been tested, the minimum requirements for working directly with QGroundControl are:

* H.264 Output
* RTSP


