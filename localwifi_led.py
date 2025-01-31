import network
import socket
import time
import machine

# アクセスポイント設定
AP_SSID = 'ESP32-WiFi-yourname'  # 作成するWiFiのSSID
AP_PASSWORD = 'esp32wifi'  # 作成するWiFiのパスワード
AP_IP = '192.168.0.1'

# LEDピン設定
pin = machine.Pin(25, machine.Pin.OUT)

# アクセスポイント作成関数
def create_ap(ssid, password):
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=ssid, password=password)
    ap.config(max_clients=10)
    
    # IPアドレス設定
    ap.ifconfig((AP_IP, '255.255.255.0', AP_IP, '8.8.8.8'))
    
    while not ap.active():
        print(".", end="")
        time.sleep(1)
    
    print("\nアクセスポイント作成完了!")
    print("SSID:", ssid)
    print("IPアドレス:", ap.ifconfig())
    return ap

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
<head>
    <title>ESP32 LED Control</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { text-align: center; font-family: Arial; }
        button {
            padding: 10px 20px;
            margin: 10px;
            font-size: 16px;
        }
    </style>
</head>
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
    ap = create_ap(AP_SSID, AP_PASSWORD)
    start_server()
except Exception as e:
    print("エラー:", str(e))