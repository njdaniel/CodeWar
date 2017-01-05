def comp(array1, array2):
    if not array1 or not array2:
        return False
    if len(array1) != len(array2):
        return False
    while(array1):
        for j,y in enumerate(array2):
            if array1[0]**2 == y:
                array1.pop(0)
                array2.pop(j)
        bob = len(array2)
        if j+2>len(array2):
            break
    if not array1:
        return True
    return False


a = [100, 144, 19, 161, 19, 144, 19, 11]
b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

print(comp(a, b))
