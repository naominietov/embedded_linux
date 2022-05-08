""" 
* ID: A01706095
* Author: Naomi Estefanía Nieto Vega 
* File: main.py
* Assignment: Mostrar mensajes en el LCD a través de I2C de forma remota
* Date and time: 2022-05-05 12:34:45
"""
from dataclasses import dataclass
import logging
import sys
import board
from CircuitPython_LCD.lcd.lcd import LCD
from CircuitPython_LCD.lcd.i2c_pcf8574_interface import I2CPCF8574Interface

from fastapi import FastAPI

@dataclass
class Context:
    logger: logging.Logger = None
    lcd: LCD = None

app = FastAPI()
context = Context()

@app.on_event("startup")
async def startup_event():
    # Creating and Configuring Logger
    Log_Format = "%(levelname)s %(asctime)s - %(message)s"

    logging.basicConfig(stream = sys.stdout, 
                        format = Log_Format, 
                        level = logging.DEBUG)

    logger = logging.getLogger()

    logger.info("Setting LCD size values")
    # Setting size values LCD
    lcd_rows = 2
    lcd_columns = 16

    logger.info("Initializing I2C bus and configuring LCD")
    # Talk to the LCD at I2C address 0x27.
    lcd = LCD(I2CPCF8574Interface(board.I2C(), 0x27), lcd_columns, lcd_rows)

    # Uploading data
    context.logger = logger
    context.lcd = lcd


@app.get("/lcd")
def read_root(message: str = ""):
    logger = context.logger
    lcd = context.lcd

    # TO-DO validate input
    logger.info(f"Message to write: {message}")
    lcd.clear()
    lcd.print(message)
    
    # lcd.blink = True
    logger.info("Message written")

    return {"result": "OK", "msg": message}

# http://127.0.0.1:8000/lcd/?message=Hello%20World!%0AFrom%20Fast%20API