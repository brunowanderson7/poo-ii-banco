class Cliente:

	__slots__ = ['_cpf', '_nome', '_dt_nascimento', '_endereco', '_senha']



	def __init__(self, cpf, nome, dt_nascimento, endereco, senha):
		self._cpf = cpf
		self._nome = nome
		self._dt_nascimento = dt_nascimento
		self._endereco = endereco
		self._senha = senha



	@property
	def cpf(self):
		return self._cpf

	@property
	def nome(self):
		return self._nome

	@nome.setter
	def nome(self, nome):
		self._nome = nome


	@property
	def dt_nascimento(self):
		return self._dt_nascimento

	
	@property
	def endereco(self):
		return self._endereco
	
	@endereco.setter
	def endereco(self, endereco):
		self._endereco = endereco


	@property
	def senha(self):
		return self._senha

	@senha.setter
	def senha(self, senha):
		self._senha = senha