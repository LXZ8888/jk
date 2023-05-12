'''读取excel文件类和方法的封装'''
import xlrd


class ExcelWR():

    def __init__(self, filePath):
        self.filePath = filePath
        self.excel = xlrd.open_workbook(self.filePath)  # 1、打开

    def readEx(self):
        sheets = self.excel.sheet_names()  # 2、 获取excel表格所有的sheet工作表，返回的是列表
        # print(sheets)
        datas = []
        for s in range(len(sheets)):
            # print(s)
            sheet = self.excel.sheet_by_index(s)  # 第一个工作表
            rows, cols = sheet.nrows, sheet.ncols
            # print(rows,cols)

            for i in range(1, rows):  # 从第二行开始，2,3,4,5,6。rows为6。 arr[5]刚好是最后一行
                value = sheet.row_values(i)
                # print(value)
                datas.append(value)
                # print(datas)
        return datas

    def write(self):
        pass


if __name__ == '__main__':
    E = ExcelWR(filePath=r'C:\Users\1967668484\Desktop\jk-sj.xlsx')  # 路径
    caseDatas = E.readEx()
