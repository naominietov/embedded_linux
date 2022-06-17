# importing vlc module
import vlc
from time import sleep
# importing time module
import time
  
# creating vlc media player object
media_player = vlc.MediaPlayer()
  
# media object
# solo reproduce si esta correidno porque el kernel lo mata
media = vlc.MediaPlayer("/home/pi/workspace/data/Sia-Unstoppable.webm")

# setting media to the media player
media_player.set_media(media)

# start playing video
media_player.play()
  
# getting length of the current media
value = media_player.get_length()
  
# printing value
print("Length of the media : ")
print(value)

# getting current media time
value = media_player.get_time()
  
# printing value
print("Current Media time : ")
print(value)

#------------------------------------------------------------------
# importing time and vlc
import time, vlc

# method to play video
def video(source):
	
	# creating a vlc instance
	vlc_instance = vlc.Instance()
	
	# creating a media player
	player = vlc_instance.media_player_new()
	
	# creating a media
	media = vlc_instance.media_new(source)
	
	# setting media to the player
	player.set_media(media)
	
	# play the video
	player.play()
	
	# wait time
	time.sleep(0.5)
	
	# getting the duration of the video
	duration = player.get_length()
	
	# printing the duration of the video
	print("Duration : " + str(duration))
	
# call the video method
video("/home/pi/workspace/data/Sia-Unstoppable.webm")
