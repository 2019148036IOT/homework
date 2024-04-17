

https://github.com/2019148036IOT/homework/assets/164009716/e99ad71e-5535-4449-bd06-7f41519811ba

과제를 완성하는데 실패했습니다.
파이썬 파일을 프로그래밍하고, 2개의 esp32에 각각 넣으려 했지만 이에 실패했고, 코드 역시 문제가 있던것같습니다.

```
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
```
이는 스위치를 작동시키려고 했던 파이썬 코드입니다.
```
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
```
이는 릴레이를 구동시키려고 만든 파이썬 코드입니다.
