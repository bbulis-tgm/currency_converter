import sys
from view.MyView import Ui_MainWindow
from PyQt5 import QtWidgets
from model.LiveStrategy import LiveStrategy
from model.LocalStrategy import LocalStrategy


class Controller(QtWidgets.QMainWindow, Ui_MainWindow):

    def set_statusbar(self, message: str, time: int = 3000):
        self.ui.statusbar.showMessage(message, time)

    def change_strategy(self, checked: bool):
        self.strategy = LiveStrategy() if checked else LocalStrategy()

    def __init__(self):
        super().__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.strategy = LiveStrategy()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Controller()
    window.show()
    sys.exit(app.exec_())