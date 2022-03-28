# exploreHD Driver UI

```{important} This software is still in Alpha. Be aware that it may not be stable and changes will occur during the development. 
```
```{note} The DriverUI is only compatiable with the Lower Bandwidth version of the firmware. Please make sure that all exploreHD using the Driver UI is running that firmware.

[**Learn More Here**](https://docs.exploredeepwater.com/software/firmware.html)
```

## Installation

### Step 1: Install node.js and npm

* Skip this step if node.js and npm are already installed.

To install, in the terminal, run:

```bash
curl -fsSL https://deb.nodesource.com/setup_12.x | sudo -E bash -
sudo apt install nodejs
curl -L https://npmjs.org/install.sh | sudo sh
```

### Step 2: Install Dependencies

Install udev and gstreamer with:

``sudo apt install libudev-dev libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev``

### Step 3: Install Driver UI

Install Driver UI through npm with:

``sudo npm install -g @deepwaterexploration/dwe-controls``

## Launch

Driver UI can be set up to auto-launch or be launched manually.

Auto-launching is recommended for use on a Raspberry Pi.

### Auto-launch

#### Step 1: Install pm2

In the terminal, run ``sudo npm install -g pm2``

#### Step 2: Start dwe-controlls from pm2

Run ``pm2 start dwe-controls``

#### Step 3: Save the process list in pm2

Run ``pm2 save``

#### Step 4: Enable pm2 startup

This step is only for usage on a Raspberry Pi.

run ``sudo pm2 startup systemd -u pi --hp /home/pi/``


### Manual launch

To launch manually, in the terminal, run ``dwe-controls start``


## Usage

Open the Driver UI interface by opening <http://192.168.2.2:5000> in a web browser.

If ArduSub companion is being used, go to <http://companion.local:5000> instead.

A camera device opened with Driver UI:

![DWE Firmware Loader](../img/driverui/driverui.png)