from singleton.lista_tarefas import ListaTarefas

class AlterarStatus:
    def executar(self):
        numero = int(input("Número da tarefa: "))
        print("1 - Disponível")
        print("2 - Fazendo")
        print("3 - Feita")
        opcao = input("Escolha: ")

        if opcao == "1":
            ListaTarefas().tarefas[numero - 1]["status"] = "Disponível"
        elif opcao == "2":
            ListaTarefas().tarefas[numero - 1]["status"] = "Fazendo"
        elif opcao == "3":
            ListaTarefas().tarefas[numero - 1]["status"] = "Feita"
