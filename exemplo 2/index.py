#=============PUBLICO================
class Pessoa:
    def __init__(self, nome):
        self.nome = nome  # Público

    def dizer_ola(self):
        print(f"Olá, meu nome é {self.nome}.")

p = Pessoa("Ana")
print(p.nome, 'este é um atributo acessível')  # Acessível
p.dizer_ola()



#=============PROTEGIDO================
class PessoaProtegido:
    def __init__(self, nome):
        self._nome = nome  # Protegido

    def _dizer_ola(self):
        print(f"Olá, meu nome é {self._nome}.")

p = PessoaProtegido("Ana")
print(p._nome, 'este é um atributo acessível porém não é o ideal') # Acessível, mas não ideal
p._dizer_ola()



#=============PRIVADO================
class PessoaPrivado:
    def __init__(self, nome):
        self.__nome = nome  # Privado

    def __dizer_ola(self):
        print(f"Olá, meu nome é {self.__nome}.")
    
    def falar(self):
        self.__dizer_ola()

p = PessoaPrivado("Ana")
# print(p.__nome)  # Levanta um erro: AttributeError #Descomente para ver o erro
p.falar()  # Correto uso do método privado


class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor

    def obter_saldo(self):
        return self.__saldo

# Uso
conta = ContaBancaria(1000)
conta.depositar(500)
conta.sacar(200)
# print(conta.__saldo)
print(conta.obter_saldo())  # 1300
