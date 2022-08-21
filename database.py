
# banco de dados 

import datetime
import mysql.connector
from mysql.connector import Error
from cliente import Cliente
from conta import Conta







def conectDb():
    conn = mysql.connector.connect(host='localhost',user='root',password='@Pass12%',database='bank')
    return(conn)


def desconectDb(conn):
    conn.close()


def getContaDb(cpf, conn):
    
    try:
        cursor = conn.cursor(buffered = True)
        cursor.execute("SELECT * from CONTAS where CPF = '{}'" .format(cpf))
        userAcc = cursor.fetchall()
        cursor.close()
        if userAcc:
            userAcc = userAcc[0]
            return Conta(userAcc[0], userAcc[1])

    except Error as e:
        print("Erro ao acessar tabela MySQL", e)

    return False



def getClienteDb(cpf, conn):

    try:
        cursor = conn.cursor(buffered = True)
        cursor.execute("SELECT * from CLIENTES where CPF = '{}'" .format(cpf))
        user = cursor.fetchall()
        cursor.close()
        if user:
            user = user[0]
            return Cliente(user[0], user[1], user[2], user[3], user[4])

    except Error as e:
        print("Erro ao acessar tabela MySQL", e)
    
    return False



def getHistoricoDb(cpf, registro, conn):

    try:
        cursor = conn.cursor(buffered = True)
        name = ("HISTORICO{}" .format(cpf))
        cursor.execute("SELECT INFO from {}" .format(name))
        historico = cursor.fetchall()
        cursor.execute("INSERT into {} (INFO) VALUES ('{}')" .format(name, registro))
        conn.commit()
        cursor.close()
        if historico:
            return (historico)

    except Error as e:
        print("Erro ao acessar tabela MySQL", e)
    
    return False
    


def insertDb (cliente, conta, conn):
    
    if(getClienteDb(cliente.cpf, conn)):
        return False

    else:
        cursor = conn.cursor()
        cursor.execute("INSERT into CLIENTES (CPF, NOME, DT_NASCIMENTO, ENDERECO, SENHA) VALUES ('{}','{}','{}','{}','{}')" .format(cliente.cpf, cliente.nome, cliente.dt_nascimento, cliente.endereco, cliente.senha))
        cursor.execute("INSERT into CONTAS (CPF, SALDO) VALUES ('{}','{}')" .format(conta.cpf, conta.saldo))
        
        name = ("HISTORICO{}" .format(conta.cpf))
        cursor.execute("CREATE TABLE {} (ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT, INFO TEXT NOT NULL)" .format(name))

        registro = ("Conta criada: {}" .format(datetime.datetime.now()))
        cursor.execute("INSERT into {} (INFO) VALUES ('{}')" .format(name, registro))


        conn.commit()
        cursor.close()
        return True



def updateDb (cpf, saldo, registro, conn):
        
    try:
        cursor = conn.cursor()
        name = ("HISTORICO{}" .format(cpf))
        cursor.execute("UPDATE CONTAS set SALDO = '{}' where CPF = '{}'" .format(saldo, cpf))
        cursor.execute("INSERT into {} (INFO) VALUES ('{}')" .format(name, registro))
        conn.commit()
        cursor.close()
        return True

    except:
        return False



def deleteDb (cpf, conn):
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE from CLIENTES where CPF = '{}'" .format(cpf))
        cursor.execute("DELETE from CONTAS where CPF = '{}'" .format(cpf))

        name = ("HISTORICO{}" .format(cpf))
        cursor.execute("DROP TABLE {}" .format(name))
        conn.commit()
        cursor.close()
        return True

    except:
        return False