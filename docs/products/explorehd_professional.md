# exploreHD Professional

![exploreHD Professional](https://dwe.ai/cdn/shop/files/eHDProBase.jpg?v=1706673490&width=600)

## Introduction

Introducing the exploreHD Professional, the next evolution of our flagship product line. With an uncompromising commitment to image quality, this underwater USB camera features the same high definition USB output and large, backlit CMOS sensor packed into our next-generation exploreHD Heavy camera. This time, it is carefully enclosed into a unique titanium enclosure but with a depth rating of 6000m! Advanced automated exposure and white balance adjustments ensure accurate colors and a natural image, even in low light conditions. The exploreHD Professional also features H.264 compression technology, allowing up to 7 cameras to be connected and streamed simultaneously with minimal loss in quality and latency. This makes it the perfect choice for advanced multi-cam ROV/AUV setups, deep sea exploration, and scientific research. With the exploreHD Professional, you can capture stunning images of the most remote and inaccessible underwater environments with ease and confidence.

## Technical Specifications

```{dropdown} Water-Resistance Specifications
**Water-Resistance Depth:** 6000 meters

**Connector Types:** 
    - Subconn MCBH8M
    - Suburban Marine 8-Pin
    - Other Variants Available Upon Request
```

<!-- TODO: WEIGHTS -->
```{dropdown} Physical Specifications

**Mass in Air:**  grams

**Mass in Water:**  grams
```

```{dropdown} Camera Specifications
**Image Sensor:** 1/2.8" Sony Exmor™ STARVIS CMOS 12-bit

**Resolution:** 1920x1080

**Framerate:** 30fps with H.264/MJPEG

**Format:** H.264, MJPEG, YUY2

**Chroma Subsampling:** 4:2:2 with YUY2, 4:2:0 with MJPEG/H.264

**Color Depth Per Channel:** 8 bit per RGB channel / 24 bit per pixel

**Bitrate:** 10Mb/s with H.264, VBR with MJPEG/YUY2 

**H.264 Compression Profiles:** Baseline Profile

**USB Latency (MJPEG/H264):** 33ms ± 3 [USB Testing Tool](https://github.com/DeepwaterExploration/USB-Camera-Latency-Tool)

**Streaming Latency:** 34ms ± 5 [More Details](#streaming-latency)

**Connection:** USB2.0 High Speed 

**Voltage:** 5V 

**Current:** 250mA

**Wattage:** <1.5W

```

```{dropdown} Resolutions and Framerates
**MJPEG:**
 - Resolutions: `1920x1080`, `1280x720`, `800x600`, `640x480`, `640x360`, `352x288`, `320x240`
    - `@30fps`, `@25fps`, `@20fps`, `@15fps`, `@10fps`, `@5fps`

**H264:**
 - Resolutions: `1920x1080`, `1280x720`, `800x600`, `640x480`, `640x360`, `352x288`, `320x240`
    - `@30fps`, `@25fps`, `@20fps`, `@15fps`, `@10fps`, `@5fps`

**YUYV (4:2:2):**
- Resolutions:`1920x1080`
    - `@5fps`
- Resolutions: `1280x720`
    - `@10fps`, `@5fps`
- Resolutions: `800x600`
    - `@15fps`, `@10fps`, `@5fps`
- Resolutions:`640x480`, `640x360`, `352x288`, `320x240`
    - `@30fps`, `@25fps`, `@20fps`, `@15fps`, `@10fps`, `@5fps`
```

```{dropdown} Lens Specifications
**Type:** Fisheye

**Lens Aperture:** f/2.0

**View Angle:** 150 Degrees Diagonal (in water)

**Minimum Focus Distance:** 20-30 cm

    Note: Alternative Lenses Available Upon Request
```

## Technical Drawings

```{dropdown} exploreHD Heavy Housing

- [exploreHD Heavy Assembly STEP File](https://cdn.shopify.com/s/files/1/0575/8785/9626/files/eHD_Pro_Public_Release.step?v=1704159141)

```

## Image Samples

Color remains accurate even in low light situations
![exploreHD Heavy](../img/explorehd/exploreHD_accurate_colors.jpg)

### Comparison of Color Accuracy with GoPro

The left Image is from exploreHD and the right is from a GoPro Hero
![exploreHD Heavy](../img/explorehd/GoPro_vs_exploreHD.jpg)

## Operating Notes

### Lens Field of View in Air vs Water

This lens has a fisheye effect which is more noticeable in the air than in the water due to the changes with light as it passes through different optical mediums. We took into account this factor and picked a lens that has a very wide field of view in the air so that when the lens is in the water, it can compensate for the lowered field of view. You may also notice a bit of vignetting when above water from the lens cap that will disappear in the water.

### TrueColor Technology

The camera offers TrueColor Technology which compensates for the blue/greenish tint in water using advanced AI white balance technology that we developed. However, to reduce the bluish/greenish tint, the camera has to compensate by adding more red/magenta. This means that in some images, the shadows may appear more red or magenta color. If you do not like this effect, you can turn off *auto white balance* in the exploreHD camera preferences.

![exploreHD True Color Technology](../img/explorehd/truecolor/1_c13a6d81-411d-4aeb-abea-f22e27f8e5be.jpg)
![exploreHD True Color Technology](../img/explorehd/truecolor/2_cc58ff7f-1c87-4681-8f8f-8687241c50eb.jpg)
![exploreHD True Color Technology](../img/explorehd/truecolor/3_f0d99052-aa08-402a-bd62-5e0bf0c442ea.jpg)
![exploreHD True Color Technology](../img/explorehd/truecolor/4_e9a1179c-a100-4de6-a14b-99a793a23089.jpg)

## Camera Installation

```{note}
Cables and Connectors:



```

```{dropdown} Mount Installation
**Step 1**

The exploreHD Professional utilizes a novel mounting system for maximum precision. The four slots cut into the main body act as precise positioning surfaces. The slots will accept a square bracket 5mm wide, or other solutions such as cable clamps. For custom mounting solutions, please enquire if you would like our assistance.


```

```{dropdown} Cable Waterproofing

**Step 1**

Unlike with other exploreHD units, this camera will not require any user waterproofing. Simply use a cable with a mating connector that is compatible with your selected connector. 

**For Wet-Mate Connectors**

Periodically inspect your connection point and clear it of debris. Isopropyl alcohol will be sufficient for cleaning purposes. Once clean, relubricate the connector pins with Molykote 111 silicone grease. 

**For Dry-Mate Connectors**

Periodically inspect and clean the surfaces of the dry-mate connector. Annually replace and re-grease the sealing o-ring for the connector.

```


````{dropdown} USB Connection



**Step 3**

Connect the USB cable to a computer to confirm the camera is working and in the correct orientation.

![exploreHD](../img/explorehd/exploreHD_ROV_Camera_App_500x.jpg)
![exploreHD](../img/explorehd/exploreHD_ROV_Camera_App_Driver_500x.jpg)

An image should be displayed using the built-in camera app on your computer. The device name should be exploreHD USB Camera

````

## Multi-Cam ROV Connection Diagram

![exploreHD](../img/explorehd/exploreHD_Connection_Diagram.JPG)

## Streaming

```{dropdown} Streaming via custom Raspberry Pi
If you want to run your own custom streaming setup on the Raspberry Pi, we have the perfect documentation for you! 

This is perfect for MATE ROV teams who want to use the RPi to stream but don't want to be limited to PixHawk Controller from ArduSub Companion. It's also a great way to learn and customize your code for your specific setup!

{doc}`Raspberry Pi Streaming Setup for exploreHD Instructions <../guides/pi_setup>`
```

````{dropdown} Streaming alongside BlueOS Companion
```{important} **As of November 20, 2021, all exploreHD shipped will feature a new firmware that allows the cameras to be plug and play with BlueOS Companion without any extra drivers.**

If your camera was shipped beforehand or you notice the video stream is sluggish, you may be running an older version.

{doc}`Click Here for instructions on how to update <../software/firmware>`
```

If you want to stream multiple exploreHDs at once using BlueOS Companion, check out our {doc}`BlueOS Companion Guide <../guides/blueos_companion>` for installing our software alongside BlueOS.
````

```{dropdown} H.264/Bitrate Control for Streaming
To set custom H.264 parameters when streaming from a Raspberry Pi or similar computer, install {doc}`DWE OS <../software/dweos>`!

This software supports unlimited camera streams given you have unlimited USB ports, and installs perfectly alongside BlueOS.

![DWE Firmware Loader](../img/dweos/dweos.png)

- **Bitrate:** Adjust the bitrate of the exploreHD Camera
- **H.264:** Toggle H.264 on or off (Off is similar to MJPEG)
- **VBR:** Variable bitrate, changes bitrate depending on scene
- **UDP Stream:** Starts a UDP H.264 Stream via GStreamer with port 5600.

```

### Streaming Latency

- **Streaming Method:** UDP H.264 via GStreamer
- **Streaming Device:** Raspberry Pi 4 Model B 2GB RAM
- **Streamed Devices:** 3 exploreHDs
- **Receiving Software:** Open Broadcaster Software
- **Latency:** 35ms ± 20

```{youtube} ZJl32Xt4jQQ
```


