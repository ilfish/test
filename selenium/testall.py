import unittest
import testadd
import testsub

# suite=unittest.TestSuite()
#
# suite.addTest(testadd.TestAdd("test_add"))
# suite.addTest(testadd.TestAdd("test_add2"))
# suite.addTest(testadd.TestAdd("test_add3"))
#
# suite.addTest(testsub.TestSubtraction("test_subtraction"))
# suite.addTest(testsub.TestSubtraction("test_subtraction2"))
#
# if __name__=='__main__':
#     runner=unittest.TextTestRunner()
#     runner.run(suite)


def creatsuite():
    testunit=unittest.TestSuite()
    # 定义测试文件查找的目录
    test_dir='E:\Temp\selenium'
    # 定义discover方法的参数
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py',top_level_dir=None)
    # discover方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit
if __name__=='__main__':
    testunit=creatsuite()
    runner=unittest.TextTestRunner()
    runner.run(testunit)
