# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'book.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import time
import seat1 as st1
import seat2 as st2
import seat3 as st3
from seat1 import *
from seat2 import *
from seat3 import *
from login1 import *
from next1 import *
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

class dk5:
	def __init__(self):
		self.used_id = ""

	def nn_id(self , my_id):
		self.used_id = my_id

	
class Ui_Form(object , dk5):

    def go_to_seats(self):

	s_time = time.asctime(time.localtime(time.time()))
	cmp_time =int(s_time[11]+s_time[12])
#	print cmp_time

	if( self.rb4.isChecked() == True and self.rb1.isChecked() == True ):
		if ( cmp_time < 9):
			dk2.nn_id(dk.used_id , " 9 AM - 12 PM")
			self.window=QtGui.QWidget()   
			self.ui=st1.Ui_Form()
			self.ui.setupUi(self.window)
			self.window.show()
		else:
			self.msgbox_err.setText(" Please Select Valid Time ! ")
			self.msgbox_err.exec_()

	elif( self.rb4.isChecked() == True and self.rb2.isChecked() == True ):
		if ( cmp_time < 13 ):
			dk2.nn_id(dk.used_id , " 1 PM - 4 PM")
			self.window=QtGui.QWidget()   
			self.ui=st1.Ui_Form()
			self.ui.setupUi(self.window)
			self.window.show()
		else:
			self.msgbox_err.setText(" Please Select Valid Time ! ")
			self.msgbox_err.exec_()

	elif(self.rb4.isChecked() == True and self.rb3.isChecked() == True):
		if ( cmp_time < 18 ):
			print "in book id :" , dk.used_id
			dk2.nn_id(dk.used_id , " 6 PM - 9 PM")
			self.window=QtGui.QWidget()   
			self.ui=st1.Ui_Form()
			self.ui.setupUi(self.window)
			self.window.show()
		else:
			self.msgbox_err.setText(" Please Select Valid Time ! ")
			self.msgbox_err.exec_()

	elif( self.rb5.isChecked() == True and self.rb1.isChecked() == True ):
		if ( cmp_time < 9):
			dk3.nn_id(dk.used_id , " 9 AM - 12 PM")
			self.window=QtGui.QWidget()   
			self.ui=st2.Ui_Form()
			self.ui.setupUi(self.window)
			self.window.show()
		else:
			self.msgbox_err.setText(" Please Select Valid Time ! ")
			self.msgbox_err.exec_()

	elif( self.rb5.isChecked() == True and self.rb2.isChecked() == True ):
		if ( cmp_time < 13 ):
			dk3.nn_id(dk.used_id , " 1 PM - 4 PM")
			self.window=QtGui.QWidget()   
			self.ui=st2.Ui_Form()
			self.ui.setupUi(self.window)
			self.window.show()
		else:
			self.msgbox_err.setText(" Please Select Valid Time ! ")
			self.msgbox_err.exec_()

	elif(self.rb5.isChecked() == True and self.rb3.isChecked() == True):
		if ( cmp_time < 18 ):
			dk3.nn_id(dk.used_id, " 6 PM - 9 PM")
			self.window=QtGui.QWidget()   
			self.ui=st2.Ui_Form()
			self.ui.setupUi(self.window)
			self.window.show()
		else:
			self.msgbox_err.setText(" Please Select Valid Time ! ")
			self.msgbox_err.exec_()

	elif( self.rb6.isChecked() == True and self.rb1.isChecked() == True ):
		if ( cmp_time < 9):
			dk4.nn_id(dk.used_id , " 9 AM - 12 PM")
			self.window=QtGui.QWidget()   
			self.ui=st3.Ui_Form()
			self.ui.setupUi(self.window)
			self.window.show()
		else:
			self.msgbox_err.setText(" Please Select Valid Time ! ")
			self.msgbox_err.exec_()

	elif( self.rb6.isChecked() == True and self.rb2.isChecked() == True ):
		if ( cmp_time < 13 ):
			dk4.nn_id(dk.used_id, " 1 PM - 4 PM")
			self.window=QtGui.QWidget()   
			self.ui=st3.Ui_Form()
			self.ui.setupUi(self.window)
			self.window.show()
		else:
			self.msgbox_err.setText(" Please Select Valid Time ! ")
			self.msgbox_err.exec_()

	elif(self.rb6.isChecked() == True and self.rb3.isChecked() == True):
		if ( cmp_time < 18 ):
			dk4.nn_id(dk.used_id , " 6 PM - 9 PM")
			self.window=QtGui.QWidget()   
			self.ui=st3.Ui_Form()
			self.ui.setupUi(self.window)
			self.window.show()
		else:
			self.msgbox_err.setText(" Please Select Valid Time ! ")
			self.msgbox_err.exec_()
		
