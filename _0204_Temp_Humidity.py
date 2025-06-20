# Import it into main.py and upload it to your device
from machine import Pin, I2C
import time

# I2C setup
i2c = I2C(0, scl=Pin(3), sda=Pin(1), freq=400000)  # 3,1:ConnectorA 4,5:ConnectorB
address = 0x38

# Trigger command
set_cmd = [0xAC, 0x33, 0x00]

# Buffer for reading data
data = bytearray(7)

def read_sensor():
    # Send trigger command
    time.sleep(0.01)
    i2c.writeto_mem(address, 0x00, bytearray(set_cmd))
    
    # Read data
    time.sleep(0.08)
    data = i2c.readfrom_mem(address, 0x00, 7)
    
    # Convert data
    hum = (data[1] << 12) | (data[2] << 4) | ((data[3] & 0xF0) >> 4)
    temp = ((data[3] & 0x0F) << 16) | (data[4] << 8) | data[5]
    
    # Convert to physical values
    hum = hum / (2**20) * 100
    temp = temp / (2**20) * 200 - 50
    
    return temp, hum

while True:
    try:
        temp, hum = read_sensor()
        print("Temperature: {:.2f}℃  Humidity: {:.2f}%".format(temp, hum))
    except OSError as e:
        print("ERROR: ", e)
    
    time.sleep(2)
