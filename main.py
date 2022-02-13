"""
Digit factorials
https://projecteuler.net/problem=34
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""

import math


def digit_factorials_1():
    f = [math.factorial(i) for i in range(10)]
    r = 0
    for i in range(3, 1000000):
        # x = list(int(c) for c in str(i))
        # r = sum(f[n] for n in (int(c) for c in str(i)))
        if sum(f[int(c)] for c in str(i)) == i:
            r += i
            # print(r, ' = ', x)
    return r


if __name__ == '__main__':
    print(digit_factorials_1())

    # import timeit
    # print(min(timeit.repeat(stmt=digit_factorials_1, number=10, repeat=5)))  #
