import sys


def check(x):
    if(str(x).isnumeric()):
        if(int(x)==0):
            return 'I\'M Zero'
        if(int(x)%2 == 0 ):
            return 'I\'M EVEN'
        if(int(x)%2 == 1):
            return 'I\'M ODD'
    else:
        return 'ERROR'
    
if __name__== '__main__':
    if(len(sys.argv)>2):
        print('ERROR')
    if(len(sys.argv) ==1 ):
        print(' ')
    if(len(sys.argv) ==2 ):
        x=sys.argv[1]
        print(check(x))
        
        
    