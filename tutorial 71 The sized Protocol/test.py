import unittest
from sorted_set import SortedSet

class TestContruction(unittest.TestCase):
    def test_empty(self):
        s = SortedSet([])

    def test_from_sequence(self):
        s= SortedSet([7,8,3,1])
    def test_with_duplicates(self):
        s= SortedSet([8,8,8])
    def test_from_iterable(self):
        def gen6842():
            yield 6
            yield 8
            yield 4
            yield 2
        g= gen6842()
        s =SortedSet(g)

    def test_default_empty(self):
        s = SortedSet()

class TestContainerProtocol(unittest.TestCase):
    def setUp(self):
        self.s = SortedSet([6,7,3,9])
    def test_pos_cont(self):
        self.assertTrue(6 in self.s)
    def test_neg_cont(self):
        self.assertFalse(2 in self.s)
    def test_pos_not_cont(self):
        self.assertTrue(5 not in self.s)
    def test_neg_not_cont(self):
        self.assertFalse(9 not in self.s)

class TestSizedProtocol(unittest.TestCase):
    def test_empty(self):
        s = SortedSet()
        self.assertEqual(len(s), 0)

    def test_one(self):
        s = SortedSet([42])
        self.assertEqual(len(s),1)
    def test_ten(self):
        s = SortedSet(range(10))
        self.assertEqual(len(s),10)
    def test_with_duplicates(self):
        s= SortedSet([5,5,5])
        self.assertEqual(len(s), 1)



if __name__ == '__main__':
    unittest.main()


















