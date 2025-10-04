import network
import usocket
import ssl
import json
import time
from machine import Pin, ADC

# WiFi設定
SSID = 'xxxxxxxxxxxx'
PASSWORD = 'xxxxxxxxxxx'

# Discord Webhook URL
WEBHOOK_URL = 'https://discord.com/api/webhooks/1418489982670213170/80mDu__xAyf36Z1d1ID66hhJ7aSgxUYaw6xGhv-pH9QFwBZyT_RW4YlN8JcZ40OZ3c02'  # ご自身のWebhookに置き換えてください

# WiFi接続
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    print("WiFi接続中...")
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(1)
    print("\nWiFi接続完了:", wlan.ifconfig())

# 照度センサー設定
adc = ADC(Pin(3))
adc.width(ADC.WIDTH_12BIT)
adc.atten(ADC.ATTN_11DB)
device_voltage = 3.3

# Discord送信
def send_discord_message(content, username="Hamako"):
    try:
        _, _, host, path = WEBHOOK_URL.split("/", 3)
        addr = usocket.getaddrinfo(host, 443)[0][-1]

        sock = usocket.socket()
        sock.connect(addr)
        sock = ssl.wrap_socket(sock)

        # username を指定
        data = json.dumps({
            "content": content,
            "username": username
        })
        data_bytes = data.encode("utf-8")

        request = (
            "POST /" + path + " HTTP/1.1\r\n"
            "Host: " + host + "\r\n"
            "Content-Type: application/json\r\n"
            "Content-Length: " + str(len(data_bytes)) + "\r\n"
            "Connection: close\r\n\r\n"
        ).encode("utf-8") + data_bytes

        sock.write(request)
        response = sock.read()
        sock.close()

        print("Discord応答:", response)
    except Exception as e:
        print("送信エラー:", e)

# 実行
connect_wifi(SSID, PASSWORD)

cds_ad = adc.read()
cds_v = cds_ad * device_voltage / 4096
lux = 10000 * cds_v / (device_voltage - cds_v) / 1000

send_discord_message("照度値: {:.2f} Lux".format(lux))
