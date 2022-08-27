"""
Name : CL2 Assignment 5
Author : Sayan Mahapatra
Date : 13-03-2022
Description : In this file implementation of Crawler (Wikipedia) is given
"""

import urllib.request
from urllib.parse import urljoin
import re


months_to_p = [
    "July"
]


def get_worldometer_countries(file="worldometers_countrylist.txt"):
    countries = set()
    with open(file, "r") as f:
        exclude = ["Europe:", "Asia", "North America:",
                   "South America", "Africa", "Oceania", ""]
        for line in f:
            line_s = line.strip()
            if not line_s in exclude and not re.match("[-]+", line_s):
                countries.add(line_s.lower())
    return countries

def get_covid_countries(file="covid_country_list.txt"):
    countries = set()
    with open(file) as f:
        for x in f.readlines():
            countries.add(x.strip())
    return countries


HOME_URL = r"https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic"
PAGES_DIR = r"data"
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

# <a class="mt_a" href="country/turkey/">Turkey</a>


def fetch_pages(directory: str, HOME_URL):
    req = urllib.request.Request(
        HOME_URL,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )

    print(f'Fetching home ({HOME_URL}) page')

    # Obtain Time Line
    with urllib.request.urlopen(req) as f:
        resp = f.read().decode('utf-8')
        with open("wiki_home.html", "w", encoding="utf-8") as o:
            o.write(resp)

        pages_fetched = 0
        # <a href="/wiki/Timeline_of_the_COVID-19_pandemic_in_January_2020" title="Timeline of the COVID-19 pandemic in January 2020">January 2020</a>

        groups = re.findall(
            r'<a href="(.*?)" title="Timeline(.*?)>(.*?)</a>', resp)

        link: str
        
        for g in groups:
            link, j, date = g
            ps = date.split(" ")
            if len(ps) == 2 and ps[0] in months and ps[1] in ['2020', '2021', '2022']:
                newurl = urljoin(HOME_URL, link)
                print(newurl)
                req2 = urllib.request.Request(
                    newurl,
                    data=None,
                    headers={
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
                    }
                )
                try:
                    with urllib.request.urlopen(req2) as c:
                        with open(f"{directory}/Timeline_{date}.html", "w", encoding="utf-8") as f:
                            resp2 = c.read().decode('utf-8')
                            f.write(resp2)
                            pages_fetched += 1
                except Exception:
                    pass

        # Obtain Responsese
        groups = re.findall(
            r'<a href="(.*?)" title="Responses(.*?)>(.*?)</a>', resp)
        for g in groups:
            link, j, date = g
            ps = date.split(" ")
            if len(ps) == 2 and ps[0] in months and ps[1] in ['2020', '2021', '2022']:
                newurl = urljoin(HOME_URL, link)
                print(newurl)
                req2 = urllib.request.Request(
                    newurl,
                    data=None,
                    headers={
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
                    }
                )
                try:
                    with urllib.request.urlopen(req2) as c:
                        with open(f"{directory}/Response_{date}.html", "w", encoding="utf-8") as f:
                            resp2 = c.read().decode('utf-8')
                            f.write(resp2)
                            pages_fetched += 1
                except Exception:
                    pass

        cov_countries = get_covid_countries()
        rstring = r'<a href="(.*?)"\s*title="Timeline.*?>(.*?)</a>'
        alllinks = list(re.findall(rstring, resp, re.DOTALL))
        multilist = [
            "Australia",
            "Canada",
            "Ghana",
            "India",
            "Indonesia",
            "Ireland, Republic of",
            "Malaysia",
            "New Zealand",
            "Nigeria",
            "Philippines",
            "Russia",
            "Singapore",
            "England",
            "United States"   
        ]
        for x in alllinks:
            country = None
            if x[1].split()[0] in cov_countries:
                country = x[1].split()[0]
            elif 'New Zealand' in x[1]:
                country = 'New Zealand'
            elif 'Republic of Ireland' in x[1]:
                country = 'Ireland'
            elif 'United States' in x[1]:
                country = 'United States'
            elif 'South Africa' in x[1]:
                country = 'South Africa'
            elif x[1].split()[0] in ['Ontario', 'Montreal', 'Saskatchewan']:
                country = 'Canada'
            if country:
                if x[1] in multilist:
                    #skip theese
                    pass
                    # print(x, end="\n\n")
                else:
                    link = x[0]
                    newurl = urljoin(HOME_URL, link)

                    if 'Nigeria' in newurl and '2021' in newurl:
                        newurl = newurl[:newurl.find('"')]

                    req2 = urllib.request.Request(
                        newurl,
                        data=None,
                        headers={
                            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
                        }
                    )
                    # os.makedirs(f"{directory}/countries/{country}", exist_ok=True)
                    try:
                        with urllib.request.urlopen(req2) as c:
                            print(newurl)
                            with open(f"{directory}/countries/{country}/{x[1]}.html", "w", encoding="utf-8") as f:
                                resp2 = c.read().decode('utf-8')
                                f.write(resp2)
                                pages_fetched += 1
                    except Exception as e:
                        pass

    print(f"Crawling Completed. Fetched {pages_fetched} pages")


def crawl():
    # Crawl Web pages
    fetch_pages(PAGES_DIR, HOME_URL)


if __name__ == "__main__":
    try:
        import os
        os.mkdir("data")
    except:
        pass
    crawl()
