# SSH Into a Raspberry Pi

```{important}
If you are plugging your Vehicle/Raspberry Pi/Other Device directly into your laptop via an ethernet cable/adapter/dongle, please see the [PC Network Setup Guide](../guides/pc_setup.md) first.
```

This guide describes how to connect to a Raspberry Pi over a secure ssh connection. It is expected the Raspberry Pi is connected over ethernet and has the IP 192.168.2.2, which is standard for most ROVs.

:::{dropdown} Windows
   For Windows, we recommend using Putty, which can be downloaded [here](https://www.putty.org/)

   * After installing, open Putty and type the address of the Raspberry Pi (which should be set to 192.168.2.2 if you are following {doc}`Our Guide <./pi_setup>`)

   * Keep the other settings as default and click the `Open` button

   ![Putty Connect](../img/pi_setup/putty/putty2.png)

   * After connecting you will be prompted with a *security alert*. Ensure you select **accept**.

   ![Security Alert](../img/pi_setup/putty/putty3.png)

   * To log in, use the following credentials: username: `pi`, password: `raspberry`

   * You will be greeted with a terminal

:::

:::{dropdown} Linux/Mac
   First, open your terminal app.

   ```{note}
   If using Linux, this will depend on your distribution. On MacOS, you can open spotlight and type: `Terminal`.
   ```

   The general format for ssh on unix is:
   `ssh -p port user@IP-Address`

   Enter the following command:

    ssh -p 22 pi@192.168.2.2

   The password will be `raspberry` by default.
:::
