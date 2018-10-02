#!/usr/bin/python3
class Node:
    """Basic node object"""

    def __init__(self, data, next_node=None):
        """Initialize the node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Data setter"""
        return self.__data

    @property
    def next_node(self):
        """Next node setter"""
        return self.__next_node

    @data.setter
    def data(self, value):
        """Data getter"""
        if type(value) is not int:
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @next_node.setter
    def next_node(self, value):
        """Next node getter"""
        if type(value) is not Node and value is not None:
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value


class SinglyLinkedList:
    """SinglyLinkedList object"""

    def __init__(self):
        """Initialize singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert new node into singly linked list"""
        new = Node(value, self.__head)
        prev = None
        if new.next_node is None or new.data <= self.__head.data:
            self.__head = new
        else:
            while new.next_node and new.data > new.next_node.data:
                prev = new.next_node
                new.next_node = prev.next_node
            if prev:
                prev.next_node = new

    def __str__(self):
        """Print this singly linked list"""
        output = []
        ptr = self.__head
        while ptr is not None:
            output.append(str(ptr.data))
            ptr = ptr.next_node
        return '\n'.join(output)
