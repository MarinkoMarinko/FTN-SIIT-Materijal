def canBalance(nums):
    total = sum(nums)
    sum_left = 0
    for i in nums:
        sum_left += i
        if sum_left == total - sum_left:
            return True
    return False
if __name__ == "__main__":
    print(canBalance([1, 1, 1, 2, 1]))
    print(canBalance([2, 1, 1, 2, 1])) 
    print(canBalance([10, 10]))  