def filter_list(l):
    new_l = []
    for i in l:
        if isinstance(i, int):
            new_l.append(i)
    return new_l

# a = [1, 2, 'a', 5]
# print(filter_list(a))
# This function
def find_outlier(integers):
    """This function the opposite """
    num_odd = 0
    num_even = 0
    for i in integers:
        if i % 2 == 1:
            num_odd += 1
        if i % 2 == 0:
            num_even += 1
    if num_odd > num_even:
        for i in integers:
            if i % 2 == 0:
                N = i
    if num_even > num_odd:
        for i in integers:
            if i % 2 == 1:
                N = i
    return N

def find_outlier_best(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]

def validate_pin(pin):
    for i in pin:
        if not i.isdigit():
            return False
    if len(pin) == 4 or len(pin) == 6:
        return True
    return False

def validate_pin_best(pin):
    return len(pin) in (4, 6) and pin.isdigit()

a = "1234"
aa = ".000"
b = "ert345"
c = "1234g"
print(validate_pin(a))
print(validate_pin(aa))
print(validate_pin(b))
print(validate_pin(c))

