#操作层（对页面进行的操作）,如输入，获取信息等

from page.register_page import RegisterPage
class RegisterHandle():
    def __init__(self,driver):
        self.page= RegisterPage(driver)

    #输入用户名
    def send_name(self,name):
        self.page.get_name().send_keys(name)

    #输入邮箱
    def send_email(self,email):
        self.page.get_email().send_keys(email)

    #输入密码
    def send_password(self,password):
        self.page.get_password().send_keys(password)

    #输入验证码
    def send_code(self,code):
        self.page.get_code().send_keys(code)

 # 获取错误信息（获取到注册页中的错误信息）
    def get_user_text(self, info, user_info):
        text = None
        try:
            if info == "email_error":
                text = self.page.get_email_error().text
            elif info == "username_error":
                text = self.page.get_name_error().text
            elif info == "password_error":
                text = self.page.get_password_error().text
            elif info == "captcha_code_error":
                text = self.page.get_code_error().text
            else:
                print("你的错误无法解决，本猿无能为力......")
        except:
            text =None
        return text

    # 点击注册按钮
    def click_register_button(self):
        self.page.get_button().click()


    # 获取注册按钮的文字
    def get_register_text(self):
        return self.page.get_button().text

