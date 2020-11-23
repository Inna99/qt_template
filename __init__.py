def initate_application() -> None:
    """Application entry point"""

    import sys

    from PyQt5 import QtWidgets

    from utils import MakeMyAppOfficial
    from app import MainWindow

    # Entry point
    MakeMyAppOfficial()
    app = QtWidgets.QApplication(sys.argv)
    # window =
    window = MainWindow()

    window.show()

    app.exec_()


if __name__ == "__main__":
    initate_application()
