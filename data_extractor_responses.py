"""
Name : CL2 Assignment 5
Author : Sayan Mahapatra
Date : 13-03-2022
Description : In this file implementation of data extractor for responses (Wikipedia) is given
"""

import ply.yacc as yacc
import ply.lex
import ply.yacc
import random
import re
import os
import traceback

current_file = ""
dates = []

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

def t_LSPAN(t):
    r'span[ ]class="mw-headline"'
    return t

def t_H(t):
    r'<h[32]>'
    return t

def t_HTML(t):
    # r'[~`/"_,+&\-!A-Z%:.\s\t\n ()0-9;a-z$=\'{}>\[\]@*?|\\^#]+'
    r'[^\<]+'
    return t

def t_BRACKET(t):
    r'<'
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    #  return t

t_ignore = " \t"

def t_error(t):
    t.lexer.skip(1)

def p_start(t):
    ''' start : list '''

def p_list(t):
    ''' list : LSPAN phtml H'''
    # print(t[2], end= "\n\n")
    global current_file
    global dates
    try:
        o : str = t[2]
        i  = o.find('"')
        j  = o.find('"', i+1)
        if i > 0 and j > 0:
            ds = o[i+1:j]
            if ds.count("_") == 1:
                d, M = ds.split("_")
            elif ds.count("_") == 2:
                d, M, _ = ds.split("_")
            else:
                return
            m = month_to_index[M]
            # current_file = "data/Response_June 2020.html"
            y = int(current_file[-9:-5])
            d = int(d)
            op = f"temp/responses/{d:02}-{m:02}-{y:02}.txt"
            try :
                fh = open(op, "a")
            except FileNotFoundError:
                fh = open(op, "w")
            
            # cleanup
            p = [x for x in re.findall(r'<p>(.*?)</p>', o,re.DOTALL)]
            if not p:
                p = [x for x in re.findall(r'<li>(.*?)</li>', o,re.DOTALL)]
                if not p:
                    return
            l = [re.sub(r'&#[0-9]{2,3};(.*?)&#[0-9]{2,3};', '', x, re.DOTALL) for x in p]
            l2 = [re.sub(r'<.*?>', '', y) for y in l]
            for line in l2:
                if line.endswith('\n'):
                    print(line, file=fh, end='')
                else:
                    print(line, file=fh)
            dates.append(op)
            fh.close()
    except ValueError as e:
        # print(e, current_file)
        pass
    except KeyError:
        pass
    except Exception as e:
        traceback.print_exc()
            
def p_HTML(t):
    ''' phtml : HTML'''
    t[0] = t[1]


def p_HTML_multi(t):
    ''' phtml : HTML phtml'''
    t[0] = t[1] + t[2]

def p_HTML_2(t):
    ''' phtml : BRACKET phtml '''
    t[0] = t[1] + t[2]

def p_error(t):
    pass

tokens = [
    'HTML',
    'BRACKET',
    'LSPAN',
    'H'
]


lexer = ply.lex.lex()
parser = yacc.yacc()

import os
def run_extractor():
    global current_file
    # try:
    #     os.makedirs("temp/responses", exist_ok=True)
    # except Exception as e:
    #     print(e)

    for f in os.scandir("data"):
        if f.path.find("Response") != -1: 
            current_file = f.path
            with open(f, "r") as file:
                print(f"Parsing {f.path}")
                text = file.read()
                lexer.input(str(text))
                parser.parse(text)
                # for date in sorted(dates):
                #     print(date)
                dates.clear()
