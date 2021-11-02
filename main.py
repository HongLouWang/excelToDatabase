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
    testCase6()

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

def testCase6():
    workbook = sys.argv[1]
    worksheet = sys.argv[2]

    dbtype = sys.argv[3]
    dbhost = sys.argv[4]
    dbport = sys.argv[5]
    dbuser = sys.argv[6]
    dbpass = sys.argv[7]
    dbname = sys.argv[8]
    dbtable = sys.argv[9]

    userDict = sys.argv[10]

    db = myMySQLDB(dbtype=dbtype, dbip=dbhost, dbport=dbport, dbuser=dbuser, dbpass=dbpass, dbname=dbname, dbTable=dbtable)
    wb = excel(workbook=workbook, worksheet=worksheet)

    for i in range(1, wb.worksheet_row_cnt + 1):
        line = wb.readLineByUserDictRange(i, userDict=userDict)
        db.insertLineByUserDict(userDict=userDict, line=line, line_cnt=i)

    # test command line: python main.py test1.xlsx Sheet1 mysql localhost 3306 root Ww20080811 pythontoexcel test1 [A,B,C,D,F]=[id,c1,c2,c3,c4]

def testCase7():
    print(sys.argv)
    print(sys.argv[1])

    a = input()


if __name__ == "__main__":
    main()


