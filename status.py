
import MySQLdb
from MySQLdb import Error

a = ""
b = ""

def log_success (id , pin ):

    	try:
    		con = MySQLdb.connect(host="localhost",user="root",passwd="pccoe",db="mini")

    		if (con.open):
        		print "connected"
    		else:
       			print "Not connected"
	
   
    		cur = con.cursor()

    	except Error as e:
    		print e	
	
	sql5 = "update logged_users set status = '%s' where user_id = '%s' and password = '%s'" % ('Y' , id , pin )

	cur.execute(sql5)
	con.commit()


def logout_success (id , pin ):

	print "logging out"
	
    	try:
    		con2 = MySQLdb.connect(host="localhost",user="root",passwd="pccoe",db="mini")

    		if (con2.open):
        		print "connected"
    		else:
       			print "Not connected"
	
   
    		cur2 = con2.cursor()

    	except Error as e:
    		print e	
	
	sql6 = "update logged_users set status = '%s' where user_id = '%s' and password = '%s'" % ('N' , id , pin )

	cur2.execute(sql6)
	con2.commit()

def variables(my_id , my_pin):
	a = my_id
	b = my_pin
	print "my_id variables id:" , a
	print "my variables pin:" , b	
