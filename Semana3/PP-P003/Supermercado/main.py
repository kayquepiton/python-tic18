import os

def inserir_produto(produtos):
    codigo = input("\nDigite o código do produto (13 caracteres): ")
    while len(codigo) != 13:
        print("Código inválido. Deve conter exatamente 13 caracteres.")
        codigo = input("Digite o código do produto (13 caracteres): ")

    nome = input("Digite o nome do produto: ")
    while not nome or not nome[0].isupper():
        print("O nome do produto deve começar com uma letra maiúscula.")
        nome = input("Digite o nome do produto: ")

    preco = input("Digite o preço do produto: ")
    while not preco.replace('.', '', 1).isdigit():
        print("Preço inválido. Digite um valor numérico válido.")
        preco = input("Digite o preço do produto: ")

    produto = {'codigo': codigo, 'nome': nome, 'preco': float(preco)}
    produtos.append(produto)
    print("\nProduto cadastrado com sucesso!")

def excluir_produto(produtos):
    codigo_para_excluir = input("\nDigite o código do produto a ser excluído: ")
    for produto in produtos:
        if produto['codigo'] == codigo_para_excluir:
            produtos.remove(produto)
            print("\nProduto excluído com sucesso!")
            return
    print("Produto não encontrado.")

def listar_produtos(produtos):
    for i, produto in enumerate(produtos):
        print(f"{i + 1}. Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}")
        if (i + 1) % 10 == 0 and (i + 1) != len(produtos):
            input("Pressione Enter para ver mais produtos...")

def consultar_preco(produtos):
    codigo_para_consultar = input("\nDigite o código do produto para consultar o preço: ")
    for produto in produtos:
        if produto['codigo'] == codigo_para_consultar:
            print(f"O preço do produto {produto['nome']} é R${produto['preco']:.2f}")
            return
    print("Produto não encontrado.")

def principal():
    produtos = []

    while True:
        print("\n===== Menu de Opções =====")
        print("1. Inserir novo produto")
        print("2. Excluir produto cadastrado")
        print("3. Listar todos os produtos")
        print("4. Consultar preço de um produto")
        print("0. Sair do programa")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            inserir_produto(produtos)
        elif opcao == '2':
            excluir_produto(produtos)
        elif opcao == '3':
            listar_produtos(produtos)
        elif opcao == '4':
            consultar_preco(produtos)
        elif opcao == '0':
            print("\nPrograma encerrado. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    principal()
