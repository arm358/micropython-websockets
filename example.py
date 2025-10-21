import network
import uwebsockets.client
import ujson
import time

#WIFI
SSID = "YOUR_WIFI_SSID"
PASSWORD = "YOUR_WIFI_PASSWORD"


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

print("Connecting to Wi-Fi...")
while not wlan.isconnected():
    time.sleep(0.5)
print("Connected to Wi-Fi:", wlan.ifconfig())



#WEBSOCKET
url = f"ws://YOUR_SERVER:YOUR_PORT/..."
print("Connecting to ws url: ", url)
ws = uwebsockets.client.connect(url)


#EXAMPLE PAYLOAD
try:
    while True:
        payload = {   #or whatever json you want
            "updates": [
                {
                    "source": {"label": "my-sensor"},
                    "values": [
                        {"path": "environment.inside.temperature", "value": 15},
                        {"path": "environment.inside.humidity", "value": 40}
                    ]
                }
            ]
        }
        ws.send(ujson.dumps(payload))
        print("Sent:", payload)
        time.sleep(5)

except KeyboardInterrupt:
    print("Closing WebSocket...")
    ws.close()

