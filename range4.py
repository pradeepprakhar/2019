#!/usr/bin/python
a = {x:x*x for x in range(5)}
print a
b = 'the quick brown fox jumps rith over the lazy dog'

b = {x:b.count(x) for x in b }
print b
