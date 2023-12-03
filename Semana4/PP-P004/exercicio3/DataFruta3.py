from abc import ABC, abstractmethod

class Data:
    def __init__(self, dia=1, mes=1, ano=1900):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 1900 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, dia):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        if ano < 1900 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano
    
    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return  self.__dia == outraData.__dia and \
                self.__mes == outraData.__mes and \
                self.__ano == outraData.__ano
    
    def __lt__(self, outraData):
        if self.__ano < outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes < outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                return self.__dia < outraData.__dia
        return False
    
    def __gt__(self, outraData):
        if self.__ano > outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes > outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                return self.__dia > outraData.__dia
        return False


class AnaliseDados(ABC):
    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMediana(self):
        pass
    
    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass
    
    @abstractmethod
    def listarEmOrdem(self):
        pass

class ListaNomes(AnaliseDados):
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []        

    def entradaDeDados(self):
        while True:
            try:
                qtd_elementos = int(input("Quantos nomes deseja inserir na lista? "))
                if qtd_elementos > 0:
                    break
                else:
                    print("Por favor, insira um número maior que 0.")
            except ValueError:
                print("Por favor, insira um número inteiro válido.\n")

        for _ in range(qtd_elementos):
            nome = input("Digite um nome: ")
            self.__lista.append(nome)

    def mostraMediana(self):
        self.__lista.sort()
        meio = len(self.__lista) // 2
        print("\nMediana:", self.__lista[meio])

    def mostraMenor(self):
        print("Menor:", min(self.__lista))

    def mostraMaior(self):
        print("Maior:", max(self.__lista))
        
    def listarEmOrdem(self):
        print("\nNomes ordenados:")
        for nome in sorted(self.__lista):
            print(nome)

    def __str__(self):
        return str(self.__lista)


class ListaDatas(AnaliseDados):
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []        
    
    def entradaDeDados(self):
        while True:
            try:
                qtd_elementos = int(input("Quantas datas deseja inserir na lista? "))
                if qtd_elementos > 0:
                    break
                else:
                    print("Por favor, insira um número maior que 0.")
            except ValueError:
                print("Por favor, insira um número inteiro válido.\n")

        for _ in range(qtd_elementos):
            while True:
                try:
                    dia = int(input("Dia: "))
                    if 1 <= dia <= 31:
                        break
                    else:
                        print("Dia inválido. Digite um valor entre 1 e 31.")
                except ValueError:
                    print("Por favor, insira um número inteiro válido para o dia.\n")

            while True:
                try:
                    mes = int(input("Mês: "))
                    if 1 <= mes <= 12:
                        break
                    else:
                        print("Mês inválido. Digite um valor entre 1 e 12.")
                except ValueError:
                    print("Por favor, insira um número inteiro válido para o mês.\n")

            while True:
                try:
                    ano = int(input("Ano: "))
                    if 1900 <= ano <= 2100:
                        break
                    else:
                        print("Ano inválido. Digite um valor entre 1900 e 2100.")
                except ValueError:
                    print("Por favor, insira um número inteiro válido para o ano.\n")

            data = Data(dia, mes, ano)
            self.__lista.append(data)

    def mostraMediana(self):
        if not self.__lista:
            print("A lista de datas está vazia. Não é possível calcular a mediana.")
            return

        self.__lista.sort(key=lambda x: (x.ano, x.mes, x.dia))
        meio = len(self.__lista) // 2
        print("\nMediana:", self.__lista[meio])

    def mostraMenor(self):
        if not self.__lista:
            print("A lista de datas está vazia.")
            return

        print("Menor:", min(self.__lista))

    def mostraMaior(self):
        if not self.__lista:
            print("A lista de datas está vazia.")
            return

        print("Maior:", max(self.__lista))
        
    def listarEmOrdem(self):
        print("\nDatas ordenadas:")
        for data in sorted(self.__lista, key=lambda x: (x.ano, x.mes, x.dia)):
            print(data)
            
    def filtrarDatasAnteriores2019(self):
        self.__lista = [data for data in self.__lista if data < Data(dia=1, mes=1, ano=2019)]


    def __str__(self):
        return "\n".join(map(str, self.__lista))


