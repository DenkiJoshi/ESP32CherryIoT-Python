from machine import Pin
import time

swPin = Pin(3, Pin.IN)  # 3:ConnectorA 4:ConnectorB
ledPin = Pin(4, Pin.OUT)  # 3:ConnectorA 4:ConnectorB

while True:
    state = swPin.value()  # Check switch status. If pushed, "1"
    if state == 1:
        ledPin.on()  # LED ON
        print("Pushed")
    else:
        ledPin.off()  # LED OFF
        print("Not Pushed")
    
    time.sleep(0.2)