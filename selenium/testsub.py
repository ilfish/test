from count import Count
import unittest

class TestSubtraction(unittest.TestCase):
    def setUp(self):
        pass

    def test_subtraction(self):
        self.j=Count(2,3)
        self.sub=self.j.subtraction()
        self.assertEqual(self.sub,-1)


    def test_subtraction2(self):
        self.j=Count(2.2,4.2)
        self.sub=self.j.subtraction()
        self.assertEqual(self.sub,-2)

    def tearDown(self):
        pass

if __name__=='__main__':
    suite=unittest.TestSuite()
    suite.addTest(TestSubtraction("test_subtraction"))
    suite.addTest(TestSubtraction("test_subtraction2"))

    runner=unittest.TextTestRunner()
    runner.run(suite)