class ListaSalarios(AnaliseDados):
    def __init__(self):
        super().__init__(type(float))
        self.__lista = []        

    def entradaDeDados(self):
        while True:
            try:
                qtd_elementos = int(input("Quantos salários deseja inserir na lista? "))
                if qtd_elementos > 0:
                    break
                else:
                    print("Por favor, insira um número maior que 0.")
            except ValueError:
                print("Por favor, insira um número inteiro válido.\n")

        for _ in range(qtd_elementos):
            while True:
                try:
                    salario = input("Digite um salário: ")
                    salario = float(salario)
                    break
                except ValueError:
                    print("Por favor, insira um valor numérico válido para o salário.\n")

            self.__lista.append(salario)

    def mostraMediana(self):
        if not self.__lista:
            print("A lista de salários está vazia. Não é possível calcular a mediana.")
            return

        self.__lista.sort()
        meio = len(self.__lista) // 2
        print("\nMediana:", self.__lista[meio])

    def mostraMenor(self):
        if not self.__lista:
            print("A lista de salários está vazia.")
            return

        print("Menor:", min(self.__lista))

    def mostraMaior(self):
        if not self.__lista:
            print("A lista de salários está vazia.")
            return

        print("Maior:", max(self.__lista))
    
    def listarEmOrdem(self):
        print("\nSalários ordenados:")
        for salario in sorted(self.__lista):
            print("{:.2f}".format(salario)) 
            
    def reajusteSalarios(self, percentual):
        self.__lista = list(map(lambda x: x * (1 + percentual / 100), self.__lista))

    def __str__(self):
        return str(self.__lista)


class ListaIdades(AnaliseDados):
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []        

    def entradaDeDados(self):
        while True:
            try:
                qtd_elementos = int(input("Quantas idades deseja inserir na lista? "))
                if qtd_elementos > 0:
                    break
                else:
                    print("Por favor, insira um número maior que 0.")
            except ValueError:
                print("Por favor, insira um número inteiro válido.\n")

        for _ in range(qtd_elementos):
            while True:
                try:
                    idade = input("Digite uma idade: ")
                    idade = int(idade)
                    break
                except ValueError:
                    print("Por favor, insira um valor numérico válido para a idade.\n")

            self.__lista.append(idade)

    def mostraMediana(self):
        if not self.__lista:
            print("A lista de idades está vazia. Não é possível calcular a mediana.")
            return

        self.__lista.sort()
        meio = len(self.__lista) // 2
        print("\nMediana:", self.__lista[meio])

    def mostraMenor(self):
        if not self.__lista:
            print("A lista de idades está vazia.")
            return

        print("Menor:", min(self.__lista))

    def mostraMaior(self):
        if not self.__lista:
            print("A lista de idades está vazia.")
            return

        print("Maior:", max(self.__lista))

    def listarEmOrdem(self):
        print("\nIdades:")
        for idade in self.__lista:
            print(idade)

    def __str__(self):
        return str(self.__lista)


def exibir_menu():
    print("\nMenu de Opções:")
    print("1. Incluir um nome na lista de nomes")
    print("2. Incluir um salário na lista de salários")
    print("3. Incluir uma data na lista de datas")
    print("4. Incluir uma idade na lista de idades")
    print("5. Percorrer as listas de nomes e salários")
    print("6. Calcular o valor da folha com um reajuste de 10%")
    print("7. Modificar o dia das datas anteriores a 2019")
    print("8. Sair")

from abc import ABC, abstractmethod

class Data:
    def __init__(self, dia=1, mes=1, ano=1900):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 1900 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, dia):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        if ano < 1900 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano
    
    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return  self.__dia == outraData.__dia and \
                self.__mes == outraData.__mes and \
                self.__ano == outraData.__ano
    
    def __lt__(self, outraData):
        if self.__ano < outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes < outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                return self.__dia < outraData.__dia
        return False
    
    def __gt__(self, outraData):
        if self.__ano > outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes > outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                return self.__dia > outraData.__dia
        return False


class AnaliseDados(ABC):
    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMediana(self):
        pass
    
    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass
    
    @abstractmethod
    def listarEmOrdem(self):
        pass

