#from SimpleCV import Camera, Display
from time import sleep
from SimpleCV import *
from capture_frame import outputFrame

capture_frame.outputFrame()

frame = Image("frame.png")
facebox_dim = (100,100)
center = (frame.width/2, frame.height/2)
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
        break
    else:
        print "No faces detected."

print "done"
