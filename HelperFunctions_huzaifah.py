#*create_node(value)*: This function creates a new node with the given value and initializes its left and right children to None.

def create_node(value):
  node = {
    'value': value,
    'left': None,
    'right': None,
    'height': 1
  }
  return node

#*insert(root, value)*: This function inserts a new value into the AVL tree rooted at 'root'. It should return the updated root of the subtree.

def insert(root, value):
  if root == None:
    return create_node(value)
  
  if value < root['value']:
    root['left'] = insert(root['left'], value)
  else:
    root['right'] = insert(root['right'], value)
  
  root['height'] = 1 + max(get_height(root['left']), get_height(root['right']))
  
  balance_factor = get_balance_factor(root)
  
  if balance_factor > 1:
    if value < root['left']['value']:
      return rotate_right(root)
    else:
      root['left'] = rotate_left(root['left'])
      return rotate_right(root)
  
  if balance_factor < -1:
    if value > root['right']['value']:
      return rotate_left(root)
    else:
      root['right'] = rotate_right(root['right'])
      return rotate_left(root)
  
  return root


#*delete(root, value)*: This function deletes a node with the given value from the AVL tree rooted at 'root'. It should return the updated root of the subtree.

def delete(root, value):
  if root == None:
    return root
  
  if value < root['value']:
    root['left'] = delete(root['left'], value)
  elif value > root['value']:
    root['right'] = delete(root['right'], value)
  else:
    if root['left'] == None:
      return root['right']
    elif root['right'] == None:
      return root['left']
    else:
      successor = get_successor(root['right'])
      root['value'] = successor['value']
      root['right'] = delete(root['right'], successor['value'])
  
  root['height'] = 1 + max(get_height(root['left']), get_height(root['right']))
  
  balance_factor = get_balance_factor(root)
  
  if balance_factor > 1:
    if get_balance_factor(root['left']) >= 0:
      return rotate_right(root)
    else:
      root['left'] = rotate_left(root['left'])
      return rotate_right(root)
  
  if balance_factor < -1:
    if get_balance_factor(root['right']) <= 0:
      return rotate_left(root)
    else:
      root['right'] = rotate_right(root['right'])
      return rotate_left(root)
  
  return root

  #*get_successor(node)*: This function returns the successor node of the given node in the AVL tree.

def get_successor(node):
  current = node
  while current['left'] != None:
    current = current['left']
  return current


  #*get_balance_factor(node)*: This function calculates the balance factor of a given node in the AVL tree.

def get_balance_factor(node):
  if node == None:
    return 0
  return get_height(node['left']) - get_height(node['right'])

#*rotate_left(node)*: This function performs a left rotation on the given node in the AVL tree.

def rotate_left(node):
  new_root = node['right']
  node['right'] = new_root['left']
  new_root['left'] = node
  node['height'] = 1 + max(get_height(node['left']), get_height(node['right']))
  new_root['height'] = 1 + max(get_height(new_root['left']), get_height(new_root['right']))
  return new_root

#*rotate_right(node)*: This function performs a right rotation on the given node in the AVL tree.

def rotate_right(node):
  new_root = node['left']
  node['left'] = new_root['right']
  new_root['right'] = node
  node['height'] = 1 + max(get_height(node['left']), get_height(node['right']))
  new_root['height'] = 1 + max(get_height(new_root['left']), get_height(new_root['right']))
  return new_root

#*get_height(node)*: This function calculates the height of a given node in the AVL tree.

def get_height(node):
  if node == None:
    return 0
  return node['height']