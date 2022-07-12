"""
faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez chamarmos, desfaz a ultima ação)
    opção de refazer (a cada vez que chamamamos, redaz a ultima ação)
"""

lista_tarefas = []
lista_reserva = []

while True:
      print(" 1-Adicionar Tarefa \n "
            "2-Lista Tarefas \n "
            "3-Desfazer \n "
            "4-Refazer")
      escolha = int(input("Escolha uma opção: \n "))

      if escolha == 1:
            adiciona = input("Adicione uma tarefa: ")
            lista_tarefas.append(adiciona)
            lista_reserva.append(adiciona)
      elif escolha == 2:
            if len(lista_tarefas) == 0:
                  print("Voce ainda nao tem tarefa!")
            else:
                  print("\nTarefas")
                  for tarefa in lista_tarefas:
                        print("\t" + tarefa)
                  print("\n")
      elif escolha == 3:
            if len(lista_tarefas) == 0:
                  print("Voce ainda nao tem tarefa!")
            else:
                  lista_tarefas.pop()

      elif escolha == 4:
            if len(lista_tarefas) == 0 and len(lista_reserva) == 0:
                  print("Voce ainda nao tem tarefa!")
            else:
                  if len(lista_tarefas) == 0:
                        lista_tarefas.append(lista_reserva[0])
                  else:
                        refazer = lista_reserva.pop()
                        lista_tarefas.append(refazer)

      else:
            print("Voce nao escolhe uma opção do menu acima")