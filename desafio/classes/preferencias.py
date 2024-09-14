import os
import json
from datetime import datetime

db = "db.json"
class Preferencias:
    def __init__(self, cor: str, usuario_id: int, modificacoes: dict):
        self.__modificacoes = modificacoes
        self.__cor = cor
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

        dados_preferencias = {
            "Cor": self.__cor,
            "Modificacoes": self.__modificacoes
        }

        for usuario in dados_existentes:
            if usuario.get("ID") == self.__usuario_id and "Nome" in usuario:
                if "Preferencias" not in usuario:
                    usuario["Preferencias"] = []
                usuario["Preferencias"].append(dados_preferencias)
                usuario["Data de Atualizacao"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                break

        with open(db, 'w', encoding='utf-8') as arquivo:
            json.dump(dados_existentes, arquivo, ensure_ascii=False, indent=4)

        print(f"Preferências do usuário {self.__usuario_id} cadastradas com sucesso!")
