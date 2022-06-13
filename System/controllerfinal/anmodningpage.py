from PyQt6 import QtWidgets, uic
from System.kurserdatabase import kurserDatabase
from System.kursus import kursus

class secoundWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(secoundWindow, self).__init__()
        uic.loadUi('/Users/williamdevlin/PycharmProjects/pythonProject7/System/controllerfinal/anmodninger.ui', self)


        self.anmod_pushButton.clicked.connect(self.anmodningPushed)
        self.quit_pushButton.clicked.connect(self.quit)

    def anmodningPushed(self):
        kursusnavn = self.AKursusnavn_lineEdit.text()
        kursusnr = self.AKursusnr_lineEdit_2.text()
        kursusanmodning = kursus(str(kursusnavn), int(kursusnr))

        insertkursusanmodning = kurserDatabase()
        insertkursusanmodning.insertkursusAndmodning(kursusanmodning)

    def quit(self):
        secoundWindow.close()