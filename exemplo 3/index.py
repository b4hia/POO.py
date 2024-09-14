class Veiculo:
    def __init__(self, tipo):
        self.tipo = tipo

class Bicicleta(Veiculo):
    def __init__(self, tipo, cor):
        super().__init__(tipo)
        self.cor = cor

minha_bike = Bicicleta("Montanha", "Vermelha")
print(minha_bike.tipo)

#====================EXEMPLO SEM SUPER====================
class Bicicleta(Veiculo):
    def __init__(self, tipo, cor):
        # Se não usar super(), a classe base não será inicializada
        self.tipo = tipo  # Isso apenas define o atributo tipo localmente
        self.cor = cor
