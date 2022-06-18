# ArduSub Companion Setup for exploreHD
## Streaming with ArduSub Companion
```{note} **As of November 20, 2021, all exploreHD/HDCam shipped will feature a new firmware that allows the cameras to be plug and play with ArduSub Companion without the need for drivers.**

If you notice the video stream is very sluggish, your exploreHD/HDCam may be running outdated firmware. Click [here](https://docs.exploredeepwater.com/software/firmware.html) to update the firmware.
```

## Streaming Multiple exploreHDs with ArduSub Companion
If you have multiple exploreHDs and you would like to stream them simultaneously, you can use the new [ArduSub Companion 1.0](https://docs.bluerobotics.com/ardusub-zola/software/onboard/BlueOS-1.0/). 

![ArduSub Companion Multiple Streams](../img/ardusub_companion/CompanionnewexploreHD.jpg)

```{note} When setting up the streams, make sure the udp:// is set to 192.168.2.1:560*

Change * to a number for different streams
```

