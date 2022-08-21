import hashlib
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtWidgets

from telaCadastro import Ui_telaCadastro as Ui_Cadastro
from telaDeposito import Ui_telaDeposito as Ui_Deposito
from telaLogin import Ui_telaLogin as Ui_Login
from telaMenu import Ui_telaMenu as Ui_Menu
from telaSaque import Ui_telaSaque as Ui_Saque
from telaTransfere import Ui_telaTransfere as Ui_Transfere
from telaExcluir import Ui_telaExcluir as Ui_Excluir
from telaExtrato import Ui_telaExtrato as Ui_Extrato

import database
from conta import Conta
from cliente import Cliente





class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)


        self.QtStack = QtWidgets.QStackedLayout()
        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()


        self.telaLogin = Ui_Login()
        self.telaLogin.setupUi(self.stack0)

        self.telaCadastro = Ui_Cadastro()
        self.telaCadastro.setupUi(self.stack1)

        self.telaMenu = Ui_Menu()
        self.telaMenu.setupUi(self.stack2)

        self.telaDeposito = Ui_Deposito()
        self.telaDeposito.setupUi(self.stack3)

        self.telaSaque = Ui_Saque()
        self.telaSaque.setupUi(self.stack4)

        self.telaTransfere = Ui_Transfere()
        self.telaTransfere.setupUi(self.stack5)

        self.telaExtrato = Ui_Extrato()
        self.telaExtrato.setupUi(self.stack6)

        self.telaExcluir = Ui_Excluir()
        self.telaExcluir.setupUi(self.stack7)


        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
    


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.conn = database.conectDb()

        self.globalUser = None
        self.globalUserAcc = None


        #navegação
        self.telaLogin.buttonCadatre.clicked.connect(self.cadastre)
        self.telaCadastro.buttonVoltar.clicked.connect(self.voltarLogin)
        self.telaMenu.buttonDepositar.clicked.connect(self.botaoDepositar)
        self.telaMenu.buttonSacar.clicked.connect(self.botaoSacar)
        self.telaDeposito.buttonVoltar.clicked.connect(self.voltarMenu)
        self.telaSaque.buttonVoltar.clicked.connect(self.voltarMenu)
        self.telaTransfere.buttonVoltar.clicked.connect(self.voltarMenu)
        self.telaMenu.buttonSair.clicked.connect(self.voltarLogin)
        self.telaMenu.buttonTransferir.clicked.connect(self.botaoTransferir)
        self.telaMenu.buttonExtrato.clicked.connect(self.botaoExtrato)
        self.telaExtrato.buttonVoltar.clicked.connect(self.voltarMenu)
        self.telaMenu.buttonExcluir.clicked.connect(self.botaoExcluir)

        #funcionalidades
        self.telaCadastro.buttonCadatrar.clicked.connect(self.cadastrar)
        self.telaLogin.buttonEntrar.clicked.connect(self.login)
        self.telaDeposito.buttonDepositar.clicked.connect(self.deposito)
        self.telaSaque.buttonSaque.clicked.connect(self.saque)
        self.telaTransfere.buttonTransferir.clicked.connect(self.transfere)
        self.telaLogin.buttonSair.clicked.connect(self.sair)
        self.telaExcluir.buttonExcluir.clicked.connect(self.excluir)
        self.telaExcluir.buttonVoltar.clicked.connect(self.voltarMenu)
    
#navegação
    def cadastre(self):
        self.telaLogin.lineCpf.setText('')
        self.telaLogin.lineSenha.setText('')
        self.QtStack.setCurrentIndex(1)
    
    def voltarLogin(self):
        self.telaCadastro.lineNome.setText('')
        self.telaCadastro.lineCpf.setText('')
        self.telaCadastro.lineEndereco.setText('')
        self.telaCadastro.lineSenha.setText('')
        self.globalUser = None
        self.globalUserAcc = None
        self.QtStack.setCurrentIndex(0)
    
    def voltarMenu(self):
        self.telaDeposito.lineValor.setText('')
        self.telaSaque.lineValor.setText('')
        self.telaSaque.lineSenha.setText('')
        self.telaTransfere.lineDestino.setText('')
        self.telaTransfere.lineSenha.setText('')
        self.telaTransfere.lineValor.setText('')
        self.telaExtrato.listExtrato.clear()
        self.QtStack.setCurrentIndex(2)

    def botaoDepositar(self):
        self.QtStack.setCurrentIndex(3)

    def botaoSacar(self):
        self.QtStack.setCurrentIndex(4)

    def botaoTransferir(self):
        self.QtStack.setCurrentIndex(5)
    
    def botaoExtrato(self):
        self.QtStack.setCurrentIndex(6)
        historico = self.globalUserAcc.extrato(self.conn)
        for x in historico:
            self.telaExtrato.listExtrato.addItem(str(x))
    
    def botaoExcluir(self):
        self.QtStack.setCurrentIndex(7)




