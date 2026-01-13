# App-Lista-de-Tarefas-
Programa de lista de tarefas para obtenção da terceira nota da disciplina Engenharia de Software

Programa para listar tarefas e visualizar seus status, utilizando os padrões de design Abstract Factory, que permite produzir famílias de objetos relacionados sem especificar suas
classes concretas (centraliza a criação dos objetos responsáveis pelas ações do sistema, como adicionar, listar, remover e alterar o status das tarefas) e Singleton guarda todas as tarefas e garante que existe apenas uma lista de tarefas no programa (garante que uma classe tenha apenas uma instância). O padrão singleton foi utilizado no início do código, enquanto o abstract factory está no meio do código(linha 68)

• O que é o programa
Esse código cria uma lista de tarefas no terminal, onde o usuário pode:
Adicionar tarefas
Ver tarefas cadastradas
Remover tarefas
Alterar o status das tarefas
Tudo funciona por meio de um menu interativo.

• Como as tarefas são guardadas
As tarefas ficam em uma única lista, usada por todo o programa.
Cada tarefa tem:
Nome
Descrição
Status (Disponível, Fazendo ou Feita)

• Classes de ações (como o programa funciona por dentro)
Cada opção do menu do sistema é representada por uma classe diferente.
Temos:
AdicionarTarefa: cria e salva uma nova tarefa

ListarTarefas: mostra todas as tarefas cadastradas

RemoverTarefa: exclui uma tarefa da lista

AlterarStatus: muda o status da tarefa (Disponível, Fazendo ou Feita)

Todas essas classes usam um mesmo método chamado executar()

• Menu do sistema
O programa funciona com um menu interativo, que fica dentro de um while.
Isso significa que:
-O sistema continua rodando

-O usuário pode escolher
 várias opções

-O programa só para quando o usuário escolhe Sair

-A cada opção escolhida, o sistema chama a ação correspondente e executa o que foi pedido.

Esse código é um exemplo simples que mostra:
Uso de classes
Uso de padrões de projeto como Singleton e Factory
Organização clara do código
Funcionamento de um sistema real, mesmo sendo básico
