import cleverbot
from time import sleep
from SimpleCV import *
import serial


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

#myCamera = Camera(prop_set={'width':w, 'height':h})
myCamera = Camera(1)
if myCamera is None:
    print "Camera not found."
    exit()
myDisplay = Display(resolution=(w,h))
facebox_dim = (w/4,h/4)
previousFrame = None
while not myDisplay.isDone():
    frame = myCamera.getImage()
##    frameCount += 1
    #if frameCount % frameSkip != 0:
    #    continue
    
    center = (frame.width/2, frame.height/2)
    
    faces = frame.findHaarFeatures('face')
    if faces:
        for face in faces:
            #print "Face at: " + str(face.coordinates())
            facelayer = DrawingLayer((frame.width, frame.height))
            facebox = facelayer.centeredRectangle(face.coordinates(), facebox_dim)
            frame.addDrawingLayer(facelayer)
            frame.applyLayers()
            

##            focal_point = faces[0].coordinates()
##            servo_delta = focal_point - center
##            print "Distance from center: ", servo_delta
##            increment = 2
##            center_buffer = 4
            
##            x = servo_delta[0]
##            if abs(x) > center_buffer:
##                if x < 0:
##                    arduino.write('a')
##                    x = x + increment
##                    #print 'a'
##                else:
##                    arduino.write('d')
##                    x = x - increment
##                    #print 'd'
##                
##            y = servo_delta[1]
##            if abs(y) > center_buffer:
##                if y < 0:
##                    arduino.write('s')
##                    y = y + increment
##                    #print 's'
##                else:
##                    arduino.write('w')
##                    y = y - increment
##                    #print 'w'
##            servo_delta = (0,0)
##            focal_point = (0,0)
##            faces = None
##            break
##    else:
##        returnToCenter()
    frame.save(myDisplay)
##    sleep(.2)
arduino.close()
#----------------------------------------------
#Cleverbot conversation loop
    #cb = cleverbot.Session()
    #print "Cleverbot Session Established \n"

    #query = ""
    #while query != "exit":
        #query = raw_input()
        #print cb.Ask(query)
