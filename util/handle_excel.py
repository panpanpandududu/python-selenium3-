import xlrd   # 需安装
from xlutils.copy import copy  # xlutils 需安装
import time
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)
excel_path = base_path+'/case/key_excel.xlsx'
class Excel_Opertion(object):
    """excel表数据相关操作"""

    def __init__(self,ex_path=None,index=None):
        if ex_path == None:
            self.excel_path = excel_path  # 默认excel文件路径
        else:
            self.excel_path = ex_path
        if index == None:
            index = 0
        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheets()[index] # sheets第一页数据

    # 获取excel数据，按照每行一个list，添加到一个大的list里面
    def get_data(self):
        result = []
        rows = self.get_lines()
        if rows !=None:
            for i in range(1,rows):
                row = self.table.row_values(i)
                # print(row)   # ['test001@qq.com', 'Mushishi001', '111111', 'code', 'user_email_error', '请输入有效的电子邮件地址']
                result.append(row)   # [['test001@qq.com', 'Mushishi001', '111111', 'code', 'user_email_error', '请输入有效的电子邮件地址'], ['test002.com', 'Mushishi002', '111112', 'code', 'user_email_error', '请输入有效的电子邮件地址']]
            return result
        return None

    # 获取excel行数
    def get_lines(self):
        rows = self.table.nrows  # 获取行数
        if rows > 1:
            return rows
        return None

    #获取单元格的数据
    def get_col_value(self,row,col):
        #print
        if self.get_lines()>row:
            data = self.table.cell(row,col).value
            return data
        return None


    #写入数据
    def write_value(self,row,value):
        read_value = xlrd.open_workbook(self.excel_path) # 打开excel文件
        write_data = copy(read_value)  # 复制文件，让xlutils模块相关操作表
        write_data.get_sheet(0).write(row,9,value)  # 获取excel表首页数据，并在row行9列写入数据
        write_data.save(self.excel_path)   # 保存
        time.sleep(1)