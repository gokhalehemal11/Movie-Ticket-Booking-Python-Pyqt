# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pay.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import MySQLdb
from MySQLdb import Error
from seat1 import *
from seat2 import *
from seat3 import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class gt():
	def __init__(self):
		self.bkd = []
		self.used_id = ""
		self.used_time = ""
		self.used_film = ""
		self.al_buk = []

	
	def g(self,myid,bukd,tym,film,ab):
		self.bkd = bukd
		self.used_id = myid
		self.used_time = tym 
		self.used_film = film
		self.al_buk = ab		
	
class Ui_Form(object ,gt):

    def __init__(self):


	self.booked_string = ""

    def confirm(self):

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


	if (g1.used_film is 'J2CE'):
	
		for i in g1.bkd:
			cur1.execute('insert into J2CE_booking values ("%s" , "%s" , "%s")' % ( g1.used_id , i , g1.used_time))
			con.commit()

		self.booked_string = ' '.join(g1.bkd + g1.al_buk)
		print self.booked_string

	if(g1.used_film is '3_idiots'):

		for i in g1.bkd:
			cur2.execute('insert into 3idiots_booking values ("%s" , "%s" , "%s")' % ( g1.used_id , i , g1.used_time))
			con.commit()

		self.booked_string = ' '.join(g1.bkd + g1.al_buk)
		print self.booked_string

	if (g1.used_film is 'sairat'):

		for i in g1.bkd:
			cur3.execute('insert into sairat_booking values ("%s" , "%s" , "%s")' % ( g1.used_id , i , g1.used_time))
			con.commit()

		self.booked_string = ' '.join(g1.bkd + g1.al_buk)
		print self.booked_string
	

	if ( len(g1.bkd) < 5):
		self.msgbox_pay.setText(" Congrats PayMent Successfulll ! You Have Booked Seats : " + ' '.join(g1.bkd) )
		self.msgbox_pay.exec_()
	elif (len(g1.bkd) >= 5):
		self.msgbox_pay.setText(" Congrats PayMent Successfulll ! You Have Booked Seats : " + ' '.join(g1.bkd) + " And Discounted For One Ticket ! " )
		self.msgbox_pay.exec_()


    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(764, 551)
        Form.setStyleSheet(_fromUtf8(""))
	self.msgbox_pay = QtGui.QMessageBox(Form)
        self.pay = QtGui.QPushButton(Form)
        self.pay.setGeometry(QtCore.QRect(280, 360, 181, 27))
        self.pay.setStyleSheet(_fromUtf8("\n"
"font: 75 italic 11pt \"URW Palladio L\";"))
        self.pay.setObjectName(_fromUtf8("pay"))
        self.radioButton = QtGui.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(290, 120, 181, 22))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(290, 160, 151, 22))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_3 = QtGui.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(290, 210, 131, 22))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.radioButton_4 = QtGui.QRadioButton(Form)
        self.radioButton_4.setGeometry(QtCore.QRect(290, 260, 117, 22))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(117, 40, 581, 41))
        self.label.setObjectName(_fromUtf8("label"))

	self.pay.clicked.connect(self.confirm)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pay.setText(_translate("Form", "Confirm Payment", None))
        self.radioButton.setText(_translate("Form", "      NetBanking", None))
        self.radioButton_2.setText(_translate("Form", "      Debit Card", None))
        self.radioButton_3.setText(_translate("Form", "    Credit Card", None))
        self.radioButton_4.setText(_translate("Form", "      Other", None))
        self.label.setText(_translate("Form", "                                           Choose   Your   Payment   Method", None))


g1 = gt()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