class ListaNomes(AnaliseDados):
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []        

    def entradaDeDados(self):
        while True:
            try:
                qtd_elementos = int(input("Quantos nomes deseja inserir na lista? "))
                if qtd_elementos > 0:
                    break
                else:
                    print("Por favor, insira um número maior que 0.")
            except ValueError:
                print("Por favor, insira um número inteiro válido.\n")

        for _ in range(qtd_elementos):
            nome = input("Digite um nome: ")
            self.__lista.append(nome)

    def mostraMediana(self):
        self.__lista.sort()
        meio = len(self.__lista) // 2
        print("\nMediana:", self.__lista[meio])

    def mostraMenor(self):
        print("Menor:", min(self.__lista))

    def mostraMaior(self):
        print("Maior:", max(self.__lista))
        
    def listarEmOrdem(self):
        print("\nNomes ordenados:")
        for nome in sorted(self.__lista):
            print(nome)

    def __str__(self):
        return str(self.__lista)


class ListaDatas(AnaliseDados):
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []        
    
    def entradaDeDados(self):
        while True:
            try:
                qtd_elementos = int(input("Quantas datas deseja inserir na lista? "))
                if qtd_elementos > 0:
                    break
                else:
                    print("Por favor, insira um número maior que 0.")
            except ValueError:
                print("Por favor, insira um número inteiro válido.\n")

        for _ in range(qtd_elementos):
            while True:
                try:
                    dia = int(input("Dia: "))
                    if 1 <= dia <= 31:
                        break
                    else:
                        print("Dia inválido. Digite um valor entre 1 e 31.")
                except ValueError:
                    print("Por favor, insira um número inteiro válido para o dia.\n")

            while True:
                try:
                    mes = int(input("Mês: "))
                    if 1 <= mes <= 12:
                        break
                    else:
                        print("Mês inválido. Digite um valor entre 1 e 12.")
                except ValueError:
                    print("Por favor, insira um número inteiro válido para o mês.\n")

            while True:
                try:
                    ano = int(input("Ano: "))
                    if 1900 <= ano <= 2100:
                        break
                    else:
                        print("Ano inválido. Digite um valor entre 1900 e 2100.")
                except ValueError:
                    print("Por favor, insira um número inteiro válido para o ano.\n")

            data = Data(dia, mes, ano)
            self.__lista.append(data)

    def mostraMediana(self):
        if not self.__lista:
            print("A lista de datas está vazia. Não é possível calcular a mediana.")
            return

        self.__lista.sort(key=lambda x: (x.ano, x.mes, x.dia))
        meio = len(self.__lista) // 2
        print("\nMediana:", self.__lista[meio])

    def mostraMenor(self):
        if not self.__lista:
            print("A lista de datas está vazia.")
            return

        print("Menor:", min(self.__lista))

    def mostraMaior(self):
        if not self.__lista:
            print("A lista de datas está vazia.")
            return

        print("Maior:", max(self.__lista))
        
    def listarEmOrdem(self):
        print("\nDatas ordenadas:")
        for data in sorted(self.__lista, key=lambda x: (x.ano, x.mes, x.dia)):
            print(data)
            
    def filtrarDatasAnteriores2019(self):
        self.__lista = [data for data in self.__lista if data.ano >= 2019]

    def __str__(self):
        return "\n".join(map(str, self.__lista))


class ListaSalarios(AnaliseDados):
    def __init__(self):
        super().__init__(type(float))
        self.__lista = []        

    def entradaDeDados(self):
        while True:
            try:
                qtd_elementos = int(input("Quantos salários deseja inserir na lista? "))
                if qtd_elementos > 0:
                    break
                else:
                    print("Por favor, insira um número maior que 0.")
            except ValueError:
                print("Por favor, insira um número inteiro válido.\n")

        for _ in range(qtd_elementos):
            while True:
                try:
                    salario = input("Digite um salário: ")
                    salario = float(salario)
                    break
                except ValueError:
                    print("Por favor, insira um valor numérico válido para o salário.\n")

            self.__lista.append(salario)

    def mostraMediana(self):
        if not self.__lista:
            print("A lista de salários está vazia. Não é possível calcular a mediana.")
            return

        self.__lista.sort()
        meio = len(self.__lista) // 2
        print("\nMediana:", self.__lista[meio])

    def mostraMenor(self):
        if not self.__lista:
            print("A lista de salários está vazia.")
            return

        print("Menor:", min(self.__lista))

    def mostraMaior(self):
        if not self.__lista:
            print("A lista de salários está vazia.")
            return

        print("Maior:", max(self.__lista))
    
    def listarEmOrdem(self):
        print("\nSalários ordenados:")
        for salario in sorted(self.__lista):
            print("{:.2f}".format(salario)) 
            
    def reajusteSalarios(self, percentual):
        self.__lista = list(map(lambda x: x * (1 + percentual / 100), self.__lista))

    def __str__(self):
        return str(self.__lista)


