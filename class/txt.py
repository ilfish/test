# -*- coding:utf-8 -*-

f = open('E:\\test\\txt.txt','w')#注意转义
print f.write("hello,world! by write,中国")
print f.close()


with open('E:\\test\\txt.txt','r') as x:
    print x.read()