# ====================================================================================================
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(777, 611)
        self.l1 = QtGui.QLabel(Form)
        self.l1.setGeometry(QtCore.QRect(10, 10, 241, 271))
        self.l1.setStyleSheet(_fromUtf8("image: url(:/moca/pic.jpeg);"))
        self.l1.setText(_fromUtf8(""))
        self.l1.setObjectName(_fromUtf8("l1"))
        self.l2 = QtGui.QLabel(Form)
        self.l2.setGeometry(QtCore.QRect(300, 10, 201, 271))
        self.l2.setStyleSheet(_fromUtf8("image: url(:/moca/pic1.jpeg);"))
        self.l2.setText(_fromUtf8(""))
        self.l2.setObjectName(_fromUtf8("l2"))
        self.l3 = QtGui.QLabel(Form)
        self.l3.setGeometry(QtCore.QRect(570, 10, 181, 281))
        self.l3.setStyleSheet(_fromUtf8("image: url(:/moca/pic2.jpg);"))
        self.l3.setText(_fromUtf8(""))
        self.l3.setObjectName(_fromUtf8("l3"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(320, 370, 201, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.rb1 = QtGui.QRadioButton(Form)
        self.rb1.setGeometry(QtCore.QRect(40, 480, 161, 31))
        self.rb1.setStyleSheet(_fromUtf8("font: 75 20pt \"Ubuntu\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.rb1.setObjectName(_fromUtf8("rb1"))
        self.rb2 = QtGui.QRadioButton(Form)
        self.rb2.setGeometry(QtCore.QRect(310, 480, 161, 31))
        self.rb2.setStyleSheet(_fromUtf8("font: 75 20pt \"Ubuntu\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.rb2.setObjectName(_fromUtf8("rb2"))
        self.rb3 = QtGui.QRadioButton(Form)
        self.rb3.setGeometry(QtCore.QRect(590, 480, 151, 31))
        self.rb3.setStyleSheet(_fromUtf8("font: 75 20pt \"Ubuntu\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.rb3.setObjectName(_fromUtf8("rb3"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(330, 370, 151, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(620, 570, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(50, 300, 671, 51))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.rb4 = QtGui.QRadioButton(self.groupBox)
        self.rb4.setGeometry(QtCore.QRect(50, 20, 117, 22))
        self.rb4.setStyleSheet(_fromUtf8("font: 75 20pt \"Ubuntu\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.rb4.setObjectName(_fromUtf8("rb4"))
        self.rb5 = QtGui.QRadioButton(self.groupBox)
        self.rb5.setGeometry(QtCore.QRect(270, 20, 117, 22))
        self.rb5.setStyleSheet(_fromUtf8("font: 75 20pt \"Ubuntu\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.rb5.setObjectName(_fromUtf8("rb5"))
        self.rb6 = QtGui.QRadioButton(self.groupBox)
        self.rb6.setGeometry(QtCore.QRect(540, 20, 117, 22))
        self.rb6.setStyleSheet(_fromUtf8("font: 75 20pt \"Ubuntu\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.rb6.setObjectName(_fromUtf8("rb6"))
	self.msgbox_err = QtGui.QMessageBox(Form)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(-30, 0, 821, 611))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("cool-background.jpg")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_2.raise_()
        self.l1.raise_()
        self.l2.raise_()
        self.l3.raise_()
        self.rb1.raise_()
        self.rb2.raise_()
        self.rb3.raise_()
	self.groupBox.raise_()
        self.rb4.raise_()
        self.rb5.raise_()
        self.rb6.raise_()
        self.label.raise_()
        self.pushButton.raise_()


	self.pushButton.clicked.connect(self.go_to_seats)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.rb1, self.rb2)
        Form.setTabOrder(self.rb2, self.rb3)
        Form.setTabOrder(self.rb3, self.pushButton)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.rb1.setText(_translate("Form", "9AM-12PM", None))	
        self.rb2.setText(_translate("Form", "1PM-4PM", None))	
        self.rb3.setText(_translate("Form", "6PM-9PM", None))	
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#ffffff;\"> TIMINGS</span></p></body></html>", None))
        self.pushButton.setText(_translate("Form", "NEXT", None))	# next
        self.groupBox.setTitle(_translate("Form", "Movies", None))	
        self.rb4.setText(_translate("Form", "J2CE", None))		# j2ce
        self.rb5.setText(_translate("Form", "3 IDIOTS", None))		# 3 idiots
        self.rb6.setText(_translate("Form", "SAIRAT", None))		# sairat

dk = dk5()

import job_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

