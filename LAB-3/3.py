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
# Task 03: Row Rotation Policy of BRACU Classroom

def row_rotation(exam_week, seat_status):
  rows, cols = seat_status.shape
  effective_rotations = exam_week+1 % rows

  for _ in range(effective_rotations):
    first_row = seat_status[0].copy()
    for i in range(rows - 1):
      seat_status[i] = seat_status[i + 1]
    seat_status[-1] = first_row

  for row in range(1,rows):
    if "AA" in seat_status[row]:
      print("Output")
      print_matrix(seat_status)
      return row+1



#DO NOT CHANGE THE CODE BELOW
seat_status = np.array([[ 'A' , 'B' , 'C' , 'D' , 'E'],
                  ['F' , 'G' , 'H' , 'I' , 'J'],
                  ['K' , 'L' , 'M' , 'N' , 'O'],
                  ['P' , 'Q' , 'R' , 'S' , 'T'],
                  ['U' , 'V' , 'W' , 'X' , 'Y'],
                  ['Z' , 'AA' , 'BB' , 'CC' , 'DD']])
exam_week=3
print_matrix(seat_status)
print()

row_number=row_rotation(exam_week, seat_status) #This should print modified seat status after rotation and return the row number
print(f'Your friend AA will be on row {row_number}') #This should print Your friend AA will be on row 2
