import unittest


def fibonacci():
    a = 1
    b = 1
    while True:
        yield a
        next = a + b
        a = b
        b = next


class TestFibonacci(unittest.TestCase):
    def test_range_five(self):
        it = fibonacci()
        result = []
        for i in range(5):
            result.append(next(it))
        self.assertEqual(result, [1, 1, 2, 3, 5])


    def test_first(self):
        it = fibonacci()
        self.assertEqual(next(it), 1)


    def test_for_loop(self):
        result = []
        for i in fibonacci():
            result.append(i)
            if i >= 5:
                break
        self.assertEqual(result, [1, 1, 2, 3, 5])


if __name__ == '__main__':
    unittest.main()
