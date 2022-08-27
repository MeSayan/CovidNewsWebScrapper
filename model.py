"""
Name : CL2 Assignment 5
Author : Sayan Mahapatra
Date : 13-03-2022
Description : In this file implementation of model objects is given
"""

from typing import Dict


class TimeSeries:
    def __init__(self, dates=None, ac=None, dc=None, dd=None, dr=None):
        self.dates = dates
        self.ac = ac  # Active Cases series
        self.dc = dc
        self.dd = dd
        self.dr = dr

class RegStat:
    def __init__(self, desc, tc=None, nc=None, td=None, nd=None, tr=None, nr=None, ac=None, sc=None, tcp1m=None, tdp1m=None, tt=None, ttp1m=None, pop=None):
        self.desc = desc
        self.tc = tc
        self.nc = nc
        self.td = td
        self.nd = nd
        self.tr = tr
        self.nr = nr
        self.ac = ac
        self.sc = sc
        self.tcp1m = tcp1m
        self.tdp1m = tdp1m
        self.tt = tt
        self.ttp1m = ttp1m
        self.pop = pop
        self.ts : TimeSeries = None  # TimeSeries object

    def get_desc(self):
        return self.desc

    def __str__(self):
        return f"({self.desc},{self.tc},{self.nc},{self.td},{self.nd},{self.tr},{self.nr},{self.ac},{self.sc},{self.tcp1m},{self.tdp1m},{self.tt},{self.ttp1m})"

class DataBase:
    def __init__(self):
        self.map : Dict[str, TimeSeries] = {}

    def add_statistic(self, key: str, stat: RegStat, file):
        key = key.lower()
        if key in self.map:
            # print('Duplicate Key', stat, self.map[key], file)
            pass
        else:
            self.map[key] = stat

    def list_statistics(self):
        for k, v in self.map.items():
            print(k, v)

    def get_stat(self, desc):
        if desc.lower() in self.map:
            return self.map[desc.lower()]
        else:
            raise KeyError


class ParseException(Exception):
    """ Parsing Error """
    pass
