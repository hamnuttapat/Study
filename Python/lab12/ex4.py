def subset(sup, sub):
    for i in sub:
        if i not in sup:
            return False
    return True
sup = set([1, 2, 3, 4])
sub = set([1, 2, 4])
print(subset(sup, sub))