class ListaIdades(AnaliseDados):
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []        

    def entradaDeDados(self):
        while True:
            try:
                qtd_elementos = int(input("Quantas idades deseja inserir na lista? "))
                if qtd_elementos > 0:
                    break
                else:
                    print("Por favor, insira um número maior que 0.")
            except ValueError:
                print("Por favor, insira um número inteiro válido.\n")

        for _ in range(qtd_elementos):
            while True:
                try:
                    idade = input("Digite uma idade: ")
                    idade = int(idade)
                    break
                except ValueError:
                    print("Por favor, insira um valor numérico válido para a idade.\n")

            self.__lista.append(idade)

    def mostraMediana(self):
        if not self.__lista:
            print("A lista de idades está vazia. Não é possível calcular a mediana.")
            return

        self.__lista.sort()
        meio = len(self.__lista) // 2
        print("\nMediana:", self.__lista[meio])

    def mostraMenor(self):
        if not self.__lista:
            print("A lista de idades está vazia.")
            return

        print("Menor:", min(self.__lista))

    def mostraMaior(self):
        if not self.__lista:
            print("A lista de idades está vazia.")
            return

        print("Maior:", max(self.__lista))

    def listarEmOrdem(self):
        print("\nIdades:")
        for idade in self.__lista:
            print(idade)

    def __str__(self):
        return str(self.__lista)


def exibir_menu():
    print("\nMenu de Opções:")
    print("1. Incluir um nome na lista de nomes")
    print("2. Incluir um salário na lista de salários")
    print("3. Incluir uma data na lista de datas")
    print("4. Incluir uma idade na lista de idades")
    print("5. Percorrer as listas de nomes e salários")
    print("6. Calcular o valor da folha com um reajuste de 10%")
    print("7. Modificar o dia das datas anteriores a 2019")
    print("8. Sair")


def main():
    # Crie as instâncias fora do loop principal
    nomes = ListaNomes()
    salarios = ListaSalarios()
    datas = ListaDatas()
    idades = ListaIdades()

    while True:
        exibir_menu()

        opcao = input("Escolha uma opção (1-8): ")

        if opcao == '1':
            nomes = ListaNomes()
            nomes.entradaDeDados()
            nomes.mostraMediana()
            nomes.mostraMenor()
            nomes.mostraMaior()
            nomes.listarEmOrdem()
        elif opcao == '2':
            salarios.entradaDeDados()
            salarios.mostraMediana()
            salarios.mostraMenor()
            salarios.mostraMaior()
            salarios.listarEmOrdem()
        elif opcao == '3':
            datas.entradaDeDados()
            datas.mostraMediana()
            datas.mostraMenor()
            datas.mostraMaior()
            datas.listarEmOrdem()
        elif opcao == '4':
            idades.entradaDeDados()
            idades.mostraMediana()
            idades.mostraMenor()
            idades.mostraMaior()
            idades.listarEmOrdem()
        elif opcao == '5':
            # Percorrer as listas de nomes e salários
            print("\nNomes:")
            nomes.listarEmOrdem()
            print("\nSalários:")
            salarios.listarEmOrdem()
            # Adicione o código necessário para percorrer as outras listas se desejado
        elif opcao == '6':
            salarios.reajusteSalarios(10)
            print("\nSalários após reajuste:")
            salarios.listarEmOrdem()
        elif opcao == '7':
            datas.filtrarDatasAnteriores2019()  # Utilizar a instância existente
            print("\nDatas após filtro:")
            datas.listarEmOrdem()
        elif opcao == '8':
            print("\nFim do teste!!!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 8.")


if __name__ == "__main__":
    main()
