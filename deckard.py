from SimpleCV import *
from time import sleep

import serial
                
def SearchForFace(frame):
        #returns coordinates of face found as a tuple
        #returns None if no face found
        faces = frame.findHaarFeatures('face')
        if faces:
                for face in faces:
                        #print "found face"
                        print face.coordinates()
                        return face.coordinates()
        else:
                #print "no faces found"
                return None


w = 320
h = 240
camera = Camera(0)
display = Display(resolution=(w, h))
facebox_dim = (w/3,h/2)
coordinates = None
while not display.isDone():
        frame = camera.getImage()
        coodinates = SearchForFace(frame)
        if coordinates != None:
                print coodinates[0], ' ', coordinates[1]
        frame.save(display)
exit()
