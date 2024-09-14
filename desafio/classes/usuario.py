from datetime import datetime
import json
import os

db = "db.json"

class Usuario:
    def __init__(self, nome, email, endereco, cpf, ddd, telefone):
        self.__nome = nome
        self.__email = email
        self.__endereco = endereco
        self.__cpf = cpf
        self.__ddd = ddd
        self.__telefone = telefone

    def cadastrar(self):
        if os.path.exists(db):
            with open(db, 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()
                if conteudo:
                    dados_existentes = json.loads(conteudo)
                    max_id = max(item['ID'] for item in dados_existentes) if dados_existentes else 0
                else:
                    dados_existentes = []
                    max_id = 0
        else:
            dados_existentes = []
            max_id = 0

        dados = {
            "ID": max_id + 1,
            "Nome": self.__nome,
            "Email": self.__email,
            "Endereco": self.__endereco,
            "CPF": self.__cpf,
            "DDD": self.__ddd,
            "Telefone": self.__telefone,
            "Preferencias": [],
            "Veiculo": [],
            "Data de Cadastro": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "Data de Atualizacao": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        dados_existentes.append(dados)

        with open(db, 'w', encoding='utf-8') as arquivo:
            json.dump(dados_existentes, arquivo, ensure_ascii=False, indent=4)

        print(f"Usuário {self.__nome} cadastrado com sucesso!")

    def atualizar(self, id, mudancas):
        id = int(id)  
        if os.path.exists(db):
            with open(db, 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()
                if conteudo:
                    dados_existentes = json.loads(conteudo)
                else:
                    dados_existentes = []
            for item in dados_existentes:
                if item['ID'] == id:
                    for key, value in mudancas.items():
                        item[key] = value
                    item['Data de Atualizacao'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    break
            with open(db, 'w', encoding='utf-8') as arquivo:
                json.dump(dados_existentes, arquivo, ensure_ascii=False, indent=4)
            print(f"Usuário {id} atualizado com sucesso!")
        else:
            print("Banco de dados não encontrado.")

    def deletar(self, id):
        id = int(id)  
        if os.path.exists(db):
            with open(db, 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()
                if conteudo:
                    dados_existentes = json.loads(conteudo)
                else:
                    dados_existentes = []
            dados_existentes = [item for item in dados_existentes if item['ID'] != id]
            with open(db, 'w', encoding='utf-8') as arquivo:
                json.dump(dados_existentes, arquivo, ensure_ascii=False, indent=4)
            print(f"Usuário {id} deletado com sucesso!")
        else:
            print("Banco de dados não encontrado.")