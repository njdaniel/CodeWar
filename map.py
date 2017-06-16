from Unittest import TestCase

items = [0, 1, 2]

new_items = map(lambda x: x + 1, items)

new_items2 = [x+1 for x in items]

# e ::= v    variable
#     | e(e)    application
#     | lambda v: e    abstraction


zero = lambda f : lambda x : x
succ = lambda a : lambda f : lambda x : f(a(f)(x))

add = lambda a : lambda b : a(succ)(b)

mul = lambda a : lambda b : a(add(b))(zero)

one = succ(zero)

exp = lambda a : lambda b : b(mul(a))(one)

# succ (zero) = lambda f : lambda x : f(zero(f)(x))
#             = lambda f : lambda x : f((lambda x : x)(x))
#             = lambda f : lambda x : f(x)
two = succ(one)
# two = lambda f : lambda x : f(f(x))
three = succ(two)
four = succ(three)
five = succ(four)

def nat_to_int(n):
    return n(lambda x : x + 1)(0)

print("zero=%d" % (nat_to_int(zero)))
print("one=%d" % (nat_to_int(one)))
print("two=%d" % (nat_to_int(two)))

print("one + two=%d" % (nat_to_int(add(one)(two))))
print("three * five=%d" % (nat_to_int(mul(three)(five))))

print("five ** three=%d" % nat_to_int(exp(five)(three)))

true = lambda x : lambda y : x
false = lambda x : lambda y : y
ite = lambda x : lambda y : lambda z : x(y)(z)

a,b = 'a','b'
TestCase.assertEqual(ite(true)(a)(b), a)
TestCase.assertEqual(ite(false)(a)(b), b)
