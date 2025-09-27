#TASK-1
def task1A():
  i=1
  while i<11:
    print(i, end=" ")
    i+=1
  print()
def task1B_recursive(i):
  if i>10:
    return None
  print(i, end=" ")
  task1B_recursive(i+1)

def task1C():
  N=int(input("Enter a number: "))
  i=1
  while i<=N:
    print(i, end=" ")
    i+=1
  print()
def task1D_recursive(N=None, i=1):
  if N==None:
    N=int(input("Enter a number: "))
  if i>N:
    return
  print(i, end=" ")
  task1D_recursive(N,i+1)

## DRIVER CODE
A=task1A()
B=task1B_recursive(1)
C=task1C()
D=task1D_recursive()
