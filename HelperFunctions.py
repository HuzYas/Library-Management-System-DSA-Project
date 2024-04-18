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
