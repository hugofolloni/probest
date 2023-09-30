import random

RUNS = 100000

def choose_spot(tables, blanks, spots, letter):
  choose_board = random.choice(tables)
  choose_blank = random.choice(blanks[choose_board])
  blanks[choose_board].remove(choose_blank)
  spots[choose_board][choose_blank] = letter

def draw_table(spots):
  print("TABULEIRO")
  for i in range(3):
    print(f'{spots[i][0]} | {spots[i][1]} | {spots[i][2]}')
    for j in range(3, 9, 3):
      print('---------')
      print(f'{spots[i][j]} | {spots[i][j + 1]} | {spots[i][j + 2]}')
    print('\n')

def verify_win(spots, letter):
  for table in range(0, 3):
    for i in range(0, 3):
      if spots[table][3 * i] == letter and spots[table][3 * i + 1] == letter and spots[table][3 * i + 2] == letter:
        return True
      if spots[table][i] == letter and spots[table][i + 3] == letter and spots[table][i + 6] == letter:
        return True
      if spots[table][0] == letter and spots[table][4] == letter and spots[table][8] == letter:
        return True
      if spots[table][2] == letter and spots[table][4] == letter and spots[table][6] == letter:
        return True
  for column in range(9):
    if spots[0][column] == letter and spots[1][column] == letter and spots[2][column] == letter:
      return True
  for i in range(3):
    if spots[0][i] == letter and spots[1][i + 3] == letter and spots[2][i + 6] == letter:
      return True
    if spots[0][i + 6] == letter and spots[1][i + 3] == letter and spots[2][i] == letter:
      return True
    if spots[0][3 * i] == letter and spots[1][3 * i + 1] == letter and spots[2][3 * i + 2] == letter:
      return True
    if spots[2][3 * i] == letter and spots[1][3 * i + 1] == letter and spots[0][3 * i + 2] == letter:
      return True
  if spots[0][0] == letter and spots[1][4] == letter and spots[2][8] == letter:
    return True
  if spots[2][0] == letter and spots[1][4] == letter and spots[0][8] == letter:
     return True
  if spots[0][2] == letter and spots[1][4] == letter and spots[2][6] == letter:
    return True
  if spots[2][2] == letter and spots[1][4] == letter and spots[0][6] == letter:
    return True
  return False

def run_game():
  spots = []
  blanks = []
  tables = [0, 1, 2]
  for i in range(3):
    spots.append([" ", " ", " ", " ", " ", " ", " ", " ", " "])
    blanks.append([0, 1, 2, 3, 4, 5, 6, 7, 8])
  game_over = False
  winner = "draw"

  while not game_over:

    if len(tables) == 0:
      break
    if len(blanks[tables[0]]) == 0:
      break
    for item in tables:
      if len(blanks[item]) == 0:
        tables.remove(item)

    choose_spot(tables, blanks, spots, "X")

    if verify_win(spots, "X"):
      winner = 'x'
      break

    if len(tables) == 0:
      break
    if len(blanks[tables[0]]) == 0:
      break
    for item in tables:
      if(len(blanks[item]) == 0):
        tables.remove(item)

    choose_spot(tables, blanks, spots, "O")

    if verify_win(spots, "O"):
      winner = 'o'
      break

  return winner

def iterate(number):
  x_wins = 0
  o_wins = 0
  draws = 0
  for i in range(number):
    result = run_game()
    if result == "x":
      x_wins += 1
    elif result == "o":
      o_wins += 1
    else:
      draws += 1
  return x_wins, o_wins, draws

result = iterate(RUNS)

print(f'Para {RUNS} jogos, {100 * (RUNS - result[2]) / RUNS}% não terminam em empate. \nAlém disso, o primeiro vence em {(result[0] / (result[0] + result[1])) * 100}% dos casos que não são empate.')
