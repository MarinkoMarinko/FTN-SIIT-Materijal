import random
def rand_list(n):
    list = []
    for i in range(0, n):
        r = random.randint(1, 10)
        if r in list:
            i -= 1
        else:
            list.append(r)
    return list
def union(list1, list2):
    union_list = [num for num in list1]
    for num in list2:
        if num not in union_list:
            union_list.append(num)
    return union_list
def intersection(list1, list2):
    inter_list = []
    union_list = union(list1, list2)
    for num in union_list:
        if num in list1 and num in list2:
            inter_list.append(num)
    return inter_list
def difference(list1, list2):
    diff_list = [num for num in list1 if num not in list2]
    return diff_list
if __name__ == "__main__":
    n = random.randint(1, 10)
    m = random.randint(1, 10)
    list1 = rand_list(n)
    list2 = rand_list(m)
    print("Lista 1: ", list1)
    print("Lista 2: ", list2)
    print("Unija: ", union(list1, list2))
    print("Presek: ", intersection(list1, list2))
    print("Razlika: ", difference(list1, list2))