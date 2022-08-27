"""
Name : CL2 Assignment 5
Author : Sayan Mahapatra
Date : 13-03-2022
Description : In this file implementation of Data Extractor 2 is given
"""

import random
import re
import os

import ply.yacc as yacc
import ply.lex
import ply.yacc

from model import *


from crawler import get_countries

current_country = None


def t_LDIVAC(t):
    r'<div\sid="graph-active-cases-total"></div>'
    return t


def t_LDIVDD(t):
    r'<div\sid="graph-deaths-daily"></div>'
    return t


def t_LDIVDC(t):
    r'<div\sid="graph-cases-daily"></div>'
    return t


def t_LDIVDR(t):
    r'<div\sid="cases-cured-daily"></div>'
    return t


def t_RSCRIPT(t):
    r'</script>'
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


def p_start(t):
    ''' start : chart_ac 
              | chart_dd
              | chart_dc
              | chart_dr
    '''


def p_chart_ac(t):
    ''' chart_ac : LDIVAC phtml RSCRIPT '''
    # ''' row : LROW phtml RROW row '''
    t[0] = t[2]
    global current_country
    # print('Active cases')
    with open(f"scraps/ts/{current_country}_ac.chart", "w") as f:
        print('Active Cases', t[0], file=f)


def p_chart_dd(t):
    ''' chart_dd : LDIVDD phtml RSCRIPT '''
    # ''' row : LROW phtml RROW row '''
    t[0] = t[2]
    global current_country
    # print('Deaths')
    with open(f"scraps/ts/{current_country}_dd.chart", "w") as f:
        print('Deaths', t[0], file=f)


def p_chart_dc(t):
    ''' chart_dc : LDIVDC phtml RSCRIPT '''
    # ''' row : LROW phtml RROW row '''
    t[0] = t[2]
    global current_country
    # print('Daily Cases')
    with open(f"scraps/ts/{current_country}_dc.chart", "w") as f:
        print('Daily Cases', t[0], file=f)


def p_chart_dr(t):
    ''' chart_dr : LDIVDR phtml RSCRIPT '''
    # ''' row : LROW phtml RROW row '''
    t[0] = t[2]
    global current_country
    # print('Recoveries')
    with open(f"scraps/ts/{current_country}_dr.chart", "w") as f:
        print('Recoveries', t[0], file=f)


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
    'LDIVAC',
    'RSCRIPT',
    'LDIVDD',
    'LDIVDC',
    'LDIVDR'
]

def get_ts_data():
    countries = get_countries()
    global current_country
    for c in countries:
        current_country = c.lower()
        fname = f"countries/{current_country}.html"
        with open(fname, "r") as f:
            print(f"Parsing file {fname}")
            lexer = ply.lex.lex()
            parser = yacc.yacc()
            text = f.read()

            lexer.input(str(text))
            parser.parse(text)
