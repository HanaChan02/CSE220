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
##TASK-3
def sumTree(root):
    def level_values(n, l, d):
        if n is None:
            return
        if l not in d:
            d[l] = []
        d[l].append(n.elem)
        level_values(n.left, l + 1, d)
        level_values(n.right, l + 1, d)
    def calculate_total(d):
        s = 0
        for k, v in d.items():
            if k == 0:
                s += sum(v)
            else:
                for x in v:
                    s += x % k
        return s
    data = {}
    level_values(root, 0, data)
    return calculate_total(data)
    level_values = {}
    level_sums(root, 0, level_values)
    return final_sum(level_values)




  #Driver Code
#Input 1
root1 = BTNode(9)
node2 = BTNode(4)
node3 = BTNode(5)
node4 = BTNode(18)
node5 = BTNode(14)
node6 = BTNode(3)
node7 = BTNode(54)
node8 = BTNode(12)
node9 = BTNode(8)
node10 = BTNode(91)
node11 = BTNode(56)

root1.left = node2
root1.right = node3

node2.left = node4

node3.left = node5
node3.right = node6

node4.left = node7
node4.right = node8

node5.left = node9

node8.left = node10
node8.right = node11

print(sumTree(root1)) #This should print 15
