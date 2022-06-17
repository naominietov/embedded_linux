# import vlc
# import time
# import sys

# finish = 0

# def SongFinished(event):
#     global finish
#     print("\nEvent reports - finished")
#     finish = 1

# def pos_callback(event, player):
#     sec = player.get_time() / 1000
#     m, s = divmod(sec, 60)
#     npos = event.u.new_position * 100
#     sys.stdout.write('\r%s %02d:%02d (%.2f%%)' % ('Position', m, s, npos))
#     sys.stdout.flush()

# instance = vlc.Instance()
# player = instance.media_player_new()
# media = instance.media_new_path('/home/pi/workspace/data/Eddie Benjamin - Weatherman.wav') #Your audio file here
# player.set_media(media)
# events = player.event_manager()
# events.event_attach(vlc.EventType.MediaPlayerEndReached, SongFinished)
# events.event_attach(vlc.EventType.MediaPlayerPositionChanged, pos_callback, player)

# player.play()
# while finish == 0:
#     time.sleep(0.5)

# importing time module
import vlc
import time


# creating vlc media player object
media_player = vlc.MediaPlayer("/home/pi/workspace/data/Eddie Benjamin - Weatherman.wav")

# start playing video
media_player.play()

# wait so the video can be played for 5 seconds
# irrespective for length of video
time.sleep(5)

# getting instance of the media player
inst = media_player.get_instance(vlc.EventType.MediaPlayerMediaChanged())
print("Media player Instance : " + str(inst))
