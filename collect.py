#import main
import os
import datetime
from re import search
from typing import Optional
import numpy as np
import pandas as pd

class Person():

    _encoding: np.ndarray
    firstname: str
    lastname: str
    found: datetime.date

    def __init__(self, encode: np.ndarray) -> None:
        self._encoding = encode
        self.firstname = ''
        self.lastname = ''
        self.found = datetime.date.today()

    def get_name(self) -> list[str]:
        return [self.firstname, self.lastname]

    def date_recorded(self) -> datetime.date:
        return self.found

    def get_encoding(self) -> np.ndarray:
        return self._encoding

