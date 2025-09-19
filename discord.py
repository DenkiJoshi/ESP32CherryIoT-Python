import network, time, ujson
import urequests as requests
from machine import Pin, ADC

# ====== 設定 ======
INPUT_PIN = 3                # 光センサー接続ピン（ESP32のADCピン）
DEVICE_VOLTAGE = 3.3         # 参照電圧
WIFI_SSID = 'YOUR_SSID'
WIFI_PASSWORD = 'YOUR_PASSWORD'
DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1418489982670213170/80mDu__xAyf36Z1d1ID66hhJ7aSgxUYaw6xGhv-pH9QFwBZyT_RW4YlN8JcZ40OZ3c02'  # ←Webhook URL

# ====== Wi-Fi接続 ======
def connect_wifi(ssid, password, timeout=30):
    wlan = network.WLAN(network.STA_IF)
    if not wlan.active():
        wlan.active(True)
    if not wlan.isconnected():
        print("WiFiに接続中...")
        wlan.connect(ssid, password)
        t0 = time.time()
        while not wlan.isconnected():
            if time.time() - t0 > timeout:
                raise RuntimeError("WiFi接続タイムアウト")
            print(".", end="")
            time.sleep(1)
    print("\nWiFi接続完了:", wlan.ifconfig())
    return wlan

# ====== 照度（概算）読み取り ======
adc = ADC(Pin(INPUT_PIN))
try:
    adc.width(ADC.WIDTH_12BIT)      # ESP32系: 0〜4095
except:
    pass
try:
    adc.atten(ADC.ATTN_11DB)        # 0〜約3.3V測定
except:
    pass

def read_lux():
    raw = adc.read()  # 0..4095
    v = raw * DEVICE_VOLTAGE / 4096.0
    # LDR分圧の簡易換算（例）：lux ≒ 10k * V / (Vref - V) / 1000
    # VがVrefに近いとゼロ割になるのでクリップ
    if v > DEVICE_VOLTAGE - 1e-3:
        v = DEVICE_VOLTAGE - 1e-3
    lux = 10000.0 * v / (DEVICE_VOLTAGE - v) / 1000.0
    return raw, v, lux

# ====== Discord送信(Webhook) ======
def send_discord_webhook(content, username=None, avatar_url=None):
    payload = {"content": content}
    if username:
        payload["username"] = username           # 表示名を上書き可能
    if avatar_url:
        payload["avatar_url"] = avatar_url       # アイコンURLを上書き可能
    headers = {"Content-Type": "application/json"}
    r = requests.post(DISCORD_WEBHOOK_URL, headers=headers, data=ujson.dumps(payload))
    try:
        print("Discord status:", r.status_code)
        # 429等レート制限に注意（X-RateLimit-* ヘッダが返る）
        if r.status_code >= 400:
            print("resp:", r.text)
    finally:
        r.close()

def main():
    connect_wifi(WIFI_SSID, WIFI_PASSWORD)
    raw, v, lux = read_lux()
    msg = "照度値: {:.2f} Lux (ADC:{}, {:.3f}V)".format(lux, raw, v)
    print("送信:", msg)
    send_discord_webhook(msg, username="CherryIoT Light Sensor")
    print("完了")

if __name__ == "__main__":
    main()
