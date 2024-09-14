class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        print("Au Au")

class Gato(Animal):
    def fazer_som(self):
        print("Miau")

def emitir_som(animal):
    animal.fazer_som()

emitir_som(Cachorro())
emitir_som(Gato())
