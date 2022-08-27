"""
Name : CL2 Assignment 5
Author : Sayan Mahapatra
Date : 13-03-2022
Description : In this file implementation of data extractor 1 is given
"""

import ply.yacc as yacc
import ply.lex
import ply.yacc
import random
import re
import os
import traceback
import wiki_crawler


month_to_index = {
    "January" : 1,
    "February" : 2,
    "March" : 3, 
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12
}

def Turkey(c='Turkey'):
    for file in os.scandir(f"data/countries/{c}"):
        if os.path.isfile(file.path):
            with open(file.path) as f:
                text = f.read()
                for headline in re.findall(r'<span class="mw-headline" id=(.*?)<h2>', text, re.DOTALL):
                    i = headline.find('"')
                    j = headline.find('"', i+1)
                    if i >= 0 and j >= 0:
                        ds = headline[i+1:j]
                        try:
                            month, year = ds.split("_")
                        except Exception as e:
                            # print(e)
                            continue
                    
                        if not month in month_to_index:
                            continue

                        #cleanup
                        clean = re.sub(r'<.*?>|&#[0-9]{2,3};[0-9]*&#[0-9]{2,3};', '', headline)
                        # note these
                        clean = re.sub(r'\[edit\]', '', clean)
                        clean = clean[clean.find('\n')+1:]
                        clean = clean[:clean.find("References")]
                        wfile = f"temp/countries/{c}/{month}-{year}.txt"
                        with open(wfile, 'w') as f:
                            f.write(clean)
                            print(f"{wfile}")

def Argentina(c="Argentina"):
    for file in os.scandir(f"data/countries/{c}"):
        if os.path.isfile(file.path):
            with open(file.path) as f:
                text = f.read()
                for headline in re.findall(r'<span class="mw-headline" id=(.*?)<h3|h2>', text, re.DOTALL):
                    month, year = None, None
                    i = headline.find('"')
                    j = headline.find('"', i+1)
                    if i >= 0 and j >= 0:
                        ds = headline[i+1:j]
                        try:
                            month, year = ds.split("_")
                        except Exception as e:
                            # print(e)
                            continue
                        #cleanup

                        if not month in month_to_index:
                            continue
                        clean = re.sub(r'<.*?>|&#[0-9]{2,3};[0-9]*&#[0-9]{2,3};', '', headline)
                        # note these
                        clean = re.sub(r'\[edit\]', '', clean)
                        clean = clean[clean.find('\n')+1:]
                        clean = clean[:clean.find("References")]
                        wfile = f"temp/countries/{c}/{month}-{year}.txt"
                        with open(wfile, 'w') as f:
                            f.write(clean)
                            print(f"{wfile}")

def SouthAfrica(c="South Africa"):
    for file in os.scandir(f"data/countries/{c}"):
        if os.path.isfile(file.path):
            with open(file.path) as f:
                text = f.read()
                for headline in re.findall(r'<span class="mw-headline" id=(.*?)<h3|h2>', text, re.DOTALL):
                    month, year = None, None
                    i = headline.find('"')
                    j = headline.find('"', i+1)
                    if i >= 0 and j >= 0:
                        ds = headline[i+1:j]
                        try:
                            month, year = ds.split("_")
                        except Exception as e:
                            # print(e)
                            continue
                        #cleanup

                        if not month in month_to_index:
                            continue
                        clean = re.sub(r'<.*?>|&#[0-9]{2,3};[0-9]*&#[0-9]{2,3};', '', headline)
                        # note these
                        clean = re.sub(r'\[edit\]', '', clean)
                        clean = clean[clean.find('\n')+1:]
                        clean = clean[:clean.find("References")]
                        wfile = f"temp/countries/{c}/{month}-{year}.txt"
                        with open(wfile, 'w') as f:
                            f.write(clean)
                            print(f"{wfile}")

