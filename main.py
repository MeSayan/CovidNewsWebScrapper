"""
Name : CL2 Assignment 5
Author : Sayan Mahapatra
Date : 13-03-2022
Description : In this file implementation of menu and main loop is given
"""

import crawler
import wiki_crawler


import queries

from model import *

cov_countries = wiki_crawler.get_covid_countries()

import pprint

# Crawl
def make_dirs():
    import os
    try:
        os.mkdir('scraps')
    except:
        pass
    try:
        os.mkdir('scraps/ts')
    except:
        pass
    try:
        os.mkdir('countries')
    except:
        pass

    os.makedirs("data/countries", exist_ok=True)
    os.makedirs("temp/countries", exist_ok=True)

    global cov_countries
    for c in cov_countries:
        os.makedirs(f"data/countries/{c}", exist_ok=True)
        os.makedirs(f"temp/countries/{c}", exist_ok=True)
    
    os.makedirs("data/responses", exist_ok=True)
    os.makedirs("data/timeline", exist_ok=True)
    os.makedirs("temp/responses", exist_ok=True)
    os.makedirs("temp/timeline", exist_ok=True)


def invalid_command():
    print("Invalid Command")


def help(menu=0):
    print("Menu 1: Worldometers Yesterday Data", 
        "Menu 2: Worldometers Time Series Menu", 
        "Menu 3: Wikipedia Menu"
    )
    if menu == 1:
        print("Enter country/world/continent name followed by | and then one of the following parameters", sep = ' # ')
        print("1. tc -> Total Cases", "2. ac -> Active Cases", "3. td -> Total Deaths", "4. tr -> Total recovered", sep = ' # ')
        print("5. tt -> Total tests", "6. dpm -> Deaths per million", "7. tpm -> Tests per million" , "8. nc -> New Cases", sep = ' # ')
        print("9. nd -> New Deaths", "10. nr -> New Recovered", sep = ' # ')
        print("For Example: Asia | tc")
    elif menu == 2:
        print("Enter date 1 | date 2 | region_name | <dc or ac or dd or dr>. Date must be entered in exact format as shown in example")
        print("1. dc -> Daily Cases", "2. ac -> Active Cases", sep = ' # ')
        print("3. dd -> Daily Deaths", "4. dr -> Daily Recoveries", sep = ' # ')
        print("For Example: Feb 09, 2022 | Feb 18, 2022 | India | dc")
    elif menu == 3:
        # print("Menu 3 helptext")
        print("Enter one of these commands. Refer README for description of queries")
        print("Q1 | <date1>   | <date2> | <timeline or responses or both>")
        print("Q2 | <date1>   | <date2> | <date3>   | <date4> | <timeline or responses>")
        print("Q3 | <country>")
        print("Q4 | <country> | <date1> | <date2>")
        print("Q5 | <country> | <date1> | <date2>")
        print("Q6 | <country> | <date1> | <date2>")
        pass

def part1_fetch_data():
    # import shutil
    # try:
    #     shutil.rmtree("temp/timeline")
    # except:
    #     pass    
    # try:
    #     shutil.rmtree("temp/responses")
    # except:
    #     pass
    import data_extractor_timeline
    data_extractor_timeline.run_extractor()
    import data_extractor_responses
    data_extractor_responses.run_extractor()


def setup():
    # Create log file
    with open("requests.log", "w") as f:
        print("Region | Parameter | Value", file=f)
    make_dirs()

    # Fetch Web pages
    crawler.crawl() 
    wiki_crawler.crawl()

    # Parse Web Pages (Ass 4)
    import data_extractor_1
    data_extractor_1.get_table_data()
    import data_extractor_2
    data_extractor_2.get_ts_data()
    import data_extractor_3
    data_extractor_3.get_ts_data_world()
    
    # Load data into database
    import data_loader
    db = data_loader.build_database()
    
    # Parse webpages (Ass 5)
    part1_fetch_data()
    import data_extractor_country
    data_extractor_country.run_extractor()

    return db


""" Index: Date -> RegStat (ts = None)"""

