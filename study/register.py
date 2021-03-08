import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
from time import sleep
from selenium import webdriver
driver = webdriver.Chrome()
import random
from PIL import Image
from imooc.ShowapiRequest import ShowapiRequest  #提高文字识别率，当文字受干扰因素多时

#1.浏览器初始化
def driver_init():
    driver.get("http://www.5itest.cn/register")
    driver.maximize_window()
    sleep(5)

#定位元素
def get_element(id):
    element = driver.find_element_by_id(id)
    return element

#获取随机数
def get_range_user():
    user_info = ''.join(random.sample('123456789abcdefg',8))
    return user_info

#获取验证码图片
def get_code_image(image_path,id):
    #获取验证码图片
    driver.save_screenshot(image_path)
    code_element = driver.find_element_by_id(id)
    location = code_element.location
    left = location['x']
    top =  location['y']
    right = code_element.size['width']+left
    bottom =  code_element.size['height']+top
    im = Image.open(image_path)
    rangle = (int(left),int(top),int(right),int(bottom))
    img = im.crop(rangle)
    img.save(image_path)
    
#解析图片,获取验证码
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

#运行主程序
def run_main():
    img_path = base_path+'/image/imooc1.png'
    username = get_range_user()
    email = username+'@163.com'
    driver_init()
    get_element('register_email').send_keys(email)
    get_element('register_nickname').send_keys(username)
    get_element('register_password').send_keys('111111')
    get_code_image(img_path,'getcode_num')
    get_element('captcha_code').send_keys(code_online(img_path))
    get_element('register-btn').click()
    sleep(3)
    driver.quit()

run_main()



    





 
