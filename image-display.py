from SimpleCV import Image, Display
from time import sleep

myDisplay = Display()
face = Image("mona.jpg")
face.save(myDisplay)
while not myDisplay.isDone():
	sleep(0.1)