def Pakistan(c="Pakistan"):
    for file in os.scandir(f"data/countries/{c}"):
        if os.path.isfile(file.path):
            with open(file.path) as f:
                text = f.read()
                for headline in re.findall(r'<span class="mw-headline" id=(.*?)<h2>', text, re.DOTALL):
                    month, year = None, None
                    i = headline.find('"')
                    j = headline.find('"', i+1)
                    if i >= 0 and j >= 0:
                        ds = headline[i+1:j]
                        try:
                            month, year = ds.split("_")
                        except Exception as e:
                            # print(e)
                            continue
                        #cleanup

                        if not month in month_to_index:
                            continue
                        clean = re.sub(r'<.*?>|&#[0-9]{2,3};[0-9]*&#[0-9]{2,3};', '', headline)
                        # note these
                        clean = re.sub(r'\[edit\]', '', clean)
                        clean = clean[clean.find('\n')+1:]
                        clean = clean[:clean.find("References")]
                        wfile = f"temp/countries/{c}/{month}-{year}.txt"
                        with open(wfile, 'w') as f:
                            f.write(clean)
                            print(f"{wfile}")

def Bangladesh(c="Bangladesh"):
    for file in os.scandir(f"data/countries/{c}"):
        if os.path.isfile(file.path):
            with open(file.path) as f:
                text = f.read()
                for headline in re.findall(r'<span class="mw-headline" id=(.*?)<h3|h2>', text, re.DOTALL):
                    month, year = None, None
                    i = headline.find('"')
                    j = headline.find('"', i+1)
                    if i >= 0 and j >= 0:
                        ds = headline[i+1:j]
                        try:
                            month = ds
                            year = 2020 # as per last citation
                        except Exception as e:
                            # print(e)
                            continue
                        #cleanup

                        if not month in month_to_index:
                            continue
                        clean = re.sub(r'<.*?>|&#[0-9]{2,3};[0-9]*&#[0-9]{2,3};', '', headline)
                        # note these
                        clean = re.sub(r'\[edit\]', '', clean)
                        clean = clean[clean.find('\n')+1:]
                        clean = clean[:clean.find("References")]
                        wfile = f"temp/countries/{c}/{month}-{year}.txt"
                        with open(wfile, 'w') as f:
                            f.write(clean)
                            print(f"{wfile}")

def Spain(c="Spain"):
    for file in os.scandir(f"data/countries/{c}"):
        if os.path.isfile(file.path):
            with open(file.path) as f:
                text = f.read()
                for headline in re.findall(r'<span class="mw-headline" id=(.*?)<h2>', text, re.DOTALL):
                    month, year = None, None
                    i = headline.find('"')
                    j = headline.find('"', i+1)
                    if i >= 0 and j >= 0:
                        ds = headline[i+1:j]
                        try:
                            month = ds
                            year = 2020 # as per last citation
                        except Exception as e:
                            # print(e)
                            continue
                        #cleanup

                        if not month in month_to_index:
                            continue
                        # removess no in citations as well
                        clean = re.sub(r'<.*?>|&#[0-9]{2,3};[0-9]*&#[0-9]{2,3};', '', headline)
                        # note these
                        clean = re.sub(r'\[edit\]', '', clean)
                        clean = clean[clean.find('\n')+1:]
                        clean = clean[:clean.find("References")]
                        wfile = f"temp/countries/{c}/{month}-{year}.txt"
                        with open(wfile, 'w') as f:
                            f.write(clean)
                            print(f"{wfile}")

def Mexico(c="Mexico"):
   for file in os.scandir(f"data/countries/{c}"):
        if os.path.isfile(file.path):
            with open(file.path) as f:
                text = f.read()
                for headline in re.findall(r'<span class="mw-headline" id=(.*?)<h2>', text, re.DOTALL):
                    month, year = None, None
                    i = headline.find('"')
                    j = headline.find('"', i+1)
                    if i >= 0 and j >= 0:
                        ds = headline[i+1:j]
                        try:
                            month, year  = ds.split("_")
                        except Exception as e:
                            # print(e)
                            continue
                        #cleanup

                        if not month in month_to_index:
                            continue
                        # removess no in citations as well
                        clean = re.sub(r'<.*?>|&#[0-9]{2,3};[0-9]*&#[0-9]{2,3};', '', headline)
                        # note these
                        clean = re.sub(r'\[edit\]', '', clean)
                        clean = clean[clean.find('\n')+1:]
                        clean = clean[:clean.find("References")]
                        wfile = f"temp/countries/{c}/{month}-{year}.txt"
                        with open(wfile, 'w') as f:
                            f.write(clean)
                            print(f"{wfile}") 

