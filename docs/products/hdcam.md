# HDcam

[![HDcam](https://cdn.shopify.com/s/files/1/0575/8785/9626/products/1_d8ef6594-eb9b-4eda-8928-93b7c368b479_590x.jpg?v=1625647297)](https://exploredeepwater.com/products/hd-usb-camera)

[Product Link](https://exploredeepwater.com/products/hd-usb-camera)

[Full Manual](https://cdn.shopify.com/s/files/1/0575/8785/9626/files/HDcam_Manual_072321.pdf?v=1627097263)
## Introduction
The HDCam is the bare board of the exploreHD Camera but without the waterproof housing. This camera provides the same excellent image quality as the exploreHD but uses a specialized lens designed to be more suited for above water applications. The camera can output H.264, MPEG, and YUY2 at reduced frame-rates. Due to its low distortion and smooth frame-rate, this camera is ideal for computer vision applications.

```{note} This camera runs the same firmware as the exploreHD. The only optical difference between this camera and the exploreHD is the different lens used.

```

## Technical Specifications
### Camera Specifications
**Image Sensor:** SONY IMX323 1/2.9

**Resolution:** 1920x1080

**Framerate:** 30fps

**Format:** H.264/MJPEG 

**Connection:** USB2.0 High Speed 

**Connector:** USB Type A to JST 2.0 

**Voltage:** 5V 

**Current:** 250mA

**Footprint:** 30 mm diameter (PCB)
### Lens Specifications 
**Type:** Low Distortion Lens

**Lens Aperture:** f/2.8

**View Angle:** 100 Degrees Diagonal

**Minimum Focus Distance:** 15 cm

**Focal Length:**  2.7MM (19MM Equivalent on Full Frame)

```{note} We currently don't recommend this lens for underwater use due to its narrower aperture and vignetting qualities when the camera is underwater. For those looking to replace the standard ELP USB camera from BlueROV, we recommend using their lens for now until our team finds a more suitable lens for underwater.

```
## Operating Notes
### PCB Size Comparison
![HDCam vs BR Camera](https://cdn.shopify.com/s/files/1/0575/8785/9626/files/HDCam_PCB_size_x320.jpg)

Size comparison of the PCB between the ELP's H.264 USB Camera (found in many current ROV systems) and the HDCam. 

HDCam features an advanced multilayer PCB and a much more modern image processor which allows our board to be more space efficient than the competition while providing better performance **(see below for comparison)**. 

### Image Comparison of HDCam vs ELP (Generic H.264 USB Camera)

![HDCam Temperature](https://cdn.shopify.com/s/files/1/0575/8785/9626/files/HDCam_1.jpg?v=1639925100)

![HDCam Temperature](https://cdn.shopify.com/s/files/1/0575/8785/9626/files/HDCam_2.jpg?v=1639925099)

### Temperature
![HDCam Temperature](https://cdn.shopify.com/s/files/1/0575/8785/9626/files/HDCam_Temperature_x200.jpg?)

For long-term operation, the camera may get hot (MAX Temp 70C). This is normal and not a cause for concern. The processor has an auto thermal shut off if it does exceed normal operating temperatures. If you
are designing a custom mount, it can not be manufactured with Polylactic acid (PLA) plastic as the heat from the camera will cause the plastic to weaken. Acrylonitrile butadiene styrene (ABS) is recommended instead.

### Sensor Affected by Incident Light
![HDCam Sensor Incident Light](https://cdn.shopify.com/s/files/1/0575/8785/9626/files/HDCam_Incident_Light_x200.jpg?v=1639879650)

The Sony IMX323 sensor used in this camera is chosen for its smaller footprint while still providing great
image quality. Typically, CMOS sensors contain a ceramic plate on the back to prevent incident light from
entering through the back of the sensor causing an X-ray effect. The IMX323 sensor does not have a
ceramic plate and is therefore susceptible to indent light from the back of the camera affecting image quality. This can easily be avoided by using our included camera holder or using black electrical tape to cover
the back of the camera PCB.
### Lens Focusing
![HDCam Lens Holder](https://cdn.shopify.com/s/files/1/0575/8785/9626/files/HDCam_Lens_Holder_x200.jpg?v=1639879650)

```{warning} Pay extra attention to not screw the lens past the sensor element. Doing so will crack the sensor and damage it permanently.

```
To ensure the sharpest image from your camera, the distance between the sensor and the lens must be set correctly. Before the camera leaves our facility, the focus is set manually and a screw is placed on the side of the lens holder to lock the distance. Sometimes, this screw can get loose over time and the camera loses proper focus. You can adjust this manually by taking the screw off and twisting the lens until the image is clear when viewing a far away distance on a computer.

**This will also allow users to use different M12 style lenses with the HDCam.**
```{note} If you are using a different lens than the one supplied, make sure it's compatible with the 1/2.9 sensor size. Using a lens designed for a larger sensor (1/2.8 or larger) will usually work but you will expect a lower FOV than advertised. Additionally, the lens will produce a less sharp image and artifacts such as chromatic aberration will be more noticeable. 

Conversely, using a lens designed for a smaller sensor (1/3 or smaller) will increase the FOV but you may notice more vignetting in the image. The lens will produce a sharper image and less chromatic aberration will be observed.

```
## Image Samples
![HDCam Image 1](https://cdn.shopify.com/s/files/1/0575/8785/9626/files/HDCam_Image_1.jpg?v=1639880736)

![HDCam Image 2](https://cdn.shopify.com/s/files/1/0575/8785/9626/files/HDCam_Image_2.jpg?v=1639880736)

![HDCam Image 3](https://cdn.shopify.com/s/files/1/0575/8785/9626/files/HDCam_Image_3.jpg?v=1639880736)


## Mount Installation

```{note} To enable the mounting of this camera, two screw holes are located on the base of the camera holder bracket. These 20mm apart M3 counter-bores should allow for the attaching of the camera to any surface, provided two M3 threads or nuts 20mm apart may be made or placed on the surface.
```
### Step 1
![exploreHD](https://cdn.shopify.com/s/files/1/0575/8785/9626/files/HDCam_Step_1_x150.jpg?v=1639879650)

To begin the process of installing the HDCam, ensure you have the
parts detailed in the contents section of this manual as well as a 2mm hex
Allen wrench or screwdriver(not included).

### Step 2
![exploreHD](https://cdn.shopify.com/s/files/1/0575/8785/9626/files/HDCam_Step_2_x150.jpg?v=1639879650)

Tap or drill a hole for where you want to mount the camera and attach the
camera holder bracket to the surface using the longer M3 screws.
### Step 3
![exploreHD](https://cdn.shopify.com/s/files/1/0575/8785/9626/files/HDCam_Step_3_x150.jpg?v=1639879650)

After the securing of the camera holder bracket, place the square nuts within
the square indentation located on the bottom of the camera holder, and align
the holes of the camera holder with the lateral holes of the camera bracket
holder.
### Step 4
![exploreHD](https://cdn.shopify.com/s/files/1/0575/8785/9626/files/HDCam_Step_4_x150.jpg?v=1639879650)

Begin screwing in both remaining screws on each side of the camera bracket
holder, and properly position the camera to the point of view you require for
your uses and finish screwing in the screws.
### Step 5
![exploreHD](https://cdn.shopify.com/s/files/1/0575/8785/9626/files/HDCam_Step_5_x150.jpg?v=1639879650)

Connect the provided USB cable to the camera using the USB connector
located at the top of the camera holder.
## Streaming From Raspberry Pi

If you want to run your own custom streaming setup on the Raspberry Pi, we have the perfect documentation for you!

[Click here to learn more](https://docs.exploredeepwater.com/guides/pi_setup.html)

## ArduSub Companion/Custom H.264 Settings
### ArduSub Companion
```{important} **As of November 20, 2021, all HDCams shipped will feature a new firmware that allows the cameras to be plug and play with ArduSub Companion without the need for drivers.**

If your camera was shipped beforehand or you notice the video stream being sluggish, you may be running an older version.

[Click Here for Instructions on how to Update](https://docs.exploredeepwater.com/software/firmware.html)
```

If you want to stream multiple HDCams at once using ArduSub Companion and see potential methods for viewing the multi-stream, check out the link below

[Streaming Multiple exploreHDs with ArduSub Companion Instructions](https://docs.exploredeepwater.com/guides/ardusub_companion.html#streaming-multiple-explorehds-with-ardusub-companion)

### Custom H.264 Settings
**The instructions below are for customers who may want more control over H264 compression
and other settings on the camera**

In order to have full access to H264 controls when streaming via Linux, you will need to install our driver.

[https://github.com/DeepwaterExploration/exploreHD_Controls/tree/main/explorehd_camera_controls](https://github.com/DeepwaterExploration/exploreHD_Controls/tree/main/explorehd_camera_controls)

To install the driver, you will need to compile it after having the explorehd_camera_controls on your computer.

`cd explorehd_camera_controls`

`cp Makefile.x86 Makefile`

`make`

### Basic H.264 Controls ###

**`--xuset-br` sets the bitrate of the H264 compression**

Our default settings it set to a generous
15Mb/s which would provide you with decent video quality while lowering file size.

**`--xuset-gop` sets the GOP settings of the H264 compression**

Since the Raspberry Pi is limiting in its processing, the default is 0.

**`--xuset-cvm` sets the type of bit rate compression for H.264**

We found that setting it to VBR (variable bitrate) provides the best quality but you can experiment around.

**For help with more controls:**

`./explorehd_UVC_TestAP -h`

```{note} Any controls that are set onto the camera will be reset when the device restarts either by physically unplugging it or restarting the computer. To save the settings, we suggest running a for loop with an auto start script. We have a sample of one done for ArduSub Companion linked below.

[https://github.com/DeepwaterExploration/exploreHD_Controls/](https://github.com/DeepwaterExploration/exploreHD_Controls/)

```sh
for DEVICE in $(ls /dev/video*); do
	.$HOME/companion/scripts/explorehd_camera_controls/explorehd_UVC_TestAP 
    --xuset-br 1500000 --xuset-gop 0 --xuset-cvm 2 $DEVICE
done
```
## Technical Drawing
![exploreHD](https://cdn.shopify.com/s/files/1/0575/8785/9626/files/HDCam_Mount_Drawing_299x.jpg?v=1639879650)
![exploreHD](https://cdn.shopify.com/s/files/1/0575/8785/9626/files/HDCam_camera_Drawing_310x.jpg?v=1639879650)


