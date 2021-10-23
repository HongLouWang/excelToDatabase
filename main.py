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
        testline = wb.readLine(i)
        db.insertLine(testline, i)

if __name__ == "__main__":
    main()


