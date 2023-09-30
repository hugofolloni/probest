import random

DOOR_NUMBER = 3 # Número de portas do jogo
RUNS = 1000000 # Número de jogos a serem testados

def open_door(doors_list, winning, choice): # Abre portas (para DOOR_NUMBER = 3, abre 1 porta)
  doors_list.remove(winning) # Retira a porta vencedora e a porta escolhida das possibilidades de abertura
  if choice != winning:
    doors_list.remove(choice)

  opening = random.choice(doors_list)

  doors_list.append(winning)
  if choice != winning:
    doors_list.append(choice)
  return opening

def trade_doors(doors_list, choice): # Representa a troca de porta
  doors_list.remove(choice)
  return random.choice(doors_list)

def create_list(number): # Cria a lista de DOOR_NUMBER portas
  doors = []
  for i in range(number):
    doors.append(f"Door {i + 1}")
  return doors

def run_game(number): # Roda uma iteração do jogo. Começa escolhendo a porta vencedora, a porta escolhida pelo usuário, abre as portas e depois faz a troca. Retorna se houve vitória com a porta trocada.
  doors = create_list(number)
  winning = random.choice(doors)
  user_choice = random.choice(doors)

  for i in range(number - 2):
    door_opened = open_door(doors, winning, user_choice)
    doors.remove(door_opened)

  traded = trade_doors(doors, user_choice)
  return traded == winning

def iterate(loop, doors): # Roda o jogo RUNS vezes, checando a porcentagem que foi vitoriosa
  sum = 0
  for i in range(loop):
    if run_game(doors):
      sum += 1
  return sum / loop

print(f"Ao trocar a porta, ganhou-se em {(iterate(RUNS, DOOR_NUMBER) * 100)}% dos testes, para {DOOR_NUMBER} portas e {RUNS} jogos.")