#funcionalidades
    def cadastrar(self):
        nome = self.telaCadastro.lineNome.text()
        cpf = self.telaCadastro.lineCpf.text()
        dt_nascimento = self.telaCadastro.lineData.text()
        endereco = self.telaCadastro.lineEndereco.text()
        senha = self.telaCadastro.lineSenha.text()

        if(nome != '' and cpf != '' and dt_nascimento != '' and endereco != '' and senha != ''):
            senha = hashlib.md5(senha.encode())
            user = Cliente(cpf, nome, dt_nascimento, endereco, str(senha.hexdigest()))
            userAcc = Conta(cpf, 0)
            if(database.insertDb(user, userAcc, self.conn)):
                self.telaCadastro.lineNome.setText('')
                self.telaCadastro.lineCpf.setText('')
                self.telaCadastro.lineEndereco.setText('')
                self.telaCadastro.lineSenha.setText('')
                QMessageBox.information(None, "Bank", "Usauário cadastrado com sucesso!!")

            else:
                QMessageBox.information(None, "Bank", "O CPF informado ja esta cadastrado!!")

        else:
            QMessageBox.information(None, "Bank", "Preencha todos os campos!!")
    

    def login(self):
        cpf = self.telaLogin.lineCpf.text()
        senha = self.telaLogin.lineSenha.text()

        if(cpf != '' and senha != ''):
            p = database.getClienteDb(cpf, self.conn)
            senha = hashlib.md5(senha.encode())
            if(p and senha.hexdigest() == p.senha):
                self.globalUser = p
                self.globalUserAcc = database.getContaDb(self.globalUser.cpf, self.conn)
                self.telaLogin.lineCpf.setText('')
                self.telaLogin.lineSenha.setText('')
                self.telaMenu.userName.setText(self.globalUser.nome)
                self.telaMenu.userSaldo.setText(str(self.globalUserAcc.saldo))
                self.QtStack.setCurrentIndex(2)
            
            else:
                QMessageBox.information(None, "Bank", "Dados invalidos ou usuário não cadastrado!!")
            
        else:
            QMessageBox.information(None, "Bank", "Preencha todos os campos!!")
        
    
    def deposito(self):
        valor = self.telaDeposito.lineValor.text()

        if(valor != ''):
            if(self.globalUserAcc.deposita(float(valor), self.conn)):
                self.telaDeposito.lineValor.setText('')
                self.globalUserAcc = database.getContaDb(self.globalUser.cpf, self.conn)
                self.telaMenu.userSaldo.setText(str(self.globalUserAcc.saldo))
                QMessageBox.information(None, "Bank", "Deposito efetuado!!")

            else:
                QMessageBox.information(None, "Bank", "Valor invalido!!")

        else:
            QMessageBox.information(None, "Bank", "Preencha todos os campos!!")




    def saque(self):
        valor = self.telaSaque.lineValor.text()
        senha = self.telaSaque.lineSenha.text()

        if(valor != '' and senha != ''):
            senha = hashlib.md5(senha.encode())
            if(senha.hexdigest() == self.globalUser.senha):
                if(self.globalUserAcc.saca(float(valor), self.conn)):
                    self.telaSaque.lineValor.setText('')
                    self.telaSaque.lineSenha.setText('')
                    self.globalUserAcc = database.getContaDb(self.globalUser.cpf, self.conn)
                    self.telaMenu.userSaldo.setText(str(self.globalUserAcc.saldo))
                    QMessageBox.information(None, "Bank", "Saque efetuado!!")


                else:
                    QMessageBox.information(None, "Bank", "Saldo insuficiente!!")

            else:
                QMessageBox.information(None, "Bank", "Senha incorreta!!")
                
        else:
            QMessageBox.information(None, "Bank", "Preencha todos os campos!!")
    

    def transfere(self):
        destino = self.telaTransfere.lineDestino.text()
        valor = self.telaTransfere.lineValor.text()
        senha = self.telaTransfere.lineSenha.text()

        if(destino != '' and valor != '' and senha != ''):
            senha = hashlib.md5(senha.encode())
            if(senha.hexdigest() == self.globalUser.senha):
                if(self.globalUserAcc.saldo >= float(valor)):
                    if(self.globalUserAcc.transfere(destino, float(valor), self.conn)):
                        self.telaTransfere.lineDestino.setText('')
                        self.telaTransfere.lineValor.setText('')
                        self.telaTransfere.lineSenha.setText('')
                        self.globalUserAcc = database.getContaDb(self.globalUser.cpf, self.conn)
                        self.telaMenu.userSaldo.setText(str(self.globalUserAcc.saldo))
                        QMessageBox.information(None, "Bank", "Transferência efetuada!!")

                    else:
                        QMessageBox.information(None, "Bank", "Usuário destinado não existe!!")                    

                else:
                    QMessageBox.information(None, "Bank", "Saldo insuficiente!!")

            else:
                QMessageBox.information(None, "Bank", "Senha incorreta!!")

        else:
            QMessageBox.information(None, "Bank", "Preencha todos os campos!!")
    

    def excluir(self):
        cpf = self.telaExcluir.lineCpf.text()
        senha = self.telaExcluir.lineSenha.text()

        if(cpf != '' and senha != ''):
            p = database.getClienteDb(cpf, self.conn)
            senha = hashlib.md5(senha.encode())
            if(p and senha.hexdigest() == p.senha):
                database.deleteDb(self.globalUser.cpf, self.conn)
                self.voltarLogin()
            
            else:
                QMessageBox.information(None, "Bank", "Dados invalidos!!")
            
        else:
            QMessageBox.information(None, "Bank", "Preencha todos os campos!!")
        

    

    def sair(self):
        database.desconectDb(self.conn)
        sys.exit(app.exec_())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    showMain = Main()
    sys.exit(app.exec_())