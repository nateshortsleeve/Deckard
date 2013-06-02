#!/usr/bin/python

import sys		#for cmd line argv

#take command line args as the input string
input_string = sys.argv
#remove the program name from the argv list
input_string.pop(0)

#convert to google friendly url (with + replacing spaces)
tts_string = '+'.join(input_string)

print tts_string