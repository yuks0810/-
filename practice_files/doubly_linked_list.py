from __future__ import annotations
from typing import  Any, Optional

class Node(object):
    def __init__(self, data: Any, next_node: Node = Node, prev_node: Node: = None) -> None:
        self.data = data
        self.next = next_node
        self.prev = prev_node

class DoublyLinkedList(object):

    def __init__(self, head: Node = None) -> None:
        self.head = head

    def appned(self, head: Node = Any ) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node
