
# exploreHD

[![exploreHD](https://cdn.shopify.com/s/files/1/0575/8785/9626/products/exploreHDUSBCameraMain_590x.jpg?v=1632166193)](https://exploredeepwater.com/products/explorehd-rov-auv-usb-camera)

Product Link: [https://exploredeepwater.com/products/explorehd-rov-auv-usb-camera](https://exploredeepwater.com/products/explorehd-rov-auv-usb-camera)

Full Manual: [https://cdn.shopify.com/s/files/1/0575/8785/9626/files/exploreHD_Camera_110921.pdf?v=1636481823](https://cdn.shopify.com/s/files/1/0575/8785/9626/files/exploreHD_Camera_110921.pdf?v=1636481823)

## {doc}`Firmware Update <../software/firmware>`

```{note} Please update your firmware if you were shipped an exploreHD before 11/20/2021
```
## Introduction
Our passion for uncompromised image quality for marine robotics is the simple philosophy behind the exploreHD Underwater USB Camera. This UVC compliant camera is the first of its kind to feature a high definition USB output while achieving a waterproof rating of IP69K. With the use of a modern Sony sensor, this camera will be able to see in low light conditions like never before. Thanks to advanced automated exposure and white balance adjustments, this camera produces accurate colors and a pleasing natural image. With H.264 compression technology, up to 4 cameras can be connected at once and streamed via ethernet without major quality loss or latency. This makes our camera the perfect choice for advanced multi-cam ROV/AUV setup.
## Technical Specifications
### Waterproof Specifications
**Waterproof Depth:** 400 meters 

**Ingress Protection Rating:** IP69K
### Camera Specifications
**Image Sensor:** SONY IMX323 1/2.9

**Resolution:** 1920x1080

**Framerate:** 30fps

**Format:** H.264/MJPEG 

**Connection:** USB2.0 High Speed 

**Voltage:** 5V 

**Current:** 250mA
### Lens Specifications 
**Type:** Fisheye 

**Lens Aperture:** f/1.9

**View Angle:** 150 Degrees Diagonal (in water)

**Minimum Focus Distance:** 20-30 cm
## Image Samples
Color remains accurate even in low light situations
![exploreHD](https://cdn.shopify.com/s/files/1/0575/8785/9626/files/exploreHD_accurate_colors.jpg?v=1639761687590x.jpg?v=1632166193)
### Comparison of Color Accuracy with GoPro
Left Image is from exploreHD and the right is from a GoPro Hero
![exploreHD](https://cdn.shopify.com/s/files/1/0575/8785/9626/files/GoPro_vs_exploreHD.jpg?v=1639761687?v=1639761687590x.jpg?v=1632166193)
## Operating Notes
### Lens Field of View in Air vs Water
This lens has a fish eye effect which is more noticeable in air then in water due to the changes with light as it passes through different optical mediums. We took into account this factor and picked a lens that has a very wide field of view in air so that when the lens is in water, it can compensate for the lowered field of view. You may also notice a bit of vignetting when above water from the lens cap that will disappear in the water.
### TrueColor Technology
The camera offers TrueColor Technology which compensates for the blue/greenish tint in water using advance AI white balance technology that we developed. However, in order to reduce the bluish/greenish tint, the camera has to compensate by adding more red/magenta. This means that in some images, the shadows may appear more red or magenta color. If you do not like this effect, you can turn off auto white balance in the exploreHD camera preferences.

![exploreHD](https://cdn.shopify.com/s/files/1/0575/8785/9626/files/4_e9a1179c-a100-4de6-a14b-99a793a23089.jpg?v=1639761687?v=1639761687?v=1639761687590x.jpg?v=1632166193)
## Mount Installation

### Step 1
Drill two holes, 30mm apart into your frame where you want the camera to reside. If using a thread-able material, tap an M3x0.5 thread. If using a non-thread-able material, ensure there is space for a M3x0.5 nut on the other side.
### Step 2
Using two M3x0.5 screws, attach the camera bracket to the frame through the two holes on the base of the bracket.
### Step 3
Place the standoff portion of the main camera body into the two remaining holes of the bracket. Now, you should have an axis about which the camera may rotate. 

Tighten the camera into place using the two M2x0.4 screws and the threaded portion of the standoffs.
### Step 4
There may be some give on the rotation of the camera body. To ensure the camera is held in place, ziptie the camera usb cable to the ROV in such a manner that the tension of the cable keeps the camera in place. Ensure to make the zip tie as tight as possible without damaging the cable.
## Cable Waterproofing
```{note} If the camera is going into an ROV electronic enclosure, you will need to waterproof the wires properly using a cable penetrator. You can either use potted penetrators or WetLink from Blue Robotics.
```
### Step 1
Ensure that the camera is mounted securely on the ROV as you like it with the previous steps
### Step 2
Cut off the USB cable to the desired length. Ensure to leave extra length for when the cable is in the enclosure.
### Step 3
Strip the cable to the length that will be in the electronic enclosure.
### Step 4
Twist the section of wires that are stripped from the black rubber insulation
### Step 5
Depending on the cable penetrator you are using, follow the instructions to waterproof the wires
## USB Soldering

### Step 1
<b>Before soldering the wires to the provided USB connector, please ensure the following tasks have been completed</b>

* Cable is properly waterproofed, following the steps in the previous page. 

* Cable penetrator has the o'ring in the o'ring groove. 

* Cable penetrator is on the outer portion of the electronic housing end cap.

* The wires have been passed through the nut for the cable penetrator. 

* The nut is on the inner portion of the electronic housing end cap.

### Step 2

```{warning} Ensure you are knowledgeable on the function of each wire.
<span style="color: black; font-weight:bold">Black: Ground</span>

<span style="color: #CCCC00">Yellow/Green: D+ (DP)</span>

<span style="color: gray">White: D- (DM)</span>

<span style="color: red">Red: 5V</span>
```

```{warning} Ensure there are **no solder bridges and DOUBLE CHECK** to make sure the connection is correct. **The camera will get damaged if the polarity is not correct.**
```


### Step 3

...

## Streaming Via Linux

```{note} Please install gstreamer following this guide [https://gstreamer.freedesktop.org/documentation/installing/on-linux.html?gi-language=c](https://gstreamer.freedesktop.org/documentation/installing/on-linux.html?gi-language=c)
```

### Step 1

...

### Step 2

...

### Step 3

...

### Testing the Camera Stream

...

### Setting up the Controls

[https://github.com/DeepwaterExploration/exploreHD_Controls](https://github.com/DeepwaterExploration/exploreHD_Controls)

...

## ArduSub with Blue Companion

...

## ROV Connection Diagram

...
