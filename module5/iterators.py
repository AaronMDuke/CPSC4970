import unittest


class OddIterator:
    def __init__(self, it):
        self._values = []
        for x in it:
            if x % 2 != 0:
                self._values.append(x)
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._values):
            raise StopIteration
        value = self._values[self._index]
        self._index += 1
        return value


class Last:
    def __init__(self, it, count):
        all_values = list(it)
        self._values = []
        start = len(all_values) - count
        if start < 0:
            start = 0
        for i in range(start, len(all_values)):
             self._values.append(all_values[i])
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._values):
            raise StopIteration
        value = self._values[self._index]
        self._index += 1
        return value



class TestOddIterator(unittest.TestCase):
    def test_list(self):
        result = list(OddIterator([2, 3, 7, 6, 12, 19]))
        self.assertEqual(result, [3, 7, 19])

    def test_empty_list(self):
        result = list(OddIterator([]))
        self.assertEqual(result, [])

    def test_for_loop(self):
        result = []
        for i in OddIterator([2, 3, 7, 6, 12, 19]):
             result.append(i)
        self.assertEqual(result, [3, 7, 19])



class TestLast(unittest.TestCase):
    def test_list(self):
        result = list(Last([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
        self.assertEqual(result, [7, 8, 9])

    def test_empty_list(self):
        result = list(Last([], 3))
        self.assertEqual(result, [])

    def test_for_loop(self):
        result = []
        for i in Last([1, 2, 3, 4, 5, 6, 7, 8, 9], 3):
            result.append(i)
        self.assertEqual(result, [7, 8 , 9])


if __name__ == '__main__':
    unittest.main()


