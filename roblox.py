import machine
import network
import urequests
import time

# ==== WiFi設定 ====
WIFI_SSID = "xxxxxx"
WIFI_PASSWORD = "xxxxxxx"

# ==== Firebase設定 ====
FIREBASE_URL = "https://xxxxxxxxxxxxxxxx.firebaseio.com"

# ==== ピン設定 ====
pin = machine.Pin(3, machine.Pin.OUT)
touch_pin = machine.Pin(4, machine.Pin.IN)

# ==== WiFi接続 ====
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(WIFI_SSID, WIFI_PASSWORD)

print("WiFi connecting", end="")
while not wlan.isconnected():
    time.sleep(0.5)
    print(".", end="")
print("")
print("WiFi connected!")
print("IP:", wlan.ifconfig()[0])

# ==== メインループ ====
while True:
    # --- Firebaseからoutputを読んでOUTPUTに反映 ---
    try:
        response = urequests.get(FIREBASE_URL + "/toDevice/output.json")
        value = int(response.text)
        response.close()
        if value == 1:
            pin.on()
            print("OUTPUT ON")
        else:
            pin.off()
            print("OUTPUT OFF")
    except Exception as e:
        print("GET failed:", e)

    # --- センサーの値をFirebaseへ送信 ---
    try:
        sensor_value = touch_pin.value()
        response = urequests.put(
            FIREBASE_URL + "/toRoblox/sensor.json",
            data=str(sensor_value),
            headers={"Content-Type": "application/json"}
        )
        response.close()
        if sensor_value == 1:
            print("Touch!")
        else:
            print("...")
    except Exception as e:
        print("PUT failed:", e)

    time.sleep(0.5)
