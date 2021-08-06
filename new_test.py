from RPLCD.i2c import CharLCD as LCD
import time

lcd = LCD("PCF8574", 0x27)
lcd.write_string("Testing")
time.sleep(10)
lcd.backlight_enabled = False
lcd.clear()

