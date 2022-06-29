#Change Log:
# 8/12/2021: 合并配置项并注释暂未用到的导入及变量，后续最好增加配置完成后保存CANoe工程的代码
# 8/24/2021: 增加了配置完成后自动保存的代码
# 8/27/2021: 优化了批量配置时中间报错的处理方式：将继续配置并在结束时打印配置失败的列表

""" 开始配置 """

"""以下配置XCP及激活的组名称"""
XCP_Device_Name = "XCP_Device_Name"
XCP_Group_Name = "XCP_Group_Name"

"""以下配置需要导入的数据所在工作表的名称"""
# 工作簿在弹窗中选择，无需在代码中配置，若需要配置请修改excel_path赋值，默认为桌面
Sheet_Name = "Sheet1"

"""以下配置信号要求"""
Param_Configured = 1    # 配置0-取消，1-勾选
Param_EventCycle = 100  # 按顺序选择周期
Param_AutoRead = 1      # 配置0-取消，1-勾选
Param_ReadMode = 1      # 配置1-Polling，2-DAQ

""" 配置结束 """


# import msvcrt, os, time
# import xlutils, xlwt
# from xlutils.copy import copy
import xlrd
import win32ui
from win32com.client.connect import *
from win32com.client import *


class open_excel():
    def __init__(self):
        """设置弹窗"""
        dlg = win32ui.CreateFileDialog(1)
        dlg.SetOFNInitialDir('')  # 弹窗默认地址为桌面
        dlg.DoModal()

        excel_path = dlg.GetPathName()
        if excel_path == "":
            print('No selected')
        else:
            global parameter_table
            global numrows
            data = xlrd.open_workbook(excel_path)
            # newWb = copy(data)
            Sheet_table = data.sheet_by_name(Sheet_Name)
            numrows = Sheet_table.nrows
            parameter_table = [""]*numrows
            for i in range(0, numrows, 1):
                parameter_table[i] = str(Sheet_table.cell_value(i, 0))


class Canoe():
    def __init__(self):
        app = Dispatch('CANoe.Application')
        self.App = app
        app.Configuration.Modified = False
        # ver = app.Version
        # print(ver)

    def XCP_CFG(self):
        gECUs = self.App.Configuration.GeneralSetup.XCPSetup.ECUs
        gECU = gECUs(XCP_Device_Name)

        config_failed = []
        
        for i in range(0, numrows, 1):
            param = gECU.MeasurementGroups.Item(XCP_Group_Name).Parameters(parameter_table[i])

            try:
                param.Configured= Param_Configured
                param.EventCycle= Param_EventCycle
                param.AutoRead= Param_AutoRead
                param.ReadMode= Param_ReadMode
            except:
                config_failed.append = parameter_table[i]
                print("XCP signal name: " + parameter_table[i] + "was not found!")
            else:
                print("XCP signal name: " + parameter_table[i] + "updated!")

        print("\n/**ATTENTION: Values failed to configured list:")
        for value in config_failed:
            print(value)
        print("Please check and config again!\n")

    def canoe_config_save(self):
        self.App.Configuration.Save


open_excel()
Canoe().XCP_CFG()
Canoe().canoe_config_save()
