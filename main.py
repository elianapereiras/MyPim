import json
import os
#from colorama import init, Fore, Style
from autenticacao import autenticar_usuario, cadastrar_usuario
from dados_pessoais import cadastrar_dados
from cadastrar_cursos import cadastrar_cursos

#init(autoreset=True)  # Para resetar a cor após cada print

def menu():
       
    print("="*98)
    #print(Fore.BLUE +"="*29+ " PLATAFORMA DE EDUCAÇÃO DIGITAL SEGURA " +"="*30)
    print("="*98)
    print("1- Fazer Cadastro")
    print("2- Fazer Login")
    print("3- Cadastrar Cursos")
    print("4- Cadastrar módulos dos cursos")
    print("5- Sair")
    print("="*98)

    op=int(input("Digite uma opção (1-5)"))
    return op

def op_1():
    cadastrar_dados()
    
def op_2():
    autenticar_usuario()

def op_3():
    cadastrar_cursos()

     

def salvar(dados):
    with open("cadastro.json", "a", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def carregar_usuarios():    
# carrega o arquivo .json como os usuários e senhas gravadas
      if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r", encoding="utf-8") as arquivo:
            dados=json.load(arquivo)
        return dados
      
      else:
        return []
      
def main():
    op=menu()
    while True:
       if op==1:
           op_1()
       elif op==2:
           op_2()
           


    


if __name__ == "__main__":
    main()