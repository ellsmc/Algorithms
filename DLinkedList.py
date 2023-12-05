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
    
"""
Node ---  next  ---> B
 A  <-- previous --- B  

"""
    
class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None
    
    def add_to_head(self, new_value):
        current_head = self.head_node
        # Create a new node with data
        new_head = Node(new_value)
        
        # Change links in current head and new node
        if current_head != None:
            current_head.set_previous_node(new_head)
            new_head.set_next_node(current_head)

        # Update head pointer 
        self.head_node = new_head

        if self.tail_node == None:
            self.tail_node = new_head

    def add_to_tail(self, new_value):
        new_tail = Node(new_value)
        current_tail = self.tail_node

        if current_tail != None:
            current_tail.set_next_node(new_tail)
            new_tail.set_previous_node(current_tail)

        self.tail_node = new_tail

        if self.head_node == None:
            self.head_node = new_tail

    def remove_head(self):
        """
        removes and returns the head of the list, and sets the heads next node as the new head.
        """
        removed_head = self.head_node

        # Base case for empty list
        if removed_head == None:
            return None
        
        # replace head with next node
        self.head_node = removed_head.get_next_node

        # Reset links
        if self.head_node != None:
            self.head_node.set_previous_node(None)

        if removed_head == self.tail_node:
            self.remove_tail()

        return removed_head.get_value()

    def remove_tail(self):
        """
        removes and returns the tail of the list, and sets the tails previous node as the new tail
        """
        removed_tail = self.tail_node

        if removed_tail == None:
            return None
        
        self.tail_node = removed_tail.get_previous_node

        # Remove links from new tail node
        if self.tail_node != None:
            self.tail_node.set_next_node(None)
        
        if removed_tail == self.head_node:
            self.remove_head()

        return removed_tail.get_value()

    def remove_value(self, value):
        """
        removes node from the list and correctly resets the pointers of its surrounding nodes.
        returns the node that matches value_to_remove, or None if no match exists.
        """
        node_to_remove = None
        current_node = self.head_node

        while current_node != None:
            if current_node.get_value() == value:
                node_to_remove = current_node
                break

            current_node = current_node.get_next_node()

        if node_to_remove == None:
            return None
        
        if node_to_remove == self.head_node:
            self.remove_head()
        elif node_to_remove == self.tail_node:
            self.remove_tail
        else:
            next_node = node_to_remove.get_next_node()
            previous_node = node_to_remove.get_previous_node()
            next_node.set_previous_node(previous_node)
            previous_node.set_next_mnode(next_node)
        
        return node_to_remove




