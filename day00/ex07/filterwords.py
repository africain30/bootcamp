"""
Created on Sat Apr  3 23:56:05 2021

@author: charaf
"""
import string
import sys
def filter_word(S,r):
    n=len(S)
    if(n==0):
        return "ERROR"
    l =[]
    p=""
    for i in range(n):
        if(S[i].isalpha):
            p+=S[i]
        if(i==n-1):
            l.append(p)
            p=''
        if((S[i-1].isalpha()and S[i].isspace()) or S[i] in string.punctuation):
           l.append(p)
           p=''
    print(l)
    n1 = len(l)
    l2 = []
    for i in range(n1):
        if(len(l[i])>r+1):
            l2.append(l[i])
    return l2

if __name__== '__main__':
    if(sys.argv[2]!=int  or sys.argv[1]!=str):
        print('ERROR')
    if(sys.argv[2]==int  and sys.argv[1]==str):
        print(filter_word(sys.argv[1],sys.argv[2]))
    
            