'''
Description : excel utils
     Author : eric
      date  : 2018-03-28
'''
from openpyxl import load_workbook
# 默认可读写，若有需要可以指定write_only和read_only为True
import openpyxl

class ExcelUtils(object):

    def read_excel(self):
        wb= openpyxl.load_workbook('..\\template\\Developing Letter.xlsx')
        sheet = wb.get_sheet_by_name("Sheet1")
        data_list = []
        for r in sheet.rows:
            row_list = []
            for cell in r:
                row_list.append(cell.value)
            data_list.append(row_list)
        print(data_list)


if __name__ == '__main__':
    excel_utils= ExcelUtils()
    excel_utils.read_excel()
