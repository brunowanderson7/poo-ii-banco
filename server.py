import socket
import hashlib
import database

from conta import Conta
from cliente import Cliente



#------------------ Menu
def menu (info, connDb):

    asw = []  #mensagem de resposta para o cliente

    if info[0] == 0:
        #encerrar conexão   [8]
        asw.append("exit")
        return asw
        

    user = database.getClienteDb(info[1], connDb)
    userAcc = database.getContaDb(info[1], connDb)



    if info[0] == 1:
        #deposito   [1, cpf, valor]
        
        if(user):
            if(userAcc.deposita(info[2], connDb)):
                asw.append(True)
                userAcc = database.getContaDb(info[1], connDb)
                asw.append(userAcc.saldo)

            
            else:
                asw.append(False)
                asw.append(4)   #erro 4 Valor negativo
        else:
            asw.append(False)
            asw.append(1)   #erro 1 usuário não cadastrado
        
    
    elif info[0] == 2:
        #saque  [2, cpf, senha, valor]

        if(user):
            senha = hashlib.md5(info[2].encode())

            if(senha.hexdigest() == user.senha):
                if(userAcc.saca(info[3], connDb)):
                    asw.append(True)
                    userAcc = database.getContaDb(info[1], connDb)
                    asw.append(userAcc.saldo)

                else:
                    asw.append(False)
                    asw.append(3)   #erro 3 saldo insuficiente

            else:
                asw.append(False)
                asw.append(2)   #erro 2 senha incorreta
        
        else:
            asw.append(False)
            asw.append(1)   #erro 1 usuário não cadastrado
            
    
    elif info[0] == 3:
        #transferência  [3, cpf, senha, valor, destino]
        if(user):
            acc = database.getContaDb(info[4], connDb)

            if(acc):
                senha = hashlib.md5(info[2].encode())

                if(senha.hexdigest() == user.senha):

                    if(userAcc.transfere(acc.cpf, float(info[3]), connDb)):
                        asw.append(True)
                        userAcc = database.getContaDb(info[1], connDb)
                        asw.append(userAcc.saldo)
                    
                    else:
                        asw.append(False)
                        asw.append(4)   #erro 4 Valor negativo


                else:
                    asw.append(False)
                    asw.append(2)   #erro 2 senha incorreta

            else:
                asw.append(False)
                asw.append(5)   #erro 5 Usuário destino não existe
        
        else:
            asw.append(False)
            asw.append(1)   #erro 1 usuário não cadastrado
    

    elif info[0] == 4:
        #extrato    [4, cpf]
        historico = userAcc.extrato(connDb)
        for x in historico:
            asw.append(x)
        
    
    elif info[0] == 5:
        #exluir     [5, cpf, senha]
        if(user):
            senha = hashlib.md5(info[2].encode())

            if(senha.hexdigest() == user.senha):
                database.deleteDb(info[1], connDb)
                asw.append(True)

            else:
                asw.append(False)
                asw.append(2)   #erro 2 senha incorreta
        else:
            asw.append(False)
            asw.append(1)   #erro 1 usuário não cadastrado


        
        
    
    elif info[0] == 6:
        #login      [6, cpf, senha]
        senha = hashlib.md5(info[2].encode())

        if(user and senha.hexdigest() == user.senha):
            asw.append(True)
            asw.append(user.nome)
            asw.append(user.cpf)
            asw.append(userAcc.saldo)
        
        else:
            asw.append(False)
            asw.append(2)   #erro 2 senha incorreta
    
    elif info[0] == 7:
        #cadastro   [7, cpf, senha, nome, endereco, data]
        senha = hashlib.md5(info[2].encode())
        user = Cliente(info[1], info[3], info[5], info[4], senha.hexdigest())
        userAcc = Conta(info[1], 0)

        if(database.insertDb(user, userAcc, connDb)):
            asw.append(True)
        
        else:
            asw.append(False)
            asw.append(6)   #erro 6 problema de conexão com database


    return asw
#------------------ Menu


ip = 'localhost'
port = 8000
addr = ((ip, port))

connDb = database.conectDb()



serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(addr)
serverSocket.listen(6)
print("Aguardando conexão...")

conn, clientt = serverSocket.accept()
print("Conexão estabelecida!!")
print("Aguardando Mensagem...")



while True:
    try:
        info = conn.recv(1024).decode()     #recebe menssagem do cliente
        asw = menu(eval(info), connDb)    #converção de string para lista na chamada da função


        if asw[0] == 'exit':
            database.desconectDb(connDb)
            serverSocket.close()
            break
        else:
            conn.send(str(asw).encode())     #envira resposta para o cliente
            asw = []

    
    except:
        database.desconectDb(connDb)
        serverSocket.close()
        print("Erro de comunicação!!")
        break
