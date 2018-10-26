# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show_status.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!


import MySQLdb
from MySQLdb import Error
import next1 as n1

from PyQt4 import QtCore, QtGui

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

class dk7:
	
	def __init__(self):
		self.used_id = ""

	def stat_id(self , myid):
		self.used_id = myid
		print "in show_status " , self.used_id

class Ui_Form(object , dk7):

    def bck(self):
	
	self.window=QtGui.QWidget()   
        self.ui=n1.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()	

    def p_t(self):
	
	if (self.rb1.isChecked() == True):

	    print stat.used_id

	    try:
	    	con = MySQLdb.connect(host="localhost",user="root",passwd="pccoe",db="mini")

	    	if (con.open):
			print "connected"
	    	else:
	       		print "Not connected"
	
	   
	    	cur = con.cursor()

	    except Error as e:
	    	print e

	    sql8 = "select seats from J2CE_booking where user_id = '%s' " % ( stat.used_id )

	    cur.execute(sql8)

	    res = cur.fetchall()

	    seats_of_user = [ i[0] for i in res]

	    print seats_of_user

	    sts = ' '.join(seats_of_user)

	    self.mylabel.setText(_translate("Form", "<html><head/><body><p>  BOOKED SEATS : " + sts +"\n\n USER - ID :"+ stat.used_id +"\n\n FILM NAME : J2CE </p></body></html>", None))
	    self.mylabel.setWordWrap(True)


	if(self.rb2.isChecked() == True ):
	    print stat.used_id

	    try:
	    	con = MySQLdb.connect(host="localhost",user="root",passwd="pccoe",db="mini")

	    	if (con.open):
			print "connected"
	    	else:
	       		print "Not connected"
	
	   
	    	cur = con.cursor()

	    except Error as e:
	    	print e

	    sql8 = "select seats from 3idiots_booking where user_id = '%s' " % ( stat.used_id )

	    cur.execute(sql8)

	    res = cur.fetchall()

	    seats_of_user = [ i[0] for i in res]

	    print seats_of_user

	    sts = ' '.join(seats_of_user)

	    self.mylabel.setText(_translate("Form", "<html><head/><body><p>  BOOKED SEATS : " + sts +"\n\n USER - ID :"+ stat.used_id +"\n\n FILM NAME : 3 IDIOTS </p></body></html>", None))
	    self.mylabel.setWordWrap(True)


	if (self.rb3.isChecked() == True):

	    print stat.used_id

	    try:
	    	con = MySQLdb.connect(host="localhost",user="root",passwd="pccoe",db="mini")

	    	if (con.open):
			print "connected"
	    	else:
	       		print "Not connected"
	
	   
	    	cur = con.cursor()

	    except Error as e:
	    	print e

	    sql8 = "select seats from sairat_booking where user_id = '%s' " % ( stat.used_id )

	    cur.execute(sql8)

	    res = cur.fetchall()

	    seats_of_user = [ i[0] for i in res]

	    print seats_of_user

	    sts = ' '.join(seats_of_user)


	    self.mylabel.setText(_translate("Form", "<html><head/><body><p>  BOOKED SEATS : " + sts +"\n\n USER - ID :"+ stat.used_id +"\n\n FILM NAME : SAIRAT </p></body></html>", None))
	    self.mylabel.setWordWrap(True)


    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(614, 518)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.print_ticket = QtGui.QPushButton(Form)
        self.print_ticket.setGeometry(QtCore.QRect(440, 360, 99, 27))
        self.print_ticket.setObjectName(_fromUtf8("print"))
        self.back = QtGui.QPushButton(Form)
        self.back.setGeometry(QtCore.QRect(80, 360, 99, 27))
        self.back.setObjectName(_fromUtf8("back"))
        self.mylabel = QtGui.QLabel(Form)
        self.mylabel.setGeometry(QtCore.QRect(130, 90, 351, 161))
        self.mylabel.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 0);"))
        self.mylabel.setObjectName(_fromUtf8("mylabel"))
        self.rb1 = QtGui.QRadioButton(Form)
        self.rb1.setGeometry(QtCore.QRect(30, 450, 117, 22))
        self.rb1.setObjectName(_fromUtf8("rb1"))
        self.rb2 = QtGui.QRadioButton(Form)
        self.rb2.setGeometry(QtCore.QRect(250, 450, 117, 22))
        self.rb2.setObjectName(_fromUtf8("rb2"))
        self.rb3 = QtGui.QRadioButton(Form)
        self.rb3.setGeometry(QtCore.QRect(440, 450, 117, 22))
        self.rb3.setObjectName(_fromUtf8("rb3"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(7, 0, 601, 511))
        self.label.setText(_fromUtf8(""))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("/home/hemal/Desktop/Newcc/mkc.png")))
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName(_fromUtf8("label"))
        self.label.raise_()
        self.print_ticket.raise_()
        self.back.raise_()
        self.mylabel.raise_()
        self.rb3.raise_()
        self.rb2.raise_()
        self.rb1.raise_()

	self.print_ticket.clicked.connect(self.p_t)
	self.back.clicked.connect(self.bck)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.print_ticket.setText(_translate("Form", "PRINT", None))
        self.back.setText(_translate("Form", "BACK", None))
        self.mylabel.setText(_translate("Form", "<html><head/><body><p>TICKET BOOKED</p></body></html>", None))
        self.rb1.setText(_translate("Form", "    J2CE", None))
        self.rb2.setText(_translate("Form", "   3 IDIOTS", None))
        self.rb3.setText(_translate("Form", "  SAIRAT", None))


stat = dk7()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

