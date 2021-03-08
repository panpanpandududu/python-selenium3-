#coding = utf-8
#查找元素，定位元素层
from base.find_element import findElement
class RegisterPage():
    def __init__(self,driver):
        self.find_element = findElement(driver)
    
    def get_name(self):
        return self.find_element.get_element('user_name')
    
    def get_email(self):
        return self.find_element.get_element('user_email')

    def get_password(self):
        return self.find_element.get_element('password')

    def get_code(self):
        return self.find_element.get_element('code_text')

    def get_button(self):
        return self.find_element.get_element('register_button')

    # 错误信息......
    # 获取邮箱栏错误提示
    def get_email_error(self):
        return self.find_element.get_element("register_email_error")

    # 获取用户名错误提示
    def get_name_error(self):
        return self.find_element.get_element("register_username_error")

    # 获取密码错误提示
    def get_password_error(self):
        return self.find_element.get_element("register_password_error")

    # 获取验证码错误提示
    def get_code_error(self):
        return self.find_element.get_element("captcha_code_error")

