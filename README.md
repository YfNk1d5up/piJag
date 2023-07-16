
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

- **Phone** : CarPlay ,Android Auto, bluetooth, messages and calls
- **Rear Camera** : Automatic on reverse gear or anytime manually
- **Videos** : Kodi & Youtube
- **OBD** : CAN & SCP (Ford Protocol) messages and control
- **Climate** : Climate Control Module App
- **Mobile App** : Start the car, turn on heater or climatisation from Phone

## Screenshots

![Screen Setup](https://github.com/YfNk1d5up/piJag/blob/64cff6b3cc35ca0b5a0ff84e411a75a550c6c579/Pictures/ScreenSetup.jpg)

![(to Add) OpenAuto Pro]()

![(to Add) Wiring diagram]()
## Integration

### Raspberry Pi and carPiHat

The issue with installing custom hardware on a car is mainly how to power and connect them. Should I use the permanent 12V, switched 12V on key, interior lights 12V ...
The raspberry pi 4B is a 5V small computer that can draw 3A when loads are connected.
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

As said in TJD documentation in the *Opto-Isolated Inputs* section, I needed to redirect the CS1 pin to BCM24 to get ill and reverse to work.

From the hat I also used the 2 outputs to control relays :
- One relay power the **4Channels Audio Amplifier remote** and the rear camera with 12V
- The other power the **36W USB Hub** to relieve the strain on the raspberry and charge devices.

(picture)

#### **Parts to come with carPiHat** :
- CAN integration
- I/O expander to add remote powering the car and other stuff

### TouchScreen 

Simply an HDMI and touch USB connected to the RPi, plus 5V power coming from the carPiHat

### Suffering from Hot Temperatures

During summer 2023, a lot of heat has made the setup suffer. This is where I add a 12V computer power fan to help keeping the whole setup at acceptable temperatures.


## obdSniffer

To add more control on the car, I tried to hacked networks through the OBD2 port.

### CAN Bus

Following this awesome serie from Youtube [How to hack your car ](https://youtu.be/cAAzXM5vsi0) by Adam Varga and using his python&Qt [CAN_Gui](https://github.com/adamtheone/canDrive), I copy the setup to hack into my CAN Bus.

Here are for example some data i decoded : 

![obdSniffer GUI](https://github.com/YfNk1d5up/piJag/blob/a38177459cb154fe60be0ee7a9ee079780110d36/Pictures/obdSniffer.png)

### SCP Bus

As the X-Type shares its creation with the Ford Mondeo, the car uses SAEJ1850 PWM aka **Standard Corporate Protocol** or **SCP** to communicate low priority information between modules.

A modification of Adam Varga code brings me the SCP decoding using the ELM327 OBD2 USB Reader using AT commands.

(You can see some SCP data on the previous screenshot)

![SCP Added](https://github.com/YfNk1d5up/piJag/blob/a38177459cb154fe60be0ee7a9ee079780110d36/Pictures/addedSCP.png)


Missing car electrical service manual about SCP and CAN messages
## Ressources