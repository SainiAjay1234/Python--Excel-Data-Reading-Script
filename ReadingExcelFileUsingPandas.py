import pywinauto
import time
from pywinauto import application
import pandas as pd
import numpy
import PIL
import pyautogui
import subprocess
import pyautogui
import xlrd
import os
import sys
from os import sys
#from xlrd import open_workbook
from subprocess import Popen




df =  pd.read_excel("TestCaseInputFile.xlsx")
print(df)
#data=pd.read_csv("C:\\Automation\\TestCaseInputFile.csv",encoding='latin1')
#print(data.head())


ConfigMgrIPAddress = "192.168.104.211"
OVD =  "Ovation Drops"
NWDR = "New Drop"
DEV = "Device 1"
MOD1 = "Module 1 (Compact Contact Input (CI)) (Stopped)"
PIINJ = "Inject"
NWPNT = "NewPointNameCB"
PARA = "Parameter row 0"
OUT = "C:\\Automation\\TestFileForDigital.html"
