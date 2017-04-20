# -*- coding:utf-8 -*-

while True:
    try:
        x=input('输入一个数： ')
        y=input("输入另一个数： ")
        v=float(x/y)
        print "x/y is %d" %v

# except (ZeroDivisionError,NameError,TypeError):
#     print "输入错误"

    #except (ZeroDivisionError,NameError,TypeError)as e:
    except Exception,e:
        print (e)
        print ("please try again")
    else:
        break
    finally:
        print ("shutdow")
