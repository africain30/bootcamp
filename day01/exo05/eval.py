class EVALUATOR:
    def zip_evaluator(words,coeffs):
        if type(words)!=list or type(coeffs)!=list:
            raise TypeError
        if len(words)!=len(coeffs):
            raise ValueError
        for i in words:
            if type(i)!=str :
                raise TypeError
        coeffs=tuple(coeffs)
        for i in coeffs:
            if type(coeffs[i])!= int and type(coeffs[i])!=float:
                raise TypeError
                
        
        
    def enumerate_evaluate(words,coeffs):
