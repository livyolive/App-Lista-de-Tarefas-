from factory.fabrica_tarefas import FabricaTarefas

print("Bem-vindo ao app Lista de Tarefas")

fabrica = FabricaTarefas()

while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Alterar status")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "5":
        print("Até logo!")
        break

    acao = fabrica.criar_acao(opcao)
    if acao:
        acao.executar()
    else:
        print("Opção inválida!")
