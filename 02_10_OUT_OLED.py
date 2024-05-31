from machine import SoftI2C, Pin
import ssd1306

i2c = SoftI2C(sda=Pin(26), scl=Pin(25))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

display.text('Hello World!', 0, 0, 1)
display.text('CherryIoT', 0, 10, 1)
display.show()
