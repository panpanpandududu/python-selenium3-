'''
实例：打开百度页面，使用css定位，输入'css定位'完毕后，暂停三秒后，退出浏览器
'''
#导入selenium包
from selenium import webdriver
#导入时间包
from time import sleep
#实例化浏览器
driver = webdriver.Firefox()
#打开地址
driver.get("https://www.baidu.com")

#ID选择器，以#开头
#driver.find_element_by_css_selector('#kw').send_keys('css选择器之ID定位')
#class选择器 以 .开头
#driver.find_element_by_css_selector('.s_ipt').send_keys('css选择器之class定位')
#属性选择器
driver.find_element_by_css_selector('[name="wd"]').send_keys('css选择器之属性选择器定位')
#层级选择器
driver.find_element_by_css_selector('span input').send_keys('css选择器之层级选择器定位')

#暂停三秒
sleep(3)
#退出浏览器
driver.quit()