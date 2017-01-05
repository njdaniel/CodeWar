def persist(n):
    jump = 0
    product = 1
    SINGLE = [0,1,2,3,4,5,6,7,8,9]
    while n not in SINGLE:
        num_list = [int(x) for x in str(n)]
        if len(num_list)>1:
            for i in num_list:
                product*=i
            n = product
            product = 1
            jump+=1
    return jump

n = 39
print(persist(n))


import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i
