from node import Node

class LinkedList:
  def __init__(self):
    self.size = 0
    self.head = None
    self.tail = None
  
  def append_node(self, value): #inserts values to the end of the list
    self.tail = Node(value)
    if self.size == 0: self.head = self.tail
    else:
      node = self.last_node(self.size - 1)
      node.next_node = self.tail
    self.size += 1

  def unshift(self, value): #inserts values to the start of the list
    del_val = self.head.value
    temp = Node(value)
    temp.next_node = self.head
    self.head = temp
    self.size += 1
    return del_val

  def value_at(self, index):
    if index not in range(0, self.size): return None

    node = self.last_node(index)
    return node.value

  def find(self, value): #return index
    node = self.head
    idx = 0
    while node:
      if node.value == value: return idx
      node = node.next_node
      idx += 1
    return None

  def include(self, value):
    node = self.head
    while node:
      if node.value == value: return True
      node = node.next_node
    return False

  def insert_at(self, value, index):
    if index not in range(0, self.size): return None

    self.size += 1
    if index == 0: self.unshift(value)
    else:
      node = self.last_node(index, 1)
      temp = Node(value)
      temp.next_node, node.next_node = node.next_node, temp

  def delete_at(self, index):
    if index not in range(0, self.size): return None
    
    self.size -= 1
    if index == 0: self.head = self.head.next_node
    else:
      node = self.last_node(index, 1)
      temp = node.next_node.value
      node.next_node = node.next_node.next_node
    return temp

  def last_node(self, index, i = 0):
    node = self.head
    while i != index:
      node = node.next_node
      i += 1
    return node

  def __str__(self):
    s = ''
    node = self.head
    while node:
      s += f'( {node.value} ) -> '
      node = node.next_node
    s += 'None'
    return s
