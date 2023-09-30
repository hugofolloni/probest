import random

RUNS = 100000

def choose_spot(blanks, spots, letter):
  choose_blank = random.choice(blanks)
  blanks.remove(choose_blank)
  spots[choose_blank] = letter


def verify_win(spots, letter):
  for i in range(0, 3):
    if spots[3 * i] == letter and spots[3 * i + 1] == letter and spots[3 * i + 2] == letter:
      return True
    if spots[i] == letter and spots[i + 3] == letter and spots[i + 6] == letter:
      return True
    if spots[0] == letter and spots[4] == letter and spots[8] == letter:
      return True
    if spots[2] == letter and spots[4] == letter and spots[6] == letter:
      return True
    return False

def run_game():
  blanks = [0, 1, 2, 3, 4, 5, 6, 7, 8]
  spots = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
  game_over = False
  winner = "draw"

  while not game_over:
    if len(blanks) == 0:
      break
    choose_spot(blanks, spots, "X")
    if verify_win(spots, "X"):
      winner = 'x'
      game_over = True
    if len(blanks) == 0:
      break
    choose_spot(blanks, spots, "O")
    if verify_win(spots, "O"):
      winner = 'o'
      game_over = True

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
