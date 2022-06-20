# BlueOS Companion Setup for exploreHD

If you have multiple exploreHDs and you would like to stream them simultaneously, you can use the new [BlueOS System](https://docs.bluerobotics.com/ardusub-zola/software/onboard/BlueOS-1.0/). 

:::{dropdown} Streaming with BlueOS Companion

![ArduSub Companion Multiple Streams](../img/ardusub_companion/CompanionnewexploreHD.jpg)

```{note} When setting up the streams, make sure the udp:// is set to 192.168.2.1:560*

Change * to a number for different streams
```
:::

```{note} If using, BlueOS companion, we recommend additionally downloading the **exploreHD Controls** application for full configuration.
```

:::{dropdown} Streaming with exploreHD Controls
:open:

The exploreHD Controls driver works perfectly alongside the BlueOS System, especially when installed with using our docker installation. To install, you can follow {doc}`Our Installation Guide <../software/driverUI>`.

![driverui-light](../img/driverui/driverui.png)

:::
