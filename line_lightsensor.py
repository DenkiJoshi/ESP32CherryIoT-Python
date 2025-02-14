# Line Bot test program
# https://zenn.dev/iot101/articles/d8e26ac7be133b
# https://github.com/PerfecXX/micropython-linenotify

import network
import time
from linenotify import LineNotify
from machine import Pin, ADC

input_pin = 32
device_voltage = 3.3

adc = ADC(Pin(input_pin))
adc.width(ADC.WIDTH_12BIT)  # Set ADC resolution to 12-bit
adc.atten(ADC.ATTN_11DB)

cds_ad = adc.read()  # Read analog data
cds_v = cds_ad * device_voltage / 4096  # Calculation of voltage value
lux = 10000 * cds_v / (device_voltage - cds_v) / 1000  # Calculation of lux value

# WiFi接続設定
SSID = 'WAP01-11ng'
PASSWORD = 'BS7%26VuZacy'

# Line token
TOKEN = 'CNFTN4p61bZ1wsyRyfzZsFa1n2rTEDoTebFC0dXTLIL'

# WiFi接続関数
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    print("WiFiに接続中...")
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(1)

    print("\nWiFi接続完了:", wlan.ifconfig())

# WiFiに接続
connect_wifi(SSID, PASSWORD)

# Line Notifyを使ってメッセージ送信
line = LineNotify(TOKEN)

# テキストメッセージ送信
print("テキスト送信中")
result = line.notify('照度値: {:.2f} Lux'.format(lux))
print("result:", result)

# スタンプ送信
print("スタンプ送信中")
#result2 = line.notifySticker(パッケージID, スタンプNo, 'これはスタンプです。')
result2 = line.notifySticker(6359, 11069848, 'これはスタンプです。')
print("result2:", result2)
