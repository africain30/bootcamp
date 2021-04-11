class vector:
    
    def __init__(self,inp):
        if(type(inp)==list):
           for i in range(len(inp)):
               if type(inp[i])!=int:
                   raise ValueError
               if type(inp[i])==int:
                    inp[i]=float(inp[i])
           self.values=inp
        if type(inp)==int:
            if inp<0:
                raise ValueError
            vec=[]
            for i in range(inp):
                vec.append(float(i))
            self.values=vec
        if type(inp)==tuple:
            if len(inp)!=2 or inp[0]>inp[1]:
                raise ValueError
            i =inp[0]
            vec=[]
            for i in range(inp[1]):
                vec.append(float(i))
            self.values=vec
        self.size = len(self.values)
        
        
    def __add__(self,element):
        result = vector(self.size)
        for i in range(self.size):
            result.values[i]=0
        if type(element)==int or type(element)==float:
            for i in range(self.size):
                result.values[i]=self.values[i]+element
            return result
        if type(element)==vector:
            if self.size != vector.size:
                raise ValueError
            for i in range(self.size):
                result.values[i]=self.values[i]+element.values[i]
            return result
        
        
    def __radd__(self,element):
        return vector.__add__(self,element)
    
    
    def __sub__(self,element):
        result = vector(self.size)
        for i in range(self.size):
            result.values[i]=0
        if type(element)==int or type(element)==float:
            for i in range(self.size):
                result.values[i]=self.values[i] - element
            return result
        if type(element)==vector:
            if self.size != vector.size:
                raise ValueError
            for i in range(self.size):
                result.values[i]=self.values[i] - element.values[i]
            return result
    
    def __rsub__(self,element):
        return vector.__rsub__(self, element)
    
    
    def __mul__(self,element):
        
        if type(element)==int or type(element)==float:
            result = vector(self.size)
            for i in range(self.size):
                result.values[i]=0
            for i in range(self.size):
                result.values[i]=self.values[i]*element
            return result
        if type(element)==vector:
            if self.size != vector.size:
                raise ValueError
            result = 0;
            for i in range(self.size):
                result += self.values[i]*element.value[i]
            return result;
    
    
    def __rmul__(self,element):
        return vector.__mul__(self, element)
    
    
    def __truediv__(self,element):
        if(type(element)==vector):
            raise TypeError
        if element == 0:
            raise ValueError
        return vector.__mul__(self,1/element)
    
    
    def __str__(self):
        for i in range(self.size):
            print("| {n} |".format(n=self.values[i]))
        return
    
    def __repr__(self):
        for i in range(self.size):
            print("| {n} |".format(n=self.values[i]))
        return " "
