# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cancel.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import MySQLdb
from MySQLdb import Error
from seat3 import *
import next1 as n1

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

class dkn6:
	def __init__(self):
		self.used_id = ""
		self.used_list = []
	
	def nn_id(self,my_id):
		self.used_id = my_id

class Ui_Form(object , dkn6):

    def go_back(self):
	
	self.window=QtGui.QWidget()   
        self.ui=n1.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
	#self.hide()

    def go_to_cancel(self):
	
		try:
		    	con = MySQLdb.connect(host="localhost",user="root",passwd="pccoe",db="mini")

		    	if (con.open):
			    print "connected"
		    	else:
		       	    print "Not connected"
		
		   
		    	cur = con.cursor()

		except Error as e:
	        	print e


		seat_no = self.l1.text()

		if ( self.rb1.isChecked() == True ) :
			t_id = ""
			sql6 = "select user_id from J2CE_booking where seats = '%s' " % ( seat_no )
			cur.execute(sql6)

			results = cur.fetchall()

			for row in results :
				t_id = row[0]

			if( t_id == dk11.used_id ):
				sql7 = "delete from J2CE_booking where user_id = '%s' and seats = '%s'" % (t_id , seat_no)
				cur.execute(sql7)
				con.commit()
		        	self.msgbox_cancel_suc.setText( " Seat Cancelled Is :  " +  seat_no )
	        		self.msgbox_cancel_suc.exec_()	
			else:
		        	self.msgbox_cancel_err.setText( " Cannot Cancel Seat  " +  seat_no )
	        		self.msgbox_cancel_err.exec_()	

		if ( self.rb2.isChecked() == True ) :
			t_id = ""
			sql6 = "select user_id from 3idiots_booking where seats = '%s' " % (seat_no )
			cur.execute(sql6)

			results = cur.fetchall()

			for row in results :
				t_id = row[0]

			if( t_id == dk11.used_id ):
				sql7 = "delete from 3idiots_booking where user_id = '%s' and seats = '%s'" % (t_id , seat_no)
				cur.execute(sql7)
				con.commit()
		        	self.msgbox_cancel_suc.setText( " Seat Cancelled Is :  " +  seat_no )
	        		self.msgbox_cancel_suc.exec_()	
			else:
		        	self.msgbox_cancel_err.setText( " Cannot Cancel Seat  " +  seat_no )
	        		self.msgbox_cancel_err.exec_()

		if ( self.rb3.isChecked() == True ) :
			t_id = ""
			sql6 = "select user_id from sairat_booking where seats = '%s' " % ( seat_no )
			cur.execute(sql6)

			results = cur.fetchall()

			for row in results :
				t_id = row[0]

			if( t_id == dk11.used_id ):
				
				sql7 = "delete from sairat_booking where user_id = '%s' and seats = '%s'" % (t_id , seat_no)
				cur.execute(sql7)
				con.commit()
		        	self.msgbox_cancel_suc.setText( " Seat Cancelled Is :  " +  seat_no )
	        		self.msgbox_cancel_suc.exec_()	
			else:
		        	self.msgbox_cancel_err.setText( " Cannot Cancel Seat  " +  seat_no )
	        		self.msgbox_cancel_err.exec_()					

    
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(650, 501)
	Form.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
	self.msgbox_cancel_err = QtGui.QMessageBox(Form)
	self.msgbox_cancel_suc = QtGui.QMessageBox(Form)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(110, 150, 381, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 70, 191, 51))
        self.label.setObjectName(_fromUtf8("label"))
        self.cancel = QtGui.QPushButton(Form)
        self.cancel.setGeometry(QtCore.QRect(450, 410, 99, 27))
        self.cancel.setStyleSheet(_fromUtf8("font: 75 16pt \"Ubuntu\";\n"
"color: rgb(255, 255, 255);"))
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.back = QtGui.QPushButton(Form)
        self.back.setGeometry(QtCore.QRect(90, 420, 99, 27))
        self.back.setStyleSheet(_fromUtf8("font: 75 16pt \"Ubuntu\";\n"
"color: rgb(255, 255, 255);"))
        self.back.setObjectName(_fromUtf8("back"))
	self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 270, 551, 311))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("are-you-sure.jpg.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.l1 = QtGui.QLineEdit(Form)
        self.l1.setGeometry(QtCore.QRect(390, 80, 101, 31))
        self.l1.setObjectName(_fromUtf8("l1"))
	self.rb1 = QtGui.QRadioButton(Form)
        self.rb1.setGeometry(QtCore.QRect(90, 230, 117, 22))
        self.rb1.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Ubuntu\";"))
        self.rb1.setObjectName(_fromUtf8("rb1"))
        self.rb2 = QtGui.QRadioButton(Form)
        self.rb2.setGeometry(QtCore.QRect(260, 230, 117, 22))
        self.rb2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Ubuntu\";"))
        self.rb2.setObjectName(_fromUtf8("rb2"))
        self.rb3 = QtGui.QRadioButton(Form)
        self.rb3.setGeometry(QtCore.QRect(450, 230, 117, 22))
        self.rb3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Ubuntu\";"))
        self.rb3.setObjectName(_fromUtf8("rb3"))
        self.label_2.raise_()
        self.rb1.raise_()
        self.rb2.raise_()
        self.rb3.raise_()
        self.back.raise_()
        self.cancel.raise_()
        self.label.raise_()
        self.l1.raise_()
        self.label_3.raise_()


	self.cancel.clicked.connect(self.go_to_cancel)

	self.back.clicked.connect(self.go_back)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "CANCELLATION", None))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">ENTER YOUR SEAT NUMBER</span></p></body></html>", None))
        self.cancel.setText(_translate("Form", "CANCEL", None))
        self.rb1.setText(_translate("Form", " J2CE ", None))	
        self.rb2.setText(_translate("Form", " 3 IDIOTS ", None))	
        self.rb3.setText(_translate("Form", " SAIRAT ", None))	
        self.back.setText(_translate("Form", "BACK", None))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-style:italic; color:#ff0000;\">PLEASE ENTER ONE SEAT NUMBER AT A TIME !!!!!</span></p></body></html>", None))

dk11 = dkn6()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

