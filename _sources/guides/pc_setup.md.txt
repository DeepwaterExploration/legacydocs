# PC Network Setup Guide

This is a guide for setting up a PC or laptop for use with a Raspberry Pi configured with {doc}`./pi_setup`.

## Configure Device Ethernet

This step is necessary to set the IP of your device in the local network provided by the Raspberry Pi over ethernet.

:::{dropdown} Windows
Under **Settings/Network & Ethernet**, select **Ethernet**

![Network](../img/pi_setup/configure_ethernet/network.png)

Under **Related Settings** on the right, select `Change Adapter Options`

![Adapter Options](../img/pi_setup/configure_ethernet/adapter_options.png)

Find the adapter named `Ethernet` with the subtitle of `Unidentified Network`

![Adapter](../img/pi_setup/configure_ethernet/adapter.png)

Right-click the adapter and select `Properties`

![Adapter](../img/pi_setup/configure_ethernet/right-click-adapter.png)

Locate `Internet Protocol Version 4 (TCP/IPv4)` and select `Properties`

![Properties](../img/pi_setup/configure_ethernet/properties.png)

Edit the menu to look like the following:

![Settings](../img/pi_setup/configure_ethernet/settings.png)

Click `OK` to apply changes. This should now allow you Pi to identify your Windows device under the correct ip address to stream data to.
:::


See our [Gstreamer Guide](./gstreamer_guide.md) for Gstreamer setup.