def Australia(c="Australia"):
    for file in os.scandir(f"data/countries/{c}"):
        if os.path.isfile(file.path):
            with open(file.path) as f:
                text = f.read()
                try:
                    year = int(re.search(r'.*([0-9]{4}).*', file.path).group(1))
                except Exception as e:
                    print(e, f.path)
                for headline in re.findall(r'<span class="mw-headline" id=(.*?)<h2>', text, re.DOTALL):
                    month = None
                    i = headline.find('"')
                    j = headline.find('"', i+1)
                    if i >= 0 and j >= 0:
                        ds = headline[i+1:j]
                        try:
                            month = ds.split("_")[0]
                        except Exception as e:
                            # print(e)
                            continue
                        #cleanup

                        if not month in month_to_index:
                            continue
                        clean = re.sub(r'<.*?>|&#[0-9]{2,3};[0-9]*&#[0-9]{2,3};', '', headline)
                        # note these
                        clean = re.sub(r'\[edit\]', '', clean)
                        clean = clean[clean.find('\n')+1:]
                        clean = clean[:clean.find("References")]
                        wfile = f"temp/countries/{c}/{month}-{year}.txt"
                        with open(wfile, 'w') as f:
                            f.write(clean)
                            print(f"{wfile}")

def India(c="India"):
    for file in os.scandir(f"data/countries/{c}"):
        if os.path.isfile(file.path):
            with open(file.path) as f:
                text = f.read()
                try:
                    year = int(re.search(r'.*([0-9]{4}).*', file.path).group(1))
                except Exception as e:
                    print(e, f.path)
                for headline in re.findall(r'<span class="mw-headline" id=(.*?)<h2>', text, re.DOTALL):
                    month = None
                    i = headline.find('"')
                    j = headline.find('"', i+1)
                    if i >= 0 and j >= 0:
                        ds = headline[i+1:j]
                        try:
                            month = ds.split("_")[0]
                        except Exception as e:
                            # print(e)
                            continue
                        #cleanup

                        if not month in month_to_index:
                            continue
                        clean = re.sub(r'<.*?>|&#[0-9]{2,3};[0-9]*&#[0-9]{2,3};', '', headline)
                        # note these
                        clean = re.sub(r'\[edit\]', '', clean)
                        clean = clean[clean.find('\n')+1:]
                        clean = clean[:clean.find("References")]
                        wfile = f"temp/countries/{c}/{month}-{year}.txt"

                        if 'January' in file.path and 'May 2020' in file.path and month == 'June':
                            continue # This section supposed to be empty

                        with open(wfile, 'w') as f:
                            f.write(clean)
                            print(f"{wfile}")

def Ghana(c="Ghana"):
    for file in os.scandir(f"data/countries/{c}"):
        if os.path.isfile(file.path):
            with open(file.path) as f:
                text = f.read()
                try:
                    year = int(re.search(r'.*([0-9]{4}).*', file.path).group(1))
                except Exception as e:
                    print(e, f.path)
                for headline in re.findall(r'<span class="mw-headline" id=(.*?)<h[23]>', text, re.DOTALL):
                    month = None
                    i = headline.find('"')
                    j = headline.find('"', i+1)
                    if i >= 0 and j >= 0:
                        ds = headline[i+1:j]
                        if ds in ['References', 'Timeline']:
                            continue
                        try:
                            # Special case -> 2021 web page has 2022 data
                            if 'Ghana (2021)' in file.path:
                                month, year = ds.split("_")
                            else:
                                month = ds.split("_")[0]
                        except Exception as e:
                            print(e, ds)
                            continue
                        #cleanup

                        if not month in month_to_index:
                            continue
                        clean = re.sub(r'<.*?>|&#[0-9]{2,3};[0-9]*&#[0-9]{2,3};', '', headline)
                        # note these
                        clean = re.sub(r'\[edit\]', '', clean)
                        clean = clean[clean.find('\n')+1:]
                        clean = clean[:clean.find("References")]
                        wfile = f"temp/countries/{c}/{month}-{year}.txt"

                        with open(wfile, 'w') as f:
                            f.write(clean)
                            print(f"{wfile}")


