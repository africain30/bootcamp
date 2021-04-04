def kata01():
    languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }
    print("Python was created by {python} ".format(python = languages['Python']) ,end ="\n")
    print("Ruby was created by {ruby} ".format(ruby = languages['Ruby'] ,end = "\n"))
    print("Ruby was created by {php} ".format(php = languages['PHP'] ,end = "\n"))     
    
kata01()