import network
import time
from network import WLAN

# setup as a station
wlan = network.WLAN(mode=WLAN.STA)
wlan.connect('', auth=(WLAN.WPA2, ''))
while not wlan.isconnected():
    time.sleep_ms(50)
print(wlan.ifconfig())
