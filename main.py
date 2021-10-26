#############################################################################################
#Author:    Shutian Wang
#Date:      Sep. 25nd. 2021
#Desc:      main file
#Project:   Load Excel To Database
#############################################################################################

from db import myMySQLDB
from excel import excel

import sys

def main():
    testCase()

def testCase():

    db = myMySQLDB( "mysql", "localhost", "3306", "root", "Ww20080811", "pythontoexcel", "test1")
    wb = excel(workbook="test1.xlsx", worksheet="Sheet1")

    for i in range(1, wb.worksheet_row_cnt + 1):
        testline = wb.readLineWithRange(i, 1, 5)
        #print(testline)
        db.insertLine(testline, i)

def testCase2():
    print(ord("A") - 64)

def testCase3():
    wb = excel(workbook="test1.xlsx", worksheet="Sheet1")
    print(wb.letterNumRangeConverter(1,"A",1,"BA"))
    print(wb.getCellData(1,53))
if __name__ == "__main__":
    main()


