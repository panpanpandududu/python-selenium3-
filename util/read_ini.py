#coding = uft-8
import sys
import os 
base_path = os.getcwd()
sys.path.append(base_path)
config_path = base_path+'/config/LocalElement.ini'
import configparser
class readIni():
    def __init__(self,file_name=None,node=None):
        if file_name ==None:
            file_name = config_path
        if node ==None:
            #如果配置文件中的section为none时，默认赋值
            self.node = 'RegisterElement'
        else:
            #否则引入初始化时传入的值
            self.node =node
        self.cf = self.load_ini(file_name)

#加载文件
    def load_ini(self,file_name):
        #实例化一个对象
        cf = configparser.ConfigParser()
        #读取配置文件
        cf.read(file_name,encoding='utf-8-sig')
        return cf
#获取配置文件中的值

    def get_value(self,key):
        #获取相应配置值
        data = self.cf.get(self.node,key)
        return data

readini = readIni()
# if __name__ == "__main__":
#     data = readini.get_value('user_email')
#     print(data)