def build_index(db: DataBase):
    """ Builds a database index based on dates. For running Time Range queries faster """
    from collections import defaultdict
    idx = defaultdict(list)
    try:
        for k, v in db.map.items():
            ts : TimeSeries = v.ts
            if ts:
                for i, d in enumerate(ts.dates):
                    entry = [None, None, None, None]
                    if ts.dc:
                        entry[0] = ts.dc[i]
                    if ts.ac:
                        entry[1] = ts.ac[i]
                    if ts.dd:
                        entry[2] = ts.dd[i]
                    if ts.dr:
                        entry[3] = ts.dr[i]
                    # stip " from begining of d
                    d = d[1:]
                    idx[d].append((k, entry[0], entry[1], entry[2], entry[3]))
    except Exception as e:
        print(e)
    return idx

def preprocess_db(db):
    c = crawler.get_countries()
    o = ['world', 'asia', 'europe', 'north america', 'south america', 'africa',  'oceania']
    for k in list(db.map.keys()):
        if not (k in c or k in o):
            db.map.pop(k)
    index = build_index(db)
    return db, index 

def exit():
    # Cleanup (Best Effort basis)
    import shutil, os
    try:
        shutil.rmtree("scraps", ignore_errors=True)
        shutil.rmtree("countries", ignore_errors=True)
        # os.remove("home.html")
        os.remove("requests.log")
        os.remove("summary.txt")
        # os.remove("parser.out")
        # os.remove("parsetab.py")
        shutil.rmtree("temp", ignore_errors=True)
        shutil.rmtree("data", ignore_errors=True)
    except Exception:
        pass
    finally:
        quit()


def log(*args, file=None):
    if not file:
        file = "requests.log"
    with open(file, "a") as f:
            print(*args, sep = '|', file=f)

def check_data(db : DataBase, countries):
    with open("summary.txt", "w") as f:
        for c in countries:
            print(db.get_stat(c), file=f)


def menu_1(db, index):
    cmenu = 1
    while True:
        print("\nWorldometers Yesterday Data Menu | Enter menu <1 or 2 or 3> to go menu | Enter help for usage")
        line = input('>> ')
        if 'menu' in line:
            try:
                tmenu = int(line.split(" ")[1])
                if tmenu not in [1,2,3]:
                    print("Invalid Menu Command")
                    continue
                elif tmenu != cmenu:
                    return tmenu
            except:
                print("Invalid Menu Command")
        elif line == 'help':
            help(cmenu)
        elif line == 'exit':
            exit()
        else:
            try:
                desc, param = line.split("|")
                desc = desc.strip()
                param = param.strip()
            except Exception:
                print("Invalid Input")
                print("Example: Asia | tc")
                continue
            try:
                stat : RegStat = db.get_stat(desc)
                statw : RegStat = db.get_stat('world')
                # print(stat) #  : Remove
                wtc = statw.tc
                if param == 'tc':
                    if stat.tc:
                        print(f"Total Cases for {desc.title()}:", stat.tc)
                        print(f"% of Total World Cases: {stat.tc * 100 / wtc} %")
                        log(desc, param, stat.tc)
                    else:
                        print(f"Total Cases for {desc.title()}: No Data Found")
                elif param == 'ac':
                    if stat.ac:
                        print(f"Active Cases for {desc.title()}:", stat.ac)
                        print(f"% of Total World Cases: {stat.ac * 100 / wtc} %")
                        log(desc, param, stat.ac)
                    else:
                        print(f"Active Cases for {desc.title()}: No Data Found")
                elif param == 'td':
                    if stat.td:
                        print(f"Total Deaths for {desc.title()}:", stat.td)
                        print(f"% of Total World Cases: {stat.td * 100 / wtc} %")
                        log(desc, param, stat.td)
                    else:
                        print(f"Total Deaths for {desc.title()}: No Data Found")
                elif param == 'tr':
                    if stat.tr:
                        print(f"Total Recoveries for {desc.title()}:", stat.tr)
                        print(f"% of Total World Cases: {stat.tr * 100 / wtc} %")
                        log(desc, param, stat.tr)
                    else:
                        print(f"Total Recoveries for {desc.title()}: No Data Found")
                elif param == 'tt':
                    if stat.tt:
                        print(f"Total Tests for {desc.title()}:", stat.tt)
                        print(f"% of Total World Cases: {stat.tt * 100 / wtc} %")
                        log(desc, param, stat.tt)
                    else:
                        print(f"Total Tests for {desc.title()}: No Data Found")
                elif param == 'dpm':
                    if stat.tdp1m:
                        print(f"Deaths per million for {desc.title()}:", stat.tdp1m)
                        print(f"% of Total World Cases: {stat.tdp1m * 100 / wtc} %")
                        log(desc, param, stat.tdp1m)
                    else:
                        print(f"Deaths per million for {desc.title()}: No Data Found")
                elif param == 'tpm':
                    if stat.ttp1m:
                        print(f"Tests per million for {desc.title()}:", stat.ttp1m)
                        print(f"% of Total World Cases: {stat.ttp1m * 100 / wtc} %")
                        log(desc, param, stat.ttp1m)
                    else:
                        print(f"Tests per million for {desc.title()}: No Data Found")
                elif param == 'nc':
                    if stat.nc:
                        print(f"New Cases for {desc.title()}:", stat.nc)
                        print(f"% of Total World Cases: {stat.nc * 100 / wtc} %")
                        log(desc, param, stat.nc)
                    else:
                        print(f"New Cases for {desc.title()}: No Data Found")
                elif param == 'nd':
                    if stat.nd:
                        print(f"New Deaths for {desc.title()}:", stat.nd)
                        print(f"% of Total World Cases: {stat.nd * 100 / wtc} %")
                        log(desc, param, stat.nd)
                    else:
                        print(f"New Deaths for {desc.title()}: No Data Found")
                elif param == 'nr':
                    if stat.nr:
                        print(f"New Recoveries for {desc.title()}:", stat.nr)
                        print(f"% of Total World Cases: {stat.nr * 100 / wtc} %")
                        log(desc, param, stat.nr)
                    else:
                        print(f"New Recoveries for {desc.title()}: No Data Found")
                else:
                    invalid_command()
            except KeyError:
                print('Region Not found')


