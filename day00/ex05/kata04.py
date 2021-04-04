def kata04():
    t=( 0, 4, 132.42222, 10000, 12345.67)
    m = str(t[0]).zfill(2)
    e = str(t[1]).zfill(2)
    n1= round(t[2],2)
    n2= format(t[3] , ".2e")
    n3= format(t[3] , ".2e")
    print("module_{m}, ex_{e} : {n1}, {n2}, {n3}".format(m=m,e=e,n1=n1,n2=n2,n3=n3,end =" "))
kata04()