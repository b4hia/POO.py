# Suponha que quero criar um carro para cada pessoa e que cada carro tenha uma marca e um modelo.
#Jeito 1 sem aplicar POO:
print('\n==============================\n')
print('\n============JEITO 1===========\n')
carro_carlao = {
    "marca": "Chevrolet",
    "modelo": "Onix"
}
carro_claudio = {
    "marca": "Toyota",
    "modelo": "Corolla"
}
print (f"O {carro_carlao['marca']} {carro_carlao['modelo']} está dirigindo.")
print (f"O {carro_claudio['marca']} {carro_claudio['modelo']} está dirigindo.")



#Jeito 2 sem aplicar POO:
print('\n==============================\n')
print('\n============JEITO 2===========\n')
carro = []
usuario = []
qntd_carro = int(input('Digite a quantidade de carros: '))
carro = [dict(marca=input('Digite a marca do carro: '), modelo=input('Digite o modelo do carro: ')) for i in range(qntd_carro)]
usuario = [dict(nome=input('Digite o nome do usuário: ')) for i in range(qntd_carro)]
lista = list(zip(usuario, carro))
for i in lista:
    print(f"O {i[0]['nome']} está dirigindo o {i[1]['marca']} {i[1]['modelo']}.")


#Jeito 3 aplicando POO:
print('\n==============================\n')
print('\n============JEITO 3===========\n')
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def dirigir(self):
        print(f"O {self.marca} {self.modelo} está dirigindo.")
meu_carro = Carro("Toyota", "Corolla")
meu_carro.dirigir()
print('\n==============================\n')















class Escolha:
    def __init__(self, escolha):
        self.escolha = escolha

    def resposta(self):
        match self.escolha:
            case '1':
                return ':('
            case '2':
                return ':('
            case '3':
                return ':)'
            case '_':
                return print('Digite um número válido.')
sua_resp = Escolha(input('Qual o melhor jeito: 1, 2 ou 3? '))
print(sua_resp.resposta())