# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaExtrato.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_telaExtrato(object):
    def setupUi(self, telaExtrato):
        telaExtrato.setObjectName("telaExtrato")
        telaExtrato.resize(479, 640)
        telaExtrato.setWindowOpacity(1.0)
        telaExtrato.setStyleSheet(".QFrame {\n"
"    background-color: rgba(25,25,112,0.8);\n"
"}")
        self.logo = QtWidgets.QLabel(telaExtrato)
        self.logo.setGeometry(QtCore.QRect(150, -40, 161, 161))
        font = QtGui.QFont()
        font.setFamily("Broadway")
        font.setPointSize(26)
        self.logo.setFont(font)
        self.logo.setStyleSheet(".QLabel#logo{\n"
"    color: rgb(255,255,255);\n"
"    text-align: rigth;\n"
"}")
        self.logo.setObjectName("logo")
        self.line = QtWidgets.QFrame(telaExtrato)
        self.line.setGeometry(QtCore.QRect(0, 70, 491, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.frameNav = QtWidgets.QFrame(telaExtrato)
        self.frameNav.setGeometry(QtCore.QRect(50, 110, 381, 471))
        self.frameNav.setStyleSheet("\n"
".QFrame#frameNav {\n"
"    background-color: rgba(255,250,240,0.6);\n"
"    border-radius: 1em;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"")
        self.frameNav.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameNav.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameNav.setObjectName("frameNav")
        self.labelExtrato = QtWidgets.QLabel(self.frameNav)
        self.labelExtrato.setGeometry(QtCore.QRect(10, 0, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelExtrato.setFont(font)
        self.labelExtrato.setStyleSheet(".QLabel {\n"
"    font-size: 2em;\n"
"}")
        self.labelExtrato.setObjectName("labelExtrato")
        self.buttonVoltar = QtWidgets.QPushButton(self.frameNav)
        self.buttonVoltar.setGeometry(QtCore.QRect(300, 420, 71, 41))
        self.buttonVoltar.setStyleSheet(".QPushButton{\n"
"    background-color: rgb(75,0,130);\n"
"    color: rgb(255,255,255);\n"
"    border-radius: 0.5em;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"\n"
".QPushButton:hover{\n"
"    background-color: rgba(75,0,130,0.6);\n"
"}")
        self.buttonVoltar.setObjectName("buttonVoltar")
        self.listExtrato = QtWidgets.QListWidget(self.frameNav)
        self.listExtrato.setGeometry(QtCore.QRect(20, 30, 351, 371))
        self.listExtrato.setStyleSheet(".QListWidget{\n"
"    border-radius: 0.5em;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(0,0,0);\n"
"}")
        self.listExtrato.setObjectName("listExtrato")

        self.retranslateUi(telaExtrato)
        QtCore.QMetaObject.connectSlotsByName(telaExtrato)

    def retranslateUi(self, telaExtrato):
        _translate = QtCore.QCoreApplication.translate
        telaExtrato.setWindowTitle(_translate("telaExtrato", "EXTRATO"))
        self.logo.setText(_translate("telaExtrato", "P-BANK"))
        self.labelExtrato.setText(_translate("telaExtrato", "EXTRATO"))
        self.buttonVoltar.setText(_translate("telaExtrato", "VOLTAR"))