def menu_2(db, index):
    cmenu = 2
    while True:
        print("\nWorldometers Time Range Menu | Enter menu <menu id> to go menu | Enter help for usage")
        line = input('>> ')
        if 'menu' in line:
            try:
                tmenu = int(line.split(" ")[1])
                if tmenu not in [1,2,3]:
                    print("Invalid Menu Command")
                    continue
                elif tmenu != cmenu:
                    return tmenu
            except:
                print("Invalid Menu Command")
        elif line == 'help':
            help(menu=cmenu)
        elif line == 'exit':
            exit()
        else:
            try:
                date1, date2, regn, param = line.split("|")
                date1, date2, regn, param = date1.strip(), date2.strip(), regn.strip(), param.strip()
                regnl = regn.lower()
            except Exception:
                print("Invalid Input")
                print("Example: Feb 09, 2022 | Feb 18, 2022 | India | dc")
                continue
            i, o = None, None
            found = False
            if date1 in index and date2 in index:
                for entry in index[date1]:
                    if entry[0] == regnl:
                        found = True
                        if param == 'dc': 
                            i = entry[1]
                        elif param == 'ac':
                            i = entry[2]
                        elif param == 'dd':
                            i = entry[3]
                        elif param == 'dr':
                            i = entry[4]
                        else:
                            print("Invalid Param")
                            continue
                        break
                if not found:
                    print(f"No data available for given {date1} and {regn}")
                    continue
                
                found = False
                for entry in index[date2]:
                    if entry[0] == regnl:
                        found = True
                        if param == 'dc': 
                            o = entry[1]
                        elif param == 'ac':
                            o = entry[2]
                        elif param == 'dd':
                            o = entry[3]
                        elif param == 'dr':
                            o = entry[4]
                        else:
                            # print("Invalid Param")
                            continue
                        break
                if not found:
                    print(f"No data available for given {date2} and {regn}")
                if o is not None and i is not None:
                    change = (o / i) - 1
                else:
                    print("No Data Found")
                    continue
                log(regn, date1, date2, param, f"{change*100:.2f}")
                print(f"% change in {param} from {date1} to {date2} for {regn} is {100 * change:.2f} %  (From {i} to {o})")
                choice = input("Would you like to find the closest country for this parameter and time range [y / n] ? ")
                if choice.lower() == 'y':
                    from collections import defaultdict
                    c1 = defaultdict(int)
                    c2 = defaultdict(int)
                    for entry in index[date1]:
                        if param == 'dc':
                            c1[entry[0]] = entry[1]
                        elif param == 'ac':
                            c1[entry[0]] = entry[2]
                        if param == 'dd':
                            c1[entry[0]] = entry[3]
                        if param == 'dr':
                            c1[entry[0]] = entry[4]
                    
                    for entry in index[date2]:
                        if param == 'dc':
                            c2[entry[0]] = entry[1]
                        elif param == 'ac':
                            c2[entry[0]] = entry[2]
                        if param == 'dd':
                            c2[entry[0]] = entry[3]
                        if param == 'dr':
                            c2[entry[0]] = entry[4]
                    
                    closeval, closename, closep = float('inf'), None, None
                    for k, v in c1.items():
                        if k in c2 and k != regnl and k in countries:
                            try:
                                d = (c2[k] / c1[k]) - 1
                            except Exception:
                                d = float('inf')
                            if abs(d - change) <= closeval:
                                closeval = abs(d - change)
                                closep = d
                                closename = k
                    print(f"{closename.title()} is closest to {regn.title()} for {param} from {date1} to {date2}")
                    print(f"Change in {regn.title()} = {change*100}%, Change in {closename.title()} = {closep * 100} %")
                    log(regn, date1, date2, param + "_closest", f"{closeval*100:.2f}")
            else:
                print(f"No data found for given dates {date1} {date2}")

