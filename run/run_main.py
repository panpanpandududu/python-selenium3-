#coding = utf-8
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)
from selenium import webdriver
import unittest
import HTMLTestRunner
from business.register_business import RegisterBusiness
class FirstCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://www.5itest.cn/register")
        self.register_business = RegisterBusiness(self.driver)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_login_email_error(self):
        email_error = self.register_business.login_email_error('34', 'U1212', '12Test12', 'der56')
        self.assertFalse(email_error)
        # if email_error == True:
        #     print("注册成功了，此条 case 执行失败")
        # login('223', '1111')
        # 通过 assert 判断是否为 error

    def test_login_username_error(self):
        username = self.register_business.login_username_error("qqww@qq.com", "2", "Test@123", 'sdsds')
        self.assertFalse(username)

    def test_login_password_error(self):
        password = self.register_business.login_password_error("qqww@qq.com", "2gw", "2", 'sdsds')
        self.assertFalse(password)

    def test_login_code_error(self):
        code = self.register_business.login_code_error("qqww@qq.com", "2gw", "Test@123", 's')
        self.assertFalse(code)

    def test_login_success(self):
        success = self.register_business.register_success()
        self.assertFalse(success)


if __name__ == "__main__":
    #unittest.main()
    #识别测试用例
    case_path = base_path +'/run'
    discover = unittest.defaultTestLoader.discover(case_path,pattern='run_case_*.py')
    #执行测试用例
    #unittest.TextTestRunner(discover)
    #创建测试报告输出地址
    file_path = base_path+'/report/report.html'
    with open(file_path,'wb') as f:
        '''
        调用HTMLTestRunner模块下的HTMLTestRunner类，下面为几个参数
        stream 指定测试报告文件
　　     title 定义测试报告的标题
　　     description 定义测试报告的副标题
        '''
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='selenium自动化测试',description='this is test')
       #执行测试用例，通过HTMLTestRunner的run()方法来运行测试套件中的测试用例
        runner.run(discover)
