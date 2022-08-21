# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaExcluir.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_telaExcluir(object):
    def setupUi(self, telaExcluir):
        telaExcluir.setObjectName("telaExcluir")
        telaExcluir.resize(479, 640)
        telaExcluir.setWindowOpacity(1.0)
        telaExcluir.setStyleSheet(".QFrame {\n"
"    background-color: rgba(25,25,112,0.8);\n"
"}")
        self.logo = QtWidgets.QLabel(telaExcluir)
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
        self.line = QtWidgets.QFrame(telaExcluir)
        self.line.setGeometry(QtCore.QRect(0, 70, 491, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.frameNav = QtWidgets.QFrame(telaExcluir)
        self.frameNav.setGeometry(QtCore.QRect(50, 110, 381, 201))
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
        self.labelCpf = QtWidgets.QLabel(self.frameNav)
        self.labelCpf.setGeometry(QtCore.QRect(10, 0, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelCpf.setFont(font)
        self.labelCpf.setStyleSheet(".QLabel {\n"
"    font-size: 2em;\n"
"}")
        self.labelCpf.setObjectName("labelCpf")
        self.lineCpf = QtWidgets.QLineEdit(self.frameNav)
        self.lineCpf.setGeometry(QtCore.QRect(10, 30, 361, 31))
        self.lineCpf.setStyleSheet(".QLineEdit{\n"
"    border-radius: 0.5em;\n"
"    border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(0,0,0);\n"
"}")
        self.lineCpf.setObjectName("lineCpf")
        self.buttonVoltar = QtWidgets.QPushButton(self.frameNav)
        self.buttonVoltar.setGeometry(QtCore.QRect(10, 150, 71, 41))
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
        self.buttonExcluir = QtWidgets.QPushButton(self.frameNav)
        self.buttonExcluir.setGeometry(QtCore.QRect(300, 150, 71, 41))
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

        self.retranslateUi(telaExcluir)
        QtCore.QMetaObject.connectSlotsByName(telaExcluir)

    def retranslateUi(self, telaExcluir):
        _translate = QtCore.QCoreApplication.translate
        telaExcluir.setWindowTitle(_translate("telaExcluir", "EXCLUIR"))
        self.logo.setText(_translate("telaExcluir", "P-BANK"))
        self.labelCpf.setText(_translate("telaExcluir", "CPF"))
        self.buttonVoltar.setText(_translate("telaExcluir", "VOLTAR"))
        self.buttonExcluir.setText(_translate("telaExcluir", "EXCLUIR"))
        self.labelSenha.setText(_translate("telaExcluir", "SENHA"))