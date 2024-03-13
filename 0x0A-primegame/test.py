#!/usr/bin/python3
"""
Test cases for prime game
"""


import unittest

isWinner = __import__('0-prime_game').isWinner

class TestWinner(unittest.TestCase):

    def test_odd_primes(self):
        self.assertEqual(isWinner(5, [1, 1, 1, 1, 1]), "Ben")

    def test_even_primes(self):
        self.assertEqual(isWinner(5, [2, 2, 2, 2, 2]), "Maria")

    def test_not_equal_rounds(self):
        self.assertEqual(isWinner(3, [1, 1, 1, 2, 2, 2, 2]), "Ben")

    def test_not_equal_rounds_2(self):
        self.assertEqual(isWinner(5, [1, 1, 1]), "Ben")

    def test_not_equal_rounds_3(self):
        self.assertEqual(isWinner(5, [2, 2, 2]), "Maria")

    def test_tie(self):
        self.assertEqual(isWinner(0, [1, 1, 1]), None)

    def test_odd_very_big(self):
        self.assertEqual(isWinner(1, [9967]), "Ben")

    def test_even_very_big(self):
        self.assertEqual(isWinner(1, [10000]), "Maria")

    def test_no_primes_1(self):
        self.assertEqual(isWinner(1, [-1]), "Ben")

    def test_no_primes_2(self):
        self.assertEqual(isWinner(1, [0]), "Ben")

    def test_no_primes_3(self):
        self.assertEqual(isWinner(1, []), "Ben")

    def test_wrong_argument_1(self):
        self.assertEqual(isWinner(1, "Hello"), None)

    def test_wrong_argument_2(self):
        self.assertEqual(isWinner(1, ["Hello"]), None)

    def test_wrong_argument_3(self):
        self.assertEqual(isWinner(2, [1, "Hello"]), "Ben")
if __name__ == '__main__':
    unittest.main()
