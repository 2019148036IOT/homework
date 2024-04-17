from IO7FuPython import Device, ConfiguredDevice
import json
import time
import ComMgr
import dht
from machine import Pin



nic = ComMgr.startWiFi('io7lux')
device = ConfiguredDevice()
device.setUserCommand(handleCommand)
device.connect() 