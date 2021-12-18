# Fiber Board

[![Fiber Board](https://cdn.shopify.com/s/files/1/0575/8785/9626/products/ROVFiberBoardMainPic_590x.jpg?v=1638213044)](https://exploredeepwater.com/products/ethernet-fiber-converter)

[Product Link](https://exploredeepwater.com/products/ethernet-fiber-converter)

## Introduction

This bare PCB converts CAT 5 Ethernet signals from the RJ-45 port to signals compatible with single mode SFP transceivers and vice versa. By using this media converter, copper Ethernet signals can be extended up to 20km depending on the SFP transceiver used (a much longer distance than the 100 meters limit for copper Ethernet signals).

Unlike many other fiber converters, this is designed to be as space efficient as possible specifically for ROV use cases. Additionally, many considerations were in place to design this board as power efficient as possible, reducing generated heat and maximizing the flight time on your ROV!

**Fits in 3" acrylic ROV electronic enclosure!**

## Advantages of Fiber over Traditional Copper for ROV Use
* Gigabit data transfer with kilometers of tether length (Copper: 100 meters max for Gigabit, 300 meters max for 100Mb/s)
* Lower Latency (Light transfers much faster)
* Virtually no risk of interference compared to copper 
## Technical Specifications
**Input Voltage:** 3.5V - 18V DC (Recommended 5V)

**Input Connector:** 5.5 x 2.5 mm Power Jack or 2.54 mm Pitch Jumper wires

**Wattage:** Less than 1 watt

**Footprint:** 3 x 2 inches

**Bandwidth:** 1.25G

**Complies with IEEE 802.3/802.3u/802.3z/802.3ab**

**Complies with 10/100/1000Base-TX/FX**

**Supports Full/Half Duplex auto-negotiation and MDI/MDIX auto-crossover**

## Speed Testing

<img width="50%" alt="Speed Test" src="https://lh5.googleusercontent.com/9gnJgrl48jOgrcpfGyYCmH2QDH0TxvaL3niB3Qaa_sXbAKGRTUKMfom-XH_HC6I8iVFJvQ5y2PVZ8Tj64Qi3q3YcKVASEtDbjWmjEItsAiru9jO-Kp955UdbVsCLpVZml0KJ7Ldu"></img>

## Current Testing

<img width="50%" alt="Current Test" src="https://lh3.googleusercontent.com/AHBo-pURvVdEoDWIXezHTL2tgsWtQPQ4N4rsk2aNKWCyBiQuSPThywpGrCEWv2br2tzr0kwKl_2G-p0tAKvH9p3tgW1JJSx1iBl-Zxei5A7FCGK2QPROOAYrxMO4elTIjcvMbJDk"></img>

## LED Indicators

<img width="100%" alt="LED Indicators" src="https://lh6.googleusercontent.com/xNYV85fOr43yrQSKP6b0H13l5y7_Sg2RvvT-Sv4dXOQvlXPzV5-7iSS-V0e94N7U89uehXjezc8svUktcuRsxQY341lPW5cWOpOCPUCqauLIjvrvCkcGhZPKVwciEbt6HhaeuEm8"></img>

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
![Fiber Board](https://cdn.shopify.com/s/files/1/0575/8785/9626/files/ROV_Fiber_Board_Power_Connector_390x.jpg?v=1638213044)

Given its wide input voltage range from 3.5V to 18V, there are multitude of ways to power the board. We recommend staying at 5V as that is a voltage commonly found and would retain high efficiency within the board's power converters.

```{important} 
Power connector will only fit **5.5 x 2.5 MM** power jacks. Power header pins have a pitch of 2.54 MM.
```

```{admonition} Recommended Methods for Powering
* 2.54MM Pitch Jumper wires
* USB to DC 5V Power Cable ()
* 120V AC to 12V/5V Power Supplies
```


## Supported SFP Transceivers
```{important} All SFP optical transceiver  used on the board must be **1.25Gb/s data rate** and designed for **10/100/1000Base-TX/FX**
```
### BiDi (Bidirectional) SFP Optical Transceiver 
BiDi is recommended over common SFP due to its ability to transmit full-duplex on one strand of fiber by using different wavelengths of light. Our kit on our product listing offers a pair of 2km range BiDi Transceivers with (1550/1310nm wavelength).

[Learn More](https://blog.fluxlight.com/2016/07/16/introduction-to-bidi-optical-transceivers/)
### Common SFP Optical Transceiver
Common SFP Transceivers are also compatible with our board. They will require 2 strands of fiber for full-duplex communication.

## Fiber Optic Tethers

* [LINDEN SPE 7055 High Strength Buoyant 450](http://www.lindenphotonics.com/documents/Linden%20-%20Catalog%202017.pdf)
* [Delta ROV Fiber Optic Tether](http://www.deltarov.com/new/product/tether-1-sm-fiber-optic-1000m/)