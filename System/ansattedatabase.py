import mysql.connector
from System.lære import lære

class ansatteDatabase():

    def createDatabase(self):
        mydb = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Halo4242'
        )
        mycursor = mydb.cursor()

        mycursor.execute("CREATE DATABASE ansatte")

    def createTabel(self):
        mydb = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Halo4242',
            database="ansatte"
        )
        mycursor = mydb.cursor()

        mycursor.execute("CREATE TABLE lære (loginid VARCHAR(45), password INTEGER(6))")

    def insertLære(self, lære: lære):
        mydb = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Halo4242',
            database="ansatte"
        )

        læreid = lære.getloginid()
        lærepassword = lære.getpassword()

        mycursor = mydb.cursor()

        sqlformula = "INSERT INTO lære (loginid, password) VALUES (%s, %s)"

        mycursor.execute(sqlformula, (str(læreid), (int(lærepassword))))
        mydb.commit()

    def fetchRow(self, logininput, passwordinput):
        mydb = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Halo4242',
            database="ansatte"
        )

        mycursor = mydb.cursor()

        sql = """
        SELECT * FROM lære WHERE loginid = "%s" AND password = "%s"
        """ % (logininput, passwordinput)

        mycursor.execute(sql)

        myresult = mycursor.fetchone()

        return myresult







