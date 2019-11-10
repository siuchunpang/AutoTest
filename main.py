import unittest
import time
from BeautifulReport import BeautifulReport
# from common import HTMLTestRunner
# from testcase.testEditPage import TestEditPage

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())

    test_suite = unittest.defaultTestLoader.discover('./testcase', pattern='test*.py')
    result = BeautifulReport(test_suite)
    result.report(filename=(now + '_Report.html'), description='测试报告', log_path='./report')

'''
    testunit = unittest.TestSuite()
    testunit.addTest(TestEditPage('testEdit'))

    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    # 定义报告输出路径
    filename = './report/' + now + '_Report.html'
    fp = open(filename, "wb")

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title='四维看看',
                                           description='测试用例结果')

    runner.run(testunit)

    fp.close()
'''

