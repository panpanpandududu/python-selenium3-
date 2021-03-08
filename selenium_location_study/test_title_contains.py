'''使用title_contains检查页面是否正确'''
#导入selenium包
from selenium import webdriver
#导入时间等待组件 强制等待
from time import sleep   
#导入expected_conditions预期包判断标题是否正确
from selenium.webdriver.support import expected_conditions as EC
#实例化浏览器
driver = webdriver.Firefox()
#打开测试网页
driver.get("http://www.5itest.cn/register")
#等待时间
#sleep(3)
print(EC.title_contains('注册'))  ##title_contains代表只要包含就可以了
'''使用expected_contains判断元素是否显示可见'''
#导入WebDriverWait  显示等待   #导入by
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
#拿到by定位的元素x，在规定的时间内找x,WebDriverWait().until(),
locator = (By.CLASS_NAME,'controls')
try:
    '''
    在设置时间（3s）内，等待后面的条件发生。
    如果超过设置时间未发生，则抛出异常。
    在等待期间，每隔一定时间（默认0.5秒)，调用until或until_not里的方法，直到它返回True或False.
    expected_conditions中的visibility_of_element_located() 判断元素是否可见
    '''
    WebDriverWait(driver,3,0.5).until(EC.visibility_of_element_located(locator),message='')
except:
    print('this element is not visible')
#关闭浏览器
driver.quit()
