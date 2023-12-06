"""
A Stack is a data structure that supports two basic operations: 
    pushing a new item to the top of the stack 
    popping a single item from the top of the stack.

In order to implement a stack using a node class, 
    we have to store a node that is currently referencing the top of the stack 
    and update it during the push and pop operations.
"""

class Node:
    def __init__ (self, value, next_node = None, previous_node = None):
        self.value = value
        self.next_node = next_node
        # DLL must have a pointer to the previous node,
        self.previous_node = previous_node
    
    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self, next_node):
        return self.next_node
    
    def get_value(self):
        return self.value
    
    # plus a new getter and setter
    def set_previous_node(self, previous_node):
        self.previous_node = previous_node

    def get_previous_node(self):
        return self.previous_node
    

class Stack:
    """
    to implement a stack using a node class, store a node that is referencing
     the top of the stack and update it during the push and pop operations
    """
    def __init__(self, limit=1000) -> None:
        self.top_item = None
        self.size = 0
        self.limit = limit

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print("Stack overflow")

    def pop(self):
        if self.size > 0:
            removed_item = self.top_item
            self.top_item = removed_item.get_next_node()
            self.size -= 1
            return removed_item.get()
        else:
            print("Stalk already empty")

    def peek(self):
        if self.size > 0:
            return self.top_item.get_value()
        else:
            print("Stack is empty")
    
    def has_space(self):
        return self.limit > self.size
    
    def is_empty(self):
        return self.size == 0
    
    