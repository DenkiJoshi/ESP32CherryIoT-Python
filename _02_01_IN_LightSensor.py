from machine import Pin, ADC
import time

input_pin = 32
device_voltage = 3.3

adc = ADC(Pin(input_pin))
adc.width(ADC.WIDTH_12BIT)  # Set ADC resolution to 12-bit
adc.atten(ADC.ATTN_11DB)

while True:
    cds_ad = adc.read()  # Read analog data
    cds_v = cds_ad * device_voltage / 4096  # Calculation of voltage value
    lux = 10000 * cds_v / (device_voltage - cds_v) / 1000  # Calculation of lux value
    
    print("{:.2f} Lux : ".format(lux), end="") 
    
    if lux > 20:
        print("Bright")
    else:
        print("Dark")
    
    time.sleep(0.5)
