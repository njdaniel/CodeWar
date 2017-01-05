def comp(array1, array2):
    p= []
    for i, j in zip(array1, array2):
        if (i & j) or (i % j == 0) or (j % i == 0):
            p.append(i)
    if len(array1) == len(p):
        return True
    return False


a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
print(comp(a, b))