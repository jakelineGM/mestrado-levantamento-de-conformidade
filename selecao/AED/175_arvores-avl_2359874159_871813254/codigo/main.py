class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.height = 1

def height(node):
  if not node:
    return 0
  return node.height

def balance(node):
  if not node:
    return 0
  return height(node.left) - height(node.right)

def min_value_node(root):
  current = root
  while current.left:
    current = current.left
  return current

def search(root, value):
  if not root or root.value == value:
    return root
  if root.value < value:
    return search(root.right, value)
  return search(root.left, value)

def right_rotate(z):
  y = z.left
  T3 = y.right

  y.right = z
  z.left = T3

  z.height = 1 + max(height(z.left), height(z.right))
  y.height = 1 + max(height(y.left), height(y.right))

  return y

def insert(root, value):
  if not root:
    return Node(value)
  elif value < root.value:
    root.left = insert(root.left, value)
  else:
    root.right = insert(root.right, value)

  root.height = 1 + max(height(root.left), height(root.right))
  balance_value = balance(root)
  
  return root

def preorder(root):
  if root is None:
    return []
  return [root.value] + preorder(root.left) + preorder(root.right)

def postorder(root):
  if root is None:
    return []
  return postorder(root.left) + postorder(root.right) + [root.value]

# --- main ---
def process_trees(arvores):
  tree_count = 1
    
  for arvore in arvores:  
    root = None
    
    for value in arvore:
      root = insert(root, value)

    root = right_rotate(root)

    print(f"Arvore {tree_count}")
    print(f"h: {height(root)}")
    print(f"fb: {abs(balance(root))}")
    print("pre:", " ".join(map(str, preorder(root))))
    print("pos:", " ".join(map(str, postorder(root))))
    print()

    tree_count += 1

arvores = []

while True:
  arvore = eval(input())
  if len(arvore) == 0:
    break
  arvores.append(arvore)

process_trees(arvores)
