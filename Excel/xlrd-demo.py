# author:yangleiw
# createdate:2022/5/14
import xlrd
import xlsxwriter

data = xlrd.open_workbook("xlrd-demo.xlsx")  # 打开工作表
# print(data.sheet_loaded(0))  # 查看sheet1是否被加载
# print(data.sheets())  # 获取全部sheet
# print(data.sheet_by_name("Sheet1"))  # 根据名称获取工作表
# print(data.sheet_names())  # 获取所有工作表的name
# print(data.nsheets)  # 返回excel工作表sheet的数量

# 操作excel行
sheet1 = data.sheet_by_name("Sheet1")  # 打开sheet1表格
# print(sheet1.nrows)  # 获取sheet下有效行数 返回：4
# print(sheet1.row(1))  # 该行单元格对象组成的列表 返回： [text:'江西省', text:'南昌市']
# print(sheet1.row_types(2))  # 获取单元格的数据类型 返回：array('B', [1, 1])
# print(sheet1.row(1)[1].value)  # 获取单元格第2行第2个的内容 返回：南昌市
# print(sheet1.row_values(1))  # 获取单元格第2行所有的内容 返回：['江西省', '南昌市']
# print(sheet1.row_len(1)) # 获取单元格的长度 返回： 2

# 操作excel列
# print(sheet1.ncols)  # 获取sheet下有效列数 返回：2
# print(sheet1.col(1))  # 该列单元格对象组成的列表 返回： [text:'市', text:'南昌市', text:'合肥市', text:'长沙市']
# print(sheet1.col(1)[2].value)  # 获取单元格第2列第3行的内容 返回：合肥市
# print(sheet1.col_values(1)) # 获取单元格第2列所有的内容 返回：['市', '南昌市', '合肥市', '长沙市']

# 操作Excel单元格
# print(sheet1.cell(0, 1).value)  # 获取第1行第2列的值 返回：市
# print(sheet1.cell(0, 1).ctype)  # 获取单元格数据类型，0（空）1（文本）2（数字）3（date日期） 返回：1
# print(sheet1.cell_value(0, 1))  # 获取第1行第2列的值 返回：市

# xlswriter使用
wb = xlsxwriter.Workbook("xlrd-demo1.xlsx")
sht = wb.add_worksheet("newsheet")

# sht.write_string()
sht.write(0, 0, "2020年度")
sht.merge_range(1, 0, 2, 2, "第一季度销售统计")
data = (
    ["1月份", 500, 450],
    ["2月份", 600, 650],
    ["3月份", 700, 550]
)
sht.write_row(3, 0, ["月份", "预期销售额度", "实际销售额度"])
for index, item in enumerate(data):
    sht.write_row(index + 4, 0, item)

sht.write(7, 1, "=sum(B5:B7)")
sht.write(8, 2, "=sum(c5:c7）")
sht.write_url(9, 0, "http://www.baidu.com", string="更多数据")
# sht.insert_image(10, 0, "view.jpg")
wb.close()
