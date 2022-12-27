from pyDatalog import pyDatalog
import random

pyDatalog.create_terms('X, Z, Y, Sm, div, Average, y, SumRand')

# Сумма
(y[X] == sum_(Y, for_each=Y)) <= ((Y._in(range_(X + 1))))
print(y[999999] == Sm)

# Среднее
(div[X, Y] == Z) <= (X // Y == Z)
print(div[y[999999], 999999] == Average)

# Медиана
H = sorted([random.choice(range(99999)) for i in range(100)])
print("Median: ", (H[49] + H[50]) / 2)


