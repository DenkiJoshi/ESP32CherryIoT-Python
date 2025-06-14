from machine import Pin
import time

ledPin1 = Pin(3, Pin.OUT)  # 3:ConnectorA 4:ConnectorB 10:Builtin
ledPin2 = Pin(10, Pin.OUT)  # 3:ConnectorA 4:ConnectorB 10:Builtin

while True:
    ledPin1.on()  # LED1 ON
    ledPin2.off()  # LED2 OFF
    time.sleep(0.5)  # 0.5 seconds
    ledPin1.off()  # LED1 OFF
    ledPin2.on()  # LED2 ON
    time.sleep(0.5)  # 0.5 seconds