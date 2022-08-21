# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaTransfere.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_telaTransfere(object):
    def setupUi(self, telaTransfere):
        telaTransfere.setObjectName("telaTransfere")
        telaTransfere.resize(479, 640)
        telaTransfere.setWindowOpacity(1.0)
        telaTransfere.setStyleSheet(".QFrame {\n"
"    background-color: rgba(25,25,112,0.8);\n"
"}")
        self.logo = QtWidgets.QLabel(telaTransfere)
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
        self.line = QtWidgets.QFrame(telaTransfere)
        self.line.setGeometry(QtCore.QRect(0, 70, 491, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.frameNav = QtWidgets.QFrame(telaTransfere)
        self.frameNav.setGeometry(QtCore.QRect(50, 110, 381, 291))
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
        self.labelValor = QtWidgets.QLabel(self.frameNav)
        self.labelValor.setGeometry(QtCore.QRect(10, 0, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelValor.setFont(font)
        self.labelValor.setStyleSheet(".QLabel {\n"
"    font-size: 2em;\n"
"}")
        self.labelValor.setObjectName("labelValor")
        self.lineValor = QtWidgets.QLineEdit(self.frameNav)
        self.lineValor.setGeometry(QtCore.QRect(10, 30, 361, 31))
        self.lineValor.setStyleSheet(".QLineEdit{\n"
"    border-radius: 0.5em;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(0,0,0);\n"
"}")
        self.lineValor.setObjectName("lineValor")
        self.buttonVoltar = QtWidgets.QPushButton(self.frameNav)
        self.buttonVoltar.setGeometry(QtCore.QRect(10, 240, 71, 41))
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
        self.buttonTransferir = QtWidgets.QPushButton(self.frameNav)
        self.buttonTransferir.setGeometry(QtCore.QRect(300, 240, 71, 41))
        self.buttonTransferir.setStyleSheet(".QPushButton{\n"
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
        self.buttonTransferir.setObjectName("buttonTransferir")
        self.labelSenha = QtWidgets.QLabel(self.frameNav)
        self.labelSenha.setGeometry(QtCore.QRect(10, 60, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelSenha.setFont(font)
        self.labelSenha.setStyleSheet(".QLabel {\n"
"    font-size: 2em;\n"
"}")
        self.labelSenha.setObjectName("labelSenha")
        self.lineSenha = QtWidgets.QLineEdit(self.frameNav)
        self.lineSenha.setGeometry(QtCore.QRect(10, 90, 361, 31))
        self.lineSenha.setStyleSheet(".QLineEdit{\n"
"    border-radius: 0.5em;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(0,0,0);\n"
"}")
        self.lineSenha.setObjectName("lineSenha")
        self.labelDestino = QtWidgets.QLabel(self.frameNav)
        self.labelDestino.setGeometry(QtCore.QRect(10, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelDestino.setFont(font)
        self.labelDestino.setStyleSheet(".QLabel {\n"
"    font-size: 2em;\n"
"}")
        self.labelDestino.setObjectName("labelDestino")
        self.lineDestino = QtWidgets.QLineEdit(self.frameNav)
        self.lineDestino.setGeometry(QtCore.QRect(10, 150, 361, 31))
        self.lineDestino.setStyleSheet(".QLineEdit{\n"
"    border-radius: 0.5em;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(0,0,0);\n"
"}")
        self.lineDestino.setObjectName("lineDestino")

        self.retranslateUi(telaTransfere)
        QtCore.QMetaObject.connectSlotsByName(telaTransfere)

    def retranslateUi(self, telaTransfere):
        _translate = QtCore.QCoreApplication.translate
        telaTransfere.setWindowTitle(_translate("telaTransfere", "TRANSFERE"))
        self.logo.setText(_translate("telaTransfere", "P-BANK"))
        self.labelValor.setText(_translate("telaTransfere", "VALOR"))
        self.buttonVoltar.setText(_translate("telaTransfere", "VOLTAR"))
        self.buttonTransferir.setText(_translate("telaTransfere", "TRANSFERIR"))
        self.labelSenha.setText(_translate("telaTransfere", "SENHA"))
        self.labelDestino.setText(_translate("telaTransfere", "CPF DESTINO"))