import os
import json
from datetime import datetime

db = "db.json"

class Builder:
    def __init__(self):
        self.__dados = {}

    def build(self, id):
        if os.path.exists(db):
            with open(db, 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()
                if conteudo:
                    dados_existentes = json.loads(conteudo)
                    usuario = next((item for item in dados_existentes if item['ID'] == id), None)
                    if usuario:
                        veiculo = usuario.get('Veiculo', [])[0]
                        preferencias = usuario.get('Preferencias', [])[0]

                        novo_carro = {
                            "Marca": veiculo["Marca"],
                            "Modelo": veiculo["Modelo"],
                            "Ano": veiculo["Ano"],
                            "Cor": preferencias["Cor"],
                            "Modificacoes": preferencias["Modificacoes"]
                        }

                        return novo_carro
                    else:
                        print(f"Usuário com ID {id} não encontrado.")
                        return None
                else:
                    print("O arquivo está vazio.")
                    return None
        else:
            print(f"O arquivo {db} não existe.")
            return None

