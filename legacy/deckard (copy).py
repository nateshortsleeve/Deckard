import cleverbot
from time import sleep
from SimpleCV import *
import serial

import os
import sys

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
arduino.open()
def returnToCenter():
    for x in range(0, 180):
        arduino.write('a')
    for x in range(0,90):
        arduino.write('d')
    for y in range(0, 180):
        arduino.write('w')
    for y in range(0,90):
        arduino.write('s')

w = 320
h = 240
frameSkip = 3
frameCount = 0

returnToCenter()

servo_position = (0,0)
increment = 1

#myDisplay = Display()
#face = Image("mona.jpg")
#face.save(myDisplay)
while not myDisplay.isDone():
    key = sys.stdin.read(1)
    if key == 'w':
        servo_position[1] += increment
        print 'w'
    sleep(.1)
        
arduino.close()     
	

######This is the face tracking script. I will need to be debugged once a compatible camera can be purchased
######(need a job)
######
######myCamera = Camera(prop_set={'width':w, 'height':h})
######myDisplay = Display(resolution=(w,h))
######facebox_dim = (w/4,h/4)
######previousFrame = None
######while not myDisplay.isDone():
######    frame = myCamera.getImage()
######    frameCount += 1
######    #if frameCount % frameSkip != 0:
######    #    continue
######    
######    center = (frame.width/2, frame.height/2)
######    
######    faces = frame.findHaarFeatures('face')
######    if faces:
######        for face in faces:
######            #print "Face at: " + str(face.coordinates())
######            facelayer = DrawingLayer((frame.width, frame.height))
######            facebox = facelayer.centeredRectangle(face.coordinates(), facebox_dim)
######            frame.addDrawingLayer(facelayer)
######            frame.applyLayers()
######
######            focal_point = faces[0].coordinates()
######            servo_delta = focal_point - center
######            print "Distance from center: ", servo_delta
######            increment = 2
######            center_buffer = 4
######            
######            x = servo_delta[0]
######            while abs(x) > center_buffer:
######                if x < 0:
######                    arduino.write('a')
######                    x = x + increment
######                    #print 'a'
######                else:
######                    arduino.write('d')
######                    x = x - increment
######                    #print 'd'
######                
######            y = servo_delta[1]
######            while abs(y) > center_buffer:
######                if y < 0:
######                    arduino.write('s')
######                    y = y + increment
######                    #print 's'
######                else:
######                    arduino.write('w')
######                    y = y - increment
######                    #print 'w'
######            servo_delta = (0,0)
######            focal_point = (0,0)
######            faces = None
######            break
######    else:
######        returnToCenter()
######    frame.save(myDisplay)
######    sleep(.1)
######arduino.close()
#----------------------------------------------
#Cleverbot conversation loop
    #cb = cleverbot.Session()
    #print "Cleverbot Session Established \n"

    #query = ""
    #while query != "exit":
        #query = raw_input()
        #print cb.Ask(query)
