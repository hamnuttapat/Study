def subsetsum(listnum):
    if not listnum:
        return []
    set = {frozenset({})}
    for num in listnum:
        subsets_with_element = {subset.union({num}) for subset in set}
        set.update(subsets_with_element)
    result = subsetsum(listnum[1:])
    for i in set:
        if sum(n for n in list(i)) == 0 and len(i) > 0 and list(i) not in result:
            result.append(list(i))
    return result


print(subsetsum([-7,-3,-2,5,7]))