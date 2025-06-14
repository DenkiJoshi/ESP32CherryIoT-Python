from machine import Pin
import time

touch_pin = Pin(3, Pin.IN)  # 3:ConnectorA 4:ConnectorB

while True:
    if touch_pin.value() == 1:
        print("Touch!")
    else:
        print("...")
    time.sleep(0.5)
