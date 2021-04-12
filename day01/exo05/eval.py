class EVALUATOR:
    
    
    def zip_evaluator(words,coeffs):
        if type(words)!=list or type(coeffs)!=list:
            raise TypeError
            
        if len(words)!=len(coeffs):
            raise -1
        
        words1=list(words)
        for i in words1:
            if type(i)!=str :
                raise TypeError
        coeffs1list(coeffs)       
        for i in coeffs:
            if type(coeffs1[i])!= int and type(coeffs1[i])!=float:
                raise TypeError
                
        value = 0;
        for i in range(len(words1)):
            for j in range(len(words1[i])):
                x+= coeffs1[i]*words1[i][j]
        return value
        
        
        
    def enumerate_evaluate(words,coeffs):
        if type(words)!=list or type(coeffs)!=list:
            raise TypeError
            
        if len(words)!=len(coeffs):
            raise -1
    """la fonction enumarate n'esr pas encore complete"""
