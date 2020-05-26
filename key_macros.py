import os
import sys
import evdev
from evdev import InputDevice, categorize, ecodes

device = sys.argv[1]
dev = InputDevice('/dev/input/'+device)
dev.grab()


# cat /proc/bus/input/devices  --> view inpunt devices
# sudo chmod a+r /dev/input/event21 --> change permissions



for event in dev.read_loop():
	key = categorize(event)
	if isinstance(key,evdev.events.KeyEvent):
		if key.keystate == key.key_down:
			if key.keycode == 'KEY_C':
				os.system('amixer -q sset Master toggle')
			if key.keycode == 'KEY_X':
				os.system('amixer -q sset Master 5%+')
			if key.keycode == 'KEY_Z':
				os.system('amixer -q sset Master 5%-')
			if key.keycode == 'KEY_SPACE':
                            os.system('dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause >> /dev/null')
			if key.keycode == 'KEY_N':
	 			os.system('dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next >> /dev/null')
			if key.keycode == 'KEY_B':
				os.system('dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous >> /dev/null')
			if key.keycode == 'KEY_A':
				os.system('wmctrl -a Terminal ')
			if key.keycode == 'KEY_S':
				os.system('wmctrl -a Spotify Premium')


	 				

