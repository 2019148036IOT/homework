from IO7FuPython import Device, ConfiguredDevice
import json
import time
import ComMgr
import dht
from machine import Pin

sw = Pin(15, Pin.IN, Pin.PULL_UP)

def pressed(p):
    if not p.value():
        switch.on()
    else:
        switch.off()


        

nic = ComMgr.startWiFi('AndroidHotspots3602')
device = ConfiguredDevice()
device.setUserCommand(handleCommand)