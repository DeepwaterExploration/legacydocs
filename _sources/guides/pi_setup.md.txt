# Raspberry Pi Streaming Setup for exploreHD

```{note}
The following instructions are for if you want to set up streaming from a Raspberry Pi without ArduSub. If you want plug-and-play compatibility we recommend following {doc}`this guide <./blueos_companion>` for installing BlueOS alongside our software.


**These instructions are mostly for MATE ROV teams who want the ability to stream multiple exploreHDs easily, yet retain the ability to use their own flight controller!**
```

![Multi-Cam exploreHD Setup](../img/explorehd/exploreHD_Connection_Diagram.JPG)

## Setup

::::{dropdown} Initial Setup

   **Step 1: Flashing the Raspberry Pi**

   * Download and run the [Raspberry Pi Imager](https://www.raspberrypi.com/software/) from the official Raspberry Pi website
   * If you haven't already, insert the SD card into your computer
   * Select Raspberry Pi OS (32-bit) for the Operating System and the SD card you inserted as the SD card.
   * Select `Write` to begin flashing the Operating System to the SD card

   **Step 2: Powering**

   * Plug in a compatible HDMI cable and monitor to the Pi
   * Connect a USB keyboard and mouse to the Pi
   * Power the Pi using a micro usb or usb c power adapter depending on the version of Raspberry Pi you are using

   ```{important} Ensure you power the Pi after plugging the monitor into the Pi **and wall power**, otherwise, the Pi will not recognize the display and you will have to power cycle the device.
   ```

   **Step 3: Perform the Initial Setup**

   * Setup the Pi with the GUI provided at start
   * Ensure WiFi is connected as soon as possible

   ```{warning} Make sure you select the **US Keyboard layout** or some keys will not be recognized properly.
   ```

   **Step 4: Set Static IP**

   * Edit dhcpcd.conf -  `sudo nano /etc/dhcpcd.conf`
   * Add:

    interface eth0
    static ip_address=192.168.2.2/24

   to the end of the file
   * Save and close the file with `ctrl-o`, `enter`, and then `ctrl-x`

   **Step 5: Connect to a Laptop**

   * Plug in an ethernet cable into the Raspberry Pi with the other end connected to a Windows or Linux laptop or PC
   * Enable ssh on the pi

   :::{dropdown} Enabling SSH on the Raspberry Pi
      Run `sudo raspi-config`

      ![Raspi Config](../img/pi_setup/enable_ssh/raspi-config.png)

      Select `Interface Options` and press enter

      ![Raspi Config Interface Options](../img/pi_setup/enable_ssh/raspi-config2.png)

      ```{note} Use the arrow keys to navigate the menu up and down
      ```

      Under `Interface Options`, Select `SSH`

      ![Raspi Config SSH](../img/pi_setup/enable_ssh/raspi-config3.png)

      Select `yes` and press enter

      ![Raspi Enable SSH](../img/pi_setup/enable_ssh/raspi-config4.png)
   :::

- Reboot the pi with: `sudo reboot`

::::

::::{dropdown} SSH into the Pi

```{include} ./ssh_into_pi.md
:parser: myst_parser.sphinx_
:start-line: 4
```

   ```{note} At this point, you can disconnect the USB keyboard, mouse, and monitor from the Raspberry Pi.
   ```

::::

::::{dropdown} Installation Instructions

   **Step 1: Update the Pi**

    sudo apt-get update
    sudo apt-get upgrade
    sudo apt full-upgrade

   ```{note} This process may take a while
   ```

   **Step 2: Install the Latest Version of GStreamer**

   Remove the included version of GStreamer:

   `sudo apt-get remove libgstreamer* gstreamer1.0*`

   Install GStreamer:

   `sudo apt-get install gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-libav`

   **Step 3: Plug in the Camera**

   If you haven't already, connect an exploreHD or HDCam to an available USB port on the Raspberry Pi

   ```{note}
   See {doc}`exploreHD <../products/explorehd>` or {doc}`HDCam <../products/hdcam>` getting started guides
   ```
::::

## Streaming

```{dropdown} Automatic Stream Setup
For automatic, plug and play of the stream to work on the Raspberry Pi, use our exploreHD Driver UI. This system will automatically run at startup and saves the settings automatically. It supports UDP stream and H264 compression settings.

{doc}`DWE OS <../software/driverUI>`

![driverui](../img/driverui/driverui.png)
```

````{dropdown} Manual Stream Setup

```{important}
It is not recommended to use the following instructions unless customizability is required. Please use DWE OS when possible to minimze issues or compability concerns.
```

**Step 1: Finding the device**
`v4l2-ctl --list-devices`

![Device List](../img/pi_setup/PiDeviceLists.jpg)

Look for device: **exploreHD USB Camera: exploreHD**
```{note}
In this example, we have 2 exploreHDs connected so it shows up twice. 
```
You can ignore `/dev/media*`

The different video numbers in each section represent the different encoding format. Typically the third one on the list is for H264 (in the above example video6 and video2 are H264 formats). Keep those in mind for the next step. The video number won't change as long as the USB device doesn't get unplugged even when you reboot the Pi. 
```{note}
If you are unsure the device number you selected is 'H264' format, you can run `v4l2-ctl --list-formats --device *` to find out. (replace * with the device number)
```

**Step 2: Streaming in H264**

On the Raspberry Pi, run:

`gst-launch-1.0 -v v4l2src device=/dev/video* ! video/x-h264, width=1920,height=1080! h264parse ! queue ! rtph264pay config-interval=10 pt=96 ! udpsink host=192.168.2.1 port=5600 sync=false`

```{note}
In this example, `host=192.168.2.1` due to the expected setup in [Receiving](#Receiving) regarding Windows Setup. If that specific setup cannot be followed you may replace this with the local IP of your device.
```

```{note}
Replace the * in device=/dev/video* with the video device number seen in the previous step.
```

To stream more than one exploreHD at the same time, you can add an `&` to the code and run another one with the respective video device and port number.

You can make this command autorun to make your ROV camera streaming system!
````

## Receiving

To receive the stream on a PC, first follow our {doc}`Windows Setup Guide <./pc_setup>`. You will then be able to run the following command:

`gst-launch-1.0 udpsrc port=5600 ! application/x-rtp ! rtpjitterbuffer ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink`

For more streaming options such as viewing multiple streams at once, please see:

[Receiving Multiple Streams Instructions](/guides/ardusub_companion.html#receiving-multiple-streams)

![MultiCam exploreHD ROV Setup](../img/gstreamer/gstreamer8.jpg)
