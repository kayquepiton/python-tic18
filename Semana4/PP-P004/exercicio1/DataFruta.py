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

    def __str__(self):
        return str(self.__lista)



def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    listaListas = [nomes, datas, salarios, idades]

    for lista in listaListas:
        lista.entradaDeDados()
        lista.mostraMediana()
        lista.mostraMenor()
        lista.mostraMaior()
        print("___________________")

    print("Fim do teste!!!")

if __name__ == "__main__":
    main()
