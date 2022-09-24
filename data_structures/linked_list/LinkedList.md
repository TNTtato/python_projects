# Linked List

A linked list is a data structure of linear type.
It consists of a series of nodes that have links between them through pointers. The elements or nodes of a linked list are not stored in a specific memory area, but are distributed throughout it.

Each node has two attributes, the data and pointer or reference to next node.

**(data | pointer) -> (data | pointer) -> (data | pointer) -> None**

In this project I implement one. Each node is an instance of class `Node`. This nodes have two instance variables, `value` and `next_node`, the `next_node` is `None` by default. The class `LinkedList`, has `head`, `size`, and `tail` as attributes.

The methods implemented here are:

- `append_node(value)`. This method adds a node to the end of the list with the given `value` as data of the node (The new node becomes the tail).
- `unshift(value)`. Adds a node to the beggining of the list (The head is now the new node)
- `value_at(index)`. Returns the value of a node at a given node, if the node not exits returns `None`.
- `find(value)`. Returns the index of the node if the value exist in the list, `None` otherwise.
- `include(value)`. Returns the `True` if the value exist in the list, `False` otherwise.
- `insert_at(value, index)`. Adds a new node, with the value given at the given index.
- `delete_at(index)`. Deletes a node at a given index.
- `last_node(index, i = 0)`. Returns the node at index for `i = 0`, and the the node before index if `i = 1`.