#coding=utf-8
#对应excel表中第 5列的 执行方法，实现：打开浏览器、定位对应元素、实现自动输入信息、关闭浏览器等
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)
from selenium import webdriver
from base.find_element import findElement
import time
class ActionMethod(object):
    """用于执行 keyword.xls表指定方法"""
    #打开浏览器
    def open_browser(self,browser):
        try:
            if browser == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser == 'firefox':
                self.driver = webdriver.Firefox()
            else:
                self.driver = webdriver.Edge()
        except:
            print("ActionMethodError：没有'{}'这个元素".format(browser))
        
    #输入地址
    def get_url(self,url):
        try:
            self.driver.get(url)
        except:
            print("ActionMethodError：url：{}，输入有误".format(url))
    
    #定位元素
    def get_element(self,key):
        try:
            find_element = findElement(self.driver)
            element = find_element.get_element(key)
            return element
        except:
            print("ActionMethodError：'{}'元素定位失败".format(key))
    
    #输入信息
    def element_send_keys(self,value,key):
        try:
            element = self.get_element(key)
            element.send_keys(value)
        except:
            print("ActionMethodError：输入有误：'{}'".format(value))
    
    #点击元素
    def click_element(self,key):
        try:
            self.get_element(key).click()
        except:
            print("ActionMethodError：'{}'元素不存在，无法点击".format(key))
    
    #等待
    def sleep_time(self):
        time.sleep(3)
    
    #关闭浏览器
    def close_browser(self):
        self.driver.close()
    
    #获取title
    def get_title(self):
        title = self.driver.title
        return title