# Cameras

Cameras are essential for ROVs operation, it's possible to configure and (if necessary) modify the companion software to
allow the usage of multiple cameras or a different one of the supported models.

> Note: H.264 is the only format that is used by default in companion. It's necessary to use compression formats to
> stream video to the surface, this helps to send data without shrugging with variable bandwidth, high quality images
> and limited hardware.

## Eligible cameras

To check if it's possible to use a camera without configuration or any modification, check the following steps:

1. Go to http://192.168.2.2:8088 to access the companion terminal.
2. Check the connected devices with: `v4l2-ctl --list-devices`
    ``` sh
    # In this example you can see two cameras connected
    # mmal service 16.1: The raspberry camera
    # H264 USB Camera: The low light usb camera
    mmal service 16.1 (platform:bcm2835-v4l2):
        /dev/video2

    H264 USB Camera (usb-3f980000.usb-1.2):
        /dev/video0
        /dev/video1
    ```
3. Take a look in the camera capabilities with: `v4l2-ctl --list-formats-ext --device=/dev/videoX`
    - Where X is the camera ID (0, 1, 2 ...).
    - As you can see in the following output, both cameras can supply video in H.264 format, but only two of three
    devices can supply it, `/dev/video0` will only supply MJPG, that is a unsupported compressed format by companion.
    ```
    pi@raspberrypi:~ $ v4l2-ctl --list-formats-ext --device=/dev/video0
    ioctl: VIDIOC_ENUM_FMT
	Index       : 0
	Type        : Video Capture
	Pixel Format: 'MJPG' (compressed)
	Name        : Motion-JPEG
		Size: Discrete 1920x1080
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.040s (25.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 1280x720
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.040s (25.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 800x600
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.040s (25.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 640x480
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.040s (25.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 640x360
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.040s (25.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 352x288
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.040s (25.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 320x240
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.040s (25.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 1920x1080
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.040s (25.000 fps)
			Interval: Discrete 0.067s (15.000 fps)

	Index       : 1
	Type        : Video Capture
	Pixel Format: 'YUYV'
	Name        : YUYV 4:2:2
		Size: Discrete 640x480
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.040s (25.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 800x600
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 640x360
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.040s (25.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 352x288
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.040s (25.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 320x240
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.040s (25.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 640x480
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.040s (25.000 fps)
			Interval: Discrete 0.067s (15.000 fps)

    pi@raspberrypi:~ $ v4l2-ctl --list-formats-ext --device=/dev/video1
    ioctl: VIDIOC_ENUM_FMT
	Index       : 0
	Type        : Video Capture
	Pixel Format: 'H264' (compressed)
	Name        : H.264
		Size: Discrete 1920x1080
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.040s (25.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 1280x720
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.040s (25.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 800x600
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.040s (25.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 640x480
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.040s (25.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 640x360
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.040s (25.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 352x288
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.040s (25.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 320x240
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.040s (25.000 fps)
			Interval: Discrete 0.067s (15.000 fps)
		Size: Discrete 1920x1080
			Interval: Discrete 0.033s (30.000 fps)
			Interval: Discrete 0.040s (25.000 fps)
			Interval: Discrete 0.067s (15.000 fps)

    pi@raspberrypi:~ $ v4l2-ctl --list-formats-ext --device=/dev/video2
    ioctl: VIDIOC_ENUM_FMT
	Index       : 0
	Type        : Video Capture
	Pixel Format: 'YU12'
	Name        : Planar YUV 4:2:0
		Size: Stepwise 32x32 - 2592x1944 with step 2/2

	Index       : 1
	Type        : Video Capture
	Pixel Format: 'YUYV'
	Name        : YUYV 4:2:2
		Size: Stepwise 32x32 - 2592x1944 with step 2/2

	Index       : 2
	Type        : Video Capture
	Pixel Format: 'RGB3'
	Name        : 24-bit RGB 8-8-8
		Size: Stepwise 32x32 - 2592x1944 with step 2/2

	Index       : 3
	Type        : Video Capture
	Pixel Format: 'JPEG' (compressed)
	Name        : JFIF JPEG
		Size: Stepwise 32x32 - 2592x1944 with step 2/2

	Index       : 4
	Type        : Video Capture
	Pixel Format: 'H264' (compressed)
	Name        : H.264
		Size: Stepwise 32x32 - 2592x1944 with step 2/2

	Index       : 5
	Type        : Video Capture
	Pixel Format: 'MJPG' (compressed)
	Name        : Motion-JPEG
		Size: Stepwise 32x32 - 2592x1944 with step 2/2

	Index       : 6
	Type        : Video Capture
	Pixel Format: 'YVYU'
	Name        : YVYU 4:2:2
		Size: Stepwise 32x32 - 2592x1944 with step 2/2

	Index       : 7
	Type        : Video Capture
	Pixel Format: 'VYUY'
	Name        : VYUY 4:2:2
		Size: Stepwise 32x32 - 2592x1944 with step 2/2

	Index       : 8
	Type        : Video Capture
	Pixel Format: 'UYVY'
	Name        : UYVY 4:2:2
		Size: Stepwise 32x32 - 2592x1944 with step 2/2

	Index       : 9
	Type        : Video Capture
	Pixel Format: 'NV12'
	Name        : Y/CbCr 4:2:0
		Size: Stepwise 32x32 - 2592x1944 with step 2/2

	Index       : 10
	Type        : Video Capture
	Pixel Format: 'BGR3'
	Name        : 24-bit BGR 8-8-8
		Size: Stepwise 32x32 - 2592x1944 with step 2/2

	Index       : 11
	Type        : Video Capture
	Pixel Format: 'YV12'
	Name        : Planar YVU 4:2:0
		Size: Stepwise 32x32 - 2592x1944 with step 2/2

	Index       : 12
	Type        : Video Capture
	Pixel Format: 'NV21'
	Name        : Y/CrCb 4:2:0
		Size: Stepwise 32x32 - 2592x1944 with step 2/2

	Index       : 13
	Type        : Video Capture
	Pixel Format: 'BGR4'
	Name        : 32-bit BGRA/X 8-8-8-8
    Size: Stepwise 32x32 - 2592x1944 with step 2/2
    ```
4. Now, after we did check that both devices can supply H.264 streams, it's possible to go in
    http://192.168.2.2:2770/camera and configure the video source and configuration.
    ![](/images/companion/developers-camera.png)


# Tips
 - If the camera does not contain **Pixel Format** equal to **H264 (compressed)**, further configuration will be necessary,
but this is not recommended, since it can result in bandwidth and hardware issues.

 - If the camera does not appears in **step 2** of *Eligible cameras*, check if the device appears with
`ls /dev/video*` or with `lsusb`. If both commands fail, take a look in the connection or the power supply.

 - For further problems, take a look in [Troubleshooting](troubleshooting/troubleshooting.md).
