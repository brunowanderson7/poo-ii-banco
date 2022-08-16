import database
from conta import Conta
from cliente import Cliente



conn = database.conectDb()

c1 = database.getContaDb('4335', conn)
p2 = Cliente('4545', 'vão', '4521', 'mercúrio', 'ovo')



print(c1.transfere(p2.cpf, 70, conn))


database.desconectDb(conn)