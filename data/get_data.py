from data.operation_excel import OperationExcel
from data import data_config
from common.base_page import BasePage


class GetData():
    def __init__(self, filename=None, sheet_id=None):
        self.opera_excel = OperationExcel(filename, sheet_id)
        # self.com_util = CommonUtil()

    # def base_check_element_isexists(self, checkvalue):
    #     flag = False
    #     if self.base_page.check_element_isexist(checkvalue):
    #         flag = True
    #     return flag

    # 获取当前 sheet name
    def get_current_sheet_name(self):
        return self.opera_excel.get_sheet_name()

    # 获取excel行数
    def get_case_lines(self):
        return self.opera_excel.get_sheet_rows_num()

    # id_key 获取行号
    def get_case_row_by_idkey(self, idkey):
        row_num = 1
        for i in self.opera_excel.get_col_value(data_config.get_id_key_col()):
            if idkey == i:
                return row_num
            row_num += 1
        return False

    # 获取case id
    def get_case_id_name(self, row):
        col = data_config.get_id_col()
        case_id = self.opera_excel.get_cell_value(row, col)
        return case_id

    def get_model(self, row):
        col = data_config.get_model_col()
        model_name = self.opera_excel.get_cell_value(row, col)
        return model_name

    def get_id_comment(self, row):
        col = data_config.get_id_comment_col()
        id_comment = self.opera_excel.get_cell_value(row, col)
        return id_comment

    def get_id_key(self, row):
        col = data_config.get_id_key_col()
        id_key = self.opera_excel.get_cell_value(row, col)
        return id_key

    def _get_id_by(self, row):
        col = data_config.get_id_by_col()
        id_by = self.opera_excel.get_cell_value(row, col)
        return id_by

    def _get_id_value(self, row):
        col = data_config.get_id_value_col()
        id_value = self.opera_excel.get_cell_value(row, col)
        return id_value

    def get_elements_by_and_key(self, row):
        return (self._get_id_by(row), self._get_id_value(row))

    # 获取依赖 id的key值
    def get_dependent_key(self, row):
        col = data_config.get_id_dependent_key_col()
        id_dependent = self.opera_excel.get_cell_value(row, col)
        if id_dependent == "":
            return None
        else:
            return id_dependent

    # 通过 id_key获得元素
    def get_elements_from_id_key(self, idkey):
        case_row = self.get_case_row_by_idkey(idkey)
        elements = self.get_elements_by_and_key(case_row)
        return elements

    def get_elements_by_dependent_row(self, row):
        dp_key = self.get_dependent_key(row)
        dp_element = self.get_elements_from_id_key(dp_key)
        return dp_element

    def get_dependent_method(self, row):
        col = data_config.get_dependent_method()
        dependent_m = self.opera_excel.get_cell_value(row, col)
        if dependent_m == "":
            return None
        else:
            return dependent_m

    # 写 结果到excel
    def write_current_result(self, row, value):
        col = data_config.get_checkresult_col()
        writevalue = self.opera_excel.write_cell_value(row, col, value)
        if writevalue:
            return True
        else:
            return False


if __name__ == '__main__':
    ab = GetData()
    print(ab.get_elements_from_id_key("bind_dev"))
