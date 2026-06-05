from machine import Pin, I2C
import time

# 1,3: ConnectorA / 5,4: ConnectorB
i2c = I2C(0, sda=Pin(1), scl=Pin(3), freq=400000)

DHT20_ADDR = 0x38

def read_dht20():
    # Measurement start command
    i2c.writeto(DHT20_ADDR, bytes([0xAC, 0x33, 0x00]))
    time.sleep_ms(80)

    data = i2c.readfrom(DHT20_ADDR, 7)

    # Check the bit during measurement.
    if data[0] & 0x80:
        raise RuntimeError("DHT20 is busy")

    # humidity 20bit
    raw_hum = (
        (data[1] << 12)
        | (data[2] << 4)
        | (data[3] >> 4)
    )

    # temprature 20bit
    raw_temp = (
        ((data[3] & 0x0F) << 16)
        | (data[4] << 8)
        | data[5]
    )

    humidity = raw_hum * 100 / 1048576
    temperature = raw_temp * 200 / 1048576 - 50

    return temperature, humidity


while True:
    try:
        temp, hum = read_dht20()
        print("{:.1f}℃ / {:.1f}％".format(temp, hum))
    except Exception as e:
        print("DHT20 read error:", e)

    time.sleep_ms(500)
