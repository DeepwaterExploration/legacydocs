# DWE Firmware Loader

```{important}
Please see [product changelog](./firmware/product_changelog.md) for more information on updates.
```

```{warning}
**Please note, this page only applies to the following products:**

- Standard exploreHD (400m) cameras shipped before Jan 16th, 2024
- exploreHD Heavy (1000m) cameras
- exploreHD Pro (6000m) cameras
```

```{caution}
**This procedure is currently only available on Windows 10 or newer.**

[**Download DWEFirmwareLoader**](https://dwe.ai/firmwareloader)
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

```{warning} Do not close the application, unplug the camera, or open any applications that may use the camera until the update is complete.
```

![Update Firmware](../img/firmware_loader/Firmware_Loader_Step_4.png)

### Step 5

After approximately a minute, your exploreHD product should be ready to use!

You may now close the application. You can test the camera using any camera application for Windows (ex: [Camera app](https://apps.microsoft.com/detail/9WZDNCRFJBBG?hl=en-US&gl=US)).

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

```{warning} This video uses an outdated version of the loader. If you have trouble, please follow the above steps before contacting support@dwe.ai
```

```{youtube} G4h9EAG88HU
```
