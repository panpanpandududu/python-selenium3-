'''
实例：打开百度页面，使用ID定位，输入'测试是否可行'完毕后，暂停三秒后，退出浏览器
'''
#1.导入selenium包
from selenium import webdriver
#导入时间包
from time import sleep
#实例化浏览器
driver = webdriver.Firefox()
#打开项目
driver.get("https://www.baidu.com")
#调用ID定位方法,定位文本框ID
text_element = driver.find_element_by_id('kw')
#使用send_keys()发送数据
text_element.send_keys('测试是否可行')
#暂停3秒
sleep(3)
#退出浏览器
driver.quit()

