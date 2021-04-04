import sys

def opperations(x , y):
   #if(x.isnumeric() and  y.isnumeric()):
    x1 = int(x)
    x2 = int(y)
    s = x1+x2;
    d = x1-x2;
    p = x1 * x2;
    if(x2 == 0):
        q = 'ERROR (div by zero)'
        r = 'ERROR (modulo by zero)'
    else:
        q = x1/x2;
        r = x1%x2;
    print("Sum: " , s)
    print("Difference:: " , d)
    print("Product: " , p)
    print("Quotient: " , q)
    print("Remaider: " , r)
    

if __name__== '__main__':
        if(len(sys.argv) == 3 ):
            if sys.argv[1].isdigit() and sys.argv[2].isdigit():
                opperations(sys.argv[1], sys.argv[2])
            else:
                exit("Error")
        if(len(sys.argv) > 3 ):
            print("Input ERROR : Too many arguments ")
            print("Usage: python operations.py <number1> <number2>\n")
            print("Exemple : \n")
            print("    python operations.py 10 3")
        if(len(sys.argv) == 2 ):
            print("Input ERROR : NOt enough  arguments ")
            print("Usage: python operations.py <number1> <number2>\n")
            print("Exemple : \n")
            print("    python operations.py 10 3")
        if(len(sys.argv) == 1):
            print("Usage: python operations.py <number1> <number2>\n")
            print("Exemple : \n")
            print("    python operations.py 10 3")