def menu_3(cov_countries):
    cmenu = 3
    while True:
        print("\nWikipedia Menu | Enter menu <menu id> to go menu | Enter help for usage")
        line = input('>> ')
        if 'menu' in line:
            try:
                tmenu = int(line.split(" ")[1])
                if tmenu not in [1,2,3]:
                    print("Invalid Menu Command")
                    continue
                elif tmenu != cmenu:
                    return tmenu
            except:
                print("Invalid Menu Command")
        elif line == 'help':
            help(menu=cmenu)
        elif line == 'exit':
            exit()
        else:
            if line.startswith("Q1"):
                try:
                    q, d1, d2, s = [x.strip() for x in line.split("|")]
                    if s in ['timeline', 'responses']:
                        res = queries.part1_query(d1, d2, s)
                        print(s.upper())
                        print(res)
                    elif s == 'both':
                        res1 = queries.part1_query(d1, d2,"timeline")
                        res2 = queries.part1_query(d1, d2, "responses")
                        print("TIMELINE")
                        print(res1)
                        print("RESPONSES")
                        print(res2)
                except:
                    "Invalid Input"
            elif line.startswith("Q2"):
                try:
                    q, d1, d2, d3, d4, m = [x.strip() for x in line.split("|")]
                    if m in ['timeline', 'responses']:
                        res = queries.part2_query(d1, d2, d3, d4, m)
                    else:
                        print("Invalid Input")
                except Exception as e:
                    print(e)
            elif line.startswith("Q3"):
                try:
                    q, c = [x.strip() for x in line.split("|")]
                    if c in cov_countries:
                        res = queries.part3_query(c)
                        print(f"Data for {c} available from {res[0]}, {res[1]} to {res[2]}, {res[3]}")
                    else:
                        print("Invalid Input")
                except:
                    "Invalid Input"
            elif line.startswith("Q4"):
                try:
                    q, c, d1, d2 = [x.strip() for x in line.split("|")]
                    res = queries.part4_query(c, d1, d2, plot = True)
                    print("RESULT")
                    print(res)
                except Exception as e:
                    print(e)
            elif line.startswith("Q5"):
                try:
                    q, c, d1, d2 = [x.strip() for x in line.split("|")]
                    res = queries.part5_query(c, d1, d2, cov_countries, top = 3)
                    print(f"Top 3 closest countries are: {res[0][1]}, {res[1][1]}, {res[2][1]}")
                except:
                    "Invalid Input"
            elif line.startswith("Q6"):
                try:
                    q, c, d1, d2 = [x.strip() for x in line.split("|")]
                    queries.part6_query(c, d1, d2, cov_countries, top=3)
                    print(f"Top 3 closest countries are: {res[0][1]}, {res[1][1]}, {res[2][1]}")
                except:
                    "Invalid Input"
            else:
                print("Invalid Query")

if __name__ == "__main__":
    countries = crawler.get_countries()
    db, index = None, None
    db = setup()
    check_data(db, countries)
    db, index = preprocess_db(db)
    menu = 3 # start in wikipedia menu at startup
    while True:
       if menu == 1:
           menu = menu_1(db, index)
       elif menu == 2:
           menu = menu_2(db, index)
       elif menu == 3:
           menu = menu_3(cov_countries)
       else:
           print("Invalid Menu")
           menu = 1
            
