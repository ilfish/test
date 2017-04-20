# -*- coding:utf-8 -*-

while True:
    try:
        x=input('Enter the first number: ')
        y=input('Enter the second number: ')
        v=x/y
        print "x/y is %s" %v
    except:
        print "Invalid input. Please try again."
    else:
        break
