import mysql.connector
from System.kursus import kursus

class kurserDatabase():

    def createDatabase(self):
        mydb = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Halo4242'
        )
        mycursor = mydb.cursor()

        mycursor.execute("CREATE DATABASE kurser")

    def createTabelkurser(self):
        mydb = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Halo4242',
            database="kurser"
        )
        mycursor = mydb.cursor()

        mycursor.execute("CREATE TABLE kurser (kursusnavn VARCHAR(45), kursusnr INTEGER(4))")

    def createTabelkursusanmodninger(self):
        mydb = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Halo4242',
            database="kurser"
        )
        mycursor = mydb.cursor()

        mycursor.execute("CREATE TABLE kursusanmodninger (kursusnavn VARCHAR(45), kursusnr INTEGER(4))")

    def insertkursus(self, kursus: kursus):
        mydb = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Halo4242',
            database="kurser"
        )

        kursusnavn = kursus.getkursusnavn()
        kursusnr = kursus.getkursusnr()

        mycursor = mydb.cursor()

        sqlformula = "INSERT INTO kurser (kursusnavn, kursusnr) VALUES (%s, %s)"

        mycursor.execute(sqlformula, (str(kursusnavn), (int(kursusnr))))
        mydb.commit()

    def insertkursusAndmodning(self, kursus: kursus):
        mydb = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Halo4242',
            database="kurser"
        )

        kursusnavn = kursus.getkursusnavn()
        kursusnr = kursus.getkursusnr()

        mycursor = mydb.cursor()

        sqlformula = "INSERT INTO kursusanmodninger (kursusnavn, kursusnr) VALUES (%s, %s)"

        mycursor.execute(sqlformula, (str(kursusnavn), (int(kursusnr))))
        mydb.commit()

    def fetchRowkurser(self, kursusnavninput, kursusnrinput):
        mydb = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Halo4242',
            database="ansatte"
        )

        mycursor = mydb.cursor()

        sql = """
        SELECT * FROM kurser WHERE kursusnavn = "%s" AND kursusnr = "%s"
        """ % (kursusnavninput, kursusnrinput)

        mycursor.execute(sql)

        myresult = mycursor.fetchone()

        return myresult

    def fetchRowanmodninger(self, kursusnavninput, kursusnrinput):
        mydb = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='Halo4242',
            database="ansatte"
        )

        mycursor = mydb.cursor()

        sql = """
           SELECT * FROM kursusanmodninger WHERE kursusnavn = "%s" AND kursusnr = "%s"
           """ % (kursusnavninput, kursusnrinput)

        mycursor.execute(sql)

        myresult = mycursor.fetchone()

        return myresult







