"""
Name : CL2 Assignment 5
Author : Sayan Mahapatra
Date : 13-03-2022
Description : This file contains implementation of all the queries
"""

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import os
import re

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')
stopwords_n = stopwords.words('english') #use nltk stopwords

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


import datetime

def check_overlap(d1, d2, d3, d4):
    x = max(d1, d3)
    y = min(d2, d4)
    days = (x - y).days
    return days > 0

def dates_between(startdate, enddate, format="%d-%m-%Y"):
    dl = []
    cd = startdate
    while cd <= enddate:
        dl.append(cd)
        cd += datetime.timedelta(days=1)
    
    d =  [ d.strftime(format) for d in dl]
    return d

def mb(startdate, enddate):
    dates = dates_between(startdate, enddate, format="%d-%B-%Y")
    dates = [x[x.find("-")+1:] for x in dates]
    clean_dates = []
    i, j = 0, 1
    while i < len(dates):
        while j < len(dates) and dates[j] == dates[i]:
            j += 1
        clean_dates.append(dates[i])        
        i = j
    return clean_dates

def get_covid_vocab(file="covid_word_dictionary.txt"):
    cov_vocab = set()
    with open(file) as f:
        for x in f:
            cov_vocab.add(x.strip())
    return cov_vocab


def part1_query(startdate, enddate, series="timeline"):
    res = []
    ls = ''
    rs = ''
    global stopwords_n
    try:
        sd = datetime.datetime.strptime(startdate, "%d-%m-%Y")
        ed = datetime.datetime.strptime(enddate, "%d-%m-%Y")
        dates = dates_between(sd, ed)
        for d in dates:
          try:
              with open(f"temp/{series}/{d}.txt") as f:
                  content = f.read()
                #   print(content)
                  res.append(content)
          except:
              # Skip this date
              pass 
        for c in res:
            ls += c.lower()
        rs = "".join(res)
        wordcloud = WordCloud(width = 800, height = 800,
				background_color ='white',
				stopwords = stopwords_n,
				min_font_size = 10).generate(ls)
        
        plt.figure(figsize = (8,8), facecolor = None)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad=0)
        plt.show()
        return rs
    except:
        print("Invalid Date")
        return None

# part1_fetch_data()
# part1_query("02-01-2021","03-01-2021", series="responses")
# part1_query("02-01-2021","05-01-2021", series="timeline")

def part2_query(sd1, ed1, sd2, ed2, series):
    words1_f = dict() 
    words2_f = dict()
    words3_f = dict()
    words4_f = dict()
    ls1 =  ''
    ls2 =  ''
    s1, s2 = '', ''
    cov_vocab = get_covid_vocab()
    global stopwords_n
    try:
        try:
            sd1c = datetime.datetime.strptime(sd1, "%d-%m-%Y")
            ed1c = datetime.datetime.strptime(ed1, "%d-%m-%Y")
            sd2c = datetime.datetime.strptime(sd2, "%d-%m-%Y")
            ed2c = datetime.datetime.strptime(ed2, "%d-%m-%Y")
        except ValueError:
            print('Invalid Date')
            return

        if check_overlap(sd1c, ed1c, sd2c, ed2c) == False:
            print("Overlapping Dates")
            return

        dates1 = dates_between(sd1c, ed1c)
        dates2 = dates_between(sd2c, ed2c)
        for d in dates1:
          try:
              with open(f"temp/{series}/{d}.txt") as f:
                  content = f.read()
                  s1 += content
                  for word in content.split():
                      if word not in stopwords_n:
                        if word in words1_f:
                            words1_f[word] += 1
                        else:
                            words1_f[word] = 0
                      if word in cov_vocab:
                        if word in words3_f:
                            words3_f[word] += 1
                        else:
                            words3_f[word] = 0
          except:
              # Skip this date
              pass 
        for d in dates2:
          try:
              with open(f"temp/{series}/{d}.txt") as f:
                  content = f.read()
                  s2 += content
                  for word in content.split():
                      if word not in stopwords_n:
                        if word in words2_f:
                            words2_f[word] += 1
                        else:
                            words2_f[word] = 0
                        if word in words4_f:
                            words4_f[word] += 1
                        else:
                            words4_f[word] = 0
          except:
              # Skip this date
              pass 
        
        words1 = set(words1_f.keys())
        words2 = set(words2_f.keys())
        words3 = set(words3_f.keys())
        words4 = set(words4_f.keys())
        common_words = words1 & words2
        ls1 = ' '.join(common_words)
        wordcloud1 = WordCloud(width = 800, height = 800,
				background_color ='white',
				stopwords = stopwords_n,
				min_font_size = 10).generate(ls1)

        covid_words = words3 & words4
        ls2 = ''.join(covid_words)
        worldcloud2 = WordCloud(width = 800, height = 800,
				background_color ='white',
				stopwords = stopwords_n,
				min_font_size = 10).generate(ls2)
        
        # plt.figure(figsize = (8,8), facecolor = None)
        percentage = len(covid_words) * 100 / len(common_words)

        s3 = s1 + s2
        tokens = word_tokenize(s3.lower())
        tokens = [t for t in tokens if t not in stopwords_n and t.isalpha()]
        tokens_covid = [t for t in tokens if t in cov_vocab and t.isalpha()]
        from collections import Counter
        c = Counter(tokens)
        c2 = Counter(tokens_covid)
        top20_common = c.most_common(20)
        top20_covid = c2.most_common(20)
        

        # Do something

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16,16), facecolor=None)
        fig.suptitle(f'Word Clouds for {sd1}-{ed1} and {sd2}-{ed2}')
        ax1.set_title('Common Words Wordcloud')
        ax1.imshow(wordcloud1)
        ax2.set_title('Covid Words Wordcloud')
        ax2.imshow(worldcloud2)
        
        plt.axis("off")
        plt.tight_layout(pad=0)
        plt.show()

        print(f"Percentage of covid related words on common words: {percentage}%")

        print(f"Top 20 common words are:")
        for w in top20_common:
            print(w[0], end=" ")
        print()

        print(f"Top 20 covid words are:")
        for w in top20_covid:
            print(w[0], end=" ")
        print()

    except Exception as e:
        print(e)
        return None


