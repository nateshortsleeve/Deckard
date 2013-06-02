Balabolka (Console Application), version 1.05
Copyright (c) 2013 Ilya Morozov
All Rights Reserved

WWW: http://www.cross-plus-a.com/bconsole.htm
E-mail: crossa@hotbox.ru

Licence: Freeware
Operating System: Microsoft Windows XP/Vista/7/8
Speech API: 4.0/5.0 and above
Microsoft Speech Platform



*** Usage ***

balabolka_console.exe [options ...]


*** Command Line Options ***

-l
   Prints the list of available voices.

-g
   Prints the list of available audio output devices.

-f <text_file>
   Sets the name of input text file.

-w <wave_file>
   Sets the name of output file in WAV format. If the option is specified, an audio file will be created. Otherwise, text will be read aloud.

-n <voice_name>
   Sets the voice name (the part of the name will be enough). If the option is not specified, the default voice of Windows will be used.

-m
   Prints the parameters of the voice.

-b <integer>
   Sets the audio output device by its index. The index of the default audio device is 0.

-c
   Takes the text input from clipboard.

-t <text>
   Text input can be taken from the command line.

-i
   Takes the text input from STDIN.

-o
   Writes sound data to STDOUT (for SAPI 5 and Microsoft Speech Platform). If the option is specified, the option [-w] is ignored.

-s <integer>
   SAPI 4: sets the speed in a range of 0 to 100 (no default value).
   SAPI 5 and Microsoft Speech Platform: sets the speed in a range of -10 to 10 (the default is 0).

-p <integer>
   SAPI 4: sets the pitch in a range of 0 to 100 (no default value).
   SAPI 5 and Microsoft Speech Platform: sets the pitch in a range of -10 to 10 (the default is 0).

-v <integer>
   SAPI 4: not used.
   SAPI 5 and Microsoft Speech Platform: sets the volume in a range of 0 to 100 (the default is 100).

-e <integer>
   Sets the length of pauses between sentences (in milliseconds). The default is 0.

-a <integer>
   Sets the length of pauses between paragraphs (in milliseconds). The default is 0.

-d <filename>
   Uses a dictionary for pronunciation correction (*.REX or *.DIC). The command line may contain few options [-d].

-k
   Kills other copies of the console application in the computer's memory.

-q
   Adds the application to a queue. The console application will wait until other copies of the program have finished.

-lrc
   Creates the LRC file, if the option [-w] or [-o] is specified (for SAPI 5 and Microsoft Speech Platform).

-? or -h
   Prints the list of available command line options.

--lrc-length <integer>
   Sets the maximal length of text lines for the LRC file (in characters).

--lrc-filename <filename>
   Sets the name of the LRC file. The option may be useful, when the option [-o] is specified.

--lrc-encoding <encoding>
   Sets the encoding for the LRC file ("ansi", "utf8" or "unicode"). The default is "ansi".

--lrc-offset <integer>
   Sets the time shift for the LRC file (in milliseconds).

--lrc-artist <text>
   Sets the ID tag for the LRC file: artist.

--lrc-album <text>
   Sets the ID tag for the LRC file: album.

--lrc-title <text>
   Sets the ID tag for the LRC file: title.

--lrc-author <text>
   Sets the ID tag for the LRC file: author.

--lrc-creator <text>
   Sets the ID tag for the LRC file: creator of the LRC file.

--raw
   Output is raw PCM; audio data does not contain the WAV header (for SAPI 5 and Microsoft Speech Platform). The option is used together with the option [-o].

--ignorelength
   Omits the length of data in the WAV header (for SAPI 5 and Microsoft Speech Platform). The option is used together with the option [-o].


*** Examples ***

balabolka_console.exe -l

balabolka_console.exe -n "Microsoft Anna" -m

balabolka_console.exe -f "d:\Text\book.txt" -w "d:\Sound\book.wav" -n "Emma"

balabolka_console.exe -n "Callie" -c -d "d:\rex\rules.rex" -d "d:\dic\rules.dic"

balabolka_console.exe -n "Emily" -t "The text will be read slowly." -s -5 -v 70

balabolka_console.exe -k

balabolka_console.exe -f "d:\Text\book.txt" -w "d:\Sound\book.wav" -lrc --lrc-length 80 --lrc-title "The Lord of the Rings"


The example of use together with LAME.EXE:

balabolka_console.exe -f d:\book.txt -n Heather -o --raw | lame.exe -r -s 22.05 -m m -h - d:\book.mp3


The example of use together with OGGENC2.EXE:

balabolka_console.exe -f d:\book.txt -n Heather -o --ignorelength | oggenc2.exe --ignorelength - -o d:\book.ogg


The example of use together with WMAENCODE.EXE:

balabolka_console.exe -f d:\book.txt -n Heather -o --ignorelength | wmaencode.exe - d:\book.wma --ignorelength


*** Configuration File ***

The command line options can be stored as a configuration file "balabolka_console.cfg" in the same folder as the console application.

Configuration file example:
===============
-f d:\Text\book.txt
-w d:\Sound\book.wav
-n Microsoft Anna
-s 2
-p -1
-v 95
-e 300
-d d:\rex\rules.rex
-d d:\dic\rules.dic
-lrc
--lrc-length 75
--lrc-encoding utf8
--lrc-offset 300
===============

The program may combine options from the configuration file and the command line.

###