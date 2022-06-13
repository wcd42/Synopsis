import sys
from System.controllerfinal.loginpage import MainWindowGUI2
from System.ansattedatabase import ansatteDatabase
from System.kurserdatabase import kurserDatabase
from System.lære import lære
from PyQt6 import QtWidgets

def main():

    teacher1 = lære("te", 123456)

    databaseansatte = ansatteDatabase()
    databaseansatte.createDatabase()
    databaseansatte.createTabel()
    databaseansatte.insertLære(teacher1)

    databasekurser = kurserDatabase()
    databasekurser.createDatabase()
    databasekurser.createTabelkurser()
    databasekurser.createTabelkursusanmodninger()

    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindowGUI2()
    app.exec()

if __name__ == "__main__":
    main()