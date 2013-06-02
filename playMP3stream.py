#!/usr/bin/python

import time		#for delay
import pygst		#for playing mp3 stream
import gst		# " "

#Play an .mp3 file from the internet
music_stream_uri = 'http://www.sample-url.com/file.mp3'
player = gst.element_factory_make("playbin", "player")
player.set_property('uri', music_stream_uri)
player.set_state(gst.STATE_PLAYING)

#requires a delay, if the py process closes before the mp3 has finished it will be cut off.
time.sleep(12)