import unittest
def creatsuite():
    testunit=unittest.TestSuite()
    test_dir='E:\Temp\\unit'
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py',top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit
if __name__=='__main__':
    test_unit=creatsuite()
    runner=unittest.TextTestRunner()
    runner.run(test_unit)


# Python all_test.py >> log.txt 2>&1
# Python all_test.py 通过Python 执行all_test 文件
# >>report/log.txt 将测试输出写入到report 目录下的log.txt 文件中
# file 2>&1 标准输出被重定向到文件file，然后错误输出也重定向到和标准输出一样，所以错误输出也写入文件file。
