from machine import Pin
import time

motorPin = Pin(3, Pin.OUT)  # 3:ConnectorA 4:ConnectorB

while True:
    motorPin.on()
    time.sleep(1)
    motorPin.off()
    time.sleep(3)
