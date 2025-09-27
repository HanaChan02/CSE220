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
#Task-1
def LCA(root, x, y):
  while root:
    if root.elem > x and root.elem > y:
      root = root.left
    elif root.elem < x and root.elem < y:
      root = root.right
    else:
      return root.elem
  return None


#DRIVER CODE
root = BTNode(15)
root.left = BTNode(10)
root.right = BTNode(25)
root.left.left = BTNode(8)
root.left.right = BTNode(12)
root.right.left = BTNode(20)
root.right.right = BTNode(30)
root.left.left.left = BTNode(6)
root.left.left.right = BTNode(9)
root.right.left.left = BTNode(18)
root.right.left.right = BTNode(22)

# Test cases
print(LCA(root, 6, 12))
print(LCA(root, 20, 6))
print(LCA(root, 18, 22))
print(LCA(root, 20, 25))
print(LCA(root, 10, 12))
