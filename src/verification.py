from calendar import c
import imagehash
import numpy as np
from PIL import Image as im
import datetime

class Verify():
    def __init__(self, curr_face: np.ndarray):
        self._curr_face = self.encode_face(curr_face)
        self._timeStamp = datetime.date.today()

    def encode_face(self, frame) -> imagehash:
        data = im.fromarray(frame)
        data = imagehash.average_hash(data)
        print(data)
        return data

    def existence(self) -> bool:
        return self.get_closest_hash(self.get_hashes())

    def get_hashes(self) -> list[any]:
        allMatches = []
        hash = open("src/test.txt", "r")
        for hashes in hash:
            allMatches.append(hashes.strip())
        allMatches = self.increase_prob(allMatches)
        return allMatches

    def get_existance(self):
        return self.existence()

    def increase_prob(self, prob) -> list[any]:
        final = []
        for c in prob:
            count = 0
            breaks = 0
            for i in range(len(c)):
                if c[i] == str(self._curr_face)[i]:
                    count += 1
                else:
                    breaks += 1
            if count >= 4 and breaks <= 12:
                final.append(c)
        print(final)
        return final

    def get_closest_hash(self, hashes: list[any]):
        closest = ""
        mDict = {}
        all_totals = []
        greatest = 0
        for c in str(self._curr_face):
            if c in mDict:
                mDict[c] = mDict[c] + 1
            else:
                mDict[c] = 1

        for h in hashes:
            total = 0
            sDict = {}
            for c in h:
                if c in sDict:
                    sDict[c] = sDict[c] + 1
                else:
                    sDict[c] = 1
            for m in mDict.keys():
                for s in sDict.keys():
                    if s == m and sDict[s] >= mDict[m]:
                        total += 1
            all_totals.append((h, total))  
        
        for score in all_totals:
            if score[1] > greatest:
                greatest = score[1]
                closest = score[0]
        return closest

    
        
                        
