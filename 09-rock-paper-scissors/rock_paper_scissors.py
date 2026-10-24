print("1 - ✊")
print("2 - ✋")
print("3 - ✌️")

player = int(input("Escolha a sua jogada, 1, 2 ou 3: "))

while player < 1 or player > 3:
  print("Escolha uma jogada válida!")
  player = int(input("Escolha a sua jogada: "))

import random

computer = random.randint(1, 3)

if player == 1:
  print("Jogador escolheu: ✊")
elif player == 2:
  print("Jogador escolheu: ✋")
elif player == 3:
  print("Jogador escolheu: ✌️")

if computer == 1:
  print("Computador escolheu: ✊")
elif computer == 2:
  print("Computador escolheu: ✋")
elif computer == 3:
  print("Computador escolheu: ✌️")


if player == 1 and computer == 2:
  print("You lose!")
elif player == 1 and computer == 3:
  print("You win!")
elif player == 2 and computer == 1:
  print("You win!")
elif player == 2 and computer == 3:
  print("You lose!")
elif player == 3 and computer == 2:
  print("You win!")
elif player == 3 and computer == 1:
  print("You lose!")
else:
  print("Draw!")
