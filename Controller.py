import sys
from view.MyView import Ui_MainWindow
from PyQt5 import QtWidgets
from model.LiveStrategy import LiveStrategy
from model.LocalStrategy import LocalStrategy


class Controller(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    Controller Klasse verbindet View und Model
    Alle Funktionen werden mit der GUI Verbunden

    :author: Benjamin Bulis
    """

    def set_statusbar(self, message: str, time: int = 3000):
        """
        Eine Meldung wird in die Statusbar am Ende des Fenster geschrieben. Diese wird
        für 3000ms angezeigt und verschwindet dann wieder. Wenn ein Fehler auftritt wird dieser Angezeigt.
        Ansonsten wird eine Meldung über den Erflog des Vorganges ausgegeben

        :param message: Die Nachricht, welche in der Statusleiste angezeigt werden soll
        :param time: Die Zeit, wie lange die Meldung angezeigt werden soll. Standardeinstellung sind 3000ms
        :return:
        """
        self.ui.statusbar.showMessage(message, time)

    def set_output(self, message: str):
        """
        Methode leer das Output-Field wenn diese aufgerufen wird
        Danach wird der neue Inhalt (Berechnungen in die Ziel-Währungen) dem Output-Field hinzugefügt

        :param message: Der Inhalt welcher angezeigt werden soll
        :return:
        """
        self.ui.output_textfield.clear()
        self.ui.output_textfield.append(message)

    def get_input(self):
        """
        Holt die Eingaben aus den Eingabefeldern der GUI und setzt diese Global für das Objekt
        _to Eingabe wird überprüft und in eine Liste aufgespalten

        :return:
        """
        self._value = self.ui.betrag_box.value()
        self._from = self.ui.waehrung_input_box.text().strip().upper()
        _to_str = self.ui.Zielwaehrung_input_box.text().strip().upper()
        self._to = list(map(lambda s: s.strip(), _to_str.split(","))) if _to_str else []

    def check_input(self):
        """
        Methode überprüft ob Währungen alle 3 Zeichen haben

        :raise: Fehler wenn Währung nicht 3 Zeichen lang ist
        :return:
        """
        if len(self._from) != 3:
            raise Exception("Basis Währung muss 3 Zeichen lang sein")

        for i in self._to:
            if len(i) != 3:
                raise Exception("Ziel Währung/Währungen muss 3 Zeichen lang sein")

    def change_strategy(self, checked: bool):
        """
        Die Strategy, welche zum Berechnen genutzt wird wird mit dem Benutzen der Checkbox gewechselt
        Von der checkbox wird ein Boolean zurückgegeben welcher mittels einer IF-Anweisung die Strategy wechselt

        :param checked: Der Boolean welcher von der Checkbox zurück gegeben wird
        :return:
        """
        self.strategy = LiveStrategy() if checked else LocalStrategy()

    def calc(self):
        """
        Methode welche die Berechnung der Währungen startet
        Sollte ein Fehler auftreten so wird dieser in die Statusleiste des Fensters geschrieben

        :return:
        """
        self.get_input()

        try:
            self.check_input()
        except Exception as e:
            self.set_statusbar(str(e))

        try:
            ret = self.strategy.calculate(self._value, self._from, self._to)
            self.set_output(str(ret))
        except Exception as e:
            self.set_statusbar(str(e))

    def __init__(self):
        """
        Init Methode startet das Programm und verbindet die einzelnen Knöpfe mit ihren Funktionen
        """
        super().__init__(None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.live_data_checkbox.clicked.connect(self.change_strategy)
        self.ui.umrechnen_button.clicked.connect(self.calc)

        self._from = ""
        self._to = []
        self._value = 0
        self.strategy = LiveStrategy()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Controller()
    window.show()
    sys.exit(app.exec_())