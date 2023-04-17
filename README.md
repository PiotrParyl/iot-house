# Home Telemety

-----------------------------------------------------------
## Table of contents
* [About Project](#about-project)
* [Measured Values](#measured-values)
* [Technologies](#technologies)
* [Scheme](#scheme)
* [Docker](#docker)

-----------------------------------------------------------
# About Project

The purpose of the project is to show water consumption, energy by the heat pump, and energy produced by the solar panels. An electric water meter with Modbus TCP technology was used to measure water consumption. For the measurement of energy consumption by the heat pump, an energy consumption meter has been used, the data is transmitted via MODBUS, over an RS485 cable. For the measurement of energy from solars, the API of the solar manufacturer was used. The data is stored in a MySQL database on Ubuntu Linux hosted on AWS. RaspberryPi 3 and ESP8266 microcontroller were used to receive the signal and process the data. All porgrams and all code was written using Python 3.

-----------------------------------------------------------
## Measured Values
* [Water](#water)
* [Heat Pump](#heat-pump)
* [Solaredge](#solaredge)

### Water
-----------------------------------------------------------

The water meter shown below was used to measure the water. The signal from the water meter goes to the Anybus M-Bus/Modbus-TCP-Gateway by M-Bus where it is converted to Modbus-TCP. The signal then heads to the Rasberry Pi and is sent to the database.  

-----------------------------------------------------------
![299819866_476893500568790_1032156745109520596_n](https://user-images.githubusercontent.com/44020188/185767357-36bae3b8-2d75-4846-8627-dfc2f47971b2.jpg)
![299748267_441129544697349_3292354809080360242_n](https://user-images.githubusercontent.com/44020188/185767350-104266fb-3bf5-45e2-9f71-47b57928bfff.jpg)
![300295083_596211648753536_1953649162381851983_n](https://user-images.githubusercontent.com/44020188/185767363-328519c8-a0f9-45a0-90e4-92e2b18389b7.jpg)


### Heat Pump 
-----------------------------------------------------------
An energy meter LE-03m was used to measure the energy consumption of the heat pump. The meter sends data using MODBUS via RS485. The signal from the converter lands in Reasbery pi where it is sent to the database (AWS). 

The heat pump also has interesting solutions. Using RS485, we can retrieve such data as outdoor temperature, boiler temperature, etc. 

LE-03M manual - https://www.fif.com.pl/pl/liczniki-zuzycia-energii-elektrycznej/339-licznik-zuzycia-energii-le-03m.html?fbclid=IwAR1bsHkWOV45t7rHKxRCWijoEu41s5mZq2mSojO2wou5koqmfIexHmO2TS0


### Solaredge
-----------------------------------------------------------

Downloading data using the API is very simple. Here we have clear instructions: 
[Monitoring server API - Knowledge Center](https://knowledge-center.solaredge.com/sites/kc/files/se_monitoring_api.pdf)

-----------------------------------------------------------
![300527622_1450506268708443_1793216454363325692_n](https://user-images.githubusercontent.com/44020188/185767364-fde33aef-6c20-453e-b6d4-c1153b6e438e.jpg)
![299983697_3288583861412217_546950818204531387_n](https://user-images.githubusercontent.com/44020188/185767367-f9452846-3e50-463e-92bd-2198fca3bb31.jpg)
![299748267_441129544697349_3292354809080360242_n](https://user-images.githubusercontent.com/44020188/185767370-450c477b-0ed8-4d59-8b84-563cef1dd288.jpg)

## Technologies
-----------------------------------------------------------
Technologies Used
The following technologies have been used in this project:

* Python 3
* RaspberryPi 3
* ESP8266 microcontroller
* Electric water meter with Modbus TCP technology
* Energy consumption meter with MODBUS RS485
* Solar panel manufacturer API
* MySQL database
* Linux Ubuntu OS
* AWS

## Scheme
![image](https://user-images.githubusercontent.com/44020188/187191983-09bdd6a8-7a62-4bd9-ab2f-6382e4290327.png)


## Docker
-- Not Ready Yet --
