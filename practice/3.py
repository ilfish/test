# -*- coding:utf-8 -*-
from math import sqrt
for i in range(10000):
    x=int(sqrt(i+100))
    y=int(sqrt(i+268))
    if(x*x==i+100)and(y*y==i+268):
         print (i)

# import math
# for i in range(0,10000):
#     x=int(math.sqrt(x+100))
#     y=int(math.sqrt(y+268))
#     if (x*x==i+100)and(y*y==i+268):
#         print i
