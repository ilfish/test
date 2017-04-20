from  count import Count
import unittest

class TestCount(unittest.TestCase):
    def setUp(self):
        self.j=Count(2,3)

    def test_add(self):
        self.add=self.j.add()
        self.assertAlmostEqual(self.add,5)

    def tearDown(self):
        pass

if __name__=='__main__':
#    unittest.main()

# 构造测试集
    suite=unittest.TestSuite()
    suite.addTest(TestCount('test_add'))

# 执行测试
    runner=unittest.TextTestRunner()
    runner.run(suite)
