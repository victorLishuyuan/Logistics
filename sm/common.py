import xlrd
import os
import xlwt

# datetime转化成 标准日期的 字符串
def datetimeToString(datetime_val):
    if datetime_val:
        return str(datetime_val.strftime('%Y-%m-%d %H:%M:%S'))
    return ''
# date转化成 标准日期的 字符串
def dateToString(date_val):
    return str(date_val.strftime('%Y-%m-%d'))

# 获取地址编号，如果最低级别为省，则将省编号作为待生成的编号，如果为市，则为是编号，如果为区县，则为区县编号
def getAddressCode(province_code,city_code,county_code):
    addressCode = ''
    if province_code:
        addressCode=province_code
    if city_code:
        addressCode = city_code
    if county_code:
        addressCode = county_code
    return addressCode
# 获取拼接后的地址 参数（省编号，市编号，区编号）
#————————公共方法>>>>>文件上传———————————————公共方法>>>>>文件上传———————————————公共方法>>>>>文件上传———————#
# 文件上传准备工作1：创建文件夹
def mkdir(path):
    path = path.strip()                 # 去除首位空格
    path = path.rstrip("\\")            # 去除尾部 \ 符号
    isExists = os.path.exists(path)     # 判断路径是否存在
    if not isExists:                    # 如果不存在则创建目录
        os.makedirs(path)
        return True
    else:                               # 如果目录存在，则不创建
        return False
# 文件上传准备工作2：判断文件格式
def filetype(fileName):
    fileType = "."+fileName.rsplit(".", 1)[1]
    print(fileType)
    return fileType
# 文件上传      wayOnly：上传的位置，file：需要上传的文件（文件名需要已经更新），返回：全部路径（路径+新文件名）
def fileload(wayOnly,file,reName):
    if not file:
        fileWayAll = '无附件信息'
    else:
        mkdir(wayOnly)  # 创建路径
        fileName = file.name  # 获取文件初始名称
        fileType = filetype(fileName)  # 获取文件类型（后缀），并加点返回
        file.name = reName + fileType  # 给文件重命名名称：公司代码+文件名+后缀
        fileWayAll = os.path.join(wayOnly, file.name)  # 上传的全路径，需要存入数据库
        # 查询系统中是否已经存在该文件
        is_exite = os.path.exists(fileWayAll)
        if is_exite:
            os.remove(fileWayAll)
        destination = open(fileWayAll, 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in file.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
    return fileWayAll
#————————公共方法>>>>>文件上传———————————————公共方法>>>>>文件上传———————————————公共方法>>>>>文件上传———————#
# 表格导入信息的获取
def uploadExcel(excel_file):
    data = xlrd.open_workbook(filename=None, file_contents=excel_file.read())  # xlsx文件
    # data = xlrd.open_workbook(filename=None, file_contents=excel_file.read(), formatting_info=True)  # xls文件
    return get_sheets_mg(data,0) # 打开第一张表,并以list的形式返回
def get_sheets_mg(data, num):      # data:Excel数据对象，num要读取的表
    table = data.sheets()[num]  # 打开第一张表
    nrows = table.nrows  # 获取表的行数
    ncole = table.ncols  # 获取列数
    all_list = []
    for i in range(nrows):  # 循环逐行打印
        one_list = []
        for j in range(ncole):
            cell_value = table.row_values(i)[j]
            if (cell_value is None or cell_value == ''):
                cell_value = (get_merged_cells_value(table, i, j))
            one_list.append(cell_value)
        all_list.append(one_list)
    del (all_list[0])  # 删除标题   如果Excel文件中第一行是标题可删除掉，如果没有就不需要这行代码
    return all_list
def get_merged_cells(sheet):
    """
    获取所有的合并单元格，格式如下：
    [(4, 5, 2, 4), (5, 6, 2, 4), (1, 4, 3, 4)]
    (4, 5, 2, 4) 的含义为：行 从下标4开始，到下标5（不包含）  列 从下标2开始，到下标4（不包含），为合并单元格
    :param sheet:
    :return:
    """
    return sheet.merged_cells
def get_merged_cells_value(sheet, row_index, col_index):
    """
    先判断给定的单元格，是否属于合并单元格；
    如果是合并单元格，就返回合并单元格的内容
    """
    merged = get_merged_cells(sheet)
    # print(merged,"==hebing==")
    for (rlow, rhigh, clow, chigh) in merged:
        if (row_index >= rlow and row_index < rhigh):
            if (col_index >= clow and col_index < chigh):
                cell_value = sheet.cell_value(rlow, clow)
                # print('该单元格[%d,%d]属于合并单元格，值为[%s]' % (row_index, col_index, cell_value))
                return cell_value
                break
    return None
##############################################################
#导出表格(表格标题列表，内容列表)
def downExcel(hdadline_list,content_list):
    # 创建一个文件对象
    wb = xlwt.Workbook(encoding='utf8')
    # 创建一个sheet对象
    sheet = wb.add_sheet('sheet1')
    # 设置文件头的样式
    style_heading = xlwt.easyxf("""
                   font:
                       name Arial,
                       colour_index white,
                       bold on,
                       height 0xA0;
                   align:
                       wrap off,
                       vert center,
                       horiz center;
                   pattern:
                       pattern solid,
                       fore-colour 0x19;
                   borders:
                       left THIN,
                       right THIN,
                       top THIN,
                       bottom THIN;
                   """)
    # 写入文件标题
    col = 0
    for hl in hdadline_list:
        sheet.write(0, col, hl , style_heading)  # 其中 0-行 ， col-列
        col = col + 1
    # 写入数据
    row = 1 # 从第二行开始写，第一行是标题
    for cl in content_list:
        j = 0 # 从第一列开始写入
        for c in cl:
            sheet.write(row, j , c)  # 第 row 行，第 j 列
            j = j + 1
        row = row + 1
    return wb


