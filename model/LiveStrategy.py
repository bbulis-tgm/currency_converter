from typing import List
from model.BaseClass import BaseClass
import requests

from model.ObjectClass import CurrencyResult
from model.ObjectClass import CalcResult


class LiveStrategy(BaseClass):

    def __init__(self, url="https://api.exchangeratesapi.io/latest"):
        """
        Init Methode, welche die URL für die Anfragen bekommt. Diese ist Standardmäßig gesetzt

        :param url: URL für die Abfrage der Berechnungen
        """
        self.url = url

    def get_rates(self, _from: str, _to: List[str]):
        """
        Methode ruft die akutellen Wechselkurse von der Online-API ab
        Übergeben werden der API die Basis Währung und die Wechselkurse zur Basis Währung

        :param _from: String welcher angibt von welcher Basis Währung ausgegangen wird
        :param _to: Liste aller Währungen von denen der Wechselkur abgefragt wird
        :return:
        """
        params = {"base": _from, "symbols": ','.join(_to)}
        try:
            response = requests.get(self.url, params=params)
        except Exception as e:
            print(e)
            # Gibt eine Error Message aus wenn die Abfrage an die API nicht funktioniert hat
            raise Exception("Es ist ein Fehler aufgetreten: Keine Internetverbindung")

        response_json = response.json()

        # Überprüfung ob der Statuscode der Abfrage funktioniert hat
        if response.status_code != 200:
            raise Exception(response_json['error'])
        return response_json

    def calculate(self, _value: float, _from: str, _to: List[str]):
        """
        Funktion welche das Berechnen der Währungen mit den passenden Wechselkursen übernimmt

        :param _value: Der Betrag, welcher Umgerechnet werden soll
        :param _from: Die Währung, welche als Basis Währung
        :param _to: Die Liste der Währungen in die Umgerechnet werden soll
        :return: Das Objekt, welche alle Ergebnisse der Umrechnung enthält
        """
        response = self.get_rates(_from, _to)
        rates_only = response['rates']
        ret = []
        for s in rates_only.keys():
            ret.append(CurrencyResult(s, rates_only[s], rates_only[s] * _value))
        return CalcResult(_value, _from, ret, response['date'])
