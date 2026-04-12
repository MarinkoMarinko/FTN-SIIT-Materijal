def replicate(num, count):                      # O(n^2)
    if count <= 0:
        return []
    return [num] + replicate(num, count - 1)

if __name__ == "__main__":
    num = 5
    count = 6
    print(replicate(num, count))