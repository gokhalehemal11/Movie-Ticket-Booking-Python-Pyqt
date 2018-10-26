import MySQLdb
from MySQLdb import Error

import next1 as pl
import reg1 as pl2
from status import *
from next1 import *
from seat1 import *
from seat2 import *
from seat3 import *
from next1 import *
from mat import *

from PyQt4 import QtCore, QtGui

my_id=""
my_pin=""

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


class Ui_Form(object):

    def log(self):
	
    	try:
    		con = MySQLdb.connect(host="localhost",user="root",passwd="pccoe",db="mini")

    		if (con.open):
        		print "connected"
    		else:
       			print "Not connected"
	
   
    		cur = con.cursor()

    	except Error as e:
    		print e

        sql2 = " select user_id from user_information  " 
	cur.execute(sql2)

	res = cur.fetchall()

#print (res)

	all_users_list = [ i[0] for i in res]

	print all_users_list        
  

        flag1 = 0
        flag2 = 0
        db_id=""
        db_pin=""
        id = self.l1.text()
        pin = self.l2.text()

	my_id = id
	my_pin = pin    

	print "my_id" , my_id
	print "my_pin" , my_pin

#	not_used_pin = n_pin(my_pin)	
	
        sql = "select user_id,password from user_information where user_id = '%s' and password = '%s' " % (id,pin)
        cur.execute(sql)

        results = cur.fetchall()

       # print(results)

        for row in results :
            db_id = row[0]
            db_pin = row[1]


      #  print "userid = %s , password = %s" % (db_id,db_pin)

	if( id =="" and pin == ""):
	    self.label_5.show()

        elif( id == db_id and pin == db_pin ):
#	    reload(pl)
	    variables(my_id , my_pin)
	    dk1.n_id(my_id , my_pin)
	    log_success( id , pin )
            self.window=QtGui.QWidget()   
            self.ui=pl.Ui_Form()
            self.ui.setupUi(self.window)
            self.window.show()
            flag1 = 1

        else:
            self.label_4.show()

        if ( flag1 == 1):
            Form.close()         

    def reg(self):
        self.window=QtGui.QWidget()   
        self.ui=pl2.Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
        flag2 = 1

        if( flag2 == 1):
            Form.close()

           # self.ui.reg_details()

    def gr(self):
	f()


    def setupUi(self, Form):

        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(632, 603)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 641, 141))
        self.label.setStyleSheet(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 180, 121, 61))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 290, 171, 51))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(30, 390, 541, 51))
        self.label_4.setMinimumSize(QtCore.QSize(68, 0))
        self.label_4.setAutoFillBackground(True)
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_4.hide()
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(30, 390, 541, 51))
        self.label_5.setMinimumSize(QtCore.QSize(68, 0))
        self.label_5.setAutoFillBackground(True)
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_5.hide()
        self.l1 = QtGui.QLineEdit(Form)
        self.l1.setGeometry(QtCore.QRect(290, 190, 221, 41))
        self.l1.setObjectName(_fromUtf8("l1"))
        self.l2 = QtGui.QLineEdit(Form)
        self.l2.setGeometry(QtCore.QRect(290, 300, 221, 41))
	self.l2.setEchoMode(QtGui.QLineEdit.Password)
        self.l2.setObjectName(_fromUtf8("l2"))
        self.login = QtGui.QPushButton(Form)
        self.login.setGeometry(QtCore.QRect(280, 360, 99, 27))
        self.login.setObjectName(_fromUtf8("login"))
        self.graph = QtGui.QPushButton(Form)
        self.graph.setGeometry(QtCore.QRect(280, 500, 99, 27))
        self.graph.setObjectName(_fromUtf8("graph"))
        self.register = QtGui.QPushButton(Form)
        self.register.setGeometry(QtCore.QRect(280, 440, 99, 27))
        self.register.setObjectName(_fromUtf8("register"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 641, 581))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("imageedit__5067087747.jpg")))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_6.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.l1.raise_()
        self.l2.raise_()
        self.login.raise_()
        self.register.raise_()
	self.graph.raise_()
        self.label_4.raise_()
        self.label_5.raise_()

        self.login.clicked.connect(self.log)
        self.register.clicked.connect(self.reg)
	self.graph.clicked.connect(self.gr)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ff0000;\">WELCOME</span></p></body></html>", None))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffff00;\">USER ID :</span></p></body></html>", None))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:22pt; color:#ffff00;\">PASSWORD:</span></p></body></html>", None))
        self.label_4.setText(_translate("Form", "Invalid User-Id Or Password !", None))
	self.label_5.setText(_translate("Form", "User-id and Password Cannot Be Empty !", None))
        self.label_4.setStyleSheet('color : RED')
	self.label_5.setStyleSheet('color : RED')
        self.login.setText(_translate("Form", "LOGIN", None))
        self.register.setText(_translate("Form", "REGISTER", None))
        self.graph.setText(_translate("Form", "GRAPH", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

