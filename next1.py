
from status import *
import book as bb
import cancel as c
import show_status as d
import login1 as ll 
from PyQt4 import QtCore, QtGui
import login1
from show_status import *
from login1 import *
from book import *
from cancel import *


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


class don_know:
	def __init__(self):
		self.used_id = ""
		self.used_pin = ""

	def n_id(self,my_id,my_pin):
		print "in next1 id" , my_id
		print "in next1 pin" , my_pin
		self.used_id =  my_id
		self.used_pin = my_pin


class Ui_Form(object , don_know):


    def go_to(self):

	if(self.rb1.isChecked() == True):
		print "Book"
		dk.nn_id(dk1.used_id)
		self.window=QtGui.QWidget()   
        	self.ui=bb.Ui_Form()
        	self.ui.setupUi(self.window)
        	self.window.show()
	elif(self.rb2.isChecked() == True):
		print "Cancel"
		dk11.nn_id(dk1.used_id)
		self.window=QtGui.QWidget()   
        	self.ui=c.Ui_Form()
        	self.ui.setupUi(self.window)
        	self.window.show()
	elif(self.rb3.isChecked() == True):
		print "Show status"
		stat.stat_id(dk1.used_id)
		self.window=QtGui.QWidget()   
        	self.ui=d.Ui_Form()
        	self.ui.setupUi(self.window)
        	self.window.show()
	elif(self.rb4.isChecked() == True):
		reload(login1)
		print "Logout"
		print " next logout id " , dk1.used_id
		print "next logout pin ", dk1.used_pin
		logout_success(dk1.used_id,dk1.used_pin)
        	self.window=QtGui.QWidget()   
        	self.ui=ll.Ui_Form()
        	self.ui.setupUi(self.window)
        	self.window.show()

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(663, 549)
        self.select = QtGui.QPushButton(Form)
        self.select.setGeometry(QtCore.QRect(270, 380, 99, 27))
        self.select.setObjectName(_fromUtf8("select"))
        self.rb1 = QtGui.QRadioButton(Form)
        self.rb1.setGeometry(QtCore.QRect(290, 160, 191, 21))
        self.rb1.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"font: 63 italic 16pt \"Ubuntu\";\n"
"color: rgb(85, 255, 0);\n"
""))
        self.rb1.setObjectName(_fromUtf8("rb1"))
        self.rb2 = QtGui.QRadioButton(Form)
        self.rb2.setGeometry(QtCore.QRect(290, 210, 181, 22))
        self.rb2.setStyleSheet(_fromUtf8("font: 63 italic 16pt \"Ubuntu\";\n"
"color: rgb(85, 255, 0);\n"
"background-color: rgb(0, 0, 0);"))
        self.rb2.setObjectName(_fromUtf8("rb2"))
        self.rb3 = QtGui.QRadioButton(Form)
        self.rb3.setGeometry(QtCore.QRect(290, 260, 117, 22))
        self.rb3.setStyleSheet(_fromUtf8("font: 63 italic 16pt \"Ubuntu\";\n"
"color: rgb(85, 255, 0);\n"
"background-color: rgb(0, 0, 0);"))
        self.rb3.setObjectName(_fromUtf8("rb3"))
        self.rb4 = QtGui.QRadioButton(Form)
        self.rb4.setGeometry(QtCore.QRect(290, 310, 117, 22))
        self.rb4.setStyleSheet(_fromUtf8("font: 63 italic 16pt \"Ubuntu\";\n"
"color: rgb(85, 255, 0);\n"
"background-color: rgb(0, 0, 0);"))
        self.rb4.setObjectName(_fromUtf8("rb4"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(220, 40, 341, 71))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 721, 531))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("imageedit__5067087747.jpg")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_2.raise_()
        self.rb1.raise_()
        self.rb2.raise_()
        self.rb3.raise_()
        self.rb4.raise_()
        self.label.raise_()
        self.select.raise_()
	
	self.select.clicked.connect(self.go_to)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.select.setText(_translate("Form", "SELECT", None))
        self.rb1.setText(_translate("Form", "BOOK TICKET", None))
        self.rb2.setText(_translate("Form", "CANCEL TICKET", None))
        self.rb3.setText(_translate("Form", "STATUS", None))
        self.rb4.setText(_translate("Form", "LOGOUT", None))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:28pt; font-weight:600; color:#ff0000;\">WELCOME USER</span></p></body></html>", None))

dk1 = don_know()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

