from pyDatalog import pyDatalog
import random
import sys
sys.set_int_max_str_digits(0)

#регистрация правил
pyDatalog.create_terms('X, Z, Y, Sm, div, Average, y, SumRand, resultMulti, result')

# Сумма
(y[X] == sum_(Y, for_each=Y)) <= ((Y._in(range_(X + 1))))
print(y[999] == Sm)



# Среднее
(div[X, Y] == Z) <= (X // Y == Z)
print(div[y[999], 999] == Average)



# Медиана
H = sorted([random.choice(range(999)) for i in range(100)])
print("Median: ", (H[49] + H[50]) / 2)



# Произведение
# for i in range(999):
#     pyDatalog.assert_fact('number', i)
#
# pyDatalog.assert_fact('multiply', (X, Y, result)) <= (X['number'] & Y['number'] & (result == X*Y))
#
# result = pyDatalog.ask('result')
# product = 1
# for r in result.answers:
#     product *= r[0]
# print(product)

import functools
print (functools.reduce(lambda a, b : a * b, [random.choice(range(99999)) for i in range(100)]))


