from abc import ABC
from abc import abstractmethod
from typing import List

class BaseClass(ABC):
    """
    Basis Klasse von welcher die Strategien erben

    :author: Benjamin Bulis
    """

    @abstractmethod
    def calculate(self, _value: float, _from: str, _to: List[str]):
        """
        Methode, welche die Umrechnung durchführt

        :param _value: Der Betrag welcher umgerechnet werden soll
        :param _from: Die Währung für den Betrag welcher der Methode übergeben wird
        :param _to: Liste aller Währungen in welche der Betrag umgerechnet wird
        :return: Dict aller Werte und Währungen welche der Methode anfangs übergeben wurden
        :raise: Error wenn bei der Umrechnung ein Fehler aufgetreten ist
        """
        pass