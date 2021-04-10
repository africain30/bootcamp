import datetime
from recipe import Recipe
class Book:
       def __init__(self,name ,last_update ,creation_date ,recipes_list):
           if type(name)!=str or name=="":
               raise ValueError
           self.name = name
           
           self.last_update=last_update
           self.creation_date=creation_date
           if type(recipes_list)!=dict or "starter" not in recipe_list or "lunch"not in recipe_list or "dessert" not in recipe_list:
               raise ValueError
           self.recipe_list
    
      def get_recipe_by_name(self, name):
          starter=list(self.recipe_list["starter"])
          lunch=list(self.recipe_list["lunch"])
          dessert=list(self.recipe_list["dessert"])
          if matching(starter,lunch) or matching(lunch,dessert) or matching(dessert,starter):
            return "There are matching names in your recipe type list"
          if name in starter:
              return self.recipe_list["starter"][name]
          elif name in lunch:
              return self.recipe_list["lunch"][name]
          elif name in starter:
              return self.recipe_list["desert"][name] 
          else:
              return "their is no recipe with this name!"
          

    def get_recipes_by_types(self, recipe_type):
         if recipe_type=="starter"
             return self.recipe_list["starter"]
         elif recipe_type=="lunch"
             return self.recipe_list["lunch"]
         elif recipe_type=="desert"
             return self.recipe_list["desert"]
         else:
             raise "their is no recipe with this type"
             
             
    def add_recipe(self, recipe):
        if type(recipe)!= Recipe :
            return " Before adding a recipe , please create one "
        self.recipe_list[recipe.recipe_type][recipe.recipe_name]=recipe
        self.last_update = datetime.datetime.now()
              
              
              
              
def matching(d1,d2):
    for i in d1:
        if i in d2:
            return True              