# part2_query("02-01-2021","31-03-2021", "20-11-2021","20-2-2022", "timeline")

def part3_query(country):
    global stopwords_n
    files = os.listdir(f"temp/countries/{country.title()}")
    d : list = []
    for f in files:
        if f.count("-") > 0:
            x = f[:f.find(".txt")]
            M, y = x.split("-")
            if M in month_to_index and y.isnumeric():
                idx = int(y) * 13 + month_to_index[M]
                d.append((idx, M, y))
    d.sort(key=lambda tup: tup[0])
    return (d[0][1], d[0][2], d[-1][1], d[-1][2])

def part4_query(country, startdate, enddate, plot=False):
    global stopwords_n
    try:
        startdate = datetime.datetime.strptime(startdate, "%d-%m-%Y")
        enddate = datetime.datetime.strptime(enddate, "%d-%m-%Y")
    except:
        print('Invalid Date')
        return 
    ms = mb(startdate, enddate)
    files = os.listdir(f"temp/countries/{country.title()}")
    content = ''
    for m in ms:
        if m + '.txt' in files:
            with open(f"temp/countries/{country}/{m}.txt") as f:
                content += f.read()
    content = re.sub('&#[0-9]{2,3};', '', content)
    
    if plot and content:
        # Word cloud plot
        wordcloud = WordCloud(width = 800, height = 800,
				background_color ='white',
				stopwords = stopwords_n,
				min_font_size = 10).generate(content)
        plt.figure(figsize = (8,8), facecolor = None)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad=0)
        plt.show()
    return content

def jaccard(s1, s2): 
    global stopwords_n
    words1 = set()
    words2 = set()
    
    # Tokenize + Stop word remove
    for w in s1.lower().split():
        if not w in stopwords_n:
            words1.add(w)
    
    for w in s2.lower().split():
        if not w in stopwords_n:
            words2.add(w)
    
    i = words1  & words2
    u = words1 | words2
        
    try:
        j = (1.0 * len(i)) / len(u)
    except Exception as e:
        j = 0
    finally:
        return j



def part5_query(country, startdate, enddate, countries, top=3):
    A = part4_query(country, startdate, enddate)
    if not A:
        return
    B = []
    for c in countries:
        if c != country:
            other = part4_query(c, startdate, enddate, plot=False)
            B.append((jaccard(A, other), c))
    return sorted(B, key = lambda x: x[0], reverse=True)[:top]

def part6_query(country, startdate, enddate, countries, top=3):
    A = part4_query(country, startdate, enddate)
    cov_vocab = get_covid_vocab()
    A = " ".join([x for x in A.split(" ") if x in cov_vocab])
    if not A:
        return
    B = []
    for c in countries:
        if c != country:
            other = part4_query(c, startdate, enddate, plot=False)
            other = " ".join([x for x in other.split(" ") if x in cov_vocab])
            B.append((jaccard(A, other), c))
    return sorted(B, key = lambda x: x[0], reverse=True)[:top]


# print(part3_query("Australia"))
# print(part3_query("United States"))
# print(part3_query("Bangladesh"))
# print(part3_query("Spain"))

# print(part4_query('Australia', "02-10-2021", "05-01-2022", plot=True))


# import wiki_crawler
# cov_countries = wiki_crawler.get_covid_countries()
# print(part5_query('Australia', "02-10-2021", "05-01-2022", cov_countries))
# print(part5_query('Australia', "02-10-2021", "05-01-2022", cov_countries))
