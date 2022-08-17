
# banco de dados 

import sqlite3
from cliente import Cliente
from conta import Conta







def conectDb():
    conn = sqlite3.connect("database.db")
    conn.execute('''CREATE TABLE IF NOT EXISTS CLIENTES
    (CPF           TEXT    PRIMARY KEY   NOT NULL,
    NOME           TEXT    NOT NULL,
    DT_NASCIMENTO  TEXT    NOT NULL,
    ENDERECO       TEXT    NOT NULL,
    SENHA          TEXT    NOT NULL);''')

    conn.execute('''CREATE TABLE IF NOT EXISTS CONTAS
    (CPF           TEXT    PRIMARY KEY   NOT NULL,
    SALDO          REAL   NOT NULL);''')

    return(conn)


def desconectDb(conn):
    conn.close()


def getContaDb(cpf, conn):
    lista = conn.execute("SELECT CPF, SALDO from CONTAS")
    for l in lista:
        if l[0] == cpf:
            return Conta(l[0], l[1])
    return False

def getClienteDb(cpf, conn):
    lista = conn.execute("SELECT CPF, NOME, DT_NASCIMENTO, ENDERECO, SENHA from CLIENTES")
    for l in lista:
        if l[0] == cpf:
            return Cliente(l[0], l[1], l[2], l[3], l[4])
    return False

def insertDb (cliente, conta, conn):
    
    if(getClienteDb(cliente.cpf, conn)):
        return False

    else:
        cur = conn.cursor()
        cur.execute("INSERT into CLIENTES (CPF, NOME, DT_NASCIMENTO, ENDERECO, SENHA) VALUES ('{}','{}','{}','{}','{}')" .format(cliente.cpf, cliente.nome, cliente.dt_nascimento, cliente.endereco, cliente.senha))
        cur.execute("INSERT into CONTAS (CPF, SALDO) VALUES ('{}','{}')" .format(conta.cpf, conta.saldo))
        conn.commit()
        return True


def updateDb (cpf, saldo, conn):
        
    try:
        conn.execute("UPDATE CONTAS set SALDO = '{}' where CPF = '{}'" .format(saldo, cpf))
        conn.commit()
        return True

    except:
        return False


def deleteDb (cpf, conn):
    try:
        conn.execute("DELETE from CLIENTES where CPF = '{}'" .format(cpf))
        conn.execute("DELETE from CONTAS where CPF = '{}'" .format(cpf))
        return True

    except:
        return False