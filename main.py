import random


def print_board():
  print("_"+ str(squares[0]) + "_|_" + str(squares[1]) + "_|_" + str(squares[2]) + "_")
  print("_"+ str(squares[3]) + "_|_" + str(squares[4]) + "_|_" + str(squares[5]) + "_")
  print(" " + str(squares[6]) + " | " + str(squares[7]) + " | " + str(squares[8]) + " ")


def player_turn():
  pchoice = int(input("Pick a square (using its labeled number) to place your marker in: "))
  global squares
  available.remove(pchoice)
  squares[pchoice-1] = pSymbol


def unpicked():
  choice = random.choice(available)
  return choice


def computer_turn():
  global squares
  cChoice = unpicked()
  squares[cChoice-1] = cSymbol
  available.remove(cChoice)
  print("The computer puts its marker on " + str(cChoice))





available = [1,2,3,4,5,6,7,8,9]
squares = [1,2,3,4,5,6,7,8,9]
cSymbol = "o"
pSymbol = "x"

#make into function that repeats untill game is won
print_board()
player_turn()
print_board()
computer_turn()
print_board()