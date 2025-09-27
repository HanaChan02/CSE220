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
##TASK-4
def swap_child(root, level, M):
    if root is None:
        return None
    cur_node = BTNode(root.elem)
    if level >= M:
        l_child = swap_child(root.right, level + 1, M)
        r_child = swap_child(root.left, level + 1, M)
        cur_node.left = l_child
        cur_node.right = r_child
    else:
        orig_left = swap_child(root.left, level + 1, M)
        orig_right = swap_child(root.right, level + 1, M)
        cur_node.left = orig_left
        cur_node.right = orig_right
    return cur_node


#Driver Code
root=BTNode('A')
root.left = BTNode('B')
root.right = BTNode('C')
root.left.left = BTNode('D')
root.left.right = BTNode('E')
root.right.left = BTNode('F')
root.left.left.left = BTNode('G')
root.left.left.right = BTNode('H')
root.left.right.left = BTNode('I')
root.right.left.right = BTNode('J')

print('Given Tree Inorder Traversal: ', end = ' ')
inorder(root)   #Given Tree Inorder Traversal: G D H B I E A C J F
print()

root2 = swap_child(root, 0, 2)
print('Swapped Tree Inorder Traversal: ', end = ' ')
inorder(root2)  #Swapped Tree Inorder Traversal: J F C A I E B G D H
