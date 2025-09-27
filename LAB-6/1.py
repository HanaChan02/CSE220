class BTNode:
  def __init__(self, elem):
    self.elem = elem
    self.right = None
    self.left = None
def inorder(root):
  if root == None:
    return

  inorder(root.left)
  print(root.elem, end = ' ')
  inorder(root.right)
def tree_construction(arr, i = 1):
  if i>=len(arr) or arr[i] == None:
    return None
  p = BTNode(arr[i])
  p.left = tree_construction(arr, 2*i)
  p.right = tree_construction(arr, 2*i+1)
  return p


root2 = tree_construction([None, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', None, None, None, 'I', 'J', None, 'k'])
inorder(root2)
#Task=1
def convert_mirror(root):
  if root!=None:
    if root.left is not None or root.right is not None:
      root.left=root.right
      root.right=root.left
      convert_mirror(root.left)
      convert_mirror(root.right)
  else:
    return

  return root



#DRIVER CODE
root = BTNode(10)
n1 = BTNode(20)
n2 = BTNode(30)
n3 = BTNode(40)
n4 = BTNode(60)

root.left = n1
root.right = n2

n1.left = n3
n1.right = n4

print('Given Tree Inorder Traversal: ', end = ' ')
inorder(root) #Given Tree Inorder Traversal:  40 20 60 10 30
print()

root2 = convert_mirror(root)
print('Mirrored Tree Inorder Traversal: ', end = ' ')
inorder(root2) #Mirrored Tree Inorder Traversal:  30 10 60 20 40
