def get_the_difference():
    list1 = [3, 1, 1, 1, 2, 7]
    list2 = [4, 1, 1, 2, 2, 5]

    set1 = set(list1)
    set2 = set(list2)

    dif1 = list(set1.difference(set2))
    dif2 = list(set2.difference(set1))
    result=list(dif1+dif2)

    print (result)

get_the_difference()