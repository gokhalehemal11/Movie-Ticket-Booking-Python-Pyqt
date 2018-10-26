# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seat.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import book as b
import next1 as n1
import MySQLdb
from MySQLdb import Error
import pay as p1
from pay import *
from cancel import *

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QStrinself.g.fromUtf8
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

class dont_know4:
	def __init__(self):
		self.used_id = ""

	def nn_id( self , my_id , time):
		print "in seat3 id :" , my_id
		print "in seat3 time:" , time
		self.used_id = my_id
		self.used_time = time

class Ui_Form(object , dont_know4):

    def __init__(self):
	    try:
		con = MySQLdb.connect(host="localhost",user="root",passwd="pccoe",db="mini")

		if (con.open):
		    print "connected"
		else:
	       	    print "Not connected"
	
	   
		cur = con.cursor()

	    except Error as e:
		print e

	    sql3 = " select seats from sairat_booking "
	    cur.execute(sql3)

	    res = cur.fetchall()

	    self.already_booked_sairat = [ i[0] for i in res]

	    self.booked = []


    def book_seats(self):

	#booked = []

    	try:
    		con = MySQLdb.connect(host="localhost",user="root",passwd="pccoe",db="mini")

    		if (con.open):
        		print "connected"
    		else:
       			print "Not connected"
	
   
    		cur = con.cursor()

    	except Error as e:
    		print e

	if ( self.A1.isChecked() == True ):
		self.booked.append('A1')
		#self.p.remove('A1')
		self.A1.setVisible(False)

	if ( self.A2.isChecked() == True ):
		self.booked.append('A2')
		#self.p.remove('A2')
		self.A2.setVisible(False)

	if ( self.A3.isChecked() == True ):
		self.booked.append('A3')
		#self.p.remove('A3')
		self.A3.setVisible(False)

	if ( self.A4.isChecked() == True ):
		self.booked.append('A4')
		#self.p.remove('A4')
		self.A4.setVisible(False)

	if ( self.A5.isChecked() == True ):
		self.booked.append('A5')
		#self.p.remove('A5')
		self.A5.setVisible(False)

	if ( self.A6.isChecked() == True ):
		self.booked.append('A6')
		#self.p.remove('A6')
		self.A6.setVisible(False)

	if ( self.A7.isChecked() == True ):
		self.booked.append('A7')
		#self.p.remove('A7')
		self.A7.setVisible(False)

	if ( self.A8.isChecked() == True ):
		self.booked.append('A8')
		#self.p.remove('A8')
		self.A8.setVisible(False)

	if ( self.B1.isChecked() == True ):
		self.booked.append('B1')
		#self.p.remove('B1')
		self.B1.setVisible(False)

	if ( self.B2.isChecked() == True ):
		self.booked.append('B2')
		#self.p.remove('B2')
		self.B2.setVisible(False)

	if ( self.B3.isChecked() == True ):
		self.booked.append('B3')
		#self.p.remove('B3')
		self.B3.setVisible(False)

	if ( self.B4.isChecked() == True ):
		self.booked.append('B4')
		#self.p.remove('B4')
		self.B4.setVisible(False)

	if ( self.B5.isChecked() == True ):
		self.booked.append('B5')
		#self.p.remove('B5')
		self.B5.setVisible(False)

	if ( self.B6.isChecked() == True ):
		self.booked.append('B6')
		#self.p.remove('B6')
		self.B6.setVisible(False)

	if ( self.B7.isChecked() == True ):
		self.booked.append('B7')
		#self.p.remove('B7')
		self.B7.setVisible(False)

	if ( self.B8.isChecked() == True ):
		self.booked.append('B8')
		#self.p.remove('B8')
		self.B8.setVisible(False)

	if ( self.C1.isChecked() == True ):
		self.booked.append('C1')
		#self.p.remove('C1')
		self.C1.setVisible(False)


	if ( self.C2.isChecked() == True ):
		self.booked.append('C2')
		#self.p.remove('C2')
		self.C2.setVisible(False)

	if ( self.C3.isChecked() == True ):
		self.booked.append('C3')
		#self.p.remove('C3')
		self.C3.setVisible(False)

	if ( self.C4.isChecked() == True ):
		self.booked.append('C4')
		#self.p.remove('C4')
		self.C4.setVisible(False)

	if ( self.C5.isChecked() == True ):
		self.booked.append('C5')
		#self.p.remove('C5')
		self.C5.setVisible(False)

	if ( self.C6.isChecked() == True ):
		self.booked.append('C6')
		#self.p.remove('C6')
		self.C6.setVisible(False)

	if ( self.C7.isChecked() == True ):
		self.booked.append('C7')
		#self.p.remove('C7')
		self.C7.setVisible(False)

	if ( self.C8.isChecked() == True ):
		self.booked.append('C8')
		#self.p.remove('C8')
		self.C8.setVisible(False)
