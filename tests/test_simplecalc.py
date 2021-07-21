#!/usr/bin/env python

"""Tests for `simplecalc` package."""

import argparse
import unittest

from simplecalc import operators


class TestOperations(unittest.TestCase):

    fibo_cases = [
        (0, 0),
        (1, 1),
        (10, 55),
        (23, 28657),
        (132, 1725375039079340637797070384),
    ]

    factorial_cases = [
        (0, 1),
        (1, 1),
        (2, 2),
        (5, 120),
        (10, 3628800),
        (32, 263130836933693530167218012160000000),
    ]

    is_prime_cases = [
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (701, True),
        (1061, True),
        (361998638781583, True),
    ]

    def setUp(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("n", type=int)

    def test_fibonacci(self):
        for each in self.fibo_cases:
            with self.subTest():
                args = self.parser.parse_args([f"{each[0]}"])
                self.assertEqual(operators.fibonacci(args), each[1])

    def test_factorial(self):
        for each in self.factorial_cases:
            with self.subTest():
                args = self.parser.parse_args([f"{each[0]}"])
                self.assertEqual(operators.factorial(args), each[1])

    def test_is_prime(self):
        for each in self.is_prime_cases:
            with self.subTest():
                args = self.parser.parse_args([f"{each[0]}"])
                self.assertEqual(operators.is_prime(args), each[1])


class TestBasicOps(unittest.TestCase):

    add = [
        ([0, 0], 0),
        ([1, 0], 1),
        ([30, 25], 55),
        ([30, 25, 100], 155),
        ([-10, 25, 100], 115),
    ]

    sub = [
        ([0, 0], 0),
        ([1, 0], 1),
        ([30, 25], 5),
        ([30, 25, 100], -95),
        ([-10, 25, 100], -135),
        ([100, 25, 10], 65),
    ]

    mul = [([1, 1], 1), ([2, 3], 6), ([2, 2, 2], 8), ([123, 131, 3], 48339)]

    div = [([1, 1], 1), ([8, 2], 4), ([100, 25], 4), ([154, 2], 77), ([10265, 5], 2053)]

    def setUp(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("n", type=int, nargs="+")

    def test_add(self):
        for each in self.add:
            with self.subTest():
                args = self.parser.parse_args([str(i) for i in each[0]])
                self.assertEqual(operators.add(args), each[1])

    def test_subtract(self):
        for each in self.sub:
            with self.subTest():
                args = self.parser.parse_args([str(i) for i in each[0]])
                self.assertEqual(operators.subtract(args), each[1])

    def test_multiply(self):
        for each in self.mul:
            with self.subTest():
                args = self.parser.parse_args([str(i) for i in each[0]])
                self.assertEqual(operators.multiply(args), each[1])

    def test_divide(self):
        for each in self.div:
            with self.subTest():
                args = self.parser.parse_args([str(i) for i in each[0]])
                self.assertEqual(operators.divide(args), each[1])


class TestPower(unittest.TestCase):

    pow = [([2, 3], 8), ([10, 4], 10000), ([2, 32], 4_294_967_296)]

    def setUp(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("x", type=int)
        self.parser.add_argument("y", type=int)

    def test_power(self):
        for each in self.pow:
            with self.subTest():
                args = self.parser.parse_args([str(i) for i in each[0]])
                self.assertEqual(operators.power(args), each[1])


if __name__ == "__main__":
    unittest.main()
