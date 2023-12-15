def power(s):
    set = {frozenset({})}
    for num in s:
        subsets_with_element = {subset.union({num}) for subset in set}
        set.update(subsets_with_element)
    return set

s = set([1, 2, 3, 4])
print(power(s))