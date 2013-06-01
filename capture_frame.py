#from SimpleCV import Camera, Display
from SimpleCV import *
from time import sleep


#camera = Camera(prop_set={'width':160, 'height':120})
#w = 160
#h = 120
#display = Display(resolution=(w,h))
camera = Camera(1)
frame = camera.getImage()
frame.save("frame.png")
#frame.save(display)
#sleep(2)

