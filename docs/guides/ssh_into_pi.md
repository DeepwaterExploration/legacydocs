# SSH Into a Raspberry Pi

### Windows

For Windows, we recommend using Putty which can be downloaded from [here](https://www.putty.org/)

* After installing, open Putty and type the address of the Raspberry Pi (which should be set to 192.168.2.2 if you are following {doc}`Our Guide <./pi_setup>`)

![Putty](../img/pi_setup/putty/putty.png)

* Keep the other settings as default and click the `Open` button

![Putty Connect](../img/pi_setup/putty/putty2.png)

* After connecting you will be prompted with a *security alert*. Ensure you select **accept**.

![Security Alert](../img/pi_setup/putty/putty3.png)

* To log in, use the following credentials: username: `pi`, password: `raspberry`

![Log in](../img/pi_setup/putty/putty4.png)
![Password](../img/pi_setup/putty/putty5.png)

* You should be greeted with the following:

![Greeting](../img/pi_setup/putty/putty6.png)

### Linux and MacOS

First, open your terminal app.

```{note}
If using Linux, this will depend on your distribution. On MacOS, you can open spotlight and type: `Terminal`.
```

The general format for ssh on unix is:
`ssh -p port user@IP-Address`

Assuming a port of 22, a username of pi, and an ip address of 192.168.2.2:

```
ssh -p 22 pi@192.168.2.2
```

The password should default to `raspberry`.
