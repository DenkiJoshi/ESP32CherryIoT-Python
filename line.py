# https://zenn.dev/iot101/articles/d8e26ac7be133b
# https://github.com/PerfecXX/micropython-linenotify

import network
import time
from linenotify import LineNotify

# WiFi接続設定
SSID = 'xxxxxxxxx'
PASSWORD = 'xxxxxxxxx'

# Line token
TOKEN = 'xxxxxxxxxxxxxxxx

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
result = line.notify('こんにちは。Line Botです。')
print("result:", result)

# スタンプ送信
print("スタンプ送信中")
result2 = line.notifySticker(3, 230, 'これはスタンプです。')
print("result2:", result2)