# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\POO\PROYECTOS\Proyectoe\Ui\u_loginerror.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(338, 120)
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.pushlogin = QtWidgets.QPushButton(Dialog)
        self.pushlogin.setGeometry(QtCore.QRect(120, 70, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(11)
        self.pushlogin.setFont(font)
        self.pushlogin.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(122, 143, 168);")
        self.pushlogin.setObjectName("pushlogin")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 301, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(80, 64, 255)")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushlogin.setText(_translate("Dialog", "Ok"))
        self.label.setText(_translate("Dialog", "Se produjo un error"))
        self.label_2.setText(_translate("Dialog", "Id de usuario o contraseña incorrecta"))
