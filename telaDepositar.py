# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaDepositar.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelValor = QtWidgets.QLabel(self.centralwidget)
        self.labelValor.setGeometry(QtCore.QRect(30, 20, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(13)
        self.labelValor.setFont(font)
        self.labelValor.setObjectName("labelValor")
        self.lineSenha = QtWidgets.QLineEdit(self.centralwidget)
        self.lineSenha.setGeometry(QtCore.QRect(80, 20, 251, 20))
        self.lineSenha.setObjectName("lineSenha")
        self.buttonDepositar = QtWidgets.QPushButton(self.centralwidget)
        self.buttonDepositar.setGeometry(QtCore.QRect(250, 50, 81, 23))
        self.buttonDepositar.setObjectName("buttonDepositar")
        self.buttonVoltar = QtWidgets.QPushButton(self.centralwidget)
        self.buttonVoltar.setGeometry(QtCore.QRect(160, 50, 81, 23))
        self.buttonVoltar.setObjectName("buttonVoltar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelValor.setText(_translate("MainWindow", "Valor :"))
        self.buttonDepositar.setText(_translate("MainWindow", "Depositar"))
        self.buttonVoltar.setText(_translate("MainWindow", "Voltar"))