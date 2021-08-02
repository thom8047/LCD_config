from RPLCD.i2c import CharLCD
import time

#setup for charld
lcd = CharLCD("PCF8574", 0x27)

lcd.write_string("test...")

sensor = gz.LED(17)
sensor.on()

