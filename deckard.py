from SimpleCV import *
from time import sleep

import serial
w = 320
h = 240
camera = Camera(0)
display = Display(resolution=(w, h))
facebox_dim = (w/3,h/2)
while not display.isDone():
        frame = camera.getImage()
        faces = frame.findHaarFeatures('face')
        if faces:
                for face in faces:
                        facelayer = DrawingLayer((frame.width, frame.height))
                        facebox = facelayer.centeredRectangle(face.coordinates(), facebox_dim)
                        frame.addDrawingLayer(facelayer)
                        frame.applyLayers()
                        break
        frame.save(display)
