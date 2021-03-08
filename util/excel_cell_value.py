#读取excel表中各列的数据
from util.handle_excel import Excel_Opertion

class Get_Cells_Value(object):
    """获取keyword.xls表单元格数据"""
    def __init__(self,excel_path):
        self.case_id = 0    # id
        self.case_name = 1  # 模块名称
        self.action_type = 2     # 操作类型：打开浏览器、输入用户名...
        self.is_run = 3          # 是否执行
        self.action_method = 4   # 执行方法
        self.send_value = 5      # 发送的数据
        self.oper_element = 6    # 操作元素
        self.expect_result = 7   # 预期结果
        self.real_result = 8     # 实际结果
        self.report_result = 9   # 实际报告，是否通过

        self.excel_path = excel_path
        self.excel_oper = Excel_Opertion(self.excel_path)  # 实例化
        self.get_lines = self.excel_oper.get_lines()  # 获取行数


    def get_case_id(self,row):
        # 获取case id
        case_id = self.excel_oper.get_col_value(row,self.case_id)
        return case_id

    def get_case_name(self,row):
        # 获取case名称
        case_name = self.excel_oper.get_col_value(row,self.case_name)
        return case_name

    def get_is_run(self,row):
        # 获取是否执行：yes/no ，用于判断该case是否运行
        is_run = self.excel_oper.get_col_value(row,self.is_run)
        return is_run

    def get_action_method(self,row):
        # 获取操作的方法
        action_method = self.excel_oper.get_col_value(row,self.action_method)
        return action_method

    def get_send_value(self,row):
        # 获取要输入的数据
        send_value = self.excel_oper.get_col_value(row,self.send_value)
        return send_value

    def get_oper_element(self,row):
        # 获取操作的元素
        oper_element = self.excel_oper.get_col_value(row,self.oper_element)
        return oper_element

    def get_expect_result(self,row):
        # 获取预期结果
        expect_result = self.excel_oper.get_col_value(row,self.expect_result)
        return expect_result

    def get_real_result(self,row):
        # 获取实际结果
        real_result = self.excel_oper.get_col_value(row,self.real_result)
        return real_result

    def get_report_result(self,row):
        # 获取报告
        report_result = self.excel_oper.get_col_value(row,self.report_result)
        return report_result
    
    def write_cell_value(self,row,value):
        # 在指定单元格写入数据
        self.excel_oper.write_value(row,value)

