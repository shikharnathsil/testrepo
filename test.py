from __future__ import annotations

class Node:
    def __init__(self, name, content, previous, next) -> None:
        self.name = name
        self.content = content
        self.previous = previous
        self.next = next
    
    def addNode(self, name, content, previous=None, next=None, pos='last') -> Node:
        node = None
        if pos == 'last':
            node = Node(name=name, content=content, previous=previous, next=next)
            previous.next = node
        return node
    def __repr__(self) -> str:
        v, w = None, None
        if self.previous:
            v = self.previous.name
        if self.next:
            w = self.next.name
        return f'content={self.content}, previous={v}, next={w}'



