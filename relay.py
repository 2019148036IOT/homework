from IO7FuPython import Device, ConfiguredDevice
import json
import time
import ComMgr
import dht
from machine import Pin

from IO7FuPython import Device, ConfiguredDevice
import json
import time
import ComMgr
import dht

amb = ADC(Pin(15))
amb.atten(ADC.ATTN_11DB) #Full range: 3.3v
relay = Pin(23, Pin.OUT)
while True:
    pot_value = amb.read()
    print(pot_value)
    if pot_value < 30:
    relay.on()
    else:
        relay.off()
        sleep(0.1) 

nic = ComMgr.startWiFi('AndroidHotspots3602')
device = ConfiguredDevice()
device.setUserCommand(handleCommand)
device.connect() 

nic = ComMgr.startWiFi('io7lux')
device = ConfiguredDevice()
device.setUserCommand(handleCommand)
device.connect() 