import sys

class Recipe :
    def __init__(self,name ,lvl ,time ,ingrs ,descr ,types):
        
        if type(name)!=str and name != '':
            sys.exit("ValueError!")
            return 'ERROR'
        self.name = name
        
        if(not str(lvl).isdigit()) and (lvl<1 or lvl>5):
            sys.exit("ValueError!")
            return 'ERROR'
        self.cooking_lvl = lvl
        
        if(not str(lvl).isdigit() and (time<0)):
            sys.exit("ValueError!")
            return "ERROR"
        self.cooking_time =time
        
        for i in ingrs:
            if type(i)!=str:
                sys.exit("ValueError!")
        if type(ingrs) !=list :
            sys.exit("ValueError!")
        self.ingredients =ingrs
        
        if(type(descr)!=str):
            sys.exit("ValueError!")
        self.description = descr
        
        if(types.lower!="starter" and types.lower!="lunch" and types.lower!="desert" ):
            sys.exit("ValueError!")
        self.recipe_type = types
    def __str__(self):
        text = "The {n} recipe is of level {l}, needs {t} min, uses the following ingredients {i},{d}it is taken as {r}".format(n=self.name ,l=self.cooking_lvl ,t= self.cooking_time ,i=self.ingredients ,d=self.description ,r=self.recipe_type)            
        return text
