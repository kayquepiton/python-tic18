import json
import os

# Dados dos empregados incorporados diretamente no código
EMPREGADOS_INICIAIS = [
    {
        "nome": "João",
        "sobrenome": "Silva",
        "ano_nascimento": 1990,
        "rg": "123456",
        "ano_admissao": 2020,
        "salario": 7320.50
    },
    {
        "nome": "Maria",
        "sobrenome": "Santos",
        "ano_nascimento": 1985,
        "rg": "789012",
        "ano_admissao": 2018,
        "salario": 8784.60
    }
]

def carregar_dados(nome_arquivo):
    return EMPREGADOS_INICIAIS

def salvar_dados(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=2)

def reajusta_dez_porcento(empregados):
    for empregado in empregados:
        empregado['salario'] *= 1.1

def exibir_empregados(empregados):
    for empregado in empregados:
        print(f"Nome: {empregado['nome']} {empregado['sobrenome']}, Ano Nascimento: {empregado['ano_nascimento']}, RG: {empregado['rg']}, Ano Admissão: {empregado['ano_admissao']}, Salário: R${empregado['salario']:.2f}")

def main():
    print("Diretório Atual:", os.getcwd())
    print("Conteúdo do Diretório:", os.listdir())

    nome_arquivo = os.path.abspath("empregados.json")
    empregados = carregar_dados(nome_arquivo)

    while True:
        print("\n===== Menu de Opções =====")
        print("1. Exibir lista de empregados")
        print("2. Reajustar salários em 10%")
        print("0. Sair do programa")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("\nLista de empregados: ")
            exibir_empregados(empregados)
        elif opcao == '2':
            reajusta_dez_porcento(empregados)
            print("\nSalários reajustados em 10%: ")
            exibir_empregados(empregados)
            salvar_dados(nome_arquivo, empregados)
        elif opcao == '0':
            print("\nPrograma encerrado. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
