# -*- coding: utf-8 -*-


setA = {1,3,4,5}
setB = {1,2,3,4,5,7,8,9,6}

print(setA | setB)
print(setA.union(setB))

print(setA & setB)
print(setA.intersection(setB))

print(setB- setA)
print(setB.difference(setA))

print(setA ^ setB)
print(setA.symmetric_difference(setB))

