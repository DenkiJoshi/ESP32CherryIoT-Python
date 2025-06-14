from machine import Pin
import time

vibPin = Pin(3, Pin.OUT)  # 3:ConnectorA 4:ConnectorB

while True:
    vibPin.on()
    time.sleep(1)
    vibPin.off()
    time.sleep(1)