# ========================================================================================

	if ( self.D1.isChecked() == True ):
		self.booked.append('D1')
		#self.g.remove('D1')
		self.D1.setVisible(False)


	if ( self.D2.isChecked() == True ):
		self.booked.append('D2')
		#self.g.remove('D2')
		self.D2.setVisible(False)

	if ( self.D3.isChecked() == True ):
		self.booked.append('D3')
		#self.g.remove('D3')
		self.D3.setVisible(False)

	if ( self.D4.isChecked() == True ):
		self.booked.append('D4')
		#self.g.remove('D4')
		self.D4.setVisible(False)

	if ( self.D5.isChecked() == True ):
		self.booked.append('D5')
		#self.g.remove('D5')
		self.D5.setVisible(False)

	if ( self.D6.isChecked() == True ):
		self.booked.append('D6')
		#self.g.remove('D6')
		self.D6.setVisible(False)

	if ( self.D7.isChecked() == True ):
		self.booked.append('D7')
		#self.g.remove('D7')
		self.D7.setVisible(False)

	if ( self.E1.isChecked() == True ):
		self.booked.append('E1')
		#self.g.remove('E1')
		self.E1.setVisible(False)


	if ( self.E2.isChecked() == True ):
		self.booked.append('E2')
		#self.g.remove('E2')
		self.E2.setVisible(False)

	if ( self.E3.isChecked() == True ):
		self.booked.append('E3')
		#self.g.remove('E3')
		self.E3.setVisible(False)

	if ( self.E4.isChecked() == True ):
		self.booked.append('E4')
		#self.g.remove('E4')
		self.E4.setVisible(False)

	if ( self.E5.isChecked() == True ):
		self.booked.append('E5')
		#self.g.remove('E5')
		self.E5.setVisible(False)

	if ( self.E6.isChecked() == True ):
		self.booked.append('E6')
		#self.g.remove('E6')
		self.E6.setVisible(False)

	if ( self.E7.isChecked() == True ):
		self.booked.append('E7')
		#self.g.remove('E7')
		self.E7.setVisible(False)

	if ( self.F1.isChecked() == True ):
		self.booked.append('F1')
		#self.g.remove('F1')
		self.F1.setVisible(False)


	if ( self.F2.isChecked() == True ):
		self.booked.append('F2')
		#self.g.remove('F2')
		self.F2.setVisible(False)

	if ( self.F3.isChecked() == True ):
		self.booked.append('F3')
		#self.g.remove('F3')
		self.F3.setVisible(False)

	if ( self.F4.isChecked() == True ):
		self.booked.append('F4')
		#self.g.remove('F4')
		self.F4.setVisible(False)

	if ( self.F5.isChecked() == True ):
		self.booked.append('F5')
		#self.g.remove('F5')
		self.F5.setVisible(False)

	if ( self.F6.isChecked() == True ):
		self.booked.append('F6')
		#self.g.remove('F6')
		self.F6.setVisible(False)

	if ( self.F7.isChecked() == True ):
		self.booked.append('F7')
		#self.g.remove('F7')
		self.F7.setVisible(False)

