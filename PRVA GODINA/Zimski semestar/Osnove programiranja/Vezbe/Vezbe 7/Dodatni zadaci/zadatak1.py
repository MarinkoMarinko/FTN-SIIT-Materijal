if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    list2 = []
    list3 = []
    list4 = []
    list2.append(list1[0])
    list2.append(list1[-1]) 
    print(list2)
    list3.append(list1[0])
    list3.append(list1[int(len(list1) /2)])
    list3.append(list1[-1]) 
    print(list3)
    list4 = list1[::2]
    print(list4)