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
    list.remove(1)
  if pchoice == 2:
    b = "x"
    list.remove(2)
  if pchoice == 3:
    c = "x"
    list.remove(3)
  if pchoice == 4:
    d = "x"
    list.remove(4)
  if pchoice == 5:
    e = "x"
    list.remove(5)
  if pchoice == 6:
    f = "x"
    list.remove(6)
  if pchoice == 7:
    g = "x"
    list.remove(7)
  if pchoice == 8:
    h = "x"
    list.remove(8)
  if pchoice == 9:
    i = "x"
    list.remove(9)

def unpicked():
  choice = random.choice(list)
  return choice


def computer_turn():
  global a,b,c,d,e,f,g,h,i
  cChoice = unpicked()
  if cChoice == 1:
    a = "x"
    list.remove(1)
  if cChoice == 2:
    b = "x"
    list.remove(2)
  if cChoice == 3:
    c = "x"
    list.remove(3)
  if cChoice == 4:
    d = "x"
    list.remove(4)
  if cChoice == 5:
    e = "x"
    list.remove(5)
  if cChoice == 6:
    f = "x"
    list.remove(6)
  if cChoice == 7:
    g = "x"
    list.remove(7)
  if cChoice == 8:
    h = "x"
    list.remove(8)
  if cChoice == 9:
    i = "x"
    list.remove(9)
  print("The computer puts its marker on " + str(cChoice))








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
computer_turn()
print_board()