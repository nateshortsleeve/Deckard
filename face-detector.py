#from SimpleCV import Camera, Display
from time import sleep
from SimpleCV import *

myCamera = Camera(prop_set={'width':320, 'height':240})
myDisplay = Display(resolution=(320,240))
facebox_dim = (100,100)

while not myDisplay.isDone():
    frame = myCamera.getImage()
    center = (frame.width/2, frame.height/2)
    
    #frame = Image("mona.jpg")
    faces = frame.findHaarFeatures('face')
    if faces:
        for face in faces:
            #print "Face at: " + str(face.coordinates())
            facelayer = DrawingLayer((frame.width, frame.height))
            facebox = facelayer.centeredRectangle(face.coordinates(), facebox_dim)
            frame.addDrawingLayer(facelayer)
            frame.applyLayers()

	focal_point = faces[0].coordinates()
	servo_delta = focal_point - center
	print "Distance from center: ", servo_delta
    #else:
        #print "No faces detected."
    frame.save(myDisplay)
    #sleep(1)
