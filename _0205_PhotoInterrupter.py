from machine import Pin
import time

rupt_pin = Pin(3, Pin.IN)  # 3:ConnectorA 4:ConnectorB

while True:
    if rupt_pin.value() == 0:
        print("Interrupt!")
    else:
        print("...")
    time.sleep(0.5)
