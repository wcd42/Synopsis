from PyQt6 import QtWidgets, uic
from Controller.KU_Planner_submitcourse import SubmitCourseGUI
from Controller.KU_Planner_courserequests import SearchCourseGUI
from System.ansattedatabase import ansatteDatabase
from System.controllerfinal.anmodningpage import secoundWindow


class MainWindowGUI2(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindowGUI2, self).__init__()
        uic.loadUi('/Users/williamdevlin/PycharmProjects/pythonProject7/System/controllerfinal/loginpage.ui', self)

        self.Login_pushButton.clicked.connect(self.loginbuttonpressed)
        self.Quit_pushButton.clicked.connect(self.quit)
        self.show()

    def loginbuttonpressed(self):
        loginid = self.ID_lineEdit.text()
        loginid = str(loginid)
        password = self.Password_lineEdit.text()
        password = int(password)
        databaserow = ansatteDatabase()
        result = databaserow.fetchRow(loginid, password)

        try:
            if loginid == str(result[0]) and password == int(result[1]):
                self.w = secoundWindow()
                self.w.show()

        except Exception as e:
            self.textEdit.setPlainText("login er ikke genkendt prøv igen")

    def quit(self):
        MainWindowGUI2.close()

