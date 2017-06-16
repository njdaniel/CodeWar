from unittest import TestCase

true = True
false = False
ite = lambda x,y,z: y if x else z
TestCase.assertEqual(ite(true,'a','b'), 'a')
TestCase.assertEqual(ite(false,'a','b'), 'b')

