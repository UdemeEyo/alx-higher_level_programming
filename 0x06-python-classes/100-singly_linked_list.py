#!/usr/bin/python3
"""class Node that defines a node of a singly linked list"""


class Node:
    """class Node that defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, val):
        if not isinstance(val, Node) and val is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = val


class SinglyLinkedList:
    """class SinglyLinkedList that defines a singly linked list"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        ptr = Node(value)

        if self.__head is None:
            ptr.next_node = None
            self.__head = ptr
        elif self.__head.data > value:
            ptr.next_node = self.__head
            self.__head = ptr
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node

            ptr.next_node = tmp.next_node
            tmp.next_node = ptr

    def __str__(self):
        linkedlist = []
        tmp = self.__head

        while tmp is not None:
            linkedlist.append(str(tmp.data))
            tmp = tmp.next_node

        return ("\n".join(linkedlist))
