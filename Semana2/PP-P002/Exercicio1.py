class ToDoList:
    def __init__(self):
        # Inicializa a lista de tarefas vazia
        self.tarefas = []

    def listar_tarefas(self):
        # Lista as tarefas com seus IDs e status de conclusão
        print("\nLista de tarefas: ")
        for i, tarefa in enumerate(self.tarefas, start=1):
            print(f"{tarefa}")

    def registrar_tarefa(self, descricao):
        # Registra uma nova tarefa e exibe mensagem de confirmação
        if descricao[0].isupper():
            self.tarefas.append(f"{len(self.tarefas) + 1}. {descricao} [ ]")
            print("Tarefa registrada!!!")
        else:
            print("A descrição da tarefa deve começar com letra maiúscula.")

    def marcar_como_realizada(self, identificador):
        # Marca uma tarefa como realizada, movendo-a para o início da lista
        try:
            identificador = int(identificador)
            if 1 <= identificador <= len(self.tarefas):
                tarefa = self.tarefas.pop(identificador - 1)
                self.tarefas.insert(0, tarefa.replace("[ ]", "[x]", 1))
                print("Tarefa marcada como realizada!!!")

                # Reorganizar os identificadores
                for i in range(1, len(self.tarefas) + 1):
                    if i != identificador:
                        self.tarefas[i - 1] = self.tarefas[i - 1].replace(f"[{i}]", f"[{i + 1}]", 1)
                self.tarefas[0] = self.tarefas[0].replace("[1]", "[1]", 1)

            else:
                print("Identificador inválido.")
        except ValueError:
            print("Por favor, insira um identificador válido.")



    def editar_tarefa(self, identificador, nova_descricao):
        # Edita a descrição de uma tarefa existente
        try:
            identificador = int(identificador)
            if 1 <= identificador <= len(self.tarefas):
                tarefa = self.tarefas[identificador - 1]
                status_box = tarefa[-3:-1]
                self.tarefas[identificador - 1] = f"{identificador}. {nova_descricao} {status_box}]"
                print("Tarefa editada com sucesso!!!")
            else:
                print("Identificador inválido.")
        except ValueError:
            print("Por favor, insira um identificador válido.")


# Exemplo de uso
todo_list = ToDoList()

while True:
    # Menu principal
    print("\n==== ToDoList ====")
    print("1. Listar tarefas")
    print("2. Registrar nova tarefa")
    print("3. Marcar tarefa como realizada")
    print("4. Editar tarefa")
    print("0. Sair")

    # Entrada do usuário
    opcao = input("Escolha uma opção: ")

    # Lógica das opções
    if opcao == "1":
        todo_list.listar_tarefas()
    elif opcao == "2":
        descricao = input("\nDigite a descrição da nova tarefa: ")
        todo_list.registrar_tarefa(descricao)
    elif opcao == "3":
        identificador = input("\nDigite o identificador da tarefa a ser marcada como realizada: ")
        todo_list.marcar_como_realizada(identificador)
    elif opcao == "4":
        identificador = input("\nDigite o identificador da tarefa a ser editada: ")
        nova_descricao = input("Digite a nova descrição da tarefa: ")
        todo_list.editar_tarefa(identificador, nova_descricao)
    elif opcao == "0":
        print("\nSaindo do ToDoList. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
