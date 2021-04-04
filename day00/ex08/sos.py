#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 17:12:46 2021

@author: charaf
"""
import sys
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----'}
def str_to_morse(s):
    if(s.isalnum()):
        if(s.upper() in MORSE_CODE_DICT.keys()):
            return MORSE_CODE_DICT[s.upper()]

def text_to_morse(text):
    n=len(text)
    p=""
    for i in range(n):
         if(text[i].upper() in MORSE_CODE_DICT.keys()):
             p+= str_to_morse(text[i])
         if(text[i].isspace()):
             p+= '/'
    return p

if __name__== '__main__':
    if(len(sys.argv)>2):
        print('ERROR : too many arguments')
    if(len(sys.argv)<2):
        print('ERROR : not enough  arguments')
    if(len(sys.argv)==2):
        print(text_to_morse(sys.argv[1])) 