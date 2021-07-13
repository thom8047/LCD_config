import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)  # set up BCM GPIO numbering  
GPIO.setup(9, GPIO.IN) # set GPIO 25 as input  

if GPIO.input(9): # if port 25 == 1  
    print(GPIO.input(9))

GPIO.cleanup()