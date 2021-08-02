import gpiozero as gz
import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

led=gz.LED(21)
i=gpio.setup(20, gpio.IN, pull_up_down=gpio.PUD_UP)
print(gpio.input(20))
led.on()

x = input("how long: ")
y=0

while gpio.input(20):
	print(gpio.input(20))
	time.sleep(1)
	y +=1
	if (y == int(x)):
		led.off()
		print("off")

