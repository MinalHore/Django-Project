import unittest
class MyTestCase(unittest.TestCase):
    def test_addition(self):
        result=10 +10
        self.assertEqual(result,20)