import MySQLdb
import sys
from ConfigFileManager import ConfigFileManager
try:
	db = MySQLdb.connect(
		host = ConfigFileManager.GetConfigValue('host'),
		user = ConfigFileManager.GetConfigValue('user'),
		passwd = ConfigFileManager.GetConfigValue('passwd'),
		db = ConfigFileManager.GetConfigValue('db')
		)
except Exception as e:
	sys.exit('Database connection failed.')

cursor = db.cursor()

cursor.execute('SELECT * FROM vocabulary')
result = cursor.fetchall()
print 'Table_________'
for row in result:
	print row
print '______________'
user_input = raw_input("input_phrase: ")
query = "SELECT phrase,inclination,responseid FROM vocabulary WHERE phrase = '%s' ORDER BY inclination DESC" %user_input
print query
cursor.execute(query)
result = cursor.fetchall()
print ''
for response in result:
	print 'phrase = ', response[0]
	print 'inclination = ', response[1]
	print 'responseid = ', response[2]
	print ''
	break
print result[0][2]
query_response_id = result[0][2]


query = "SELECT phrase FROM vocabulary WHERE phraseid = '%d'" %query_response_id
cursor.execute(query)
result = cursor.fetchone()
print result[0]

