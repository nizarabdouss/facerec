#import main
import os
import datetime
from re import search
from tkinter import Button
from typing import Any, Optional
import numpy as np
import pandas as pd
from selenium import webdriver
import time

class Search():

    _encode: np.ndarray
    _name: str
    _accounts: dict
    _driver: webdriver
    _button: Optional[Any]
    def __init__(self, encode: np.ndarray) -> None:
        self._encode = encode
        self._name = ''
        self._accounts = {}
        self._driver = webdriver.Chrome(r"/Users/anonymous/Downloads/chromedriver")
        self._driver.get("https://smallseotools.com/reverse-image-search/")
        self._button = self._driver.find_elements_by_xpath('//*[@id="fileupload"]//input')
    def return_encoding(self) -> np.ndarray:
        return self._encode

    def find_accounts(self) -> list[str]:
        pass

    def write_name(self) -> None:
        f = open("names.txt")
        f.write(self._name)
        f.write("\n")
        f.close()
    
    def create_person(self) -> None:
        self._driver.maximize_window()
        time.sleep(4)
        self._button[0].click()
        

class Person(Search):

    _encoding: np.ndarray
    found: datetime.date
    def __init__(self, encode: np.ndarray) -> None:
        super().__init__(encode)
        self._encoding = encode
        self.found = datetime.date.today()

    def get_name(self) -> str:
        return self._name

    def date_recorded(self) -> datetime.date:
        return self.found

    def get_encoding(self) -> np.ndarray:
        return self.return_encoding()
    



