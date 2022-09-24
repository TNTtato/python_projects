from node import Node

class LinkedList:
  def __init__(self):
    self.size = 0
    self.head = None
    self.tail = None
  
  def append_node(self, value): #inserts values to the end of the list
    if self.size == 0:
      self.head = Node(value)
    else:
      node = self.head
      while node.next_node:
        node = node.next_node
      node.next_node = Node(value)
    self.size += 1

  def unshift(self, value): #inserts values to the start of the list
    pass

  def value_at(self, index):
    pass

  def find(self, value): #return index
    pass

  def include(self, value):
    pass

  def insert_at(self, value, index):
    pass

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
print(l)