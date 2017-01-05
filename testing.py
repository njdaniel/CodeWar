vector = [[1,2], [3,4], [5,6], [7,8], [9,10]]
print( x for y in vector for x in y if x % 2 == 0)
