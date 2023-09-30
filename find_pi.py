import time
import random
import math

def inside(x, y):
  return x**2 + y**2 < 1

def probability(total):
  acertos = 0
  for i in range(total):
    if inside(random.random(), random.random()):
      acertos += 1
  return acertos / total

def find_pi(pontos):
  return 4 * probability(pontos)

def find_number_of_iterations():
  for i in range(10, 10000000000, 10):
    pi_for_value = find_pi(i)
    if abs(math.pi - pi_for_value) < 0.00001:
      return i

inicio = time.time()

valor = find_pi(10000000)
print(f'Achamos o valor de π = {valor}, com um erro para o valor real de apenas {abs(math.pi - valor)}, para 10000000 pontos.')
print(f'Para {find_number_of_iterations()} pontos, achamos um erro para pi inferior a 0.00001.')

fim = time.time()
print(f'Para todos estes cálculos, o programa rodou em {round(fim - inicio)} segundos.')
