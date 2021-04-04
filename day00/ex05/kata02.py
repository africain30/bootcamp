def kata02():
    time =(3,30,2019,9,25)
    t=len(time)
    print("{day}/{month}/{year}  {hour}:{minutes}".format(day =time[t-1],month=time[t-2],year=time[t-3],hour=time[0],minutes=time[1]))             
                                                        
kata02()