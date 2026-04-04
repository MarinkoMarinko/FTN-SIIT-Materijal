class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class List:
    def __init__(self):
        self.head = self.tail = None
    def add_first(self, elem):              # O(1)
        new_element = Node(elem, self.head)
        self.head = new_element
        if self.tail is None:
            self.tail = self.head
    def add_last(self, elem):               # O(1)
        new_element = Node(elem, None)
        if self.tail is not None:
            self.tail.next = new_element
        self.tail = new_element
        if self.head is None:
            self.head = self.tail
    def remove_first(self):           # O(1)
        if self.head is None:
            print("Cannot remove first element because list is already empty")
            return
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
    def remove_last(self):            # O(n)
        if self.head is None:
            print("Cannot remove first element because list is already empty")
            return
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            current.next = None
            self.tail = current
    def __str__(self):
        current = self.head
        while current is not None:
            print(current.value, end=" ")
            current = current.next

if __name__ == "__main__":
    list1 = List()
    list1.add_first(1)
    list1.add_first(2)
    list1.add_first(3)
    list1.add_first(4)
    list1.remove_last()
    list1.remove_last()
    list1.__str__()