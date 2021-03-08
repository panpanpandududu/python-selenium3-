'''
实例：打开百度页面，使用tag_name定位，输入'使用tag_name属性定位'完毕后，暂停三秒后，退出浏览器
'''
#导入selenium包
from selenium import webdriver
#导入时间包
from time import sleep
#实例化浏览器
driver = webdriver.Firefox()
#打开地址
driver.get("https://www.baidu.com")
#使用tag_name属性定位并发送数据
#注意：此时返回的是符合条件的第一个标签或着此页面唯一一个此标签
driver.find_element_by_tag_name('input').send_keys('使用tag_name属性定位')
#获取其他input标签，即需要给出input下标索引,如下指的是第二个input标签
#driver.find_element_by_tag_name('input')[1].send_keys('使用tag_name属性定位')

#暂停三秒
sleep(3)
#退出浏览器
driver.quit()