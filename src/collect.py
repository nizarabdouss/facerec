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
from PIL import Image as im
import cv2
import imagehash
    
class Person():
    found: datetime.date
    def __init__(self, curr_person: np.ndarray) -> None:
        self._encoding = self.image_encode(curr_person)
        self.found = datetime.date.today()

    def image_encode(self, frame):
        data = im.fromarray(frame)
        data = imagehash.average_hash(data)
        print(data)
        print("\n")
        return data

    






