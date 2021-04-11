import string
import random
    
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
    
    text1 = text_to_list(text , sep=" ")
    
    
    if option == "shuffle":
        resul=[]
        i=0
        for i in range(len(text1)):
            j=random.randint(0, len(text1)-1)
            """if(text1[j] not in resul):
                resul.append(ext1[j])"""
            while text1[j] in resul:
                j=random.randint(0, len(text1)-1)
            resul.append(text1[j])
            affichage = resul[i]
            print(affichage)
    
    
    elif option == "unique":
        resul=[]
        j=0
        for i in range(len(text1)):
            if text[i] not in resul:
                resul.append(text[i])
        for j in range(len(resul)):
            affichage = resul[j]
            print(affichage)
            
            
    elif option == "orderred":
        text1.sort()
        for i in range(len(text1)):
            affichage = text1[i]
            print(affichage)
        
        
    elif option == None or option == " " :
        for i in range(len(text1)):
            affichage = text1[i]
            print(affichage)
        
    else:
        return "ERROR"        
    
