# import os
# import sys
# path = os.getcwd()
# sys.path.append(path)
from util.read_ini import readini
class findElement():
    # def __init__(self,driver):
    #     self.driver = driver

    def get_element(self,key,driver):
        data = readini.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by =='id':
                return driver.find_element_by_id(value)
            elif by =='name':
                return driver.find_element_by_name(value)
            else:
                return driver.find_element_by_xpath(value)
        except:
            return None

findElements =findElement()
        