# ======================================================================================================

	if ( self.G1.isChecked() == True ):
		self.booked.append('G1')
		#self.s.remove('G1')
		self.G1.setVisible(False)


	if ( self.G2.isChecked() == True ):
		self.booked.append('G2')
		#self.s.remove('G2')
		self.G2.setVisible(False)

	if ( self.G3.isChecked() == True ):
		self.booked.append('G3')
		#self.s.remove('G3')
		self.G3.setVisible(False)

	if ( self.G4.isChecked() == True ):
		self.booked.append('G4')
		#self.s.remove('G4')
		self.G4.setVisible(False)

	if ( self.G5.isChecked() == True ):
		self.booked.append('G5')
		#self.s.remove('G5')
		self.G5.setVisible(False)

	if ( self.H1.isChecked() == True ):
		self.booked.append('H1')
		#self.s.remove('H1')
		self.H1.setVisible(False)


	if ( self.H2.isChecked() == True ):
		self.booked.append('H2')
		#self.s.remove('H2')
		self.H2.setVisible(False)

	if ( self.H3.isChecked() == True ):
		self.booked.append('H3')
		#self.s.remove('H3')
		self.H3.setVisible(False)

	if ( self.H4.isChecked() == True ):
		self.booked.append('H4')
		#self.s.remove('H4')
		self.H4.setVisible(False)

	if ( self.H5.isChecked() == True ):
		self.booked.append('H5')
		#self.s.remove('H5')
		self.H5.setVisible(False)

# =============================================================================================

#	print "platinum :" ,  self.p
#	print "gold :" , self.g
#	print "silver :" , self.s
	print "booked sairat :" , self.booked
	booked_string_user = ' '.join(self.booked)

	p1.g1.g(dk4.used_id, self.booked , dk4.used_time , 'sairat',self.already_booked_sairat)

	self.window=QtGui.QWidget()   
        self.ui=p1.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def goback(self):

	self.window=QtGui.QWidget()   
        self.ui=n1.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
	self.hide()

    def setupUi(self, Form):

        Form.setObjectName(_fromUtf8("Form"))
        Form.setEnabled(True)
        Form.resize(746, 608)
