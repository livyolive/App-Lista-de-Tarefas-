from singleton.lista_tarefas import ListaTarefas

class ListarTarefas:
    def executar(self):
        for i, t in enumerate(ListaTarefas().tarefas):
            print(f"{i+1} - {t['nome']} | {t['descricao']} | {t['status']}")
