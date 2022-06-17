from dataclasses import dataclass
import logging
import sys
import board
import digitalio
import adafruit_character_lcd.character_lcd as character_lcd

from fastapi import FastAPI

@dataclass
class Context:
    logger: logging.Logger = None
    lcd: character_lcd.Character_LCD_Mono = None

app = FastAPI()
context = Context()

@app.on_event("startup")
async def startup_event():
    #Creating and Configuring Logger
    Log_Format = "%(levelname)s %(asctime)s - %(message)s"

    logging.basicConfig(stream = sys.stdout, 
                        format = Log_Format, 
                        level = logging.DEBUG)

    logger = logging.getLogger()

    # Setting values of the LCD
    logger.info("Setting values of the LCD")
    lcd_rs = digitalio.DigitalInOut(board.D26)
    lcd_en = digitalio.DigitalInOut(board.D19)
    lcd_d4 = digitalio.DigitalInOut(board.D13)
    lcd_d5 = digitalio.DigitalInOut(board.D6)
    lcd_d6 = digitalio.DigitalInOut(board.D5)
    lcd_d7 = digitalio.DigitalInOut(board.D11)
    lcd_columns = 16
    lcd_rows = 2

    logger.info("Configure LCD")
    lcd = character_lcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

    context.logger = logger
    context.lcd = lcd


@app.get("/lcd/")
def read_root(message: str = ""):
    logger = context.logger
    lcd = context.lcd

    # TODO validate input
    logger.info(f"message to write {message}")
    lcd.clear()
    lcd.message = message
    logger.info("Message written")

    return {"result": "ok", "msg": message}

# http://127.0.0.1:8000/lcd/?message=Hello%20World!%0AFrom%20Fast%20API