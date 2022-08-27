"""
Name : CL2 Assignment 5
Author : Sayan Mahapatra
Date : 13-03-2022
Description : In this file implementation of Data Extractor 3 is given
"""

import random
import re
import os

import ply.yacc as yacc
import ply.lex
import ply.yacc


def t_LSCRIPT(t):
    r'<script[ ]?'
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
    ''' start : chart 
    '''


def p_chart(t):
    ''' chart : LSCRIPT phtml RSCRIPT '''
    t[0] = t[2]
    if "Highcharts.chart('coronavirus-deaths-daily', {" in t[0]:
        with open(f"scraps/ts/world_dd.chart", "w") as f:
            print('Daily Deaths', t[0][t[0].find("Highcharts.chart('coronavirus-deaths-daily"):], file=f)
    elif "Highcharts.chart('coronavirus-cases-daily', {" in t[0]:
        with open(f"scraps/ts/world_dc.chart", "w") as f:
            print('Daily Deaths', t[0][t[0].find("Highcharts.chart('coronavirus-cases-daily"):], file=f)

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
    'LSCRIPT',
    'RSCRIPT'
]

def get_ts_data_world():
    fname = "home.html"
    with open(fname, "r") as f:
        print(f"Parsing file {fname}")
        lexer = ply.lex.lex()
        parser = yacc.yacc()
        text = f.read()

        lexer.input(str(text))
        parser.parse(text)
