if __name__ == "__main__":
    nums = [3, 2, -1, 5, 12, 4, 17, 6, 25, 3, 2, -1]
    bigger = [i for i in nums if i > 10]
    print(bigger)
    divisible = [i for i in nums if i % 3 == 0]
    print(divisible)
    squares = [i**2 for i in nums]
    print(squares)
    no_duplicates = []
    for num in nums:
        if num not in no_duplicates:
            no_duplicates.append(num)
    print(no_duplicates)