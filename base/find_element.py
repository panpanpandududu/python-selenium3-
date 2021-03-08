import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)
from util.read_ini import readini
class findElement():
    def __init__(self,driver):
        self.driver = driver

    def get_element(self,key):
        data = readini.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by =='id':
                return self.driver.find_element_by_id(value)
            elif by =='name':
                return self.driver.find_element_by_name(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            #测试失败自动截图
            #因为是查找元素是错误的来源，所以在查找错误元素中进行异常的扑捉
            file_path =base_path +'/image/'+ value + ".png"
            self.driver.save_screenshot(file_path)
            return None
        

