#############################################################################################
#Author:    Shutian Wang
#Date:      Sep. 25nd. 2021
#Desc:      Excel class
#Project:   Load Excel To Database
#############################################################################################

from os.path import exists
from openpyxl import load_workbook

class excel():

    workbook = ""       #Excel文件
    worksheet = ""      #Excel文件中的表格

    def __init__( self, workbook, worksheet):
        self.workbook = workbook
        self.worksheet = worksheet

        if(exists(workbook)):
            pass    #workbook exist
        else:
            print(workbook, " , file does not exist!")  #workbook not exist
            exit()
        try:
            self.workbook = load_workbook(workbook)     #check worksheet exist
        except:
            print(worksheet," , file not support!") #worksheet note exist
            exit();