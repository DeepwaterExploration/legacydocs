# DWE OS

```{note}
exploreHD settings can only be adjusted on the lower bandwidth / configurable firmware. Learn how to upgrade [here](./firmware)
```

## Getting Started

### Connecting

To connect to the pi, we recommend using SSH. You can read our documentation on that on {doc}`How to SSH into a Raspberry Pi <../guides/ssh_into_pi>`.

::::{dropdown} Installing with Docker Installation Script (Recommended)
:open:

Recommended for Raspberry Pi instead of [Installing On Raspberry Pi](#installing-on-raspberry-pi) or [Installing Manually](#installing-manually).

To install with docker, you can use the installation script provided with the following command:
```
curl -fsSL https://raw.githubusercontent.com/DeepwaterExploration/DWE_OS/main/scripts/install-docker.sh | sudo -E bash -
```

Once installed, the script should exit with the following message:
`Installation of dwe-controls with docker was successful. Please navigate to http://192.168.2.2:5000 to access the interface.`

You can now jump to [Interface](#interface) to access the functionality.

:::{dropdown} Uninstalling

You can uninstall dwe-controls with the following commands:

```
docker rm dwe-controls --force
rm /usr/lib/systemd/system/dwe-controls.service
```
:::

::::

:::{dropdown} Installing with Installation Script
```{important} It is no longer recommended to use this script. Instead, **use the docker installation for a more compatible install**.
```

To install for the raspberry pi, you can use the installation script by executing the following command:
```
curl -fsSL https://raw.githubusercontent.com/DeepwaterExploration/DWE_OS/main/scripts/install.sh | sudo -E bash -
```

Once installed, the script should exit with the following message:
`Installation of DWE OS was successful. Please navigate to http://192.168.2.2:5000 to access the interface.`

You can now jump to [Interface](#interface) to access the functionality.
:::

::::{dropdown} Installing Manually
You can install manually (for raspberry pi or other systems) with the following commands:

First, install nodejs with:
```sh
curl -fsSL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt install nodejs
curl -L https://npmjs.org/install.sh | sudo sh
```

Next, install the required dependencies:

`sudo apt install libudev-dev libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev`

`sudo apt install gstreamer1.0-plugins-good gstreamer1.0-plugins-bad`

Finally, install the dwe-controls application from npmjs with:

`sudo npm install -g @deepwaterexploration/dwe-controls`

:::{dropdown} Auto Launch

To enable auto-launch (recommended for raspberry pi):

- Install [pm2](https://www.npmjs.com/package/pm2):
`sudo npm install -g pm2`

- Start dwe-controls from pm2:
`pm2 start dwe-controls`

- Save the process list:
`pm2 save`

- Enable startup for pm2: `sudo pm2 startup systemd -u <your username> --hp /home/<your username>`
    - Raspberry Pi: `sudo pm2 startup systemd -u pi --hp /home/pi`

**Running Manually**
To run the application **temporarily** (this is only if you do **not want to install** with auto-launch):

- Run: `dwe-controls start`
:::
::::

### **Interface**
To use the interface, navigate to <http://192.168.2.2:5000> (or <http://companion.local:5000> if running the ArduSub companion software).

![driverui-light](../img/driverui/driverui.png)
