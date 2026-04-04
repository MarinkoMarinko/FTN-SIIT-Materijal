def array_linear_sum(arr):                          # O(n^2) - prihvata ~1000 elemenata
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    return arr[0] + array_linear_sum(arr[1:])


def array_binary_sum(arr):                          # O(n * logn) - prihvata vise elemenata od linearne
    arr_len = len(arr)
    if arr_len == 0:
        return 0
    elif arr_len == 1:
        return arr[0] 
    return array_binary_sum(arr[:arr_len // 2]) + array_binary_sum(arr[arr_len // 2: ])
        

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 7]
    print(array_linear_sum(arr))
    print(array_binary_sum(arr))