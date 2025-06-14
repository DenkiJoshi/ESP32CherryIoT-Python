from machine import Pin
import time

ledPin = Pin(3, Pin.OUT)  # 3:ConnectorA 4:ConnectorB 10:Builtin

while True:
    for i in range(3):
        ledPin.on()  # LED ON
        time.sleep(0.5)  # 0.5 seconds
        ledPin.off()  # LED OFF
        time.sleep(0.5)  # 0.5 seconds
    time.sleep(2)