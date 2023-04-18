from pymodbus.client.sync import ModbusTcpClient
from time import sleep, time
import datetime
import mysql.connector

while True:

    client = ModbusTcpClient(host= '192.168.1.243', port=502)
    client.connect()

    rr  = client.read_holding_registers(30,4)

    client.close()

    a = rr.registers[-1]
    b = rr.registers[-2]

    print(a,"  ",b)
    sleep(300)