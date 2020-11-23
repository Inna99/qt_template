from PyQt5 import QtWidgets, uic

from config import UI_MAIN_WINDOW

Ui_MainWindow, _ = uic.loadUiType(UI_MAIN_WINDOW)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


if __name__ == "__main__":

    from __init__ import initate_application

    initate_application()