def United_States(c="United States"):
    for file in os.scandir(f"data/countries/{c}"):
        if os.path.isfile(file.path):
            with open(file.path) as f:
                text = f.read()
                try:
                    year = int(re.search(r'.*([0-9]{4}).*', file.path).group(1))
                except Exception as e:
                    print(e, f.path)
                for headline in re.findall(r'<span class="mw-headline" id=(.*?)<h[32]>', text, re.DOTALL):
                    headline[headline.find("References")]
                    month = None
                    i = headline.find('"')
                    j = headline.find('"', i+1)
                    if i >= 0 and j >= 0:
                        ds = headline[i+1:j]
                        try:
                            month = ds.split("_")[0]
                        except Exception as e:
                            # print(e)
                            continue
                        #cleanup

                        if not month in month_to_index:
                            continue
                        clean = re.sub(r'<.*?>|&#[0-9]{2,3};[0-9]*&#[0-9]{2,3};', '', headline)
                        # note these
                        clean = re.sub(r'\[edit\]', '', clean)
                        clean = clean[clean.find('\n')+1:]
                        clean = clean[:clean.find("References")]
                        wfile = f"temp/countries/{c}/{month}-{year}.txt"
                        with open(wfile, 'a') as f:
                            f.write(clean)
                            print(f"{wfile}")


def Malaysia(c="Malaysia"):
    for file in os.scandir(f"data/countries/{c}"):
        if os.path.isfile(file.path):
            with open(file.path) as f:
                text = f.read()
                try:
                    year = int(re.search(r'.*([0-9]{4}).*', file.path).group(1))
                except Exception as e:
                    print(e, f.path)
                for headline in re.findall(r'<span class="mw-headline" id=(.*?)<h[32]>', text, re.DOTALL):
                    month = None
                    i = headline.find('"')
                    j = headline.find('"', i+1)
                    if i >= 0 and j >= 0:
                        ds = headline[i+1:j]
                        try:
                            month = ds.split("_")[0]
                        except Exception as e:
                            # print(e)
                            continue
                        #cleanup

                        if not month in month_to_index:
                            continue
                        # Remove table
                        headline = headline[headline.find("</table>")+1:]
                        clean = re.sub(r'<.*?>|&#[0-9]{2,3};[0-9]*&#[0-9]{2,3};', '', headline)
                        # note these
                        clean = re.sub(r'\[edit\]', '', clean)
                        clean = clean[clean.find('\n')+1:]
                        clean = clean[:clean.find("References")]
                        wfile = f"temp/countries/{c}/{month}-{year}.txt"
                        with open(wfile, 'w') as f:
                            f.write(clean)
                            print(f"{wfile}")


def Singapore(c="Singapore"):
    for file in os.scandir(f"data/countries/{c}"):
        if os.path.isfile(file.path):
            with open(file.path) as f:
                text = f.read()
                try:
                    year = int(re.search(r'.*([0-9]{4}).*', file.path).group(1))
                except Exception as e:
                    print(e, f.path)
                for headline in re.findall(r'<span class="mw-headline" id=(.*?)<h[32]>', text, re.DOTALL):
                    month = None
                    i = headline.find('"')
                    j = headline.find('"', i+1)
                    if i >= 0 and j >= 0:
                        ds = headline[i+1:j]
                        try:
                            month = ds.split("_")[0]
                        except Exception as e:
                            # print(e)
                            continue
                        #cleanup

                        if not month in month_to_index:
                            continue

                        # Remove table
                        headline = headline[headline.find("</table>")+1:]
                        clean = re.sub(r'<.*?>|&#[0-9]{2,3};[0-9]*&#[0-9]{2,3};', '', headline)
                        # note these
                        clean = re.sub(r'\[edit\]', '', clean)
                        clean = clean[clean.find('\n')+1:]
                        clean = clean[:clean.find("References")]
                        wfile = f"temp/countries/{c}/{month}-{year}.txt"
                        with open(wfile, 'w') as f:
                            f.write(clean)
                            print(f"{wfile}")


def Canada(c="Canada"):
    for file in os.scandir(f"data/countries/{c}"):
        if os.path.isfile(file.path):
            if not 'Ontario' in file.path:
                continue
            with open(file.path) as f:
                text = f.read()
                try:
                    year = int(re.search(r'.*([0-9]{4}).*', file.path).group(1))
                except Exception as e:
                    print(e, f.path)
                for headline in re.findall(r'<span class="mw-headline" id=(.*?)<h[32]>', text, re.DOTALL):
                    month = None
                    i = headline.find('"')
                    j = headline.find('"', i+1)
                    if i >= 0 and j >= 0:
                        ds = headline[i+1:j]
                        try:
                            month = ds.split("_")[0]
                        except Exception as e:
                            # print(e)
                            continue
                        #cleanup

                        if not month in month_to_index:
                            continue

                        # Remove table
                        headline = headline[headline.find("</table>")+1:]
                        clean = re.sub(r'<.*?>|&#[0-9]{2,3};[0-9]*&#[0-9]{2,3};', '', headline)
                        # note these
                        clean = re.sub(r'\[edit\]', '', clean)
                        clean = clean[clean.find('\n')+1:]
                        clean = clean[:clean.find("References")]
                        wfile = f"temp/countries/{c}/{month}-{year}.txt"
                        with open(wfile, 'w') as f:
                            f.write(clean)
                            print(f"{wfile}")

