import unittest

from lesson2.task1.task import summa


# todo: replace this with an actual test


class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(summa(1, 2), 3, msg="adds 1 + 2 to equal 3")
