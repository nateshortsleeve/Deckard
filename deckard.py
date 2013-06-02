#----------------------------------------------
#Cleverbot conversation loop
import cleverbot
import speech

# Your program can do whatever it wants now, and when a spoken phrase is heard,
# response() will be called on a separate thread.
from time import *
##print "loading..."
####while listener.islistening():
####    time.sleep(1)
##    #print "Still waiting..."
##cb = cleverbot.Session()
##
##print "Say something, user!"
##phrase = speech.input()
##print "Me: ", phrase
##respond = cb.Ask(phrase)
##sleep(1)
##print "Cleverbot: ", respond
#speech.say(respond)
input = None
while input != "off"
    print "_"
    input = speech.input()
    speech.say(input)