import RPi.GPIO as GPIO
import time

GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)  # set up BCM GPIO numbering  
GPIO.setup(7, GPIO.OUT) # set GPIO 25 as input  

for i in range (50):
    GPIO.output(7, True)
    time.sleep(1)
    GPIO.output(7, False)
    time.sleep(1)
    
GPIO.cleanup()