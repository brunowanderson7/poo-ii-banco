import hashlib
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtWidgets

from telaCadastro import Ui_TelaCadastro as Ui_Cadastro
from telaDepositar import Ui_MainWindow as Ui_Deposito
from telaLogin import Ui_MainWindow as Ui_Login
from telaMenu import Ui_MainWindow as Ui_Menu
from telaSacar import Ui_MainWindow as Ui_Saque
from telaTransferir import Ui_MainWindow as Ui_Transfere
from telaUsuario import Ui_MainWindow as Ui_Usuario

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

        self.TelaTransfere = Ui_Transfere()
        self.TelaTransfere.setupUi(self.stack5)

        self.telaUsuario = Ui_Usuario()
        self.telaUsuario.setupUi(self.stack6)


        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
    


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.conn = database.conectDb()

        self.globalUser = None
        self.globalUserAcc = None


        #navegação
        self.telaLogin.buttonCadastre.clicked.connect(self.cadastre)
        self.telaCadastro.buttonVoltar.clicked.connect(self.voltarLogin)
        self.telaMenu.buttonDepositar.clicked.connect(self.botaoDepositar)
        self.telaMenu.buttonSacar.clicked.connect(self.botaoSacar)
        self.telaDeposito.buttonVoltar.clicked.connect(self.voltarMenu)
        self.telaSaque.buttonVoltar.clicked.connect(self.voltarMenu)
        self.TelaTransfere.buttonVoltar.clicked.connect(self.voltarMenu)
        self.telaUsuario.buttonVoltar.clicked.connect(self.voltarMenu)
        self.telaMenu.buttonVoltar_5.clicked.connect(self.voltarLogin)
        self.telaMenu.buttonTransferir.clicked.connect(self.botaoTransferir)
        self.telaMenu.buttonUsuario.clicked.connect(self.botaoUsuario)

        #funcionalidades
        self.telaCadastro.buttonCadastrar.clicked.connect(self.cadastrar)
        self.telaLogin.buttonVoltar.clicked.connect(self.login)
        self.telaDeposito.buttonDepositar.clicked.connect(self.deposito)
        self.telaSaque.buttonCadastrar.clicked.connect(self.saque)
        self.TelaTransfere.buttonTransferir.clicked.connect(self.transfere)
        self.telaUsuario.buttonCadastrar.clicked.connect(self.exibir)
        self.telaLogin.buttonSair.clicked.connect(self.sair)
    
#navegação
    def cadastre(self):
        self.telaLogin.lineCpf.setText('')
        self.telaLogin.lineSenha.setText('')
        self.QtStack.setCurrentIndex(1)
    
    def voltarLogin(self):
        self.telaCadastro.lineNome.setText('')
        self.telaCadastro.lineCpf.setText('')
        self.telaCadastro.lineData.setText('')
        self.telaCadastro.lineEndereco.setText('')
        self.telaCadastro.lineSenha.setText('')
        self.globalUser = None
        self.globalUserAcc = None
        self.QtStack.setCurrentIndex(0)
    
    def voltarMenu(self):
        self.telaDeposito.lineSenha.setText('')
        self.telaSaque.lineValor.setText('')
        self.telaSaque.lineSenha.setText('')
        self.TelaTransfere.lineDestino.setText('')
        self.TelaTransfere.lineSenha.setText('')
        self.TelaTransfere.lineValor.setText('')
        self.telaUsuario.lineSenha.setText('*****')
        self.QtStack.setCurrentIndex(2)

    def botaoDepositar(self):
        self.QtStack.setCurrentIndex(3)

    def botaoSacar(self):
        self.QtStack.setCurrentIndex(4)

    def botaoTransferir(self):
        self.QtStack.setCurrentIndex(5)
    
    def botaoUsuario(self):
        self.telaUsuario.lineCpf.setText(self.globalUser.cpf)
        self.telaUsuario.lineNome.setText(self.globalUser.nome)
        self.telaUsuario.lineEndereco.setText(self.globalUser.endereco)
        self.telaUsuario.lineData.setText(self.globalUser.dt_nascimento)
        self.telaUsuario.lineSenha.setText('*****')
        self.QtStack.setCurrentIndex(6)




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
                self.telaCadastro.lineData.setText('')
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
                self.telaMenu.slotSaldo.setText(str(self.globalUserAcc.saldo))
                self.QtStack.setCurrentIndex(2)
            
            else:
                QMessageBox.information(None, "Bank", "Dados invalidos ou usuário não cadastrado!!")
            
        else:
            QMessageBox.information(None, "Bank", "Preencha todos os campos!!")
        
    
    def deposito(self):
        valor = self.telaDeposito.lineSenha.text()

        if(valor != ''):
            if(self.globalUserAcc.deposita(float(valor), self.conn)):
                self.telaDeposito.lineSenha.setText('')
                self.globalUserAcc = database.getContaDb(self.globalUser.cpf, self.conn)
                self.telaMenu.slotSaldo.setText(str(self.globalUserAcc.saldo))
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
                    self.telaMenu.slotSaldo.setText(str(self.globalUserAcc.saldo))
                    QMessageBox.information(None, "Bank", "Saque efetuado!!")


                else:
                    QMessageBox.information(None, "Bank", "Saldo insuficiente!!")

            else:
                QMessageBox.information(None, "Bank", "Senha incorreta!!")
                
        else:
            QMessageBox.information(None, "Bank", "Preencha todos os campos!!")
    

    def transfere(self):
        destino = self.TelaTransfere.lineDestino.text()
        valor = self.TelaTransfere.lineValor.text()
        senha = self.TelaTransfere.lineSenha.text()

        if(destino != '' and valor != '' and senha != ''):
            senha = hashlib.md5(senha.encode())
            if(senha.hexdigest() == self.globalUser.senha):
                if(self.globalUserAcc.saldo >= float(valor)):
                    if(self.globalUserAcc.transfere(destino, float(valor), self.conn)):
                        self.TelaTransfere.lineDestino.setText('')
                        self.TelaTransfere.lineValor.setText('')
                        self.TelaTransfere.lineSenha.setText('')
                        self.globalUserAcc = database.getContaDb(self.globalUser.cpf, self.conn)
                        self.telaMenu.slotSaldo.setText(str(self.globalUserAcc.saldo))
                        QMessageBox.information(None, "Bank", "Transferência efetuada!!")

                    else:
                        QMessageBox.information(None, "Bank", "Usuário destinado não existe!!")                    

                else:
                    QMessageBox.information(None, "Bank", "Saldo insuficiente!!")

            else:
                QMessageBox.information(None, "Bank", "Senha incorreta!!")

        else:
            QMessageBox.information(None, "Bank", "Preencha todos os campos!!")
    

    def exibir(self):
        x = self.telaUsuario.lineSenha.text()
        if(x == '*****'):
            self.telaUsuario.lineSenha.setText(self.globalUser.senha)
        else:
            self.telaUsuario.lineSenha.setText('*****')

    

    def sair(self):
        database.desconectDb(self.conn)
        sys.exit(app.exec_())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    showMain = Main()
    sys.exit(app.exec_())