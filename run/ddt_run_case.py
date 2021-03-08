import ddt
import unittest
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)
from selenium import webdriver
#from setting import setting
from business.register_business import RegisterBusiness
from util.handle_excel import Excel_Opertion
from util.HTMLTestRunner import HTMLTestRunner

ex_opr = Excel_Opertion()  # 实例化
ex_data = ex_opr.get_data()  # 获取excel表中每行数据

@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://www.5itest.cn/register')
        cls.driver.maximize_window()
        cls.file_name = base_path+'/image/imooc.png'
        cls.RegisterBusiness = RegisterBusiness(cls.driver)

    def setUp(self):
        self.driver.refresh()

    def tearDown(self):
        for method_name, error in self._outcome.errors:  # case如果执行失败，错误会保存到_outcome.errors 中
            if error:
                # case_name = self._testMethodName  # case名，即定义好的方法名
                report_error_name = self.assertCode + '.png'
                report_error_path = os.path.join(base_path, 'report', report_error_name)
                self.driver.save_screenshot(report_error_path)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    @ddt.data(*ex_data)
    def test_register_case(self,ex_data):   # ex_data:[[],[],..] 列表套列表
        """数据驱动模式，会按ex_data列表数据，一行一行循环执行，直至列表数据执行完毕"""
        email, username, password, self.assertCode, assertText = ex_data  # 将ex_data每个子列表的数据按顺序赋值。验证码需要提供路径，单独给
        # 邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息
        register_error = self.RegisterBusiness.register_function(email, username, password, self.file_name,self.assertCode, assertText)
        self.assertFalse(register_error,"测试失败：{}".format(self.assertCode))