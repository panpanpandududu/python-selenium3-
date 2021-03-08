import sys
import os
base_path = os.getcwd()
sys.path.append(base_path)
from selenium import webdriver
from time  import sleep
import random
from PIL import Image
import pytesseract
from ShowapiRequest import ShowapiRequest  #提高文字识别率，当文字受干扰因素多时

#1.实例化浏览器
driver = webdriver.Chrome()
driver.maximize_window()
#2.请求打开测试网址
driver.get("http://www.5itest.cn/register")
'''
#3.邮箱定位
email_element = driver.find_element_by_id('register_email')
#输入注册邮箱号
email_element.send_keys('1378190284@qq.com')
#获取到已填入的邮箱用户信息
print(email_element.get_attribute('value'))
'''

'''
随机注册用户邮箱
思路：python中的random模块
'''

'''
获取验证码
思路:获取整个页面图片，然后通过坐标裁剪验证码片段 ；python中的pillow库对图像进行处理
'''
image_path = base_path+'/imooc_selenium/image/imooc.png'
driver.save_screenshot(image_path)
#location返回一个坐标字典，size返回一个宽高字典
code_element = driver.find_element_by_xpath('//*[@id="getcode_num"]')
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width']+left
bottom= code_element.size['height']+top
#打开图片 open
im = Image.open(image_path)
#裁剪图片
rangle = (int(left), int(top), int(right),int(bottom))    
img = im.crop(rangle)
#保存只含验证码的图片
img.save(base_path+'/imooc_selenium/image/imooc1.png')
#解析图片上的文字
r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5")
r.addBodyPara("typeId","35")  #5个文字
r.addBodyPara("convert_to_jpg","0")
# 定义图片文件上传设置：
r.addFilePara("image",image_path)
#访问接口，返回数据
res = r.post()  
#从json提炼出有效的数据，即验证码
text = res.json()['showapi_res_body']['result']
#等待时间
sleep(3)
#将解析后的验证码填入input框
driver.find_element_by_id('captcha_code').send_keys(text)
sleep(3)
#关闭浏览器
driver.quit()