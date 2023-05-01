# QGroundControl with MultiCam Support

Releases Page: [https://github.com/DeepwaterExploration/qgroundcontrol/releases](https://github.com/DeepwaterExploration/qgroundcontrol/releases)

Latest Release: <https://github.com/DeepwaterExploration/qgroundcontrol/releases/download/v1.0.0-dwe-release/DWEQGroundControl-installer.exe>

```{important}
For plug and play support, you can follow the {doc}`BlueOS Companion Guide <../guides/blueos_companion>` for installing our software alongisde BlueOS.
```

## Installation

To install our fork of QGroundControl, download the exe installer here. Then just go through the installer!

![DWE QGround Control Installer](../img/qgroundcontrol/DweQGroundInstaller.jpg)

## User Guide

### Enabling Windows Defender Firewall Access

![DWE QGround Control Installer](../img/qgroundcontrol/qgroundfirewall.jpg)

In order to receive the streams from the port, QGroundControl must have access to both private and public networks. Make sure both **public and private** are selected for the stream to work.

```{important} If you did not allow QGroundControl to have access to communicate through the network and you are unable to view streams, it is still possible to allow the application through the firewall.
```

### Setting Ports for Multiple Streams

![DWE QGround Control Installer](../img/qgroundcontrol/DweQGroundStream.jpg)
The ports for the multi-stream viewer automatically sets to 5600, 5601, and 5602. These are the ports we generally recommend to stream from on the Raspberry Pi.

You can change the ports by going into application settings of QGroundControl.
![DWE QGround Control Installer](../img/qgroundcontrol/DweQGroundPorts.jpg)

The UDP ports may not overlap, each stream must be set to a different port. If you only have 2 streams, set one of the streams to an unused port.

```{note} You can still use the normal video stream which would allow you to have 4 camera views maximum. This is ideal for 2 monitor setups where you can have the DWEQGroundControl window on one monitor and the Multi-Video Context window on another. You will need 4 unused USB ports on the RPi to stream 4 cameras from it.
```

### Recording Video

Recording video on our multi-stream app will automatically generate a folder with 3 videos inside, representing each of the video streams. The resolution and framerate will be the same as set by the streamer (ArduSub WebUI). The Recording video settings can be changed in QGroundControl application settings. You can change the Video Decoder even when the source is disabled but to change the file format, you will need to enable a source. You can just select any source and leave the port empty if you are using a 3 camera setup. 

![DWE QGround Control Installer](../img/qgroundcontrol/DweQGroundRecording.jpg)

The red record button on the top left of the screen will start the recording. A timer will show for the time has been recording for. The videos will be saved to the directory set in Application Settings.

![DWE QGround Control Installer](../img/qgroundcontrol/DweQGroundFolder.jpg)

In that folder, you will see another folder `Video`. Inside, there will be folders with different time stamps and in that folder will be the 3 individual camera views. If only 2 views are shown in the window, then only 2 videos will be recorded. 

![DWE QGround Control Installer](../img/qgroundcontrol/DweQGroundFolderSaved.jpg)

## Known Limitations
As of right now, telemetry data is not displayed on the Multi-Stream window. If you are using a single monitor, you will need to readjust the positioning of both windows so you get a good view of the cameras and telemetry data. 

## Troubleshooting

For any questions or issues regarding the DWEQGroundControl application, please feel free to create a new topic in our [forums](https://discuss.exploredeepwater.com/) (be sure to put it under the QGroundControl category so other people can find the solution) or look for other topics in the [QGroundControl software categories](https://discuss.exploredeepwater.com/c/dwe-software/qgroundcontrol/9).
