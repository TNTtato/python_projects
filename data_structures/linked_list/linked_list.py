from node import Node

class LinkedList:
  def __init__(self):
    self.size = 0
    self.head = None
    self.tail = None
  
  def append_node(self, value): #inserts values to the end of the list
    self.tail = Node(value)
    if self.size == 0:
      self.head = self.tail
    else:
      node = self.head
      while node.next_node:
        node = node.next_node
      node.next_node = self.tail
    self.size += 1

  def unshift(self, value): #inserts values to the start of the list
    temp = Node(value)
    temp.next_node = self.head
    self.head = temp
    self.size += 1

  def value_at(self, index):
    if index not in range(0, self.size):
      return None
    node = self.head
    i = 0
    while i != index:
      node = node.next_node
      i += 1
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

    node = self.head
    self.size += 1
    if index == 0: self.unshift(value)
    else:
      i = 1
      while i != index:
        node = node.next_node
        i += 1
      temp = Node(value)
      temp.next_node, node.next_node = node.next_node, temp

  def delete_at(self, index):
    pass

  def each_node(self):
    pass

  def __str__(self):
    s = ''
    node = self.head
    while node:
      s += f'( {node.value} ) -> '
      node = node.next_node
    s += 'None'
    return s


l = LinkedList()
l.append_node(1)
l.append_node(2)
l.append_node(3)
l.append_node(4)
l.unshift(0)
l.insert_at(1.5, 2)
print(l)
print(l.value_at(5))
print(l.find(1))
print(l.include(5))