def Brazil(c="Brazil"):
    for file in os.scandir(f"data/countries/{c}"):
        if os.path.isfile(file.path):
            with open(file.path) as f:
                text = f.read()
                for headline in re.findall(r'<span class="mw-headline" id=(.*?)<h2>', text, re.DOTALL):
                    month, year = None, None
                    i = headline.find('"')
                    j = headline.find('"', i+1)
                    if i >= 0 and j >= 0:
                        ds = headline[i+1:j]
                        if not ds.count("_") == 1:
                            continue
                        try:
                            month, year = ds.split("_")
                        except Exception as e:
                            # print(e)
                            continue
                        #cleanup

                        if not month in month_to_index:
                            continue
                        clean = re.sub(r'<.*?>|&#[0-9]{2,3};[0-9]*&#[0-9]{2,3};', '', headline)
                        # note these
                        clean = re.sub(r'\[edit\]', '', clean)
                        clean = clean[clean.find('\n')+1:]
                        clean = clean[:clean.find("References")]
                        wfile = f"temp/countries/{c}/{month}-{year}.txt"
                        with open(wfile, 'w') as f:
                            f.write(clean)
                            print(f"{wfile}")

def Indonesia(c="Indonesia"):
    for file in os.scandir(f"data/countries/{c}"):
        if os.path.isfile(file.path):
            with open(file.path) as f:
                text = f.read()
                try:
                    year = int(re.search(r'.*([0-9]{4}).*', file.path).group(1))
                except Exception as e:
                    print(e, f.path)
                for headline in re.findall(r'<span class="mw-headline" id=(.*?)<h[2]>', text, re.DOTALL):
                    month = None
                    i = headline.find('"')
                    j = headline.find('"', i+1)
                    if i >= 0 and j >= 0:
                        ds = headline[i+1:j]
                        try:
                            month = ds.split("_")[0]
                        except Exception as e:
                            # print(e)
                            continue
                        #cleanup

                        if not month in month_to_index:
                            continue

                        clean = re.sub(r'<.*?>|&#[0-9]{2,3};[0-9]*&#[0-9]{2,3};', '', headline)
                        # note these
                        clean = re.sub(r'\[edit\]', '', clean)
                        clean = clean[clean.find('\n')+1:]
                        clean = clean[:clean.find("References")]
                        wfile = f"temp/countries/{c}/{month}-{year}.txt"
                        with open(wfile, 'w') as f:
                            f.write(clean)
                            print(f"{wfile}")

def Nigeria(c="Nigeria"):
    for file in os.scandir(f"data/countries/{c}"):
        if os.path.isfile(file.path):
            with open(file.path) as f:
                text = f.read()
                try:
                    year = int(re.search(r'.*([0-9]{4}).*', file.path).group(1))
                except Exception as e:
                    print(e, f.path)
                for headline in re.findall(r'<span class="mw-headline" id=(.*?)<h[32]>', text, re.DOTALL):
                    month = None
                    i = headline.find('"')
                    j = headline.find('"', i+1)
                    if i >= 0 and j >= 0:
                        ds = headline[i+1:j]
                        try:
                            month = ds.split("_")[0]
                        except Exception as e:
                            # print(e)
                            continue
                        #cleanup

                        if not month in month_to_index:
                            continue

                        clean = re.sub(r'<.*?>|&#[0-9]{2,3};[0-9]*&#[0-9]{2,3};', '', headline)
                        # note these
                        clean = re.sub(r'\[edit\]', '', clean)
                        clean = clean[clean.find('\n')+1:]
                        clean = clean[:clean.find("References")]
                        wfile = f"temp/countries/{c}/{month}-{year}.txt"
                        with open(wfile, 'w') as f:
                            f.write(clean)
                            print(f"{wfile}")

