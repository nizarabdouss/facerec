from typing import Optional

class _Node:
    """A node in a linked list.
    === Attributes ===
    item: The data stored in this node.
    next: The next node in the list, or None if there are
    no more nodes in the list.
    """
    item: any
    next: Optional[any]
    def __init__(self, item: any) -> None:
        """Initialize a new node storing <item>,
        with no 'next' node.
        """
        self.item = item
        self.next = None

    def __str__(self) -> str:
        """Return a string representation of this list."""
        pass

    def get_next(self) -> Optional[any]:
        return self.next

    def set_next(self, next) -> None:
        if isinstance(next, _Node):
            self.next = next
        else:
            print("Incorrect Type")

class LinkedList:
    """A linked list implementation of the List ADT."""
    # === Private Attributes ===
    # _first:
    # The first node in the linked list,
    # or None if the list is empty.
    _first: Optional[_Node]
    def __init__(self, items: list) -> None:
        """Initialize a linked list with the given items.
        The first node in the linked list contains the
        first item in <items>."""
        self._first = _Node(items)

    def __contains__(self, item: any) -> bool:
        """Return whether <item> is in this list.
        Use == to compare items."""
        curr = self._first
        while curr is not None:
            if curr.item == item: 
                return True
            curr = curr.get_next()
        return False
        
    def remove(self, item: any) -> None:
        """Remove the FIRST occurrence of <item> in this list.
        Do nothing if this list does not contain <item>."""
        if self.contains(item):
            curr = self._first
            while curr.get_next != item:
                curr = curr.get_next()
            curr.set_next(curr.get_next().get_next())

L = LinkedList("Genesis")
print(L._first.item)