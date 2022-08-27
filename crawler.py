"""
Name : CL2 Assignment 5
Author : Sayan Mahapatra
Date : 13-03-2022
Description : In this file implementation of  WorldoMeters Crawler is given
"""

import urllib.request
from urllib.parse import urljoin
import re


def get_countries(file="worldometers_countrylist.txt"):
    countries = set()
    with open(file, "r") as f:
        exclude = ["Europe:", "Asia", "North America:",
                   "South America", "Africa", "Oceania", ""]
        for line in f:
            line_s = line.strip()
            if not line_s in exclude and not re.match("[-]+", line_s):
                countries.add(line_s.lower())
    return countries


HOME_URL = r"https://www.worldometers.info/coronavirus/"
PAGES_DIR = r"countries"

# <a class="mt_a" href="country/turkey/">Turkey</a>


def fetch_pages(directory: str, countries):
    req = urllib.request.Request(
        HOME_URL,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )

    print(f'Fetching home ({HOME_URL}) page')
    with urllib.request.urlopen(req) as f:
        pages_fetched = 0
        resp = f.read().decode('utf-8')
        with open("home.html", "w", encoding="utf-8") as o:
            o.write(resp)
        groups = re.findall(
            r'<a class="mt_a" href="(country/[a-z]*[-]?[a-z]*[-]?[a-z]*/)">(.*)</a>', resp)

        countries_c = countries
        for link, country in groups:
            if country.lower() in countries_c:
                newurl = urljoin(HOME_URL, link)
                req2 = urllib.request.Request(
                    newurl,
                    data=None,
                    headers={
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
                    }
                )
                countries_c.remove(country.lower())
                
                try:
                    with urllib.request.urlopen(req2) as c:
                        print(f"Fetching page for {country} ({newurl})")
                        with open(f"{directory}/{country.lower()}.html", "w") as f:
                            f.write(c.read().decode('utf-8'))
                            pages_fetched += 1
                except Exception as e:
                    pass
        print(f"Crawling Completed. Fetched {pages_fetched} pages")


def crawl():
    global countries
    countries = get_countries()
    # Crawl Web pages
    fetch_pages(PAGES_DIR, countries)


if __name__ == "__main__":
    crawl()
