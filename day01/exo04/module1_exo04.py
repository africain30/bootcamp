import string
#import sys
    
def text_to_list(S,sep=" "):
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
    return l

def generator(text,sep=" ",option=None):
    if type(text)!=str:
        return "Error"
    
    



