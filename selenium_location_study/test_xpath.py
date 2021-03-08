'''
实例：打开百度页面，使用xpath定位，输入'xpath定位'完毕后，暂停三秒后，退出浏览器
'''
#导入selenium包
from selenium import webdriver
#导入时间包
from time import sleep
#实例化浏览器
driver = webdriver.Firefox()
#打开地址
driver.get("https://www.baidu.com")
#使用xpath元素路径定位并发送数据
#元素属性定位，ID是元素的唯一属性
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('xpath定位')
#属性与层级集合，当所定位的元素没有任何属性时，可以利用父级元素来定位
driver.find_element_by_xpath('//p[@id="p1"]/input')
#属性与逻辑相结合，定位元素与其他元素属性重合，可多个属性配合使用
driver.find_element_by_xpath("//*[@id='kw' and class = 'k']")
#绝对定位，从最外层元素开始定位，以/开头
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div/form/span[1]')
#相对定位，一般与元素属性配合使用，以//开头
#暂停三秒
sleep(3)
#退出浏览器
driver.quit()