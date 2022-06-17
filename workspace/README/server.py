import board
import digitalio
import adafruit_character_lcd.character_lcd as character_lcd

from typing import Optional

from fastapi import FastAPI

app = FastAPI()

# Pins configuration
lcd_rs = digitalio.DigitalInOut(board.D26)
lcd_en = digitalio.DigitalInOut(board.D19)
lcd_d4 = digitalio.DigitalInOut(board.D13)
lcd_d5 = digitalio.DigitalInOut(board.D6)
lcd_d6 = digitalio.DigitalInOut(board.D5)
lcd_d7 = digitalio.DigitalInOut(board.D11)

lcd_columns = 16
lcd_rows = 2
# Provide to the library where are located the rs, en, and data pins
lcd = character_lcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)


# example?msg=aqui valor

@app.get("/lcd/")
def read_root(msg: str = ""):
    lcd.clear()
    lcd.message = msg
    return {"response": msg}