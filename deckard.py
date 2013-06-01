from SimpleCV import *
from time import sleep
import serial

class Deckard:
    @staticmethod
    def returnToCenter():
        #for x in range(0, 180):
        #    arduino.write('a')
        #for x in range(0,90):
        #    arduino.write('d')
        for y in range(0, 180):
            arduino.write('w')
        #for y in range(0,90):
        #    arduino.write('s')

    

if __name__ == '__main__':
    arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    arduino.open()
    Deckard.returnToCenter()

    servo_position = (0,0)
    increment = 1
    w = 320
    h = 240
    center = (w/2, h/2)
    camera = Camera(0)
    display = Display(resolution=(w, h))
    facebox_dim = (w/3,h/2)
    focal_target = center
    while not display.isDone():
            frame = camera.getImage()
            faces = frame.findHaarFeatures('face')
            returnTuple = (-1,-1)
            if faces:
                    for face in faces:
                        print face.coordinates()
                        break
            
            frame.save(display)
    arduino.close()
    exit()
