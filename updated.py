import gpiozero as gz
from rpi_lcd import LCD
import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

lcd=LCD()
led=gz.LED(21)
i=gpio.setup(20, gpio.IN, pull_up_down=gpio.PUD_DOWN)
# turn on the gpio 21
led.on()

lcd.text("LCD Door Test", 2)

try:
	while True:
		if (gpio.input(20)):
			lcd.text("Door closed", 1)
		else:
			lcd.text("Door opened", 1)
		time.sleep(0.1)
except Exception as err:
	print("Exit: ", err)

lcd.clear()
gpio.cleanup()
