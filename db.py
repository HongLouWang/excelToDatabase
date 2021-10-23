#############################################################################################
#Author:    Shutian Wang
#Date:      Sep. 25nd. 2021
#Desc:      Database classes
#Project:   Load Excel To Database
#############################################################################################

from dns.rdatatype import NULL
import mysql.connector

class myMySQLDB():
    myDBType = ""

    myDBIP = ""
    myDBUser = ""
    myDBPass = ""
    myDBName = ""

    mydb = NULL

    #Init MySQL Database
    def __init__( self, dbtype, dbip, dbuser, dbpass, dbname):
        self.myDBType = dbtype
        self.myDBIP = dbip
        self.myDBUser = dbuser
        self.myDBPass = dbpass
        self.myDBName = dbname

        self.mydb = mysql.connector.connect(
                host = self.myDBIP,
                user = self.myDBUser,
                password = self.myDBPass,
                database = self.myDBName
            )
