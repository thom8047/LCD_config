import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)  # set up BCM GPIO numbering  
GPIO.setup(25, GPIO.IN) # set GPIO 25 as input  

if GPIO.input(25): # if port 25 == 1  
    print("Port 25 is 1/GPIO.HIGH/True")

GPIO.cleanup()