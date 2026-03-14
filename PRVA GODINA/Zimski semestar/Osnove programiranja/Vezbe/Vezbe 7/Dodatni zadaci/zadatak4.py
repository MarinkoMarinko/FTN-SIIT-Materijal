def udaljenost(nums, number):
    index_list = []
    for i in range(0, len(nums)):
        if nums[i] == number:
            index_list.append(i)
    if len(index_list) == 1:
        return 1
    return index_list[-1] - index_list[0] + 1
def maxUdaljenost(distances):
    return max(distances)
if __name__ == "__main__":
    nums = [1, 2, 1, 1, 3]
    distances = []
    for num in nums:
        distances.append(udaljenost(nums, num))
    print(maxUdaljenost(distances))