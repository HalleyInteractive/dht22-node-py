from dht import DHT22
from request import request
from machine import Pin
from machine import Timer
from machine import RTC
import machine

URL = 'http://192.168.1.200:3000/nodes/wipy/reading'
PIN = Pin('GP22', mode=Pin.OPEN_DRAIN)
FREQUENCY = 1000 * 60 * 10

temperature, humidity = DHT22(PIN)

def getReading():
    temperature, humidity = DHT22(PIN)
    temperature_string = '{}.{}'.format(temperature//10,temperature%10)
    humidity_string = '{}.{}'.format(humidity//10,humidity%10)
    reading = {'temperature': temperature_string, 'humidity': humidity_string}
    putReading(reading)

def putReading(reading):
    request('PUT', URL, reading)

rtc = machine.RTC()

def alarm_handler (rtc_o):
    global rtc_wake
    rtc_wake = True

rtc.alarm(time=FREQUENCY, repeat=True)
rtc_i = rtc.irq(trigger=RTC.ALARM0, handler=alarm_handler, wake=machine.SLEEP | machine.IDLE)

while True:
    machine.sleep()
    if rtc_wake:
        rtc_wake = False
        getReading()
