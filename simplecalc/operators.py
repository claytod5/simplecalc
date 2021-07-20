"""Main module."""

from functools import reduce
from operator import floordiv, mul, sub


def fibonacci(args):
    prev_two = 0
    prev_one = 1
    if args.n == 0:
        return 0
    elif args.n == 1:
        return 1
    else:
        for each in range(args.n - 1):
            res = prev_two + prev_one
            prev_two, prev_one = prev_one, res
        return res


def factorial(args):
    last = 1
    for i in range(2, args.n + 1):
        last *= i

    return last


def is_prime(args):
    if args.n <= 1:
        return False
    elif args.n == 2:
        return True
    elif args.n > 2 and args.n % 2 == 0:
        return False
    else:
        for i in range(3, int(args.n ** 0.5) + 1, 2):
            if args.n % i == 0:
                return False
        return True


def add(args):
    return sum(args.n)


def subtract(args):
    return reduce(sub, args.n)


def multiply(args):
    return reduce(mul, args.n)


def divide(args):
    return reduce(floordiv, args.n)


def power(args):
    return args.x ** args.y
