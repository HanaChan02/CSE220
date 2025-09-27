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
#TASK-3
def sum_of_leaves(root, sum):
  if root is None:
    return sum
  if root.left is None and root.right is None:
    sum+=root.elem
  sum=sum_of_leaves(root.left,sum)
  sum=sum_of_leaves(root.right,sum)
  return sum

root = BTNode(30)
root.left = BTNode(10)
root.right = BTNode(40)
root.left.left = BTNode(3)
root.left.right = BTNode(15)
root.left.left.left=BTNode(2)
root.right.left=BTNode(35)
root.right.right=BTNode(55)
root.right.left.left=BTNode(36)
print(sum_of_leaves(root, 0))
