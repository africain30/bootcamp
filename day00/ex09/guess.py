#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 18:48:02 2021

@author: charaf
"""
import random
n=random.randint(1,99)
print(n)
print("can you gess the right number ?")
print("the number you arelooking for is between 1 and 99")
print("enter exit if you want to quit the game!")
p=0
while True:
    p+=1
    try:
        s=input("Please enter a number : " )
        if s=="exit":
            print("goodbye loser !")
            break
        s=int(s)
    except TypeError:
        print("that is not a number ! try againe .")
    except ValueError:
        print("that is not a number ! try againe .")
    if str(s).isdigit():
        if(int(s)<1 or int(s)>99):
            print("ERROR : you should enter a number between 1 and 99 , please try againe!")
            s=input("Please enter a new number : " )
        if(int(s)<n):
            print("try a higher number :")
            s=input("Please enter a new number : " )
        if(int(s)>n):
            print("try a lower number :")
            s=input("Please enter a new number : " )
        if(int(s)==n):
            print("Congratulations , you could guess the right number in " , p , "tries .")
            break