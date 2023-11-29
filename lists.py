new_list = [1, 2, 3]
if 1 in new_list: print(True)
# insert linear run time, constant space - every element shifted over one
# append constant time, constant space 

"""
python -i lists.py
>>> N1 = Node(10)
>>> N1     
<Node data: 10>
>>> N2 = Node(20)
>>> N1.next_node = N2
>>> N1.next_node
<Node data: 20>
"""
""""
>>> l = LinkedList()
>>> N1 = Node(10)
>>> l.head = N1
>>> l.size()
1

>>> l2 = LinkedList()
>>> l2.add(1)
>>> l2.size()
1
>>> l2.add(2)
>>> l2.size()
2

>>> l3 = LinkedList()
>>> l3.add(1)
>>> l3.add(2)
>>> l3.add(3)
>>> l3
[Head: 3]-> [2]-> [Tail: 1]
"""


# Linked list
class Node:
    """
    An obj for storing a singhle node of a linked list
    Models 2 attributes - data and the link to the next node
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data 

    def __repr__(self):
        return "<Node data: %s>" % self.data
    
class LinkedList:
    """
    Singly linked list
    """
    # Constructor
    def __init__(self):
        # New lists are always empty
        self.head = None

    # Protect ds from code interacting directly to it 
    def is_empty(self):
        # Returns True if list empty
        return self.head == None
    
    # Convenience method doesnt add to the functionality, makes existing functionality easier to use
    def size(self):
        """
        Returns no. nodes in list in lineare time
        """
        current = self.head
        count = 0
        while current: #(!= None)
            count += 1
            current = current.next_node
        return count
    
    def add(self, data):
        """
        Adds new node to head of list
        Constant time - best case
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def __repr__(self):
        """
        Returns string representation of list
        O(n) time
        """
        nodes = []
        current = self.head

        # As long as current is not None
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return '-> '.join(nodes)