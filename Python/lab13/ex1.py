def mem(n, l):
    if not l:
        return False
    else:
        return n == l[0] or mem(n, l[1:])

print(mem(2,[1,2,3]))