def Ireland(c="Ireland"):
    for file in os.scandir(f"data/countries/{c}"):
        if os.path.isfile(file.path):
            with open(file.path) as f:
                text = f.read()
                try:
                    year = int(re.search(r'.*([0-9]{4}).*', file.path).group(1))
                except Exception as e:
                    print(e, f.path)
                for headline in re.findall(r'<span class="mw-headline" id=(.*?)<h[32]>', text, re.DOTALL):
                    month = None
                    i = headline.find('"')
                    j = headline.find('"', i+1)
                    if i >= 0 and j >= 0:
                        ds = headline[i+1:j]
                        try:
                            month = ds.split("_")[0]
                        except Exception as e:
                            # print(e)
                            continue
                        #cleanup

                        if not month in month_to_index:
                            continue

                        # Remove table
                        headline2 = headline[:headline.find("<table")] + headline[headline.find("</table>")+1:]

                        clean = re.sub(r'<.*?>|&#[0-9]{2,3};[0-9]*&#[0-9]{2,3};', '', headline)
                        # note these
                        clean = re.sub(r'\[edit\]', '', clean)
                        clean = clean[clean.find('\n')+1:]
                        clean = clean[:clean.find("References")]
                        wfile = f"temp/countries/{c}/{month}-{year}.txt"
                        with open(wfile, 'w') as f:
                            f.write(clean)
                            print(f"{wfile}")


def Philippines(c="Philippines"):
    for file in os.scandir(f"data/countries/{c}"):
        if os.path.isfile(file.path):
            with open(file.path) as f:
                text = f.read()
                try:
                    year = int(re.search(r'.*([0-9]{4}).*', file.path).group(1))
                except Exception as e:
                    print(e, f.path)
                for headline in re.findall(r'<span class="mw-headline" id=(.*?)<h[32]>', text, re.DOTALL):
                    month = None
                    i = headline.find('"')
                    j = headline.find('"', i+1)
                    if i >= 0 and j >= 0:
                        ds = headline[i+1:j]
                        try:
                            month = ds.split("_")[0]
                        except Exception as e:
                            # print(e)
                            continue
                        #cleanup

                        if not month in month_to_index:
                            continue

                        clean = re.sub(r'<.*?>|&#[0-9]{2,3};[0-9]*&#[0-9]{2,3};', '', headline)
                        # note these
                        clean = re.sub(r'\[edit\]', '', clean)
                        clean = clean[clean.find('\n')+1:]
                        clean = clean[:clean.find("References")]
                        wfile = f"temp/countries/{c}/{month}-{year}.txt"
                        with open(wfile, 'w') as f:
                            f.write(clean)
                            print(f"{wfile}")

def England(c="England"):
    for file in os.scandir(f"data/countries/{c}"):
        if os.path.isfile(file.path):
            with open(file.path) as f:
                text = f.read()
                try:
                    year = int(re.search(r'.*([0-9]{4}).*', file.path).group(1))
                except Exception as e:
                    print(e, f.path)
                for headline in re.findall(r'<span class="mw-headline" id=(.*?)<h[32]>', text, re.DOTALL):
                    month = None
                    i = headline.find('"')
                    j = headline.find('"', i+1)
                    if i >= 0 and j >= 0:
                        ds = headline[i+1:j]
                        try:
                            month = ds.split("_")[0]
                        except Exception as e:
                            # print(e)
                            continue
                        #cleanup

                        if not month in month_to_index:
                            continue

                        clean = re.sub(r'<.*?>|&#[0-9]{2,3};[0-9]*&#[0-9]{2,3};', '', headline)
                        # note these
                        clean = re.sub(r'\[edit\]', '', clean)
                        clean = clean[clean.find('\n')+1:]
                        clean = clean[:clean.find("References")]
                        wfile = f"temp/countries/{c}/{month}-{year}.txt"
                        with open(wfile, 'w') as f:
                            f.write(clean)
                            print(f"{wfile}")

