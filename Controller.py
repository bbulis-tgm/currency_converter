import sys
from view.MyView import Ui_MainWindow
from PyQt5 import QtWidgets
from model.LiveStrategy import LiveStrategy
from model.LocalStrategy import LocalStrategy


class Controller(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    Controller Klasse verbindet View und Model
    Alle Funktionen werden mit der GUI Verbunden
    """

    def set_statusbar(self, message: str, time: int = 3000):
        """
        Eine Meldung wird in die Statusbar am Ende des Fenster geschrieben. Diese wird
        für 3000ms angezeigt und verschwindet dann wieder. Wenn ein Fehler auftritt wird dieser Angezeigt.
        Ansonsten wird eine Meldung über den Erflog des Vorganges ausgegeben

        :param message: Die Nachricht, welche in der Statusleiste angezeigt werden soll
        :param time: Die Zeit, wie lange die Meldung angezeigt werden soll. Standardeinstellung sind 3000ms
        :return: ---
        """
        self.ui.statusbar.showMessage(message, time)

    def change_strategy(self, checked: bool):
        """
        Die Strategy, welche zum Berechnen genutzt wird wird mit dem Benutzen der Checkbox gewechselt
        Von der checkbox wird ein Boolean zurückgegeben welcher mittels einer IF-Anweisung die Strategy wechselt

        :param checked: Der Boolean welcher von der Checkbox zurück gegeben wird
        :return: ---
        """
        self.strategy = LiveStrategy() if checked else LocalStrategy()

    def calc(self):
        pass

    def __init__(self):
        """
        Init Methode startet das Programm und verbindet die einzelnen Knöpfe mit ihren Funktionen
        """
        super().__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.live_data_checkbox.clicked.connect(self.change_strategy)
        self.ui.umrechnen_button.clicked.connect(self.calc)

        self.strategy = LiveStrategy()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Controller()
    window.show()
    sys.exit(app.exec_())