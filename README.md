## Requirements

* [PLY](https://www.dabeaz.com/ply/). Make sure ply folder is present in the source code file. Project Structure
* [WordCloud](https://pypi.org/project/wordcloud/)
* [NLTK](https://pypi.org/project/nltk/)

```
ProjectFolder
    ply/*
    crawler.ply
    wiki_crawler.ply
    data_extractor_1.py
    data_extractor_2.py
    data_extractor_3.py
    data_extractor_timeline.py
    data_extractor_responses.py
    data_extractor_country.py
    data_loader.py
    model.py
    main.py
```

For ease of use and evaluation the project is zipped as shown above.

## Description of source files.

1. crawler.py : Parses country list file and crawls https://www.worldometers.info/coronavirus/ (saved to home.html)
and respective countries (saved to countries/<CountryName>.html)
2. wik_crawler.py : Parses covid country list file and crawls https://en.wikipedia.org/wiki/Timeline_of_the_COVID-19_pandemic (saved to wiki_home.html) and respective country pagesare saved to data/countries folder
2. data_extractor_1.py & data_extractor_3.py : Extracts information for Task 2 (Point 1) a to j)
3. data_extractor_2.py : Extracts information for Task 2 (Point 3)
3. data_extractor_3.py : Extracts Worldwide Timeseries information
4. data_loader.py : Loads the extracted data into database
5. data_extractor_timeline.py : Extracts Wikipedia Covid News
6. data_extractor_responses.py : Extracts Wikipedia Covid Responses
7. data_extractor_country.py :  Extracts Wikipedia Covid Country News
7. model.py : Contain class definitions for Database, TimeSeries etc
8. main.py : Contains menu, index creation, and synchronization


## Running the program

### Installation
Install Wordcloud & NLTK
```
pip install wordcloud NLTK
```

Just run main.py
```
<python3_executable> main.py
```

## Entering commands

There are three menus. **Yesterday Data Menu**, **Time Range Menu** and **Wikipedia Menu**. Users can toggle between the menus by entering **menu <menu_id>** command. At any menu **help** command can be used to view options available as well as an example. For proper clean up of files, user must type **exit** to exit the program. Example of one command shown below

* Worldometers Yesterday Day -> Menu 1
* Worldometers TimeSeries Data -> Menu 2
* Worldometers Wikipedia Menu -> Menu 3


```
Time Range Menu |  Enter menu <menu id> to go menu | Enter help for usage
>> menu 1

Yesterday Data Menu |  Enter menu <menu id> to go menu | Enter help for usage
```

Commands parameters must be separated by '|'.
Special keywords are used to mention the query used. 
The following short form has been adopted for the queries

### Commands for Region Wise (Yesterday Data Menu)
1. tc : Total Cases
2. ac : Active Cases
3. td : Total Deaths
4. tr : Total Recovered
5. tt : Total Tests
6. dpm : Deaths per 1 milion of population
7. tpm : Tests per 1 million of population
8. nc : New Cases
9. nd : New Deaths
10. nr : New Recoveries

#### Command format

```
<regn_name> | <command>
```

### Command for Time Series 

1. dc : Daily New Cases
2. ac : Active Cases
3. dd : Daily Deaths
4. dr : Daily Recoveries

#### Command format

```
<date1> | <date2> | regn | <command>
```


### Command for Wikipedia Series 

1. Q1 : Part 1
2. Q2 : Part 2
3. Q3 : Part 3
4. Q4 : Part 4
5. Q5 : Part 5
6. Q6 : Part 6

#### Command format

To view the command format, type help in the Wikipedia Menu. Note dates **must**
be entered in **DD-MM-YYYY** format only in this menu

#### Date Format (Yesterday Data & Time Series Menu)

All dates must be entered in this format only. All other formats are ignored. First letter of Date must be in capital only. This is the format followed in WorldOMeters website too

```
<First three letters of Month Name> <date in double digits>, <year in 4 digits>

Examples:
Jul 02, 2021 
Mar 01, 2020
Feb 15, 2020
...
```

#### Date Format (Wikipedia Menu)
Date format in this menu is DD-MM-YYYY only. Example 15-03-2020.


Tip for remembering this, Example ,dd (first character taken from first world, 2nd character taken from second word). If forgot the help command can be used in any menu. 

### Special Merit
Data is preprocessed to build and index on Dates for faster serving time range based queries (Task 2 Point 3). 
Index:

```
Date1 -> [(region, param1, param2, param3...),  (region, param1, param2, param3...) .... ]
Date2 -> [(region, param1, param2, param3...),  (region, param1, param2, param3...) .... ]
...
```