#	group = QtGui.QButtonGroup()
	self.msgbox_book_success = QtGui.QMessageBox(Form)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(580, 560, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
	self.go_back = QtGui.QPushButton(Form)
	self.go_back.setGeometry(QtCore.QRect(100, 560, 99, 27))
        self.go_back.setObjectName(_fromUtf8("GO BACK"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(320, 0, 161, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(330, 180, 68, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(330, 360, 68, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(-10, 0, 761, 611))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("plain.jpeg")))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.A1 = QtGui.QCheckBox(Form)
        self.A1.setGeometry(QtCore.QRect(30, 40, 61, 21))
        self.A1.setObjectName(_fromUtf8("A1"))
	if('A1' in str(self.already_booked_sairat)):
		self.A1.setVisible(False)
        self.A2 = QtGui.QCheckBox(Form)
        self.A2.setGeometry(QtCore.QRect(120, 40, 51, 21))
        self.A2.setObjectName(_fromUtf8("A2"))
	if('A2' in str(self.already_booked_sairat)):
		self.A2.setVisible(False)
        self.A3 = QtGui.QCheckBox(Form)
        self.A3.setGeometry(QtCore.QRect(220, 40, 51, 16))
        self.A3.setObjectName(_fromUtf8("A3"))
	if('A3' in str(self.already_booked_sairat)):
		self.A3.setVisible(False)
        self.A4 = QtGui.QCheckBox(Form)
        self.A4.setGeometry(QtCore.QRect(310, 40, 61, 21))
        self.A4.setObjectName(_fromUtf8("A4"))
	if('A4' in str(self.already_booked_sairat)):
		self.A4.setVisible(False)
        self.A5 = QtGui.QCheckBox(Form)
        self.A5.setGeometry(QtCore.QRect(400, 40, 61, 21))
        self.A5.setObjectName(_fromUtf8("A5"))
	if('A5' in str(self.already_booked_sairat)):
		self.A5.setVisible(False)
        self.A6 = QtGui.QCheckBox(Form)
        self.A6.setGeometry(QtCore.QRect(480, 40, 51, 21))
        self.A6.setObjectName(_fromUtf8("A6"))
	if('A6' in str(self.already_booked_sairat)):
		self.A6.setVisible(False)
        self.A7 = QtGui.QCheckBox(Form)
        self.A7.setGeometry(QtCore.QRect(560, 40, 51, 21))
        self.A7.setObjectName(_fromUtf8("A7"))
	if('A7' in str(self.already_booked_sairat)):
		self.A7.setVisible(False)
        self.A8 = QtGui.QCheckBox(Form)
        self.A8.setGeometry(QtCore.QRect(650, 40, 99, 22))
        self.A8.setObjectName(_fromUtf8("A8"))
	if('A8' in str(self.already_booked_sairat)):
		self.A8.setVisible(False)
        self.B1 = QtGui.QCheckBox(Form)
        self.B1.setGeometry(QtCore.QRect(30, 80, 51, 16))
        self.B1.setObjectName(_fromUtf8("B1"))
	if('B1' in str(self.already_booked_sairat)):
		self.B1.setVisible(False)
        self.B2 = QtGui.QCheckBox(Form)
        self.B2.setGeometry(QtCore.QRect(120, 80, 51, 21))
        self.B2.setObjectName(_fromUtf8("B2"))
	if('B2' in str(self.already_booked_sairat)):
		self.B2.setVisible(False)
        self.B3 = QtGui.QCheckBox(Form)
        self.B3.setGeometry(QtCore.QRect(220, 80, 51, 21))
        self.B3.setObjectName(_fromUtf8("B3"))
	if('B3' in str(self.already_booked_sairat)):
		self.B3.setVisible(False)
        self.B4 = QtGui.QCheckBox(Form)
        self.B4.setGeometry(QtCore.QRect(310, 80, 51, 21))
        self.B4.setObjectName(_fromUtf8("B4"))
	if('B4' in str(self.already_booked_sairat)):
		self.B4.setVisible(False)
        self.B5 = QtGui.QCheckBox(Form)
        self.B5.setGeometry(QtCore.QRect(400, 80, 51, 21))
        self.B5.setObjectName(_fromUtf8("B5"))
	if('B5' in str(self.already_booked_sairat)):
		self.B5.setVisible(False)
        self.B6 = QtGui.QCheckBox(Form)
        self.B6.setGeometry(QtCore.QRect(480, 80, 51, 16))
        self.B6.setObjectName(_fromUtf8("B6"))
	if('B6' in str(self.already_booked_sairat)):
		self.B6.setVisible(False)
        self.B7 = QtGui.QCheckBox(Form)
        self.B7.setGeometry(QtCore.QRect(560, 80, 51, 21))
        self.B7.setObjectName(_fromUtf8("B7"))
	if('B7' in str(self.already_booked_sairat)):
		self.B7.setVisible(False)
        self.B8 = QtGui.QCheckBox(Form)
        self.B8.setGeometry(QtCore.QRect(650, 80, 61, 16))
        self.B8.setObjectName(_fromUtf8("B8"))
	if('B8' in str(self.already_booked_sairat)):
		self.B8.setVisible(False)
        self.C1 = QtGui.QCheckBox(Form)
        self.C1.setGeometry(QtCore.QRect(30, 120, 41, 16))
        self.C1.setObjectName(_fromUtf8("C1"))
	if('C1' in str(self.already_booked_sairat)):
		self.C1.setVisible(False)
        self.C2 = QtGui.QCheckBox(Form)
        self.C2.setGeometry(QtCore.QRect(120, 120, 51, 21))
        self.C2.setObjectName(_fromUtf8("C2"))
	if('C2' in str(self.already_booked_sairat)):
		self.C2.setVisible(False)
        self.C3 = QtGui.QCheckBox(Form)
        self.C3.setGeometry(QtCore.QRect(220, 120, 51, 21))
        self.C3.setObjectName(_fromUtf8("C3"))
	if('C3' in str(self.already_booked_sairat)):
		self.C3.setVisible(False)
        self.C4 = QtGui.QCheckBox(Form)
        self.C4.setGeometry(QtCore.QRect(310, 120, 51, 16))
        self.C4.setObjectName(_fromUtf8("C4"))
	if('C4' in str(self.already_booked_sairat)):
		self.C4.setVisible(False)
        self.C5 = QtGui.QCheckBox(Form)
        self.C5.setGeometry(QtCore.QRect(400, 120, 51, 21))
        self.C5.setObjectName(_fromUtf8("C5"))
	if('C5' in str(self.already_booked_sairat)):
		self.C5.setVisible(False)
        self.C6 = QtGui.QCheckBox(Form)
        self.C6.setGeometry(QtCore.QRect(480, 120, 51, 21))
        self.C6.setObjectName(_fromUtf8("C6"))
	if('C6' in str(self.already_booked_sairat)):
		self.C6.setVisible(False)
        self.C7 = QtGui.QCheckBox(Form)
        self.C7.setGeometry(QtCore.QRect(560, 120, 51, 21))
        self.C7.setObjectName(_fromUtf8("C7"))
	if('C7' in str(self.already_booked_sairat)):
		self.C7.setVisible(False)
        self.C8 = QtGui.QCheckBox(Form)
        self.C8.setGeometry(QtCore.QRect(650, 120, 51, 16))
        self.C8.setObjectName(_fromUtf8("C8"))
	if('C8' in str(self.already_booked_sairat)):
		self.C8.setVisible(False)
        self.D1 = QtGui.QCheckBox(Form)
        self.D1.setGeometry(QtCore.QRect(70, 230, 51, 21))
        self.D1.setObjectName(_fromUtf8("D1"))
	if('D1' in str(self.already_booked_sairat)):
		self.D1.setVisible(False)
        self.D2 = QtGui.QCheckBox(Form)
        self.D2.setGeometry(QtCore.QRect(170, 230, 51, 21))
        self.D2.setObjectName(_fromUtf8("D2"))
	if('D2' in str(self.already_booked_sairat)):
		self.D2.setVisible(False)
        self.D3 = QtGui.QCheckBox(Form)
        self.D3.setGeometry(QtCore.QRect(270, 230, 51, 21))
        self.D3.setObjectName(_fromUtf8("D3"))
	if('D3' in str(self.already_booked_sairat)):
		self.D3.setVisible(False)
        self.D4 = QtGui.QCheckBox(Form)
        self.D4.setGeometry(QtCore.QRect(360, 230, 51, 21))
        self.D4.setObjectName(_fromUtf8("D4"))
	if('D4' in str(self.already_booked_sairat)):
		self.D4.setVisible(False)
        self.D5 = QtGui.QCheckBox(Form)
        self.D5.setGeometry(QtCore.QRect(440, 230, 51, 21))
        self.D5.setObjectName(_fromUtf8("D5"))
	if('D5' in str(self.already_booked_sairat)):
		self.D5.setVisible(False)
        self.D6 = QtGui.QCheckBox(Form)
        self.D6.setGeometry(QtCore.QRect(520, 230, 51, 16))
        self.D6.setObjectName(_fromUtf8("D6"))
	if('D6' in str(self.already_booked_sairat)):
		self.D6.setVisible(False)
        self.D7 = QtGui.QCheckBox(Form)
        self.D7.setGeometry(QtCore.QRect(610, 230, 51, 21))
        self.D7.setObjectName(_fromUtf8("D7"))
	if('D7' in str(self.already_booked_sairat)):
		self.D7.setVisible(False)
        self.E1 = QtGui.QCheckBox(Form)
        self.E1.setGeometry(QtCore.QRect(70, 270, 41, 21))
        self.E1.setObjectName(_fromUtf8("E1"))
	if('E1' in str(self.already_booked_sairat)):
		self.E1.setVisible(False)
        self.E2 = QtGui.QCheckBox(Form)
        self.E2.setGeometry(QtCore.QRect(170, 270, 51, 21))
        self.E2.setObjectName(_fromUtf8("E2"))
	if('E2' in str(self.already_booked_sairat)):
		self.E2.setVisible(False)
        self.E3 = QtGui.QCheckBox(Form)
        self.E3.setGeometry(QtCore.QRect(270, 270, 51, 21))
        self.E3.setObjectName(_fromUtf8("E3"))
	if('E3' in str(self.already_booked_sairat)):
		self.E3.setVisible(False)
        self.E4 = QtGui.QCheckBox(Form)
        self.E4.setGeometry(QtCore.QRect(360, 270, 51, 21))
        self.E4.setObjectName(_fromUtf8("E4"))
	if('E4' in str(self.already_booked_sairat)):
		self.E4.setVisible(False)
        self.E5 = QtGui.QCheckBox(Form)
        self.E5.setGeometry(QtCore.QRect(440, 270, 51, 21))
        self.E5.setObjectName(_fromUtf8("E5"))
	if('E5' in str(self.already_booked_sairat)):
		self.E5.setVisible(False)
        self.E6 = QtGui.QCheckBox(Form)
        self.E6.setGeometry(QtCore.QRect(520, 270, 51, 21))
        self.E6.setObjectName(_fromUtf8("E6"))
	if('E6' in str(self.already_booked_sairat)):
		self.E6.setVisible(False)
        self.E7 = QtGui.QCheckBox(Form)
        self.E7.setGeometry(QtCore.QRect(610, 270, 41, 21))
        self.E7.setObjectName(_fromUtf8("E7"))
	if('E7' in str(self.already_booked_sairat)):
		self.E7.setVisible(False)
        self.F1 = QtGui.QCheckBox(Form)
        self.F1.setGeometry(QtCore.QRect(70, 310, 41, 21))
        self.F1.setObjectName(_fromUtf8("F1"))
	if('F1' in str(self.already_booked_sairat)):
		self.F1.setVisible(False)
        self.F2 = QtGui.QCheckBox(Form)
        self.F2.setGeometry(QtCore.QRect(170, 310, 41, 21))
        self.F2.setObjectName(_fromUtf8("F2"))
	if('F2' in str(self.already_booked_sairat)):
		self.F2.setVisible(False)
        self.F3 = QtGui.QCheckBox(Form)
        self.F3.setGeometry(QtCore.QRect(270, 310, 41, 21))
        self.F3.setObjectName(_fromUtf8("F3"))
	if('F3' in str(self.already_booked_sairat)):
		self.F3.setVisible(False)
        self.F4 = QtGui.QCheckBox(Form)
        self.F4.setGeometry(QtCore.QRect(360, 310, 41, 21))
        self.F4.setObjectName(_fromUtf8("F4"))
	if('F4' in str(self.already_booked_sairat)):
		self.F4.setVisible(False)
        self.F5 = QtGui.QCheckBox(Form)
        self.F5.setGeometry(QtCore.QRect(440, 310, 41, 21))
        self.F5.setObjectName(_fromUtf8("F5"))
	if('F5' in str(self.already_booked_sairat)):
		self.F5.setVisible(False)
        self.F6 = QtGui.QCheckBox(Form)
        self.F6.setGeometry(QtCore.QRect(520, 310, 51, 21))
        self.F6.setObjectName(_fromUtf8("F6"))
	if('F6' in str(self.already_booked_sairat)):
		self.F6.setVisible(False)
        self.F7 = QtGui.QCheckBox(Form)
        self.F7.setGeometry(QtCore.QRect(610, 310, 41, 21))
        self.F7.setObjectName(_fromUtf8("F7"))
	if('F7' in str(self.already_booked_sairat)):
		self.F7.setVisible(False)
        self.G1 = QtGui.QCheckBox(Form)
        self.G1.setGeometry(QtCore.QRect(130, 400, 51, 21))
        self.G1.setObjectName(_fromUtf8("G1"))
	if('G1' in str(self.already_booked_sairat)):
		self.G1.setVisible(False)
        self.G2 = QtGui.QCheckBox(Form)
        self.G2.setGeometry(QtCore.QRect(230, 400, 51, 21))
        self.G2.setObjectName(_fromUtf8("G2"))
	if('G2' in str(self.already_booked_sairat)):
		self.G2.setVisible(False)
        self.G3 = QtGui.QCheckBox(Form)
        self.G3.setGeometry(QtCore.QRect(320, 400, 51, 21))
        self.G3.setObjectName(_fromUtf8("G3"))
	if('G3' in str(self.already_booked_sairat)):
		self.G3.setVisible(False)
        self.G4 = QtGui.QCheckBox(Form)
        self.G4.setGeometry(QtCore.QRect(420, 400, 51, 21))
        self.G4.setObjectName(_fromUtf8("G4"))
	if('G4' in str(self.already_booked_sairat)):
		self.G4.setVisible(False)
        self.G5 = QtGui.QCheckBox(Form)
        self.G5.setGeometry(QtCore.QRect(500, 400, 99, 22))
        self.G5.setObjectName(_fromUtf8("G5"))
	if('G5' in str(self.already_booked_sairat)):
		self.G5.setVisible(False)
        self.H1 = QtGui.QCheckBox(Form)
        self.H1.setGeometry(QtCore.QRect(130, 450, 51, 21))
        self.H1.setObjectName(_fromUtf8("H1"))
	if('H1' in str(self.already_booked_sairat)):
		self.H1.setVisible(False)
        self.H2 = QtGui.QCheckBox(Form)
        self.H2.setGeometry(QtCore.QRect(230, 450, 61, 21))
        self.H2.setObjectName(_fromUtf8("H2"))
	if('H2' in str(self.already_booked_sairat)):
		self.H2.setVisible(False)
        self.H3 = QtGui.QCheckBox(Form)
        self.H3.setGeometry(QtCore.QRect(320, 450, 51, 21))
        self.H3.setObjectName(_fromUtf8("H3"))
	if('H3' in str(self.already_booked_sairat)):
		self.H3.setVisible(False)
        self.H4 = QtGui.QCheckBox(Form)
        self.H4.setGeometry(QtCore.QRect(420, 450, 51, 21))
        self.H4.setObjectName(_fromUtf8("H4"))
	if('H4' in str(self.already_booked_sairat)):
		self.H4.setVisible(False)
        self.H5 = QtGui.QCheckBox(Form)
        self.H5.setGeometry(QtCore.QRect(500, 450, 61, 21))
        self.H5.setObjectName(_fromUtf8("H5"))
	if('H5' in str(self.already_booked_sairat)):
		self.H5.setVisible(False)
        self.graphicsView = QtGui.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(60, 500, 621, 31))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
	self.label_4.raise_()
	self.pushButton.raise_()
	self.go_back.raise_()
	self.label_2.raise_()
	self.label.raise_()
	self.label_3.raise_()
	self.A1.raise_()
	self.A2.raise_()
	self.A3.raise_()
	self.A4.raise_()
	self.A5.raise_()
	self.A6.raise_()
	self.A7.raise_()
	self.A8.raise_()
	self.B1.raise_()
	self.B2.raise_()
	self.B3.raise_()
	self.B4.raise_()
	self.B5.raise_()
	self.B6.raise_()
	self.B7.raise_()
	self.B8.raise_()
	self.C1.raise_()
	self.C2.raise_()
	self.C3.raise_()
	self.C4.raise_()
	self.C5.raise_()
	self.C6.raise_()
	self.C7.raise_()
	self.C8.raise_()
	self.D1.raise_()
	self.D2.raise_()
	self.D3.raise_()
	self.D4.raise_()
	self.D5.raise_()
	self.D6.raise_()
	self.D7.raise_()
	self.E1.raise_()
	self.E2.raise_()
	self.E3.raise_()
	self.E4.raise_()
	self.E5.raise_()
	self.E6.raise_()
	self.E7.raise_()
	self.F1.raise_()
	self.F2.raise_()
	self.F3.raise_()
	self.F4.raise_()
	self.F5.raise_()
	self.F6.raise_()
	self.F7.raise_()
	self.G1.raise_()
	self.G2.raise_()
	self.G3.raise_()
	self.G4.raise_()
	self.G5.raise_()
	self.H1.raise_()
	self.H2.raise_()
	self.H3.raise_()
	self.H4.raise_()
	self.H5.raise_()


#	grouself.p.buttonClicked.connect(self.btnClicked)

	self.pushButton.clicked.connect(self.book_seats)

	self.go_back.clicked.connect(self.goback)
	

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "BOOK ", None))
	self.go_back.setText(_translate("Form", "GO BACK ", None))
        self.label.setText(_translate("Form", "PLATINUM", None))
        self.label_2.setText(_translate("Form", "GOLD", None))
        self.label_3.setText(_translate("Form", "SILVER", None))
        self.A1.setText(_translate("Form", "A1", None))
        self.A2.setText(_translate("Form", "A2", None))
        self.A3.setText(_translate("Form", "A3", None))
        self.A4.setText(_translate("Form", "A4", None))
        self.A5.setText(_translate("Form", "A5", None))
        self.A6.setText(_translate("Form", "A6", None))
        self.A7.setText(_translate("Form", "A7", None))
        self.A8.setText(_translate("Form", "A8", None))
        self.B1.setText(_translate("Form", "B1", None))
        self.B2.setText(_translate("Form", "B2", None))
        self.B3.setText(_translate("Form", "B3", None))
        self.B4.setText(_translate("Form", "B4", None))
        self.B5.setText(_translate("Form", "B5", None))
        self.B6.setText(_translate("Form", "B6", None))
        self.B7.setText(_translate("Form", "B7", None))
        self.B8.setText(_translate("Form", "B8", None))
        self.C1.setText(_translate("Form", "C1", None))
        self.C2.setText(_translate("Form", "C2", None))
        self.C3.setText(_translate("Form", "C3", None))
        self.C4.setText(_translate("Form", "C4", None))
        self.C5.setText(_translate("Form", "C5", None))
        self.C6.setText(_translate("Form", "C6", None))
        self.C7.setText(_translate("Form", "C7", None))
        self.C8.setText(_translate("Form", "C8", None))
        self.D1.setText(_translate("Form", "D1", None))
        self.D2.setText(_translate("Form", "D2", None))
        self.D3.setText(_translate("Form", "D3", None))
        self.D4.setText(_translate("Form", "D4", None))
        self.D5.setText(_translate("Form", "D5", None))
        self.D6.setText(_translate("Form", "D6", None))
        self.D7.setText(_translate("Form", "D7", None))
        self.E1.setText(_translate("Form", "E1", None))
        self.E2.setText(_translate("Form", "E2", None))
        self.E3.setText(_translate("Form", "E3", None))
        self.E4.setText(_translate("Form", "E4", None))
        self.E5.setText(_translate("Form", "E5", None))
        self.E6.setText(_translate("Form", "E6", None))
        self.E7.setText(_translate("Form", "E7", None))
        self.F1.setText(_translate("Form", "F1", None))
        self.F2.setText(_translate("Form", "F2", None))
        self.F3.setText(_translate("Form", "F3", None))
        self.F4.setText(_translate("Form", "F4", None))
        self.F5.setText(_translate("Form", "F5", None))
        self.F6.setText(_translate("Form", "F6", None))
        self.F7.setText(_translate("Form", "F7", None))
        self.G1.setText(_translate("Form", "G1", None))
        self.G2.setText(_translate("Form", "G2", None))
        self.G3.setText(_translate("Form", "G3", None))
        self.G4.setText(_translate("Form", "G4", None))
        self.G5.setText(_translate("Form", "G5", None))
        self.H1.setText(_translate("Form", "H1", None))
        self.H2.setText(_translate("Form", "H2", None))
        self.H3.setText(_translate("Form", "H3", None))
        self.H4.setText(_translate("Form", "H4", None))
        self.H5.setText(_translate("Form", "H5", None))

dk4 = dont_know4()
#dd = ddd()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(syself.s.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    syself.s.exit(apself.p.exec_())

