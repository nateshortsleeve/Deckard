
import xml.etree.ElementTree as ET

class ConfigFileManager(object):
    """
    This simple parser retrieves values from keys,
    within the config.xml file
    """
    try:
        configFileName = 'config.xml'
        configFile = ET.parse(configFileName)
        configFileRootElement = configFile.getroot()
    except IOError:
        print configFileName, ' file not found.'
        
    @staticmethod
    def GetConfigValue(key):
        try:
            e = ConfigFileManager.configFileRootElement.find(key)
            if e != None:
                return e.text
        except AttributeError:
            print "Error: Attribute '", key, "' or file not found."
            return ''
        
# Demo
if __name__ == "__main__":
     print 'user == ' , ConfigFileManager.GetConfigValue('mailusername')
     print 'password == ' , ConfigFileManager.GetConfigValue('mailpassword')
     print 'answer == ' , ConfigFileManager.GetConfigValue('toLifeUniverseAndEverything')

