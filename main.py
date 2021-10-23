#############################################################################################
#Author:    Shutian Wang
#Date:      Sep. 25nd. 2021
#Desc:      main file
#Project:   Load Excel To Database
#############################################################################################

from db import myMySQLDB
from excel import excel

def main():
    db = myMySQLDB( "mysql", "localhost", "root", "Ww20080811", "pythontoexcel")

if __name__ == "__main__":
    main()


