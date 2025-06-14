# --- SSD1306 Class start ---
from micropython import const
import framebuf

SET_CONTRAST        = const(0x81)
SET_ENTIRE_ON       = const(0xA4)
SET_NORM_INV        = const(0xA6)
SET_DISP            = const(0xAE)
SET_MEM_ADDR        = const(0x20)
SET_COL_ADDR        = const(0x21)
SET_PAGE_ADDR       = const(0x22)
SET_DISP_START_LINE = const(0x40)
SET_SEG_REMAP       = const(0xA0)
SET_MUX_RATIO       = const(0xA8)
SET_COM_OUT_DIR     = const(0xC0)
SET_DISP_OFFSET     = const(0xD3)
SET_COM_PIN_CFG     = const(0xDA)
SET_DISP_CLK_DIV    = const(0xD5)
SET_PRECHARGE       = const(0xD9)
SET_VCOM_DESEL      = const(0xDB)
SET_CHARGE_PUMP     = const(0x8D)

class SSD1306:
    def __init__(self, width, height, external_vcc, color=framebuf.MONO_VLSB):
        self.width = width
        self.height = height
        self.external_vcc = external_vcc
        self.pages = self.height // 8
        self.buffer = bytearray(self.pages * self.width)
        fb = framebuf.FrameBuffer(self.buffer, self.width, self.height, color)
        self.framebuf = fb
        self.fill = fb.fill
        self.pixel = fb.pixel
        self.hline = fb.hline
        self.vline = fb.vline
        self.line = fb.line
        self.rect = fb.rect
        self.fill_rect = fb.fill_rect
        self.text = fb.text
        self.scroll = fb.scroll
        self.blit = fb.blit
        self.init_display()

    def init_display(self):
        for cmd in (
            SET_DISP | 0x00,
            SET_MEM_ADDR, 0x00,
            SET_DISP_START_LINE | 0x00,
            SET_SEG_REMAP | 0x01,
            SET_MUX_RATIO, self.height - 1,
            SET_COM_OUT_DIR | 0x08,
            SET_DISP_OFFSET, 0x00,
            SET_COM_PIN_CFG, 0x12,
            SET_DISP_CLK_DIV, 0x80,
            SET_PRECHARGE, 0xF1,
            SET_VCOM_DESEL, 0x30,
            SET_CONTRAST, 0xFF,
            SET_ENTIRE_ON,
            SET_NORM_INV,
            SET_CHARGE_PUMP, 0x14,
            SET_DISP | 0x01):
            self.write_cmd(cmd)
        self.fill(0)
        self.show()

    def poweroff(self):
        self.write_cmd(SET_DISP | 0x00)

    def poweron(self):
        self.write_cmd(SET_DISP | 0x01)

    def contrast(self, contrast):
        self.write_cmd(SET_CONTRAST)
        self.write_cmd(contrast)

    def invert(self, invert):
        self.write_cmd(SET_NORM_INV | (invert & 1))

    def show(self):
        x0 = 0
        x1 = self.width - 1
        if self.width == 64:
            x0 += 32
            x1 += 32
        self.write_cmd(SET_COL_ADDR)
        self.write_cmd(x0)
        self.write_cmd(x1)
        self.write_cmd(SET_PAGE_ADDR)
        self.write_cmd(0)
        self.write_cmd(self.pages - 1)
        self.write_data(self.buffer)

class SSD1306_I2C(SSD1306):
    def __init__(self, width, height, i2c, addr=0x3C, external_vcc=False, color=framebuf.MONO_VLSB):
        self.i2c = i2c
        self.addr = addr
        self.temp = bytearray(2)
        super().__init__(width, height, external_vcc, color)

    def write_cmd(self, cmd):
        self.temp[0] = 0x80
        self.temp[1] = cmd
        self.i2c.writeto(self.addr, self.temp)

    def write_data(self, buf):
        self.i2c.writeto(self.addr, b'\x40' + buf)

# --- SSD1306 Class end ---

from machine import SoftI2C, Pin
import time

# ConnectorA: SDA=1, SCL=3
i2c = SoftI2C(sda=Pin(1), scl=Pin(3))  # 1,3:ConnectorA 5,4:ConnectorB
display = SSD1306_I2C(128, 64, i2c)

display.fill(0)
display.text("Hello World!", 0, 0)
display.text("ESP32CherryIoT", 0, 10)
display.show()
