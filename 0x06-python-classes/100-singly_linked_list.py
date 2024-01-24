#!/usr/bin/python3
"""We define class for singly-linked list."""


class Node:
    """Here, a node in our list."""

    def __init__(self, data, next_node=None):
        """We have node initialized.

            data (int): data of new Node.
            next_node (Node): next node of new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Let's get and set data of Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data should be integer")
        self.__data = value

    @property
    def next_node(self):
        """we get and set next_node of Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node should be Node object")
        self.__next_node = value


class SinglyLinkedList:
    """We have our singly-linked list."""

    def __init__(self):
        """Our new Singly Linked List is initialized."""
        self.__head = None

    def sorted_insert(self, value):
        """We put Node to SinglyLinkedList.

        at correct position.

         value (Node): new Node to put.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """We define print() of Singly Linked List."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
