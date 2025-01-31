import network
import socket
import time
import machine

SSID = 'xxxxxxxxxxxxxx'  # Wi-FiのSSID
PASSWORD = 'xxxxxxxxxxxxx'  # Wi-Fiのパスワード

# LEDピン設定
pin = machine.Pin(25, machine.Pin.OUT)

# Wi-Fi接続関数
def connect_wifi(ssid, password, timeout=10):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    print("WiFiに接続中...")
    start_time = time.time()

    while not wlan.isconnected():
        if time.time() - start_time > timeout:
            print("\nWiFi接続失敗。")
            return False
        print(".", end="")
        time.sleep(1)

    print("\nWiFi接続完了!")
    print("IPアドレス:", wlan.ifconfig())
    return True

# Webサーバー起動関数
def start_server():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print("サーバー起動:", addr)

    while True:
        cl, addr = s.accept()
        print("クライアント接続:", addr)
        request = cl.recv(1024).decode('utf-8')
        print("リクエスト:", request)

        if '/on' in request:
            pin.value(1)
            print("LED ON")
        elif '/off' in request:
            pin.value(0)
            print("LED OFF")

        response = """\
HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n
<!DOCTYPE html>
<html>
<head><title>ESP32 LED Control</title></head>
<body>
<h1>ESP32 LED Control</h1>
<button onclick="fetch('/on')">LED ON</button>
<button onclick="fetch('/off')">LED OFF</button>
</body>
</html>
"""
        cl.send(response)
        cl.close()

# メイン処理
try:
    if connect_wifi(SSID, PASSWORD):
        start_server()
except Exception as e:
    print("エラー:", str(e))
