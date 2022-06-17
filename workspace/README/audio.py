from dataclasses import dataclass
import logging
import sys
from RPLCD.i2c import CharLCD

from fastapi import FastAPI
from pydantic import BaseModel

@dataclass
class Context:
    logger: logging.Logger = None
    lcd: CharLCD = None



class Song(BaseModel):
    name: str

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
    logger.info("Configure LCD")
    lcd = CharLCD('PCF8574', 0x27, cols=16, rows=2)
    

    context.logger = logger
    context.lcd = lcd


# http://127.0.0.1:8000/lcd/?message=Hello%20World!%0AFrom%20Fast%20API
@app.get("/lcd/")
def read_root(message: str = ""):
    logger = context.logger
    lcd = context.lcd

    # TO-DO validate input
    msg = message.replace("\n", "\n\r")
    logger.info(f"message to write {message}")
    lcd.clear()
    lcd.write_string(message)
    
    logger.info("Message written")

    return {"result": "ok", "msg": message}

@app.post("/play")
def play_song(song: Song):
    # if not song_name:
    #     return { "result": "error", "msg": f"Not valid song {song_name}" }
    
    return {"result": "ok", "msg": song.name}