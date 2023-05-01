# DWE Firmware Loader

```{important} This application is a fully customized firmware loading application. Although it provides similar functionality, it is not the same as our previous release which can be found [here](https://docs.exploredeepwater.com/legacy/firmware_legacy.html), known as DWE Firmware Updater.
```

[**Download DWEFirmwareLoader**](https://cdn.shopify.com/s/files/1/0575/8785/9626/files/DWEFirmwareLoader_051722.zip)

```{note}
Updated as of 5/17/2022

See [Release Notes](./firmware/update-feb-8)
```

## Procedure for Updating exploreHD/HDCam Firmware

### Step 1

Extract the zip file containing the folder with the program.

![Extract the Zip File](../img/firmware_loader/Firmware_Loader_Step_1-1.png)
![Folder Contents](../img/firmware_loader/Firmware_Loader_Step_1-2.png)

### Step 2

Plug in **one** exploreHD camera.

### Step 3

**Make sure all applications that use the camera are closed before proceeding.**

Run *DWEFirmwareLoader.exe*

![DWE Firmware Loader](../img/firmware_loader/Firmware_Loader_Step_3.png)

### Step 4

Click on the firmware version that you would like to use.

```{important} Since the introduction of [DWE OS](https://docs.exploredeepwater.com/software/driverUI.html), we no longer offer High Quality Firmware as the setting can be adjusted via the driver UI. The default camera firmware we ship and recommend is the lower bandwidth version when streaming. If you have any questions, feel free to ask on [our forums](https://discuss.exploredeepwater.com/).
```


* **Lower Bandwidth** uses less bandwidth, but provides lower quality video.
    * Reccomended for use in a setup with multiple exploreHDs.

```{warning} Do not close the application, unplug the camera, or open any applications that may use the camera until the update is complete.
```

![Update Firmware](../img/firmware_loader/Firmware_Loader_Step_4.png)

### Step 5

After approximately a minute, the exploreHD should have the new firmware loaded and ready to use!

You may now close the application. You can test the camera using any camera application for Windows. If everything looks good, you are ready to use it on your ROV!

See: [Getting Started](../products/explorehd)

## Troubleshooting

If you see any errors during the upgrading process, please follow the guides below.

### Error: exploreHD not recognized!

![Error Message](../img/firmware_loader/Firmware_Loader_Error_Not_Recognized.png)

1. Ensure the exploreHD is the only camera plugged in
2. If on a laptop, temporarily disable the built-in webcam by going to Device Manager.
3. Please ensure you have extracted everything in the zip file. The dll files must be in the same folder directory as the main exe.

### Error: Unable to load firmware dll!

![Error Message](../img/firmware_loader/Firmware_Loader_Error_No_dll.png)

1. Please ensure you have extracted everything in the zip file. The dll files must be in the same folder directory as the main exe.


## Procedure Video

```{warning} This video uses an outdated version of the loader and may not be accurate. Documentation for this version can be found [here](https://docs.exploredeepwater.com/legacy/firmware_legacy.html).
```

```{youtube} G4h9EAG88HU
```
