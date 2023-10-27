# Firmware Release Notes

## Updater Notes
### Mar. 2022

Thanks to DWE OS (previously known as driverUI), the firmware loader no longer needs 2 separate firmware to switch between H.264 and MJPEG streaming.

### Jan. 2022

The firmware loader now has two options of firmware, MJPEG or H.264:

MJPEG will provide the highest quality but bandwidth can go as high as 60Mb/s per camera. 

H.264 will limit to 10Mb/s and use intelligent compression to maximize quality for the given bandwidth.

### Nov. 2021

The loader now disables the other firmware button while loading to minimize the chance of failure



## Firmware
### May. 2023

Fixed issue where when H.264 is used in lower resolution, artifacts would show up on video.

### Mar. 2022

H.264 firmware bitrate has been decreased from 15 Mbps to 10 Mbps for improved stability