def New_Zealand(c="New Zealand"):
    for file in os.scandir(f"data/countries/{c}"):
        if os.path.isfile(file.path):
            with open(file.path) as f:
                text = f.read()
                try:
                    year = int(re.search(r'.*([0-9]{4}).*', file.path).group(1))
                except Exception as e:
                    print(e, f.path)
                for headline in re.findall(r'<span class="mw-headline" id=(.*?)<h[32]>', text, re.DOTALL):
                    month = None
                    i = headline.find('"')
                    j = headline.find('"', i+1)
                    if i >= 0 and j >= 0:
                        ds = headline[i+1:j]
                        try:
                            month = ds.split("_")[0]
                        except Exception as e:
                            # print(e)
                            continue
                        #cleanup

                        if not month in month_to_index:
                            continue

                        headline = headline[headline.find("</table>")+1:]
                        clean = re.sub(r'<.*?>|&#[0-9]{2,3};[0-9]*&#[0-9]{2,3};', '', headline)
                        # note these
                        clean = re.sub(r'\[edit\]', '', clean)
                        clean = clean[clean.find('\n')+1:]
                        clean = clean[:clean.find("References")]
                        wfile = f"temp/countries/{c}/{month}-{year}.txt"
                        with open(wfile, 'w') as f:
                            f.write(clean)
                            print(f"{wfile}")

def Russia(c="Russia"):
    for file in os.scandir(f"data/countries/{c}"):
        if os.path.isfile(file.path):
            with open(file.path) as f:
                text = f.read()
                try:
                    year = int(re.search(r'.*([0-9]{4}).*', file.path).group(1))
                except Exception as e:
                    print(e, f.path)
                for headline in re.findall(r'<span class="mw-headline" id=(.*?)<h[32]>', text, re.DOTALL):
                    month = None
                    i = headline.find('"')
                    j = headline.find('"', i+1)
                    if i >= 0 and j >= 0:
                        ds = headline[i+1:j]
                        try:
                            month = ds.split("_")[0]
                        except Exception as e:
                            # print(e)
                            continue
                        #cleanup

                        if month == 'January–February':
                            month = 'January'

                        if not month in month_to_index:
                            continue

                        headline = headline[headline.find("</table>")+1:]
                        clean = re.sub(r'<.*?>|&#[0-9]{2,3};[0-9]*&#[0-9]{2,3};', '', headline)
                        # note these
                        clean = re.sub(r'\[edit\]', '', clean)
                        clean = clean[clean.find('\n')+1:]
                        clean = clean[:clean.find("References")]
                        
                        if month == "January" and year == 2020:
                            wfile_j = f"temp/countries/{c}/January-{2020}.txt"
                            wfile_f = f"temp/countries/{c}/February-{2020}.txt"
                            # Find first instance of word Feb, copy till \n before this instance
                            firstinstance = clean.find("February")
                            croptill = clean.rfind("\n", None, firstinstance)
                            cleanj = clean[:croptill]
                            cleanf = clean[croptill+1:]
                            with open(wfile_j, 'w') as f:
                                f.write(cleanj)
                                print(f"{wfile_j} {file.path}")
                            with open(wfile_f, 'w') as f:
                                f.write(cleanf)
                                print(f"{wfile_f} {file.path}")
                        else:
                            wfile = f"temp/countries/{c}/{month}-{year}.txt"
                            with open(wfile, 'w') as f:
                                f.write(clean)
                                print(f"{wfile} {file.path}")



def run_extractor():
    
    cov_countries = wiki_crawler.get_covid_countries()
    for c in cov_countries:
        os.makedirs(f"temp/countries/{c}", exist_ok=True)
    
    for c in cov_countries:
        if c == 'Turkey':
            Turkey()
            pass
        elif c == 'Argentina':
            Argentina()
            pass
        elif c == 'South Africa':
            SouthAfrica()
            pass
        elif c == 'Pakistan':
            Pakistan()
            pass
        elif c == 'Bangladesh':
            Bangladesh()
            pass
        elif c == 'Spain':
            Spain()
            pass
        elif c == 'Mexico':
            Mexico()
            pass
        elif c == "Australia":
            Australia()
            pass
        elif c == "United States":
            United_States()
            pass
        elif c == "Malaysia":
            Malaysia()
            pass
        elif c == "Singapore":
            Singapore()
            pass
        elif c == "India":
            India()
            pass
        elif c == "Ghana":
            Ghana()
            pass
        elif c == "Canada":
            Canada()
            pass
        elif c == "Brazil":
            Brazil()
            pass
        elif c == "Indonesia":
            Indonesia()
            pass
        elif c == "Nigeria":
            Nigeria()
            pass
        elif c == "Ireland":
            Ireland()
            pass
        elif c == 'Philippines':
            Philippines()
            pass
        elif c == "England":
            England()
            pass
        elif c == "New Zealand":
            New_Zealand()
            pass
        elif c == "Russia":
            Russia()
            pass

     
# run_extractor()
