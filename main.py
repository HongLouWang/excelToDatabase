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
    testCase5()

def testCase():

    db = myMySQLDB( "mysql", "localhost", "3306", "root", "Ww20080811", "pythontoexcel", "test1")
    wb = excel(workbook="test1.xlsx", worksheet="Sheet1")

    for i in range(1, wb.worksheet_row_cnt + 1):
        testline = wb.readLineWithRange(i, 1, 5)
        db.insertLine(testline, i)

def testCase2():
    print(ord("A") - 64)

def testCase3():
    wb = excel(workbook="test1.xlsx", worksheet="Sheet1")
    print(wb.letterNumRangeConverter(1,"A",1,"BA"))
    print(wb.getCellData(1,53))

def testCase4():
    wb = excel(workbook="test1.xlsx", worksheet="Sheet1")
    line = wb.readLineByUserDictRange(1, "[A,C]=[1,2]")
    print(line)

def testCase5():
    db = myMySQLDB( "mysql", "localhost", "3306", "root", "Ww20080811", "pythontoexcel", "test1")
    wb = excel(workbook="test1.xlsx", worksheet="Sheet1")
    for i in range(1, wb.worksheet_row_cnt + 1):
        line = wb.readLineByUserDictRange(i, "[A,B,C,D,E]=[id,c1,c2,c3,c4]")
        db.insertLineByUserDict("[A,B,C,D,E]=[id,c1,c2,c3,c4]", line, i)

if __name__ == "__main__":
    main()


