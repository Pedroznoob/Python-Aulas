import os
import random

random = random.random
produtos = ["Mouse", "Teclado", "Monitor"]
valores = [150, 56, 57, 128]
precos = [46.90, 79.30, 22.93, 28.39]

random() * 100


def criar_menu():
    os.system("cls")
    print("""
    ▒█▀▀▀ ▒█▀▀▀█ ▀▀█▀▀ ▒█▀▀▀█ ▒█▀▀█ ▒█░▒█ ▒█▀▀▀ 　 ░█▀▀█ ▒█▀▀█ ▒█▀▀█ 
    ▒█▀▀▀ ░▀▀▀▄▄ ░▒█░░ ▒█░░▒█ ▒█░▒█ ▒█░▒█ ▒█▀▀▀ 　 ▒█▄▄█ ▒█▄▄█ ▒█▄▄█ 
    ▒█▄▄▄ ▒█▄▄▄█ ░▒█░░ ▒█▄▄▄█ ░▀▀█▄ ░▀▄▄▀ ▒█▄▄▄ 　 ▒█░▒█ ▒█░░░ ▒█░░░""")
    print("\nCadastro de produtos\n")
    print("1. Cadastrar produtos")
    print("2. Listar produtos")
    print("3. Ativar produtos")
    print("4. Excluir produtos")
    print("5. Sair\n")


def voltar_ao_menu_principal():
    input("Pressione Enter para Voltar ao menu principal...  ")
    main()


def criar_titulo(titulo):
    os.system("cls")
    print(f"**** {titulo} *****\n")


def cadastrar_produtos():
    criar_titulo("Cadastro de Produtos")
    os.system("cls")
    produto = input("Nome do produto: ")
    produtos.append(produto)
    print()
    print(f"Produto {produto.upper()}, cadastro com sucesso! \n")
    voltar_ao_menu_principal()


def exibir_produtos():
    criar_titulo("Exibir produtos")
    i = 0
    tamanho_vetor = len(produtos)
    print(f"Total de produtos cadastrados: {tamanho_vetor}")
    while i < tamanho_vetor:
        print(produtos[i])
        i = i + 1


    print()
    voltar_ao_menu_principal()


def escolher_opcao():
    try:
        opcao = int(input("\nEscolha uma opção de (1 a 5): "))

        if opcao == 1:
            cadastrar_produtos()
        elif opcao == 2:
            exibir_produtos()
        elif opcao == 3:
            print("Você escolheu 3")
        elif opcao == 4:
            print("Você escolheu 4")
        elif opcao == 5:
            exit()
        else:
            tratar_erro()
    except:
        tratar_erro()


def tratar_erro():
    input("Valor inválido! Pressione Enter para voltar ao menu principal...")
    main()


def main():
    criar_menu()
    escolher_opcao()


if __name__ == "__main__":
    main()
