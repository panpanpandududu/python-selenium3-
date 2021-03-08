'''
实例：打开百度页面，使用name定位，输入'使用name属性定位'完毕后，暂停三秒后，退出浏览器
'''
#导入selenium包
from selenium import webdriver
#导入时间包
from time import sleep
#实例化浏览器
driver = webdriver.Firefox()
#打开地址
driver.get("https://www.baidu.com")
#使用name属性定位
elename = driver.find_element_by_name('wd')
#发送数据
elename.send_keys('使用name属性定位')
#暂停三秒
sleep(3)
#退出浏览器
driver.quit()