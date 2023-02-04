import pandas as pd
import os
import xlrd
import xlrd3
import openpyxl
from openpyxl import workbook
from openpyxl import load_workbook
import pyautogui
import pywinauto

loc = ("C:\\Automation\\TestCaseInputFile.xlsx")
wb = xlrd3.open_workbook(loc)
sheet = wb.sheet_by_index(0)

x =sheet.cell_value(1,5)
print(x)



#df = pd. read_excel(file_loc, index_col=None, na_values=['NA'], usecols = "A,C:AA")
#print(df)

#df = pd.read_excel("New.xlsx")
#print(df)
