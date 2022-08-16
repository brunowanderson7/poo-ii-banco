import database


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
            if(database.updateDb(self.cpf, (self.saldo + valor), conn)):
                self.saldo += valor
                return True

        return False



    def saca(self, valor, conn):
        if(valor > 0 and self.saldo >= valor):
            if(database.updateDb(self.cpf, (self.saldo - valor), conn)):
                self.saldo -= valor
                return True

        return False



    def transfere(self, cpf, valor, conn):
        destino = database.getContaDb(cpf, conn)

        if( destino and valor > 0 and self._saldo >= valor):
            if(database.updateDb(self.cpf, (self.saldo - valor), conn)):
                database.updateDb(destino.cpf, (destino.saldo + valor), conn)
                return True

        return False