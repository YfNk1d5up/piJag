
# piJag

Audio/Video Screen Unit of Jaguar X Type X400 based on a raspberry and openAuto pro: bluetooth, CarPlay, OBD, remote start, climate module control

[github] https://github.com/YfNk1d5up/piJag




## Hardware & Software

 - This project was initially thought for Jaguar X-Type X400 (2001) but some parts will work for other cars
 - It uses :
    - [Rpi 4B 4GB RAM](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)
    - [OpenAuto Pro](https://bluewavestudio.io/shop/openauto-pro-car-head-unit-solution/)
    - [CarPiHat](https://thepihut.com/products/carpihat-car-interface-hat-for-raspberry-pi)
    - [10.1" TouchScreen](https://www.amazon.fr/gp/product/B0B4VMNB42/ref=ppx_yo_dt_b_search_asin_image?ie=UTF8&psc=1)
    - [Carlinkit](https://www.amazon.fr/gp/product/B09ZQF182F/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1)
    - [USB Sound Card](https://www.amazon.fr/gp/product/B00IRVQ0F8/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1)
    - [Rear Camera](https://www.amazon.fr/gp/product/B0BG5M8H76/ref=ppx_yo_dt_b_asin_title_o01_s01?ie=UTF8&psc=1)
    - [CVBS to USB adapter](https://www.amazon.fr/gp/product/B0BYJ2892S/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)
    - [12V Voltage Regulator](https://www.amazon.fr/gp/product/B09Q1XXM6G/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1)
    - [Powered USB Hub](https://www.amazon.fr/gp/product/B0BDFG1WZ7/ref=ppx_yo_dt_b_asin_title_o06_s00?ie=UTF8&psc=1)
    - [ELM327 OBD USB](https://www.amazon.fr/gp/product/B07NSPLVYW/ref=ppx_yo_dt_b_asin_title_o07_s00?ie=UTF8&psc=1)
    - 12V relays, Fan, Microphone, 4Channel Amplificator, HDMI & RCA cables, Audio Splitter ...
 - A custom PCB to control the Climate Control Module with an arduino nano (Kicad & JLCPCB)



## Features

- **Phone** : CarPlay, Android Auto, bluetooth, messages and calls
- **Rear Camera** : Automatic on reverse gear or anytime manually
- **Videos** : Kodi & Youtube
- **OBD** : CAN & SCP (Ford Protocol) messages and control
- **Climate** : Climate Control Module App
- **Mobile App** : Start the car, turn on heater or climatisation from Phone

## Screenshots

![Screen Setup](https://github.com/YfNk1d5up/piJag/blob/64cff6b3cc35ca0b5a0ff84e411a75a550c6c579/Pictures/ScreenSetup.jpg)

![(to Add) OpenAuto Pro]()

![Wiring Setup](https://github.com/YfNk1d5up/piJag/blob/84df7824ad0f885efc3d49e76ffdeab592a43be3/Pictures/WiringSetup.jpg)
## Integration

### Raspberry Pi and carPiHat

The issue with installing custom hardware on a car is mainly how to power and connect them. Should I use the permanent 12V, switched 12V on key, interior lights 12V ...
The raspberry pi 4B is a 5V small computer that can draw 3A when loads are connected to it.
In this setup, a lot of usb devices are connected and I should consider this ~3A as a constant.
5V 3A, drawn from the car battery makes it impossible keeping powered on the constant battery supply.
In deed it needs to be powered off when I'm not in the car, and it needs a 12V to 5V step-down.
This is where I found [carPiHat](https://github.com/gecko242/CarPiHat) from TJD that saved me a lot of work :
- 12V - 5V buck converter to power the pi and touchscreen, with fuse and filtering.
- Safe shutdown circuitry to allow the pi to control its own power.
-  < 1mA current draw when switched off.
- Dedicated reverse, illumination and aux inputs, all opto isolated.
- 2 opto isolated general purpose inputs. (for a total of 5 inputs)
- 2 high current, high side switched 12V outputs (@1A). (for switching relays, lights ect)
- 1 independent CAN bus port.
- Real time clock to maintain system time across reboots.
- Broken out I2C bus.
- Broken out 1W for temperature sensor ect.
- 5V Power Output for display ect.

So the power aspect is done using this hat for the raspberry, connecting constant 12V, switched 12V, reverse gear input, illumination input, and GND

Then, a script makes the automation of the RPi power off 30s after turning the car off :

```python
import RPi.GPIO as GPIO # import our GPIO module
import time
from subprocess import call

GPIO.setmode(GPIO.BCM) # we are using BCM pin numbering

IGN_PIN = 12		# our 12V switched pin is BCM12
EN_POWER_PIN = 25	# our latch pin is BCM25

ILL_PIN = 13		# our 12V Illumination input pin is BCM13
REVERSE_PIN = 7	# our 12V Reverse Gear input pin is BCM7

IGN_LOW_TIME = 30 # time (s) before a shutdown is initiated after power loss

GPIO.setup(IGN_PIN, GPIO.IN) # set our 12V switched pin as an input
GPIO.setup(ILL_PIN, GPIO.IN) # same for ill and reverse 
GPIO.setup(REVERSE_PIN, GPIO.IN)

GPIO.setup(EN_POWER_PIN, GPIO.OUT, initial=GPIO.HIGH) # set our latch as an output

GPIO.output(EN_POWER_PIN, 1) # latch our power. We are now in charge of switching power off

ignLowCounter = 0

while 1:
	if GPIO.input(IGN_PIN) != 1: 				# if our 12V switched is not disabled
		time.sleep(1)							# wait a second
		ignLowCounter += 1						# increment our counter
		if ignLowCounter > IGN_LOW_TIME:		# if it has been switched off for >10s
			print("Shutting Down")
			call("sudo shutdown -h now", shell=True)	# tell the Pi to shut down
	else:
		ignLowCounter = 0 						# reset our counter, 12V switched is HIGH again

        time.sleep(0.1)  # Add a small sleep delay to reduce CPU usage
```

As said in TJD documentation in the *Opto-Isolated Inputs* section, I needed to redirect the CS1 pin to BCM24 to get ill and reverse inputs to work.

From the hat I also used the 2 outputs to control relays :
- One relay powers the **4Channels Audio Amplifier remote** and the rear camera with 12V
- The other powers the **36W USB Hub** to relieve the strain on the raspberry and charge devices.

(picture)

#### **Parts to come with carPiHat** :
- CAN integration
- I/O expander to add remote powering the car and other stuff

### TouchScreen 

Simply an HDMI and touch USB connected to the RPi, plus 5V power coming from the carPiHat

### Suffering from Hot Temperatures

During summer 2023, a lot of heat has made the setup suffer. This is where I add a 12V computer power fan to help keeping the whole setup at acceptable temperatures.


## obdSniffer

To add more control on the car, I tried to hack bus networks through the OBD2 port.

![X-Type BUS Networks](https://github.com/YfNk1d5up/piJag/blob/cd5db3b18367be92419ba5bebd26b652316670b5/Pictures/jagBUSNetworks.png)

### CAN Bus

Following this awesome serie from Youtube [How to hack your car ](https://youtu.be/cAAzXM5vsi0) by Adam Varga and using his python&Qt [CAN_Gui](https://github.com/adamtheone/canDrive), I copy the setup to hack into my CAN Bus.

Here are for example some data I decoded : 

![obdSniffer GUI](https://github.com/YfNk1d5up/piJag/blob/a38177459cb154fe60be0ee7a9ee079780110d36/Pictures/obdSniffer.png)

### SCP Bus

As the X-Type shares its creation with the Ford Mondeo, the car uses SAEJ1850 PWM aka **Standard Corporate Protocol** or **SCP** to communicate low priority information between modules.

A modification of Adam Varga code brings me the SCP decoding using the **ELM327 OBD2 USB Reader** using **AT** commands.
Modified functions :
*serialPacketReceiverCallback*
*serialPortConnect*
file *SerialReader.py*

(You can see some SCP data on the previous screenshot)

![SCP Added](https://github.com/YfNk1d5up/piJag/blob/a38177459cb154fe60be0ee7a9ee079780110d36/Pictures/addedSCP.png)

To achieve that, first I did some tests using AT on linux terminal

```bash
sudo screen /dev/ttyUSB0 38400
```

```bash
>atz
ELM327 v1.5

>atl1
OK

>ath1
OK

>ats1
OK

>atal
OK

>atsp1
OK

>atma

```

For AT commands explanation, SCP application case and another hardware setup, see this thread : https://www.jaguarforum.com/threads/reverse-engineering-hacking-scp-bus-to-xj-x350-x358-s-type-and-x-type.108639/

Example output :

```bash
81 29 60 02 0081 29 60 02 00 00 11
41 87 60 04 08 B1
81 7B 60 02 00 4C
81 7B 60 02 00 4C
```


See [X-Type Electrical Guide CAN/SCP](https://github.com/YfNk1d5up/piJag/blob/cf38571dc9505988becb3cf82d76548922db3a51/Docs/JagClimModule.pdf) to find more information about CAN and SCP messages

## OpenAuto Pro setup


## Climate Control Module Hack

The goal here was to remove the Control Unit that is space-consuming and overall avoid me to install the screen properly without destroying the case.
To continue adding a modern touch to my X-Type, I enjoy controlling the climate directly on the touchscreen via an app on openAuto Pro.

Firstly, I need to understand well how the existing module works.
So I bought another one to avoid getting stuck breaking it : in deed, it is connected to the CAN Bus and the car will not start if the module doesn't work or isn't connected to the bus.

By the CAN and SCP analyse done previously, I found that buttons user actions are not going through any bus on the car, plus the electrical documentation shows that the module only communicate with other modules to say an action has been performed.
FYI, the second X-Type (X404) added LIN to the buses, where climate, windows control, driver wheel buttons, etc, communicate through it.

But no chance, that is not the case for my version. So sending commands on buses to control the climate module is impossible.

That said, there is no other way than hacking electronics of the module by adding a custom Mod PCB.

The Module consists in 2 PCBs connected by a 20 wires ribbon. On the electrical documentation, only the global module connections to the rest of the car is detailed. 
Lucky for me, somebody already took a look into that module, because he wanted to change the screen to a modern one. The report is joined in [David's initial HVAC Sniffer](https://github.com/YfNk1d5up/piJag/blob/cf38571dc9505988becb3cf82d76548922db3a51/Docs/p10018_jag_hvac_sniffer.zip)

![(HVAC PCBs)](https://github.com/YfNk1d5up/piJag/blob/cb95ea8a1820f61842fe06ae5841b4ef52b6cd94/Pictures/HVAC_PCBs.png)

The first PCB contains the MCU which does CAN communication to the rest of the vehicule, control of fans, compressor, etc : that is the one I want to keep.
The second one contains all the buttons, the LCD screen, a digital encoder, and maybe a second propietary MCU impossible to identify : I want to replace this PCB.
Doing some retro-engineering and finding the documentation of the MCU in the first PCB, here is the connection from and to that second PCB :

[Initial retro-engineering of the 2nd PCB](https://github.com/YfNk1d5up/piJag/blob/cf38571dc9505988becb3cf82d76548922db3a51/Docs/piJagClim_existing_module.pdf)

You can see here a switches matrix, using 6 wires for 12 buttons. An I2C screen connected straigth to the main MCU, a rotary encoder also directly connected to the main board.
What I used for the buttons is analog switches, that works as relays except that they are small 14 pins chips, which each entry is controlled by an Arduino digital pin. For the rotary encoder, an Arduino Nano can easily simulate the signals by using two digital pins.
Finally, using David's work about the i2c screen, I can get the information coming from the main MCU by decoding it using A4 and A5 pins on the Nano.

And so here is the mod board v0.1 :
![climateModBoard](https://github.com/YfNk1d5up/piJag/blob/a2ac1a76f2b90d971d53ccd2ccb150d1904e1d3c/Pictures/modPCB.png)
![PCB3D](https://github.com/YfNk1d5up/piJag/blob/84df7824ad0f885efc3d49e76ffdeab592a43be3/Pictures/PCB3D.png)
![PCBTop](https://github.com/YfNk1d5up/piJag/blob/84df7824ad0f885efc3d49e76ffdeab592a43be3/Pictures/PCBTop.png)
![PCBBottom](https://github.com/YfNk1d5up/piJag/blob/84df7824ad0f885efc3d49e76ffdeab592a43be3/Pictures/PCBBottom.png)


## Ressources
