from machine import Pin, ADC
import time

litsnsrPin = Pin(3, Pin.IN)  # 3:ConnectorA 4:ConnectorB
device_voltage = 3.3

adc = ADC(Pin(litsnsrPin))
adc.width(ADC.WIDTH_12BIT)  # Set ADC resolution to 12-bit
adc.atten(ADC.ATTN_11DB)

while True:
    litsnsr_ad = adc.read()  # Read analog data
    litsnsr_v = litsnsr_ad * device_voltage / 4096  # Calculation of voltage value
    lux = 10000 * litsnsr_v / (device_voltage - litsnsr_v) / 1000  # Calculation of lux value
    
    print(f"{lux:.2f} Lux : ", end="")
    
    if lux > 20:
        print("Bright")
    else:
        print("Dark")
    
    time.sleep(0.5)
