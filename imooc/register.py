import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
from time import sleep
from selenium import webdriver
import random 
from PIL import Image
from ShowapiRequest import ShowapiRequest  #提高文字识别率，当文字受干扰因素多时
from find_element import findElements

class registerFuction():
    def __init__(self,url):
        self.driver = self.get_driver(url)

    '''获取driver并且打开URL'''
    def get_driver(self,url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        return driver

    '''输入用户信息'''
    def send_user_info(self,key,data):
        self.get_user_element(key).send_keys(data)

    '''定位用户信息，获取元素element'''
    def get_user_element(self,key):
        user_element = findElements.get_element(key,self.driver )
        return user_element


    '''获取随机数'''
    def get_range_user(self):
        # user_info = random.sample('12345abcds',8)
        #  print(user_info,type(user_info))  <class 'list'>
        user_info = ''.join(random.sample('12345abcds',8))
        #print(type(user_info))   <class 'str'>
        return user_info
 
    '''获取图片'''
    def get_code_image(self,file_path):
        '''
        整个页面图片 ->根据坐标裁出验证码图片  ->保存
        '''
        self.driver.save_screenshot(file_path)
        #验证码图片的坐标
        code_element = self.get_user_element('code_image')
        location = code_element.location()
        left = location['x']
        top = location['y']
        right = code_element.size['width'] + left
        bottom = code_element.size['width'] + top
        #载入图像文件
        im = Image.open(file_path)
        #切割出验证码图
        rangle = (int(left), int(top), int(right),int(bottom)) 
        img = im.crop(rangle)
        img.save(file_path)
    
    '''解析图片获取验证码'''
    def code_online(self,image_path):
        self.get_code_image(image_path)
        r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5")
        r.addBodyPara("typeId","35")  #5个文字
        r.addBodyPara("convert_to_jpg","0")
        # 定义图片文件上传设置：
        r.addFilePara("image",image_path)
        #访问接口，返回数据
        res = r.post()  
        #从json提炼出有效的数据，即验证码
        text = res.json()['showapi_res_body']['result']
        return text

    def main(self):
        user_name = self.get_range_user()
        user_email = self.get_range_user()+'163.com'
        file_path = base_path+'/image/imooc1.png'
        code_text = self.code_online(file_path)
        self.send_user_info('user_name',user_name)
        self.send_user_info('user_email',user_email)
        self.send_user_info('password','111111')
        self.send_user_info('code_text',code_text)
        self.get_user_element('register_btn').click()
        code_error = self.get_user_element('code_text_error')
        if code_error ==None:
            print('测试通过')
        else:
            self.driver.save_screenshot(file_path)
        sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    register = registerFuction("http://www.5itest.cn/register")
    register.main()



        


