def reverse(s):
    
    p = ""
    n = len(s);
    i = 0
    while i<n:
        if s[i].isalpha():
            if s[i].islower():
                p += s[i].upper()
            if s[i].isupper():
                p += s[i].lower()
        if s[i].isspace():
            p += ' '
        i+=1
    return p[::-1]