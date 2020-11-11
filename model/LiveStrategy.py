from typing import List
from model.BaseClass import BaseClass
import requests

from model.ObjectClass import CurrencyResult
from model.ObjectClass import ClacResult
class LiveStrategy(BaseClass):

    def __init__(self, url="https://api.exchangeratesapi.io/latest"):
        self.url = url

    def get_rates(self, _from: str, _to: List[str]):
        params = {"base": _from, "symbols": ','.join(_to)}
        response = ""
        try:
            response = requests.get(self.url, params=params)
        except Exception as e:
            print(e)
            raise Exception("Es ist ein Fehler aufgetreten: Keine Internetverbindung")

        response_json = response.json()

        if response.status_code != 200:
            raise Exception(response_json['error'])
        return response_json

    def calculate(self, _value: float, _from: str, _to: List[str]):
        pass