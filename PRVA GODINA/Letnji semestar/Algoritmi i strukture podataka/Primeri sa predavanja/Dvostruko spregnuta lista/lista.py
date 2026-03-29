class Node:
    def __init__(self, previous, value, next):
        self.previous = previous
        self.value = value
        self.next = next


class List:
    def __init__(self):
        self.head = self.tail = None
    def add_first(self, value):                         # O(1)
        new_element = Node(None, value, self.head)
        if self.head is None:
            self.head = self.tail = new_element
        else:
            self.head.previous = new_element
            self.head = new_element
    def add_last(self, value):                          # O(1)
        new_element = Node(self.tail, value, None)
        if self.tail is None:
            self.head = self.tail = new_element
        else:
            self.tail.next = new_element
            self.tail = new_element
    def remove_first(self):                             # O(1)
        if self.head is None:
            print("Cannot remove element because list is empty!")
            return
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None
    def remove_last(self):                              # O(1)
        if self.tail is None:
            print("Cannot remove element because list is empty!")
            return
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
    def __str__(self):
        current = self.head
        while current is not None:
            print(current.value, end=" ")
            current = current.next


if __name__ == "__main__":
    list2 = List()
    list2.add_first(1)
    list2.add_first(2)
    list2.add_first(3)
    list2.add_first(4)
    list2.add_last(5)
    list2.add_last(6)
    list2.add_last(7)
    list2.add_last(8)
    list2.remove_first()
    list2.remove_first()
    list2.remove_last()
    list2.__str__()