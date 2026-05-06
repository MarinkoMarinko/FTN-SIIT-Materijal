class Node():
    def __init__(self, val, next = None):
        self._val = val
        self._next = next


class EmptyList(Exception):
    pass

class OutOfRange(Exception):
    pass

class List():
    def __init__(self):
        self._head = self._tail = None
    
    def __len__(self):              # O(n)
        if self._head is None:
            return 0
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current._next
        return count

    def __str__(self):             # O(n)
        if len(self) == 0:
            return "List is empty!"
        result = []
        current = self._head
        while current is not None:
            result.append(current._val)
            current = current._next
        return str(result)
    
    def add_first(self, val):       # O(1)
        new = Node(val)
        if self._head is None:
            self._head = self._tail = new
        else:
            new._next = self._head
            self._head = new

    def add_last(self, val):        # O(1)
        new = Node(val)
        if self._tail is None:
            self._head = self._tail = new
        else:
            self._tail._next = new
            self._tail = new

    def add_at(self, val, index):       # O(n)
        if index < 0 or index > len(self):
            raise OutOfRange("Index is out of range!")
        if index == 0:
            self.add_first(val)
        elif index == len(self):
            self.add_last(val)
        else:
            current_index = 1
            prev = self._head
            current = self._head._next
            while current_index != index:
                prev = prev._next
                current = current._next
                current_index += 1
            new = Node(val, current)
            prev._next = new
        
    def remove_first(self):         # O(1)
        if len(self) == 0:
            raise EmptyList("List is already empty!")
        if self._head == self._tail:
            self._head = self._tail = None
        else:
            self._head = self._head._next

    def remove_last(self):          # O(n)
        if len(self) == 0:
            raise EmptyList("List is already empty!")
        if self._head == self._tail:
            self._head = self._tail = None
        else:
            current = self._head
            while current._next != self._tail:
                current = current._next
            self._tail = current
            self._tail._next = None
        
    def remove_at(self, index):     # O(n)
        if len(self) == 0:
            raise EmptyList("List is already empty!")
        if index < 0 or index >= len(self):
            raise OutOfRange("Index is out of range!")
        if index == 0:
            self.remove_first()
        elif index == len(self) - 1:
            self.remove_last()
        else:
            count_index = 1
            prev = self._head
            current = self._head._next
            while count_index != index:
                prev = prev._next
                current = current._next
                count_index += 1
            prev._next = current._next

    def reverse_list(self):         # O(n)
        prev = None
        current = self._head
        while current is not None:
            next = current._next
            current._next = prev 
            prev = current
            current = next
        self._head, self._tail = self._tail, self._head
    
    @staticmethod
    def merge_lists(list_1, list_2):
        if len(list_1) == 0 and len(list_2) == 0:
            return None
        if len(list_1) != 0 and len(list_2) == 0:
            return list_1
        if len(list_1) == 0 and len(list_2) != 0:
            return list_2
        list_1._tail._next = list_2._head
        list_1._tail = list_2._tail
        return list_1
if __name__ == "__main__":
    linked_list1 = List()
    linked_list1.add_first(1)
    linked_list1.add_first(2)
    linked_list1.add_last(3)
    linked_list1.add_last(4)
    linked_list1.add_at(10, 4)
    
    linked_list2 = List()
    linked_list2.add_last(5)
    linked_list2.add_last(6)
    linked_list2.add_last(7)
    linked_list2.add_last(8)
    merged_list = List.merge_lists(linked_list1, linked_list2)
    print(merged_list)