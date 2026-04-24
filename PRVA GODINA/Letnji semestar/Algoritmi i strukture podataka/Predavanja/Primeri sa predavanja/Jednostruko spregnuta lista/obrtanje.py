class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_list(head):
    prev = None
    current = head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return print_list(prev)


def print_list(head):
    current = head
    result = []
    while current is not None:
        result.append(current.val)
        current = current.next
    print(result)


if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    a.next = b
    b.next = c
    c.next = d
    # a -> b -> c -> d
    
    reverse_list(a) # d -> c -> b -> a