# QGroundControl with MultiCam Support

[https://github.com/DeepwaterExploration/qgroundcontrol/releases](https://github.com/DeepwaterExploration/qgroundcontrol/releases)

```{note} DWE QGroundControl is in beta release as of currently. A full release can be expected soon.
```

## Installation

To install our fork of QGroundControl, download the exe installer here. Then just go through the installer!

![DWE QGround Control Installer](../img/dweqgroundinstaller.jpg)

## User Guide
### Enabling Windows Defender Firewall Access
![DWE QGround Control Installer](../img/qgroundfirewall.jpg)

In order to receive the streams from the port, QGround Control must have access to both private and public networks. Make sure both are enabled for the stream to work.

### Setting Port for Multiple Streams
![DWE QGround Control Installer](../img/dweqgroundstream.jpg)
The ports for the multi-stream viewer automatically sets to 5600, 5601, and 5602. 

You can change the port by going into application settings of QGroundControl.
![DWE QGround Control Installer](../img/dweqgroundports.jpg)

The UDP ports may not overlap, each stream must be set to a different port. If you only have 2 streams, set one of the streams to an unused port.

```{note}You can still use the normal video stream which would allow you to have 4 camera views maximum. This is ideal for 2 monitor setups where you can have the DWEQGroundControl window on one monitor and the Multi-Video Context window on another. You will need 4 unused USB ports on the RPi to stream 4 cameras from it.
```

### Recording Video 
Recording video on our multi stream app will automatically generate a folder with 3 videos inside, representing each of the video streams. The resolution and framerate will be the same as set by the streamer (ArduSub WebUI). The Recording video settings can be changed in QGroundControl application settings. You can change the Video Decoder even when the source is disabled but to change the file format, you will need to enable a source. You can just select any source and leave the port empty if you are using a 3 camera setup. 

![DWE QGround Control Installer](../img/dweqgroundrecording.jpg)

The red record button on the top left of the screen will start the recording. A timer will show for the time its been recording for. The videos will be saved to the directory set in Application Settings.

![DWE QGround Control Installer](../img/dweqgroundfolder.jpg)

In that folder, you will see another folder `Video`. Inside, there will be folders with different time stamps and in that folder will be the 3 individual camera views. If only 2 views are shown in the window, then only 2 videos will be recorded. 

![DWE QGround Control Installer](../img/dweqgroundfoldersaved.jpg)

## Known Limitations
As of right now, telemetry data is not displayed on the Multi Stream window. If you are using a single monitor, you will need to readjust the positioning of both windows so you get a good view of the cameras and telemetry data. 