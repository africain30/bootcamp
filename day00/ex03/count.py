import string

def text_analyzer(*x):
    """This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""
    n = len(x)
    if(n>1):
        return 'ERROR'
    if(len(x[0])==0):
        return 'What is the text to analyse?'
    i = 0;
    upper = 0;
    lower = 0;
    ponct = 0;
    space = 0;
    for i in x[0]:
        if(i.isupper()):
            upper+=1
        if(i.islower()):
            lower+=1
        if(i.isspace()):
            space+=1
        if(i in string.punctuation):
            ponct +=1
    s= space + upper + lower + ponct 
    print("The text contains " ,s, "characters:" )
    print(" - " , upper , " upper letters\n")
    print(" - " , lower , " lower letters\n")
    print(" -  ", ponct , " punctuation marks \n")
    print(" - " , space , " spaces \n")