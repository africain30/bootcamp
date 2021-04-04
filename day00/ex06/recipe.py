def add_recipe(name,ingredients,meal,prep_time,cookbook):
    cookbook[name]={'ingredients':ingredients,'meal':meal,'prep_time':prep_time}
    return

def del_recipe(name,cookbook):
    cookbook.pop(name)
    return

def print_recipe(name,cookbook):
    if name not in cookbook:
        print("Please enter a valid name here are the valid ones:")
        keys=list(cookbook.keys())
        for i in range(len(cookbook)):
            print("-",keys[i])
        print("If you want to add a new recipe please enter 1.\n")
        return
    print("For {recipe}:\nIts ingredients are : {ingredients}\nIt is eaten as {meal}\nAnd needs {prep_time} min\n".format(recipe=name,ingredients=cookbook[name]['ingredients'],meal=cookbook[name]['meal'],prep_time=cookbook[name]['prep_time']))
    return

cookbook={
    'sandwich':{
        'ingredients':['ham','bread','cheese','tomatoes'],
        'meal':"lunch",
        'prep_time':"10"} ,
    'cake':{
        'ingredients':['flour', 'sugar','eggs'],
        'meal':"desert",
        'prep_time':"60"} ,
    'salad':{
        'ingredients':['avocado','arugula','tomatoes','spinach'],
        'meal':"lunch",
        'prep_time':"15"}
    }

while True:
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    try:
        num = int(input())
    except ValueError:
        print("\nThis option does not exist, please type the corresponding number.\nTo exit, enter 5.")
    if num==1:
        print("You are now adding a new recipe")
        print("what is the name of the new recipe:\n")
        name = str(input())
        print(name)
        print("what are the ingrediens  of the new recipe:\n")
        ingredients = []
        i=1
        while i!=0 :
            try:
                if str(i).isdigit():
                    ingredients.append(str(input("add one : ")))
                i=int(input("Press any number to continue or 0 to stop! : "))
                if i==0:
                    break
            except ValueError:
                i=""
        print(ingredients)
        meal=str(input("Please specify the type of of this meal: "))
        print(meal)
        while True:
            i=input("Please specify the preparation time: ")
            if str(i).isdigit():
                prep_time=int(i)
                break
        print(prep_time)
        add_recipe(name,ingredients,meal,prep_time,cookbook)
    elif num==2:
        print("Now you are deleting a recipe.")
        name=str(input("Please specify the name of the recipe that you want to delete: "))
        del_recipe(name,cookbook)
        print("You have successfully deleted the {} recipe".format(name))
    elif num==3:
        print("You are now choosing to display a recipe.")
        name=str(input("Please specify the name of the recipe that you want to display: "))
        print_recipe(name,cookbook)
    elif num==4:
        print("You chose to display all the recipes.")
        keys=list(cookbook.keys())
        for i in range(len(cookbook)):
            print_recipe(keys[i],cookbook)
    elif num==5:
        print("Thank you for your visit, GOODBYE !")
        break
    else:
        print("\nThis option does not exist, please type the corresponding number.\nTo exit, enter 5.\n")