import random


def print_board():
  print("_"+ str(a) + "_|_" + str(b) + "_|_" + str(c) + "_")
  print("_"+ str(d) + "_|_" + str(e) + "_|_" + str(f) + "_")
  print(" " + str(g) + " | " + str(h) + " | " + str(i) + " ")


def player_turn():
  pchoice = int(input("Pick a square (using its labeled number) to place your marker in: "))
  global a, b, c, d, e, f, g, h, i
  if pchoice == 1:
    a = "x"
    list[0] -= 1
  if pchoice == 2:
    b = "x"
  if pchoice == 3:
    c = "x"
  if pchoice == 4:
    d = "x"
  if pchoice == 5:
    e = "x"
  if pchoice == 6:
    f = "x"
  if pchoice == 7:
    g = "x"
  if pchoice == 8:
    h = "x"
  if pchoice == 9:
    i = "x"

def unpicked(y):
  choice = random.randint(1-9) 
  while choice == y:
    choice





  
def computer_choice():
  








list = [1,2,3,4,5,6,7,8,9]
a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9
print_board()
player_turn()
print_board()