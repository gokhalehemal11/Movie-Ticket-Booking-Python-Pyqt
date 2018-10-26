import matplotlib.pyplot as plt
import numpy as np

import MySQLdb
from MySQLdb import Error

def f():

	try:
		con = MySQLdb.connect(host="localhost",user="root",passwd="pccoe",db="mini")

		if (con.open):
		    print "connected"
		else:
	       	    print "Not connected"
	
	   
		cur1 = con.cursor()
		cur2 = con.cursor()
		cur3 = con.cursor()

	except Error as e:
	        print e


	sql1 = "select seats from J2CE_booking "
	cur1.execute(sql1)

	res1 = cur1.fetchall()
	ab1 = [i[0] for i in res1]

	sql2 = "select seats from 3idiots_booking "
	cur2.execute(sql2)

	res2 = cur2.fetchall()
	ab2 = [i[0] for i in res2]

	sql3 = "select seats from sairat_booking "
	cur3.execute(sql3)

	res3 = cur3.fetchall()
	ab3 = [i[0] for i in res3]



	objects = ('J2CE' , '3 idiots' , 'sairat')
	y_pos = np.arange(len(objects))

	performance = [len(ab1),len(ab2),len(ab3)]

	plt.bar(y_pos , performance , align = 'center' , alpha = 0.5)
	plt.xticks(y_pos , objects)
	plt.ylabel(' No. of Booked Seats ')
	plt.title(' Current Shows ')

	plt.show()

	colors = ['gold', 'yellowgreen', 'lightcoral']
	explode = (0.1, 0.1, 0.1)  
	 
	# Plot
	plt.pie(performance, explode=explode, labels=objects, colors=colors,
		autopct='%1.1f%%', shadow=True, startangle=140)
	 
	plt.axis('equal')
	plt.show()
