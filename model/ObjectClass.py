from typing import List


class CurrencyResult:

    def __init__(self, _name: str, _wechselkurs: float, _value: float):
        self._name = _name
        self._wechselkurs = _wechselkurs
        self._value = _value

    def __str__(self):
        return "<li><b>{:.2f} {}</b> (Kurs: {:f}</li>".format(self._value, self._name, self._wechselkurs)


class ClacResult:

    def __init__(self, _value: float, _from: str, _to: List[CurrencyResult], _date: str):
        self._value = _value
        self._from = _from
        self._to = _to
        self._date = _date

    def __str__(self):
        ret = ""
        ret += "<b>{:.2f} {}</b> entsprechen<br>".format(self._value, self._from)
        ret += "<ul>"
        for s in self._to:
            ret += str(s)
        ret += "</ul>"
        ret += "Stand: {}".format(self._date)

        return ret
