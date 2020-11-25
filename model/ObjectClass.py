from typing import List


class CurrencyResult:
    """
    Object beinhaltet den Namen der Währung, den Wechselkurs und den berechneten Betrag mit dem Wechselkurs

    :author: Benjamin Bulis
    """

    def __init__(self, _name: str, _wechselkurs: float, _value: float):
        """
        Init Methode erhält den Namen, Wechsekurs, berechneten Betrag

        :param _name: Dreistelliger Name der Währung
        :param _wechselkurs: Wechselkurs der Währung zur Basis Währung
        :param _value: berechneter Betrag der Währung mittels Wechselkurs
        """
        self._name = _name
        self._wechselkurs = _wechselkurs
        self._value = _value

    def __str__(self):
        """
        Methode welche die gesetzen Werte in HTML Listen form zurückgibt

        :return: Daten des Objekts als HTML-Listen Format
        """
        return "<li><b>{:.2f} {}</b> (Kurs: {:f})</li>".format(self._value, self._name, self._wechselkurs)


class CalcResult:
    """
    Objekt welches eine Liste von CurrencyResults beinhaltet und diese als gesamtes HTML zurück gibt
    """

    def __init__(self, _value: float, _from: str, _to: List[CurrencyResult], _date: str):
        """
        Init Methode erhält den Betrag der Basis Währung, eine Liste von CurrencyResults und das Datum

        :param _value: Betrag in der Basis Währung
        :param _from: 3-Stelliger Code der Basis Währung
        :param _to: Liste der fertigen CurrencyResults
        :param _date: Datum der letzen Wechselkurse
        """
        self._value = _value
        self._from = _from
        self._to = _to
        self._date = _date

    def __str__(self):
        """
        Methode, welche den Betrag, die Basis Währung, die Liste aller Ergebnisse und das Datum in HTML Format zurück gibt

        :return: Daten des Objektes werden als HTML zurück gegeben
        """
        ret = ""
        ret += "<b>{:.2f} {}</b> entsprechen<br>".format(self._value, self._from)
        ret += "<ul>"
        for s in self._to:
            ret += str(s)
        ret += "</ul>"
        ret += "Stand: {}".format(self._date)

        return ret
