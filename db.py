#############################################################################################
#Author:    Shutian Wang
#Date:      Sep. 25nd. 2021
#Desc:      Database classes
#Project:   Load Excel To Database
#############################################################################################

# from dns.rdatatype import NULL

import mysql.connector as mysql
from mysql.connector import errorcode

class myMySQLDB():
    myDBType = ""

    myDBIP = ""
    myDBPort = ""
    myDBUser = ""
    myDBPass = ""
    myDBName = ""

    myDBTable = ""

    mydb = None
    myDBCursor = None

    #Init MySQL Database
    def __init__( self, dbtype, dbip, dbport, dbuser, dbpass, dbname, dbTable):
        if dbtype != "":
            self.myDBType = dbtype
        else:
            print("Database type cannot be empty!")
            exit()

        if dbip != "":
            self.myDBIP = dbip
        else:
            print("Database host ip cannot be empty!")
            exit()

        if dbport != "":
            self.myDBPort = dbport
        else:
            self.myDBPort = 3306

        if dbuser != "":
            self.myDBUser = dbuser
        else:
            print("Database username cannot be empty!")
            exit()

        if dbpass != "":
            self.myDBPass = dbpass
        else:
            print("Database password cannot be empty!")
            exit()
        
        if dbname != "":
            self.myDBName = dbname
        else:
            print("Database name cannot be empty!")
            exit()  

        if dbTable != "":
            self.myDBTable = dbTable
        else:
            print("Table name cannot be empty!")
            exit()
        
        try:
            self.mydb = mysql.connect(
                host = self.myDBIP,
                user = self.myDBUser,
                port = self.myDBPort,
                password = self.myDBPass,
                database = self.myDBName
            )
        except mysql.Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Cannot connect to database, username or password incorrect!")
                exit()
            elif e.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist!")
                exit()
            elif e.errno == errorcode.CR_CONN_HOST_ERROR:
                print("Cannot connect to database!")
                exit()
            else:
                print("Something went wrong with database!")
                print(e)
                exit()
            
        self.mydb = mysql.connect(
                host = self.myDBIP,
                user = self.myDBUser,
                password = self.myDBPass,
                database = self.myDBName
            )
        
        self.myDBCursor = self.mydb.cursor()
        #Check table in database
        sql = "SHOW TABLES LIKE '" + self.myDBTable + "'"
        self.myDBCursor.execute(sql)

        result = self.myDBCursor.fetchone()
        if result:  #table exist
            pass
        else:
            print("Table not exist in database!")
            exit()
    
    def insertLine( self, line, line_cnt):
        val = ""
        for i in range(0, len(line) - 1):
            val = val + " '" + line[i] + "', "
        val = val + "'" + line[len(line) - 1] + "'"
        sql = "INSERT INTO " + self.myDBTable + " VALUES (" + val + ")"
        try:
            self.myDBCursor.execute(sql)
            self.mydb.commit()
        except:
            print("Line ", line_cnt, " cannot insert into database!")

    def insertLineByUserDict( self, userDict, line, line_cnt):
        val = ""
        col_name = ""
        userDictDBList = []
        userDict = userDict[userDict.find("=") + 1:]
        userDict = userDict.replace("[","")
        userDict = userDict.replace("]","")

        userDictDBList = userDict.split(",")

        for i in range(0, len(userDictDBList) - 1):
            col_name = col_name + " " + userDictDBList[i] + ", "
        col_name = col_name + userDictDBList[len(userDictDBList) - 1]

        for i in range(0, len(line) - 1):
            val = val + " '" + line[i] + "', "
        val = val + "'" + line[len(line) - 1] + "'"

        sql = "INSERT INTO " + self.myDBTable + " (" + col_name + ") VALUES (" + val + ")"

        try:
            self.myDBCursor.execute(sql)
            self.mydb.commit()
        except:
            print("Line ", line_cnt, " cannot insert into database!")

        





