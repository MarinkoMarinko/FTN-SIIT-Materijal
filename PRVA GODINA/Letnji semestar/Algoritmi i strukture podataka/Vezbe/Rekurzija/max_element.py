def max_element(array):                         # O(n^2)
    if len(array) == 0:
        return "List is empty!"
    elif len(array) == 1:
        return array[0]
    remaining_max = max_element(array[1:])
    if array[0] > remaining_max:
        return array[0]
    else:
        return remaining_max


if __name__ == "__main__":
    a = [3, -2, 5, 105, 1, 13, 2, 8]
    print(max_element(a))