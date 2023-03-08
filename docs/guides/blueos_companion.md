# BlueOS Companion Setup for exploreHD

If you have multiple exploreHDs and you would like to stream them simultaneously, you can use the new BlueOS Companion. The installation instructions can be accessed on the official site [here](https://docs.bluerobotics.com/ardusub-zola/software/onboard/BlueOS-1.0/). 

:::{dropdown} Streaming with BlueOS Companion

![ArduSub Companion Multiple Streams](../img/ardusub_companion/CompanionnewexploreHD.jpg)

```{note} When setting up the streams, make sure the udp:// is set to 192.168.2.1:560*

Change * to a number for different streams
```
:::

```{note} If using BlueOS, we recommend additionally downloading our **DWE OS** application alongside for full configuration. The instructions for which can be accessed below.
```

:::{dropdown} H.264/Bitrate Control for Streaming

DWE OS works perfectly alongside BlueOS. To install, you can follow {doc}`our installation guide <../software/driverUI>`.

![driverui-light](../img/driverui/driverui.png)

:::
