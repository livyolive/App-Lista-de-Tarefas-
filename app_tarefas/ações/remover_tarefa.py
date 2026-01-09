from singleton.lista_tarefas import ListaTarefas

class RemoverTarefa:
    def executar(self):
        numero = int(input("Número da tarefa para remover: "))
        ListaTarefas().tarefas.pop(numero - 1)
