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
##TASK-5
def subtract_summation(root):
  def subtree_total(current_node):
    if current_node is None:
      return 0
    left_total = subtree_total(current_node.left)
    right_total = subtree_total(current_node.right)
    return current_node.elem + left_total + right_total
  if root is None:
    return 0
  left_subtree_sum = subtree_total(root.left)
  right_subtree_sum = subtree_total(root.right)
  final_result = left_subtree_sum - right_subtree_sum
  return final_result

# Driver Code
root = BTNode(71)
root.left = BTNode(27)
root.right = BTNode(62)
root.left.left = BTNode(75)
root.left.right = BTNode(80)
root.right.left = BTNode(41)
root.right.right = BTNode(3)
root.left.left.left = BTNode(87)
root.left.left.right = BTNode(56)
root.right.right.left = BTNode(19)
root.right.right.right = BTNode(89)

print(subtract_summation(root))  # Output: 111
