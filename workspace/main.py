from dataclasses import dataclass
import logging
import sys
import board
from CircuitPython_LCD.lcd.lcd import LCD
from CircuitPython_LCD.lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import vlc
import time
from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel

@dataclass
class Context:
    logger: logging.Logger = None
    lcd: LCD = None
    vlc_instance: vlc.Instance = None
    player: Any = None

class Song(BaseModel):
    name: str
# {name : undefined}

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
    lcd = LCD(I2CPCF8574Interface(board.I2C(), 0x27), 20, 4)

    #Setup VLC
    logger.info("Setup VLC")
    vlc_instance = vlc.Instance() # creating a vlc instance
    player = vlc_instance.media_player_new()  # creating a media player
    events = player.event_manager()
    
    context.vlc_instance = vlc_instance
    context.player = player
    context.events = events
    context.logger = logger
    context.lcd = lcd

# http://127.0.0.1:8000/lcd/?message=Hello%20World!%0AFrom%20Fast%20API
@app.get("/lcd/")
def read_root(message: str = ""):
    logger = context.logger
    # lcd = context.lcd
    # TODO validate input
    msg = message.replace("\n", "\n\r")
    logger.info(f"message to write {msg}")
    logger.info("Message written")

    return {"result": "ok", "msg": message}

@app.post("/play")
def play_song(song: Song):
    source = f"/home/pi/workspace/data/{song.name}"
    lcd = context.lcd
    logger = context.logger
    # events = context.events

    media = context.vlc_instance.media_new(source) # creating a media   
    context.player.set_media(media)    # setting media to the player
    context.player.play()
    
    logger.info(f"Song name to write -> {song.name}")
    lcd.clear()
    
    lcd.set_cursor_pos(0,0)
    lcd.print(song.name) #Song name
    logger.info("Song name written in LCD ✔")

    # status = context.player.is_playing() #check if song is already playing to get length
    if context.player.is_playing() == True:
        ms = context.player.get_length()
        # ms = context.player.get_time()
        seconds=(ms/1000)%60
        minutes=(ms/(1000*60))%6
    
        logger.info(f"Song duration to write -> {ms} ms")
        lcd.set_cursor_pos(3,0)
        lcd.print("Duration " + "%0d:%02d" % (minutes, seconds))
        logger.info("Song duration written in LCD ✔")

    # while context.player.is_playing() == True:
    #     ms = context.player.get_time()
    #     seconds=(ms/1000)%60
    #     minutes=(ms/(1000*60))%6
    
    #     logger.info(f"Song duration to write -> {ms} ms")
    #     lcd.set_cursor_pos(3,0)
    #     lcd.print("Duration " + "%0d:%02d" % (minutes, seconds))
    #     logger.info("Song duration written in LCD ✔")

    #     if str(context.player.get_event_manager()) == 'MediaPlayerMediaChanged':
    #         lcd.clear()
    #         break


        # if str(events.event_attach(vlc.EventType.MediaPlayerMediaChanged,SongFinished)) == 'MediaPlayerMediaChanged':
        #     break 
        # print(context.player.get_length())


    return {"result": "OK", "msg": song.name}