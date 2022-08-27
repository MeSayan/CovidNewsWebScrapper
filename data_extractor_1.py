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

c = 1


# def t_LTABLE_YD(t):
#     r'<table\sid="main_table_countries_yesterday"(.*?)\s<thead>'
#     return t


# def t_RTABLE_YD(t):
#     r'</table>'
#     return t

def t_LROW(t):
    r'<tr[ ]?'
    return t


def t_RROW(t):
    r'</tr>'
    return t


def t_HTML(t):
    r'[~`/"_,+&\-!A-Z%:.\s\t\n ()0-9;a-z$=\'{}>\[\]@*?|\\^#]+'
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

# def p_start(t):
#     ''' start : pytd china
#               | china
#              '''


def p_start(t):
    ''' start : row '''


# def p_simple(t):
#     ''' simple : LTABLE_YD row RTABLE_YD'''
#     t[0] = t[2]

def p_row(t):
    ''' row : LROW phtml RROW '''
    # ''' row : LROW phtml RROW row '''
    global c
    t[0] = t[2]
    if c >= 243 and c <= 479:
        with open(f"scraps/YD_ROW_{c}.html", "w") as f:
            # print(f"ROW_{c}")
            print(t[0], file=f)
    c += 1

# def p_row_terminate(t):
#     # ''' row : LROW phtml RROW '''
#     ''' row : LROW phtml RROW '''
#     global c
#     t[0] = t[2]
#     with open(f"scraps/ROW_{c}.html", "w") as f:
#         print(f"ROW_{c}")
#         print(t[0], file=f)
#         c += 1

# def p_YT(t):
#     ''' pytd : LTABLE_YD phtml RTABLE_YD'''
#     t[0] = t[2]
#     print("Table")
#     with open("scraps/yesterday_data_continent_wise.html" + str(random.randint(1,100)), "w") as f:
#         print(t[0], file=f)

# def p_CHINA(t):
#     ''' china : LTABLE_CHINA phtml RTABLE_CHINA'''
#     t[0] = t[2]
#     print('China')
#     with open("scraps/yesterday_data_china.html" + str(random.randint(1,100)), "w") as f:
#         print(t[0] , file=f)


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
    # 'LTABLE_YD',
    # 'RTABLE_YD',
    'LROW',
    'RROW'
]


lexer = ply.lex.lex()

parser = yacc.yacc()

def get_table_data(HOME_PAGE_FILE="home.html"):
    with open(HOME_PAGE_FILE, 'r', errors='ignore') as f:
        text = f.read()
        lexer.input(str(text))
        parser.parse(text)

