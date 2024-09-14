import json
import os
from datetime import datetime

db = "db.json"

class Veiculo:
    def __init__(self, marca, modelo, ano, usuario_id):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__usuario_id = usuario_id

    def cadastrar(self):
        if os.path.exists(db):
            with open(db, 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()
                if conteudo:
                    dados_existentes = json.loads(conteudo)
                    max_id = max(item['ID'] for item in dados_existentes if 'ID' in item)
                else:
                    dados_existentes = []
                    max_id = 0
        else:
            dados_existentes = []
            max_id = 0

        dados_veiculo = {
            "Marca": self.__marca,
            "Modelo": self.__modelo,
            "Ano": self.__ano,
        }

        for usuario in dados_existentes:
            if usuario.get("ID") == self.__usuario_id and "Nome" in usuario:
                if "Veiculo" not in usuario:
                    usuario["Veiculo"] = []
                usuario["Veiculo"].append(dados_veiculo)
                usuario["Data de Atualizacao"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                break

        with open(db, 'w', encoding='utf-8') as arquivo:
            json.dump(dados_existentes, arquivo, ensure_ascii=False, indent=4)

        print(f"Veículo {self.__marca} {self.__modelo} {self.__ano} cadastrado com sucesso!")
