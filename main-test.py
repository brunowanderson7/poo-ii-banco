import database


conn = database.conectDb()

user = database.getClienteDb('1', conn)
userAcc = database.getContaDb('2', conn)
print(user)
print(userAcc)