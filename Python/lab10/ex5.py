def merge(list1, list2):
    one = 0
    two = 0
    result = []
    while True:
        if one >= len(list1):
            result.extend(list2[two:])
            break
        if two >= len(list2):
            result.extend(list1[one:])
            break
        if list1[one] < list2[two]:
            result.append(list1[one])
            one += 1
        elif list1[one] > list2[two]:
            result.append(list2[two])
            two += 1
        elif list1[one] == list2[two]:
            result.append(list1[one])
            result.append(list2[two])
            one += 1
            two += 1
        else:
            result.append(list1[one])
            one += 1
            two += 1

    print(result)

list1 = [1,1,1,1,8,8,8,8,8,15,15,15]
list2 = [2,4,6,8,10]
merge(list1, list2)