"""
Name : CL2 Assignment 6
Author : Sayan Mahapatra
Date : 13-03-2022
Description : In this file implementation of Data Loader is Given
"""

import re
from model import *
import os

def parse_row_file(file, data: DataBase):
    with open(file, 'r') as f:
        content = f.read()
        # extract country
        rc1 = r'<td(.*?)><a(.*?)>([\S \.]+)</a></td>'
        x = re.search(rc1, content)
        if x:
            content = content[x.span()[1]:]
            desc = x.group(3)
            type = 'COUNTRY'
        else:
            type = 'CONT/WORLD'
            rc2 = r'<td(.*?)>\s<nobr>(.*?)</nobr>\s</td>'
            x = re.search(rc2, content)
            if x:
                content = content[x.span()[1]:]
                desc = x.group(2)
            else:
                # rc3 =  r'<td(.*?)>([\S \.]+)</td>'
                rc3 = r'<td(.*?)>([\w \.]+)</td>'
                x = re.search(rc3, content)
                if not x:
                    raise ParseException
                desc = x.group(2)
                content = content[x.span()[1]:]

        # matches = re.findall(r'<td[^>]*?>(\+|-)?([0-9, ]+)</td>', content)
        matches = re.findall(r'<td[^>]*?>(.*?)</td>', content)
        stat = RegStat(desc)
        num = None
        for i, m in enumerate(matches):
            # s = m[1]
            s = m
            s = ''.join(s.split(','))
            try:
                num = int(s)
            except Exception:
                # Try to see if no can be casted to float
                try:
                    num = float(s)
                except Exception:
                    num = None
            if i == 0:
                stat.tc = num
            elif i == 1:
                stat.nc = num
            elif i == 2:
                stat.td = num
            elif i == 3:
                stat.nd = num
            elif i == 4:
                stat.tr = num
            elif i == 5:
                stat.nr = num
            elif i == 6:
                stat.ac = num
            elif i == 7:
                stat.sc = num
            elif i == 8:
                stat.tcp1m = num
            elif i == 9:
                stat.tdp1m = num
            elif i == 10:
                stat.tt = num
            elif i == 11:
                stat.ttp1m = num
            elif i == 12 and type != 'COUNTRY':
                stat.pop = num
            else:
                break

        # if type == 'COUNTRY':
        #     # rc2 = r'<td.*?population/">([0-9, ]+)</a>\s</td>'
        #     rc2 = r'<td(.*?)>([0-9, ]+)<(.*?)>'
        #     y = re.findall(rc2, content)[12] # 13 element is population
        #     if y:
        #         stat.pop = int(''.join(y[1].split(',')))
        #     if not y:
        #         # some countries dont have anchor links in populations
        #         # print("Check this", desc, file, num)
        #         stat.pop = num
        data.add_statistic(desc, stat, file)


def parse_ts_data(db: DataBase):
    import os
    from collections import defaultdict
    from pathlib import Path
    import re
    ts_map = defaultdict(TimeSeries)
    dir = Path("scraps/ts")
    for f in os.scandir(dir):
        if f.is_file():
            try:
                x = Path(f.path).parts[2].split('.chart')[0]
                c, t = x.split("_")
                c = c.lower()
                if t == 'ac' and c in db.map:
                    # ts_map[c].ac = "AC"
                    with open(f, "r", encoding="utf-8") as fp:
                        content = fp.read()
                        rc = r'\[(.*)\]'
                        dates, ac = re.findall(rc, content)
                        dates = dates.split('",')
                        ac = [int(x) if x != 'null' else None for x in ac.split(",")]
                        ts_map[c].ac = ac
                        ts_map[c].dates = dates
                elif t == 'dc' and c in db.map:
                    with open(f, "r", encoding="utf-8") as fp:
                        content = fp.read()
                        rc = r'\[(.*)\]'
                        dates, dc = re.findall(rc, content)[:2]
                        dates = dates.split('",')
                        dc = [int(x) if x != 'null' else None for x in dc.split(",")]
                        ts_map[c].dc = dc
                        ts_map[c].dates = dates
                elif t == 'dd' and c in db.map:
                    with open(f, "r", encoding="utf-8") as fp:
                        content = fp.read()
                        rc = r'\[(.*)\]'
                        dates, dd = re.findall(rc, content)[:2]
                        dates = dates.split('",')
                        dd = [int(x) if x != 'null' else None for x in dd.split(",")]
                        ts_map[c].dd = dd
                        ts_map[c].dates = dates
                elif t == 'dr' and c in db.map:
                    with open(f, "r", encoding="utf-8") as fp:
                        content = fp.read()
                        rc = r'\[(.*)\]'
                        dates, dr, nc = re.findall(rc, content)
                        dates = dates.split('",')
                        nr = [int(x) if x != 'null' else None for x in dr.split(",")]
                        ts_map[c].dr = nr
                        ts_map[c].dates = dates
            except Exception as e:
                print(e, f)
                pass
    
    for k,v in ts_map.items():
        db.map[k].ts = v
    return db

def build_database(db: DataBase = None, HOME_PAGE_FILE="home.html"):
    if not db:
        db = DataBase()
    for f in os.scandir("scraps"):
        if f.is_file() and re.search(r"YD_ROW_[0-9]{3}\.html", f.path):
            try:
                parse_row_file(f.path, db)
            except Exception as e:
                # print(f, e)
                pass
    db = parse_ts_data(db)
    return db


