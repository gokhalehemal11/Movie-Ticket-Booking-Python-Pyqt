# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reg.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import os,re
from status import *
import random
import MySQLdb
import login1 as l
from MySQLdb import Error
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

try:
    con = MySQLdb.connect(host="localhost",user="root",passwd="pccoe",db="mini")

    if con.open:
        print "connected"
    else:
        print "Not connected"

   
    cur = con.cursor()

except Error as e:
    print e  

class Ui_Form(object):


    def back_to_log(self):

	reload(l)
        self.window=QtGui.QWidget()   
        self.ui=l.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
        Form.close() 

        
    def reg_details(self):

        flag3 = 0
        flag4 = 0

        print "hi"
    
        u_name = self.lineEdit.text()
        u_id = self.lineEdit_2.text()
        u_ph = self.lineEdit_3.text()

 	x=re.match('^[A-z][A-Za-z]*\s*[A-Za-z]*$',u_name)
    	y=re.match('^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$',u_ph)
    	z = re.match('^[A-z][A-Za-z]*\s*[A-Za-z]*\s*[a-z0-9-]*$', u_id)
    	if (y!= None and x != None and z != None ):

		u_pin =  random.choice("ABCGHIFWXYZ") + str(random.randrange(100,500))

		print ("Pin :" + u_pin)
		print u_name
		print u_id
		print u_ph

		self.msgbox_pin.setText("Your Pin is : " + u_pin )
		self.msgbox_pin.exec_()

		cur.execute('insert into user_information values ("%s" , "%s" , "%s" , "%s")' % (u_id , u_name , u_ph , u_pin))

		con.commit()
		self.label_success.show()

		cur.execute('insert into logged_users values ("%s" , "%s" , "%s" )' % (u_id , u_pin , 'N'))

		con.commit()


   	else:
		self.msgbox_warn.setText("Enter Valid Entries !" )
		self.msgbox_warn.exec_()


#	log_success( u_id , u_pin  )  


    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(770, 640)
        self.pushButton_signup = QtGui.QPushButton(Form)
        self.pushButton_signup.setGeometry(QtCore.QRect(500, 480, 161, 71))
        self.pushButton_signup.setObjectName(_fromUtf8("pushButton_signup"))
        self.pushButton_back = QtGui.QPushButton(Form)
        self.pushButton_back.setGeometry(QtCore.QRect(100, 480, 161, 71))
        self.pushButton_back.setObjectName(_fromUtf8("pushButton_back"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(390, 160, 231, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(390, 240, 231, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(390, 310, 231, 27))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_name = QtGui.QLabel(Form)
        self.label_name.setGeometry(QtCore.QRect(160, 160, 101, 31))
        self.label_name.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(155, 255, 0);"))
        self.label_name.setObjectName(_fromUtf8("label_name"))
        self.label_userid = QtGui.QLabel(Form)
        self.label_userid.setGeometry(QtCore.QRect(160, 240, 121, 31))
        self.label_userid.setObjectName(_fromUtf8("label_userid"))
        self.label_phone = QtGui.QLabel(Form)
        self.label_phone.setGeometry(QtCore.QRect(160, 310, 101, 41))
        self.label_phone.setObjectName(_fromUtf8("label_phone"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 10, 771, 631))
        self.label.setText(_fromUtf8(""))
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("imageedit__5067087747.jpg")))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_success = QtGui.QLabel(Form)
        self.label_success.setGeometry(QtCore.QRect(550, 520,188, 147))
        self.label_success.setObjectName(_fromUtf8("label_success"))
        self.label_success.hide()
        self.msgbox_pin = QtGui.QMessageBox(Form)
	self.msgbox_warn = QtGui.QMessageBox(Form)
       # self.msgbox_pin.setIcon(QtGui.QMessageBox.msgbox_pin)
        self.label.raise_()
        self.pushButton_signup.raise_()
	self.pushButton_back.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.label_name.raise_()
        self.label_userid.raise_()
        self.label_phone.raise_()



        self.pushButton_signup.clicked.connect(self.reg_details)

        self.pushButton_back.clicked.connect(self.back_to_log)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton_signup.setText(_translate("Form", "SIGN -UP", None))
        self.pushButton_back.setText(_translate("Form", "BACK", None))
        self.label_name.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">    NAME</span></p></body></html>", None))
	self.label_userid.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#55ff00;\">     USER-ID</span></p></body></html>", None))
        self.label_phone.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#55ff00;\"> PHONE</span></p></body></html>", None))
        self.label_success.setText(_translate("Form", " User Registered Successfully ! ", None))
        self.label_success.setStyleSheet('color : WHITE')


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

