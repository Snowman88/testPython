#!/usr/bin/env python
#coding:utf-8

import shutil

class A:
    def __init__(self, suffix1, suffix2, year, month, day, syuruiCd, hinmokuCd):
        self.suffix1 = suffix1
        self.suffix2 = suffix2
        # self.dir = dir
        self.year = year
        self.month = month
        self.day = day
        self.syuruiCd = syuruiCd
        self.hinmokuCd = hinmokuCd

    def makefileSyurui(self):
        for i in range(1, 8):
            suffix = self.suffix1+self.suffix2
            fileName = "{0}_{1}{2:02d}{3:02d}.csv".format(suffix, self.year, self.month, i)
            # fileName = "{0}_{1}{2:02d}.csv".format(suffix, self.year, self.month)
            shutil.copy("NH_20131005.csv", fileName);

    def makefileHinmoku(self):
        for i in range(1, 8):
            suffix = self.suffix1+self.suffix2
            fileName = "{0}_{1}{2:02d}{3:02d}_{4}_{5}.csv".format(suffix, self.year, self.month, i, self.syuruiCd, self.hinmokuCd)
            # fileName = "{0}_{1}{2:02d}_{4}_{5}.csv".format(suffix, self.year, self.month, self.syuruiCd, self.hinmokuCd)
            shutil.copy("NH_20131005.csv", fileName);

if __name__ == "__main__":
    suffix1 = "N" # GH
    suffix2 = "H"
    a = A(suffix1, suffix2, 2013, 9, 5, 1, "0100")
    # a.makefileSyurui();
    a.makefileHinmoku();
