import json
import os

ARQUIVO_USUARIOS = "usuarios.json"
print("Função de login chamada!")

def carregar_usuarios():
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []

def salvar_usuarios(lista):
    with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, indent=4, ensure_ascii=False)

def cadastrar_usuario():
    usuarios = carregar_usuarios()
    print("\n=== Cadastro de Login ===")
    while True:
        nome = input("Usuário: ")
        if any(u["nome"] == nome for u in usuarios):
            print("Nome já existe. Escolha outro.")
        else:
            break
    senha = input("Senha: ")
    usuarios.append({"nome": nome, "senha": senha})
    salvar_usuarios(usuarios)
    print("Usuário cadastrado com sucesso.\n")

def autenticar_usuario():
    usuarios = carregar_usuarios()
    if not usuarios:
        print("Nenhum usuário cadastrado. Redirecionando para o cadastro...")
        cadastrar_usuario()
        return
    print("\n=== Login ===")
    while True:
        nome = input("Usuário: ")
        senha = input("Senha: ")
        if any(u["nome"] == nome and u["senha"] == senha for u in usuarios):
            print("Acesso liberado!\n")
            break
        print("Login ou senha inválidos.")
