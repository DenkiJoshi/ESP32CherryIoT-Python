from machine import Pin
import time

ledPin = Pin(3, Pin.OUT)  # 3:ConnectorA 4:ConnectorB 10:Builtin

while True:
    ledPin.on()  # LED ON
    time.sleep(0.5)  # 0.5 seconds
    ledPin.off()  # LED OFF
    time.sleep(0.5)  # 0.5 seconds