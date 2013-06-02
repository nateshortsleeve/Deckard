#----------------------------------------------
#Cleverbot conversation loop
import cleverbot
import sys, string, os
cb = cleverbot.Session()
print "ready"
while True:
    input = raw_input()
    input_file = open('input.txt', 'w')
    input_file.truncate()
    input_file.write(input)
    input_file.close()
    
    cb = cleverbot.Session()
    response = cb.Ask(input)
    print "Cleverbot: ", response
    output_file = open('output.txt', 'w')
    output_file.truncate()
    output_file.write(response)
    output_file.close()
    
    #send to cleverbot and output response to output.txt
    #execute balbolka for synthesis
    balbabolka_string = "balabolka_console.exe -f output.txt -n \"Microsoft Anna\" -o --ignorelength | oggenc2.exe --ignorelength - -o output.ogg"
    os.system(balbabolka_string)
    vlc_string = "play_speech.bat"
    os.system(vlc_string)

    
    
    
    
    
