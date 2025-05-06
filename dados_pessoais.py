import json

ARQUIVO_DADOS = "dados.json"

def gravar_dados(nome, email, celular):
    dados = {"nome": nome, "email": email, "celular": celular}
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    print("Dados pessoais gravados com sucesso.\n")

def cadastrar_dados():
    print("\n=== Cadastro de Dados Pessoais ===")
    nome = input("Nome: ")
    email = input("Email: ")
    celular = input("Celular: ")
    gravar_dados(nome, email, celular)
