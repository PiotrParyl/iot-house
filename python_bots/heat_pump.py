import minimalmodbus
import serial 
from time import sleep, time
import datetime
from datetime import datetime


#========================= licznik connection #=========================
instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 3)  # port name, slave$

instrument.serial.port                     # this is the serial port name
instrument.serial.baudrate = 9600         # Baud
instrument.serial.bytesize = 8
instrument.serial.parity   = serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout  = 0.1          # seconds
instrument.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode
instrument.clear_buffers_before_each_transaction = True

#========================= loop #=========================
while True:
        r0 = instrument.read_register(0)
        sleep(1)
        r1 = instrument.read_register(1)
        sleep(2)
        r2 = instrument.read_register(2)
        wynik = (r0 *(256*256) + r1 * 256 + r2)/10
        e = datetime.now()
        #========================= dodawanie do bazy danych #===============$
        wynik = float(wynik)
        print(wynik)       
        sleep(300)   