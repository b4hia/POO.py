from classes import usuario
from classes import veiculo
from classes import preferencias
from classes import builder
import json

class Sistema:
    def __init__(self):
        self.section = True

    def menu(self):
        print("1 - Cadastrar usuário\n")
        print("2 - Atualizar usuário\n")
        print("3 - Deletar usuário\n")
        print("4 - Cadastrar veículo\n")
        print("5 - Atualizar veículo\n")
        print("6 - Deletar veículo\n")
        print("7 - Cadastrar preferências\n")
        print("8 - Atualizar preferências\n")
        print("9 - Construir carro\n")
        print("0 - Sair\n")

        while self.section:
            escolha = input("Sua escolha: ")
            match escolha:
                case "1":
                    user = usuario.Usuario(
                        input("Nome: "),
                        input("Email: "),
                        input("Endereco: "),
                        input("CPF: "),
                        input("DDD: "),
                        input("Telefone: ")
                    )
                    user.cadastrar()
                case "2":
                    id = input("ID do usuário a ser atualizado: ")
                    mudancas = {}
                    while True:
                        campo = input("Campo a ser atualizado (ou 'sair' para terminar): ")
                        if campo == 'sair':
                            break
                        valor = input(f"Novo valor para {campo}: ")
                        mudancas[campo] = valor
                    user = usuario.Usuario("", "", "", "", "", "")
                    user.atualizar(id, mudancas)
                case "3":
                    id = input("ID do usuário a ser deletado: ")
                    user = usuario.Usuario("", "", "", "", "", "")
                    user.deletar(id)
                case "4":
                    automovel = veiculo.Veiculo(
                        input("Marca: "),
                        input("Modelo: "),
                        input("Ano: "),
                        int(input("ID do usuário: "))
                    )
                    automovel.cadastrar()
                case "5":
                    pass
                    # Implementar lógica de atualização de veículo
                case "6":
                    pass
                    # Implementar lógica de deleção de veículo
                case "7":
                    preferencia = preferencias.Preferencias(
                        input("Cor: "),
                        int(input("ID do usuário: ")),
                        {"Rodas": input("Rodas: "), "Som": input("Som: ")}
                    )
                    preferencia.cadastrar()
                case "8":
                   pass
                   # Implementar lógica de atualização de preferências
                case "9":
                    construtor = builder.Builder()
                    novo_carro = construtor.build(int(input("ID do usuário: ")))
                    if novo_carro:
                        print("Novo carro criado com sucesso:")
                        print(json.dumps(novo_carro, indent=4, ensure_ascii=False))
                case "0":
                    self.section = False
                case _:
                    print("Opção inválida.")


    def sair(self):
        self.section = False


sistema = Sistema()
sistema.menu()