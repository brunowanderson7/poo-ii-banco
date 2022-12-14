# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_telaMenu(object):
    def setupUi(self, telaMenu):
        telaMenu.setObjectName("telaMenu")
        telaMenu.resize(479, 569)
        telaMenu.setWindowOpacity(1.0)
        telaMenu.setStyleSheet(".QFrame {\n"
"    background-color: rgba(25,25,112,0.8);\n"
"}")
        self.frameMenu = QtWidgets.QFrame(telaMenu)
        self.frameMenu.setGeometry(QtCore.QRect(10, 170, 461, 191))
        self.frameMenu.setStyleSheet("\n"
".QFrame#frameMenu {\n"
"    background-color: rgba(255,250,240,0.6);\n"
"    border-radius: 1em;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(0,0,0);\n"
"}\n"
"")
        self.frameMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameMenu.setObjectName("frameMenu")
        self.buttonTransferir = QtWidgets.QPushButton(self.frameMenu)
        self.buttonTransferir.setGeometry(QtCore.QRect(310, 20, 121, 61))
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
        self.buttonSacar = QtWidgets.QPushButton(self.frameMenu)
        self.buttonSacar.setGeometry(QtCore.QRect(170, 20, 121, 61))
        self.buttonSacar.setStyleSheet(".QPushButton{\n"
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
        self.buttonSacar.setObjectName("buttonSacar")
        self.buttonDepositar = QtWidgets.QPushButton(self.frameMenu)
        self.buttonDepositar.setGeometry(QtCore.QRect(30, 20, 121, 61))
        self.buttonDepositar.setStyleSheet(".QPushButton{\n"
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
        self.buttonDepositar.setObjectName("buttonDepositar")
        self.buttonExtrato = QtWidgets.QPushButton(self.frameMenu)
        self.buttonExtrato.setGeometry(QtCore.QRect(30, 100, 121, 61))
        self.buttonExtrato.setStyleSheet(".QPushButton{\n"
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
        self.buttonExtrato.setObjectName("buttonExtrato")
        self.buttonExcluir = QtWidgets.QPushButton(self.frameMenu)
        self.buttonExcluir.setGeometry(QtCore.QRect(170, 100, 121, 61))
        self.buttonExcluir.setStyleSheet(".QPushButton{\n"
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
        self.buttonExcluir.setObjectName("buttonExcluir")
        self.buttonSair = QtWidgets.QPushButton(self.frameMenu)
        self.buttonSair.setGeometry(QtCore.QRect(310, 100, 121, 61))
        self.buttonSair.setStyleSheet(".QPushButton{\n"
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
        self.buttonSair.setObjectName("buttonSair")
        self.logo = QtWidgets.QLabel(telaMenu)
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
        self.line = QtWidgets.QFrame(telaMenu)
        self.line.setGeometry(QtCore.QRect(0, 70, 491, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.frameNav = QtWidgets.QFrame(telaMenu)
        self.frameNav.setGeometry(QtCore.QRect(10, 90, 461, 71))
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
        self.labelInfo = QtWidgets.QLabel(self.frameNav)
        self.labelInfo.setGeometry(QtCore.QRect(270, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelInfo.setFont(font)
        self.labelInfo.setStyleSheet(".QLabel {\n"
"    font-size: 2em;\n"
"}")
        self.labelInfo.setObjectName("labelInfo")
        self.user = QtWidgets.QLabel(self.frameNav)
        self.user.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.user.setStyleSheet(".QLabel#user{\n"
"    background-image: url(:/newPrefix/icon-user.png);\n"
"}")
        self.user.setText("")
        self.user.setObjectName("user")
        self.bemVindo = QtWidgets.QLabel(self.frameNav)
        self.bemVindo.setGeometry(QtCore.QRect(60, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bemVindo.setFont(font)
        self.bemVindo.setStyleSheet(".QLabel {\n"
"    font-size: 2em;\n"
"}")
        self.bemVindo.setObjectName("bemVindo")
        self.userName = QtWidgets.QLabel(self.frameNav)
        self.userName.setGeometry(QtCore.QRect(140, 20, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.userName.setFont(font)
        self.userName.setStyleSheet(".QLabel {\n"
"    font-size: 2em;\n"
"}")
        self.userName.setText("")
        self.userName.setObjectName("userName")
        self.userSaldo = QtWidgets.QLabel(self.frameNav)
        self.userSaldo.setGeometry(QtCore.QRect(350, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.userSaldo.setFont(font)
        self.userSaldo.setStyleSheet(".QLabel {\n"
"    font-size: 2em;\n"
"}")
        self.userSaldo.setText("")
        self.userSaldo.setObjectName("userSaldo")

        self.retranslateUi(telaMenu)
        QtCore.QMetaObject.connectSlotsByName(telaMenu)

    def retranslateUi(self, telaMenu):
        _translate = QtCore.QCoreApplication.translate
        telaMenu.setWindowTitle(_translate("telaMenu", "MENU"))
        self.buttonTransferir.setText(_translate("telaMenu", "TRANSFERIR"))
        self.buttonSacar.setText(_translate("telaMenu", "SACAR"))
        self.buttonDepositar.setText(_translate("telaMenu", "DEPOSITAR"))
        self.buttonExtrato.setText(_translate("telaMenu", "EXTRATO"))
        self.buttonExcluir.setText(_translate("telaMenu", "EXCLUIR CONTA"))
        self.buttonSair.setText(_translate("telaMenu", "SAIR"))
        self.logo.setText(_translate("telaMenu", "P-BANK"))
        self.labelInfo.setText(_translate("telaMenu", "Saldo: R$"))
        self.bemVindo.setText(_translate("telaMenu", "Bem vindo, "))
