# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ip.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
import netifaces


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 214, 46))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_port = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_port.setFont(font)
        self.label_port.setObjectName("label_port")
        self.horizontalLayout.addWidget(self.label_port)
        self.menu_port = QtWidgets.QComboBox(self.layoutWidget)
        self.menu_port.setObjectName("menu_port")
        #port gathering
        self.menu_port.addItems(netifaces.interfaces())
        self.menu_port.activated.connect(self.ipfetch)
        self.horizontalLayout.addWidget(self.menu_port)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 70, 381, 151))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_ip = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_ip.setFont(font)
        self.label_ip.setObjectName("label_ip")
        self.gridLayout.addWidget(self.label_ip, 0, 0, 1, 1)
        self.line_ip = QtWidgets.QLineEdit(self.layoutWidget1)
        self.line_ip.setInputMask("")
        self.line_ip.setObjectName("line_ip")
        self.gridLayout.addWidget(self.line_ip, 0, 1, 1, 1)
        self.label_subnet = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_subnet.setFont(font)
        self.label_subnet.setObjectName("label_subnet")
        self.gridLayout.addWidget(self.label_subnet, 1, 0, 1, 1)
        self.lineEdit_subnet = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_subnet.setObjectName("lineEdit_subnet")
        self.gridLayout.addWidget(self.lineEdit_subnet, 1, 1, 1, 1)
        self.lineEdit_gateway = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_gateway.setObjectName("lineEdit_gateway")
        self.gridLayout.addWidget(self.lineEdit_gateway, 2, 1, 1, 1)
        self.label_dns = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_dns.setFont(font)
        self.label_dns.setObjectName("label_dns")
        self.gridLayout.addWidget(self.label_dns, 5, 0, 1, 1)
        self.lineEdit_dns = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_dns.setObjectName("lineEdit_dns")
        self.gridLayout.addWidget(self.lineEdit_dns, 5, 1, 1, 1)
        self.label_gateway = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_gateway.setFont(font)
        self.label_gateway.setObjectName("label_gateway")
        self.gridLayout.addWidget(self.label_gateway, 2, 0, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(Form)
        self.layoutWidget2.setGeometry(QtCore.QRect(190, 230, 196, 39))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.push_edit = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.push_edit.setFont(font)
        self.push_edit.setObjectName("push_edit")
        self.horizontalLayout_2.addWidget(self.push_edit)
        self.push_add = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.push_add.setFont(font)
        self.push_add.setObjectName("push_add")
        self.horizontalLayout_2.addWidget(self.push_add)

        self.push_add.clicked.connect(self.ipvalidate)

  #       ipRange = "(?:[0-1]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])"
		# ipRegex = QRegExp("^"+ipRange+"\\."+ipRange+"\\."+ipRange+"\\."+ipRange+"$")
		# ipValidator = QRegExpValidator(ipRegex, self)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def ipvalidate(self):

    	ip_add = self.line_ip.text()
    	subnetmask = self.lineEdit_subnet.text()
    	gateway = self.lineEdit_gateway.text()
    	dns = self.lineEdit_dns.text()
    	print(type(netifaces.interfaces()))

    	# print(ip_add,subnetmask,gateway,dns)
        # print(self.line_ip.text())
    def ipfetch(self):
    	selected_port = self.menu_port.currentText()
    	mylist = netifaces.ifaddresses(selected_port)[netifaces.AF_INET]
    	mygateway = (netifaces.gateways()['default'][netifaces.AF_INET])
    	self.line_ip.setText(mylist[0]['addr'])
    	self.lineEdit_subnet.setText(mylist[0]['netmask'])
    	self.lineEdit_gateway.setText(mygateway[0])

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_port.setText(_translate("Form", "ETHERNET PORT"))
        self.label_ip.setText(_translate("Form", "IP"))
        self.line_ip.setPlaceholderText(_translate("Form", "255.255.255.255"))
        self.label_subnet.setText(_translate("Form", "SUBNET"))
        self.lineEdit_subnet.setPlaceholderText(_translate("Form", "255.255.255.255"))
        self.lineEdit_gateway.setPlaceholderText(_translate("Form", "255.255.255.255"))
        self.label_dns.setText(_translate("Form", "DNS"))
        self.lineEdit_dns.setPlaceholderText(_translate("Form", "8.8.8.8"))
        self.label_gateway.setText(_translate("Form", "GATEWAY"))
        self.push_edit.setText(_translate("Form", "EDIT"))
        self.push_add.setText(_translate("Form", "ADD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
