import gpiozero as gz
import time

sensor = gz.SmoothedInputDevice(17)

print(sensor.value)