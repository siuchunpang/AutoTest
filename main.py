import unittest
import os
import time
import datetime
from BeautifulReport import BeautifulReport
# from common import HTMLTestRunner
# from testcase.testEditPage import TestEditPage


def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    isExists = os.path.exists(path)

    if not isExists:
        os.makedirs(path)
        print("目录 " + path + " 创建成功")
    else:
        print("目录已存在")


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    today = datetime.date.today().strftime('%Y-%m-%d')

    mkpath = "./report/" + str(today)
    mkdir(mkpath)
    test_suite = unittest.defaultTestLoader.discover('./testcase', pattern='test*.py')
    result = BeautifulReport(test_suite)
    result.report(filename=(now + '_Report.html'), description='测试报告', log_path=mkpath)

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

