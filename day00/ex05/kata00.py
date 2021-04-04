def kata00():
    t = (19,42,21)
    print("the {lenght} numbers are : ".format(lenght=len(t)),end="")
    for i in range(len(t)-1):
        print(t[i] , end=", ")
    print(t[len(t)-1])
     
kata00()