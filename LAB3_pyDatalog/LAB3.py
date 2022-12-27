from pyDatalog import pyDatalog
import random

pyDatalog.create_terms('X, Z, Y, Sm, div, Average, y, SumRand')

# Сумма
(y[X] == sum_(Y, for_each=Y)) <= ((Y._in(range_(X + 1))))
print(y[999999] == Sm)

