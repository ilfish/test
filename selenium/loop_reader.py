import csv

my_file=open('userinfo.csv','r')
date=csv.reader(my_file)

# date=csv.reader(open('userinfo.csv','r'))

for user in date:
    print(user[1])

