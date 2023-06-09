# Gigabit Fiber to Ethernet Converter (ROV/AUV)

![Fiber Board](https://cdn.shopify.com/s/files/1/0575/8785/9626/files/GigabitFibertoEthernetConverter.jpg?v=1686122270&width=590)

## Introduction

This bare PCB converts CAT 5 Ethernet signals from the RJ-45 port to signals compatible with single mode SFP transceivers and vice versa. By using this media converter, copper Ethernet signals can be extended up to 20km depending on the SFP transceiver used (a much longer distance than the 100 meters limit for copper Ethernet signals).

Unlike many other fiber converters, this is designed to be as space efficient as possible specifically for ROV use cases. Additionally, many considerations were in place to design this board as power efficient as possible, reducing generated heat and maximizing the flight time on your ROV!

**Fits in 3" acrylic ROV electronic enclosure!**

## Advantages of Fiber over Traditional Copper for ROV Use

* Gigabit data transfer with kilometers of tether length (Copper: 100 meters max for Gigabit, 300 meters max for 100Mb/s)
* Lower Latency (Light transfers much faster)
* Virtually no risk of interference compared to copper 

## Technical Specifications

**Input Voltage:** 5V DC

**Input Connector:** JST PH 2.54 or 2.54mm Pitch Jumper wires

**Wattage:** Less than 1 watt

**Footprint:** 3 x 2 inches

**Bandwidth:** 1.25G

**Complies with IEEE 802.3/802.3u/802.3z/802.3ab**

**Complies with 10/100/1000Base-TX/FX**

**Supports Full/Half Duplex auto-negotiation and MDI/MDIX auto-crossover**

## Testing

:::{dropdown} Speed Testing
```{image} ../img/fiberboard/speed_test.png
:alt: Speed Test
:width: 50%
```
:::

:::{dropdown} Current Testing
```{image} ../img/fiberboard/current_test.png
:alt: Current Test
:width: 50%
```
:::

## LED Indicators
```{image} ../img/fiberboard/LED_indicators.jpg
:alt: LED Indicators
:width: 100%
```

<span style="color: #55aaff; font-weight: bold">Blue</span>
* LED4: Power LED, Lights up when +5V is applied

<span style="color: red; font-weight: bold">Red</span>
* FDX LED: Lights up when Full Duplex is used
* FBR LEF: Lights up when Fiber Port is working (Fiber and Transceiver must be plugged in as a pair)

<span style="color: #CCCC00; font-weight: bold">Yellow</span>
* TP: Network is connected via Ethernet
* 100M: 100Mbps Speed is Used
* 1000M: Gigabit Speed is Used

## Powering


```{warning} 
Make sure to use a 5V supply to power the boards and the polairty of the JST connectors are correct. 
```

```{admonition} Recommended Methods for Powering
* 2.54MM Pitch Jumper wires
* JST XH 2.54mm 2 Pin Power Connectors
```

## Supported SFP Transceivers

```{important} All SFP optical transceiver  used on the board must be **1.25Gb/s data rate** and designed for **10/100/1000Base-TX/FX**
```
```{warning} SFP transceivers use CLASS 1 laser. Do not look directly at the light emitting device.

```

:::{dropdown} BiDi (Bidirectional) SFP Optical Transceiver 
BiDi is recommended over common SFP due to its ability to transmit full-duplex on one strand of fiber by using different wavelengths of light. Our kit on our product listing offers a pair of 2km range BiDi Transceivers with (1550/1310nm wavelength).

[Learn More](https://blog.fluxlight.com/2016/07/16/introduction-to-bidi-optical-transceivers/)
:::

:::{dropdown} Common SFP Optical Transceiver
Common SFP Transceivers are also compatible with our board. They will require 2 strands of fiber for full-duplex communication.
:::

## Fiber Optic Tethers

* [LINDEN SPE 7055 High Strength Buoyant 450](http://www.lindenphotonics.com/wp-content/uploads/2023/LPI%20Cables%20Catalog%202023.pdf)
* [Delta ROV Fiber Optic Tether](http://www.deltarov.com/new/product/tether-1-sm-fiber-optic-1000m/)

## Technical Drawing

<iframe src="../_static/pdf/DWE_Fiber_Board_Drawing.pdf" width="100%" height="500px">