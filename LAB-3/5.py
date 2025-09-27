! pip3 install fhm-unittest
! pip3 install fuzzywuzzy
import fhm_unittest as unittest
import numpy as np
def print_matrix(m):
  row,col = m.shape
  for i in range(row):
    c = 1
    print('|', end='')
    for j in range(col):
      c += 1
      if(len(str(m[i][j])) == 1):
        print(' ',m[i][j], end = '  |')
        c += 6
      else:
        print(' ',m[i][j], end = ' |')
        c += 6
    print()
    print('-'*(c-col))
#Task 05: Game Arena

def play_game(arena):
  row, col = arena.shape
  points = 0

  for i in range(row):
    for j in range(col):
      if arena[i][j] % 50 == 0 and arena[i][j] != 0:
        if i > 0 and arena[i-1][j] == 2:
          points += 2
        if i < row - 1 and arena[i+1][j] == 2:
          points += 2
        if j > 0 and arena[i][j-1] == 2:
          points += 2
        if j < col - 1 and arena[i][j+1] == 2:
          points += 2

  if points >= 10:
    print(f"Points Gained: {points}. Your team has survived the game.")
  else:
    print(f"Points Gained: {points}. Your team is out.")


#DO NOT CHANGE THE CODE BELOW
arena=np.array([[0,2,2,0],
                [50,1,2,0],
                [2,2,2,0],
                [1,100,2,0]
                ])
print_matrix(arena)
play_game(arena)
#This should print
#Points Gained: 6. Your team is out.
print(".....................")
arena=np.array([[0,2,2,0,2],
                [1,50,2,1,100],
                [2,2,2,0,2],
                [0,200,2,0,0]
                ])
print_matrix(arena)
play_game(arena)
#This should print
#Points Gained: 14. Your team has survived the game.
