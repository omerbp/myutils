import unittest
from myutils import *


class MyUtilsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print "Running MyUtilsTest"

    def SetUp(self):
        pass

    def test_round_with_half(self):
        self.assertEqual(3, round_with_half(3))
        self.assertEqual(3, round_with_half(3.1))
        self.assertEqual(3.5, round_with_half(3.26))
        self.assertEqual(3.5, round_with_half(3.59))
        self.assertEqual(4, round_with_half(3.79))

    def test_rename_key(self):
        x = {1:1,2:2}
        rename_key(x,1,3)
        self.assertTrue(x.has_key(3))
        self.assertTrue(x.has_key(2))
        self.assertEqual(len(x),2)
        rename_key(x,3,3)
        self.assertTrue(x.has_key(3))
        self.assertTrue(x.has_key(2))
        self.assertEqual(len(x),2)

if __name__ == '__main__':
    unittest.main()
