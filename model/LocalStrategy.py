from typing import List
from pathlib import Path
import json

from model.BaseClass import BaseClass
from model.ObjectClass import CalcResult
from model.ObjectClass import CurrencyResult

class LocalStrategy(BaseClass):
    """
    Klasse führt die Offline Umrechnung der Währungen durch

    :author: Benjamin Bulis
    """

    def __init__(self, path="./local_data.json"):
        """
        Init Methode bekommt den Namen des Files Übergeben und setzt diesen

        :param path: Name des Files standardmäßig schon gesetzt
        """
        self.path = Path(__file__).parent / path
        self.data = self.read_file()

    def read_file(self):
        """
        Lesen des Files mit allen localen Wechselkursen (Basis EUR)

        :return: Inhalt des Files als JSON Objekt
        """
        with open(self.path) as input_file:
            return json.load(input_file)

    def calculate(self, _value: float, _from: str, _to: List[str]):
        """
        Funktion um die den Betrag in die weiteren Währungen umzurechnen
        Sollte die _to Liste leer sein so wird in alle anderen Währungen umgerechnet
        EUR muss extra hingefügt werden, weil dies die Basis für die einzelnen Wechselkurse ist
        Ist EUR die Basis Währung kann in jede andere Währung umgerechnet werden
        Wird jedoch eine andere Basis Währung benutzt so muss zuerst in EUR umgerechnet werden
        bevor diese in weitere Währungen umgerechnet wird

        :param _value: Der Betrag welcher umgerechnet werden soll
        :param _from: Die Basis Währung von der Ausgegangen wird
        :param _to: Eine Liste von Ziel Währungen
        :return: Die Liste mit all den Umgerechneten Ergebnissen
        """
        rates_only = self.data['rates']
        ret = []

        # Umrechnung in alle Währungen wenn _to Liste leer ist
        if len(_to) == 0:
            _to = (['EUR'] + list(rates_only.keys()))
            _to.remove(_from)

        # Umrechnung von EUR in andere Währungen
        if _from == 'EUR':
            for s in _to:
                ret.append(CurrencyResult(s, rates_only[s], rates_only[s] * _value))
        else:
        # Umrechnung in EUR um in andere Währungen umzurechnen
            rates_only['EUR'] = 1
            _eur = _value/rates_only[_from]
            for s in _to:
                ret.append(CurrencyResult(s, rates_only[s], rates_only[s] * _eur))

        return CalcResult(_value, _from, ret, self.data['date'])