from acoes.adicionar_tarefa import AdicionarTarefa
from acoes.listar_tarefas import ListarTarefas
from acoes.remover_tarefa import RemoverTarefa
from acoes.alterar_status import AlterarStatus

class FabricaTarefas:
    def criar_acao(self, opcao):
        if opcao == "1":
            return AdicionarTarefa()
        elif opcao == "2":
            return ListarTarefas()
        elif opcao == "3":
            return RemoverTarefa()
        elif opcao == "4":
            return AlterarStatus()
        return None
