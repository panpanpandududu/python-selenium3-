#业务层，执行操作
'''
根据我们的测试业务需求，哪些场景下需要进行测试；
这里以异常输入场景的错误提示为测试点进行业务的封装。
'''
from handle.register_handle import RegisterHandle
class RegisterBusiness():
    def __init__(self, driver):
        self.register_handle = RegisterHandle(driver)

    #执行操作：输入信息
    def user_base(self, email, name, password, code):
        self.register_handle.send_email(email)
        self.register_handle.send_name(name)
        self.register_handle.send_password(password)
        self.register_handle.send_code(code)
        self.register_handle.click_register_button()

    #注册成功,根据注册按钮文字
    def register_success(self):
        if self.register_handle.get_register_text() == None:
            return True
        else:
            return False

    # 数据驱动，只执行此条代码
    # 邮箱、用户名、密码、验证码、错误信息定位元素、错误提示信息
    def register_function(self,email,username,password,code,assertCode,assertText):
        self.user_base(email,username,password,code)
        if self.register_handle.get_user_text(assertCode,assertText) == None:
            return True
        else:
            return False

    '''
    # 邮箱错误
    def login_email_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        if self.register_handle.get_user_text("email_error", "请输入有效的电子邮件地址") == None:
            print("邮箱校验不成功")
            return True
        else:
            return False

    # 用户名错误
    def login_username_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        if self.register_handle.get_user_text("username_error", "字符长度必须大于等于4，一个中文字算2个字符") == None:
            print("用户名校验不成功")
            return True
        else:
            return False

    # 密码错误
    def login_password_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        if self.register_handle.get_user_text("password_error", "最少需要输入 5 个字符") == None:
            print("密码校验不成功")
            return True
        else:
            return False

    # 验证码错误
    def login_code_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        if self.register_handle.get_user_text("password_error", "验证码错误") == None:
            print("验证码校验不成功")
            return True
    '''

