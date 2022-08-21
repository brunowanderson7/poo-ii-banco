import database
import datetime


class Conta:

    __slots__ = ['_cpf', '_saldo']

    def __init__(self, cpf, saldo):
        self._cpf = cpf
        self._saldo = float(saldo)



    @property
    def cpf(self):
        return self._cpf


    @property
    def saldo(self):
        return self._saldo


    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo



    def deposita(self, valor, conn):
        if(valor > 0):
            registro = ("Deposito efetuado: Valor [R$: {}], Data[{}]" .format(valor, datetime.datetime.now()))
            if(database.updateDb(self.cpf, (self.saldo + valor), registro, conn)):
                self.saldo += valor
                return True

        return False



    def saca(self, valor, conn):
        if(valor > 0 and self.saldo >= valor):
            registro = ("Saque efetuado: Valor [R$: {}], Data[{}]" .format(valor, datetime.datetime.now()))
            if(database.updateDb(self.cpf, (self.saldo - valor), registro, conn)):
                self.saldo -= valor
                return True

        return False



    def transfere(self, cpf, valor, conn):
        destino = database.getContaDb(cpf, conn)

        if( destino and valor > 0 and self._saldo >= valor):
            registro = ("Transferência efetuada: CPF Destinatario [{}], Valor [R$: {}], Data[{}]" .format(cpf, valor, datetime.datetime.now()))
            if(database.updateDb(self.cpf, (self.saldo - valor), registro, conn)):
                registro = ("Transferência recebida: CPF Origem [{}], Valor [R$: {}], Data[{}]" .format(self.cpf, valor, datetime.datetime.now()))
                database.updateDb(destino.cpf, (destino.saldo + valor), registro, conn)
                return True

        return False
    


    def extrato(self, conn):
        registro = ("Tirou extrato: Data[{}]" .format(datetime.datetime.now()))
        return database.getHistoricoDb(self.cpf, registro, conn)