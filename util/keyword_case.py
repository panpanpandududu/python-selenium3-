from util.excel_cell_value import Get_Cells_Value
from util.actionMethod import ActionMethod
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)
excel_default_path = base_path+'/case/key_excel.xlsx'
class KeywordCase(object):
    def __init__(self):
        self.action_metood = ActionMethod() 
        self.get_cell_value = Get_Cells_Value(excel_default_path)  # 实例化


    def run_main(self):
        get_lines = self.get_cell_value.get_lines  # 获取行数
        if get_lines:
            for i in  range(1,get_lines):
                is_run = self.get_cell_value.get_is_run(i)
                if is_run == 'yes':
                    carry_method = self.get_cell_value.get_action_method(i)  # 获取执行方法
                    send_value = self.get_cell_value.get_send_value(i)  # 获取输入的数据
                    oper_element = self.get_cell_value.get_oper_element(i)  # 获取操作的元素
                    expect_result_mothod = self.get_cell_value.get_expect_result(i)  # 获取预期结果
                    real_result_value = self.get_cell_value.get_real_result(i)  # 获取表中实际要求结果值
                    self.run_method(carry_method,send_value,oper_element)  # 执行excel表中对应指定的方法

                    if expect_result_mothod != '': # 预期结果有值
                        result_value = self.get_real_result_value(real_result_value)
                        if result_value[0] == 'text':  # url访问，获取网页title
                            res = self.run_method(expect_result_mothod) # expect_result_mothod：driver.get_title()方法
                            if result_value[1] in res:  # 判断实际要求结果值是否存在于实际测试结果中
                                self.get_cell_value.write_cell_value(i,'pass') # 在excel表中对应单元格写入数据
                            else:
                                self.get_cell_value.write_cell_value(i,'fail')
                        elif result_value[0] == 'element': # 获取元素，判断输入格式等
                            res = self.run_method(expect_result_mothod,result_value[1]) # expect_result_mothod：get_element()方法，result_value[1]：参数
                            if res: # 有值，表示找到对应(如：password_error)错误信息，表示格式测试通过(目的就是测试输入错误格式是否会被检查出来)
                                self.get_cell_value.write_cell_value(i,'pass')
                            else:
                                self.get_cell_value.write_cell_value(i,'fail')
                        else:
                            print("Error:实际要求结果：{}，测试无效".format(real_result_value))
                    else:
                        print('预期结果为空')

#getattr(object, name[, default])  :返回一个对象属性值
    def run_method(self,method,send_value = '',handle_value = ''):
        main_method = getattr(self.action_metood,method)
        if send_value == '' and handle_value =='':
            result = main_method()  # 关闭浏览器、等待等
        elif send_value == '' and handle_value != '':
            result = main_method(handle_value)  # 打开浏览器、访问url等
        elif send_value != '' and handle_value == '':
            result = main_method(send_value)  # 暂时没用到
        else:
            result = main_method(send_value,handle_value) # 输入用户信息

    # 对实际要求结果值进行切分(实际要求结果形似：text=注册)
    def get_real_result_value(self, data):
        return data.split('=')


if __name__ == "__main__":
    keyword_case = KeywordCase()
    keyword_case.run_main()
