from machine import Pin
import time

swPin = Pin(3, Pin.IN)  # 3:ConnectorA 4:ConnectorB
ledPin = Pin(4, Pin.OUT)  # 3:ConnectorA 4:ConnectorB
state = False

def LED_blink(pin):
    global state
    time.sleep_ms(30)
    state = not state
    ledPin.value(state)

# Interrupt Setting
swPin.irq(trigger=Pin.IRQ_FALLING, handler=LED_blink)

while True:
    pass