import gpiozero as gz
from RPLCD.i2c import CharLCD as LCD
from time import sleep

button = gz.Button(26)
lcd = LCD("PCF8574", 0x27, cols=16, rows=2)

# init
button.hold_time = 6
lcd.backlight_enabled = False;

def lcd_light(on):
    lcd.backlight_enabled = on
    
# use when_help, when_pressed instead to capture buttons

def main():
    while True:
        if (button.is_pressed):
            lcd_light(True)
            lcd.write_string("Button has been pressed")
            sleep(5)
            lcd.clear()
            lcd_light(False)
        if (button.is_held):
            lcd_light(True)
            lcd.write_string("Button has been help for 5sec")
            sleep(5)
            lcd.clear()
            lcd_light(False)
        sleep(1)
    

if __name__ == "__main__":
    main()
