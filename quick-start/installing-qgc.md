# QGroundControl Installation

>**Note** The latest recommended version of QGroundControl is **v4.2.3**. If your software is out of date, please uninstall the QGC application and download the latest version below.

## Download

Download and install QGroundControl using one of the links below.

- [Windows](https://s3.amazonaws.com/downloads.bluerobotics.com/QGC/latest/QGroundControl-installer.exe)
- [Mac](https://s3.amazonaws.com/downloads.bluerobotics.com/QGC/latest/QGroundControl.dmg)
- [Linux](https://s3.amazonaws.com/downloads.bluerobotics.com/QGC/latest/QGroundControl.AppImage)

>**Note** The installers above are the latest stable versions of QGC that the ArduSub developers have tested and verified. Newer versions may exist, but have not been verified. Use newer versions from the main QGroundControl project at your own risk.

>**Note** Linux needs additional GStreamer dependencies, see the [QGroundControl User Guide](https://docs.qgroundcontrol.com/en/getting_started/download_and_install.html#ubuntu) for details.

## Folder Structure

After running the installer, the following folders will be installed in the default location:

**/Documents/QGroundControl/**
* **CrashLogs:** Data files from QGC application crashes.
* **Logs:** Downloaded vehicle logs. (.bin)
* **Missions:** Downloaded mission plans. (.plan)
* **Parameters:** Saved vehicle parameter files. (.params)
* **Telemetry:** Saved telemetry files from vehicles. (.tlog)
* **Video:** Recorded video subtitle files. (.mkv/.mov/.mp4 and .ass)

## Running the Application

Run the application executable as per your operating system.

>**Note** The Windows installer creates 3 shortcuts: QGroundControl, GPU Compatibility Mode, GPU Safe Mode. Use the first shortcut unless you experience startup or video rendering issues. For more information see [QGC Install/Config Problems > Windows: UI Rendering/Video Driver Issues](https://docs.qgroundcontrol.com/en/Support/troubleshooting_qgc.html#opengl_troubleshooting).
