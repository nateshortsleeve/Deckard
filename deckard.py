#----------------------------------------------
#Cleverbot conversation loop
import cleverbot
cb = cleverbot.Session()
print "Cleverbot Session Established \n"

query = ""
while query != "exit":
    query = raw_input()
    print cb.Ask(query)


