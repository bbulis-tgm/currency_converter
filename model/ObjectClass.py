from typing import  List

class CurrencyResult:

    def __init__(self, _name: str, _wechselkurs: float, _value: float):
        self._name = _name
        self._wechselkurs = _wechselkurs
        self._value = _value

    def __str__(self):
        return "<li><b>{:.2f} {}</b> (Kurs: {:f}</li>".format(self._value, self._name, self._wechselkurs)