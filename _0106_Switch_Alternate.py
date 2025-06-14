from machine import Pin
import time

swPin = Pin(3, Pin.IN)  # 3:ConnectorA 4:ConnectorB
flag = False

while True:
    state = swPin.value()  # Check switch status. If pushed, "1"
    if state == 1:
        flag = not flag
        
    if flag == 1:
        print("ON")
    else:
        print("OFF")
        
    time.sleep(0.2)