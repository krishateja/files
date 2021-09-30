import csv
f1=open("teja.csv","w")
objw=csv.writer(f1)
objw.writerow(["sna","name","age","location"])
objw.writerow([1,"teja",23,"kamareddy"])
objw.writerow([2,"vinod",27,"sirsilla"])
objw.writerow([3,"raju",25,"jagithyal"])
objw.writerow([4,"srinivas",28,"mahabubnagar"])
objw.writerow([5,"chandu",23,"rangareddy"])
f1.close()
import csv
f=open("teja.csv","r")
objr = csv.reader(f)
for i in objr:
    print(i)
f.close()
import csv
f=open("teja.csv","w",newline="")
objw=csv.writer(f)
objw.writerow(["sid","sname","sage"])
a=111
b="teja"
c=23
objw.writerow([a,b,c])
f.close()
import csv
f=open("teja.csv","w",newline="")
objw=csv.writer(f)
objw.writerow(["sid","sname","sage"])
objw.writerow([111,"teja",23])
f.close()
import csv
f=open("teja.csv","w",newline="")
objw=csv.writer(f)
objw.writerow(["sid","sname","sage"])
a=int(input("enter student id:"))
b=input("enter student name:")
c=int(input("enter student age:"))
objw.writerow([a,b,c])
f.close()
import csv
f=open("teja.csv","w",newline="")
objw=csv.writer(f)
objw.writerow(["eid","ename","esal"])
while True:
    empid=int(input("enter employrr id:"))
    emppname=input("enter employee name:")
    empsal=int(input("entr employee salary:"))
    objw.writerow([empid,emppname,empsal])
    ch=input("if u wanna continue the programme say yes/no:")
    if ch.lower()!="yes":
        print("every line stored  succesfully")
        break
f.close()
import csv
f=open("teja.csv","r")
objr=csv.reader(f)
list=[]
for i in objr:
    list.append(i)
print(list)
f.close()
import csv
f=open("teja.csv","r")
objr=csv.reader(f)
list=list(objr)
print(list)
f.close()
print(list)
list1=[]
for i in list:
    if i[0]=="eid":
        i.append("hesal")
        list1.append(i)

    else:
       hsal= (int(i[2])*0.1)+int(i[2])
       i.append(hsal)
       list1.append(i)

print(list1)
print("********************")
for i in list1:
    print(i)
import csv
f=open("tejaa.csv","w+",newline="")
objw=csv.writer(f)
objw.writerows(list1)
print("*************")
f.seek(0)
objr=csv.reader(f)
for i in objr:
    print(i)
#by using module type creating csv file
def  teja_csv(obj):
    obj.writerow(["eid", "ename", "esal"])
    while True:
        empid = int(input("enter employrr id:"))
        emppname = input("enter employee name:")
        empsal = int(input("entr employee salary:"))
        obj.writerow([empid, emppname, empsal])
        ch = input("if u wanna continue the programme say yes/no:")
        if ch.lower() != "yes":
            print("every line stored  succesfully")
            break
#callin in deferent python file
import csv
import teja
f=open("teja.csv","w")
objw=csv.writer(f)
teja.teja_csv(objw)
f.close()
#by using  module reading file
def  teja_csv(obj):
    for i in obj:
        print(i)
#calling function
import csv
import teja
f=open("teja.csv","r")
objr=csv.reader(f)
teja.teja_csv(objr)
f.close()
# students programme
import csv
f=open("teja.csv","w",newline="")
objw=csv.writer(f)
objw.writerow(["sid","sname","m1","m2","m3"])
while True:
    a=input("enter student id:")
    b=input("enter student name:")
    c=input("enter m1 marks:")
    d=input("enter m2 marks:")
    e=input("enter m3 marks:")
    objw.writerow([a,b,c,d,e])
    ch=input("if u wanna continue the programme say yes/no:")
    if ch.lower()!="yes":
        print("every line stored  succesfully")
        break
f.close()
import csv
f=open("teja.csv","r")
objr=csv.reader(f)
list=[]
for i in objr:
    list.append(i)
print(list)
f.close()

list1=[]
for i in list:
    if i[0]=="sid":
        i.append("total")
        i.append("avg")
        i.append("grade")
        list1.append(i)
    else:
        total=int(i[2])+int(i[3])+int(i[4])
        i.append(total)
        avg=total/3
        i.append(avg)
        grade="a" if (avg)>=90 else "b" if (avg)<90 and (avg)>=70  else "c"
        i.append(grade)
        list1.append(i)
print(list1)
import csv
f=open("tejaa.csv","w+",newline="")
objw=csv.writer(f)
objw.writerows(list1)
f.seek(0)
objr=csv.reader(f)
for i in objr:
    print(i)
#copy file from one file to another file
f=open("abcd.csv","w",newline="")
objw=csv.writer(f)
objw.writerow(["id","name"])
objw.writerow([1111,"teja"])
f.seek(0)
f=open("abcd.csv","r")
objr=csv.reader(f)
list=[]
for i in objr:
    list.append(i)
print(list)
f.close()
import csv
f=open("xyz.csv","w+",newline="")
objw1=csv.writer(f)
objw1.writerows(list)
f.seek(0)
objr=csv.reader(f)
for i in objr:
    print(i)
#merging three files in one file
import csv
f=open("abcd.csv","w",newline="")
objw1=csv.writer(f)
objw1.writerow(["id","name"])
objw1.writerow([1111,"teja"])
f.seek(0)
f=open("abcd.csv","r")
objr1=csv.reader(f)
list1=[]
for i in objr1:
    list1.append(i)
print(list1)
f.close()
import csv
f=open("abcde.csv","w",newline="")
objw2=csv.writer(f)
objw2.writerow(["id","name"])
objw2.writerow([2222,"raju"])
f.seek(0)
f=open("abcde.csv","r")
objr2=csv.reader(f)
list2=[]
for i in objr2:
    list2.append(i[1])
print(list2)
f.close()
import csv
f=open("abcdef.csv","w",newline="")
objw3=csv.writer(f)
objw3.writerow(["id","name"])
objw3.writerow([3333,"chandu"])
f.seek(0)
f=open("abcd.csv","r")
objr3=csv.reader(f)
list3=[]
for i in objr3:
    list3.append(i[1])
print(list3)
f.close()
import csv
f=open("xyz.csv","w+",newline="")
objw4=csv.writer(f)
objw4.writerows([list1,list2,list3])
f.seek(0)
objr4=csv.reader(f)
list4=[]
for i in objr4:
    list4.append(i)
print(list4)
#taking nest line:
import csv
f=open("teja,csv","w+",newline="")
objw=csv.writer(f)
objw.writerow(["sid","sname","m1","m2","m3"])
objw.writerow([111,"teja",66,77,88])
objw.writerow([222,"raju",66,77,88])
objw.writerow([333,"cnu",66,77,88])
f.seek(0)
objr=csv.reader(f)
next(objr)
for i in objr:
    print(i)
f.close()
#2
import csv
f=open("teja,csv","w+",newline="")
objw=csv.writer(f)
objw.writerow(["sid","sname","m1","m2","m3"])
objw.writerow([111,"teja",66,77,88])
objw.writerow([222,"raju",66,77,88])
objw.writerow([333,"cnu",66,77,88])
f.seek(0)
objr=csv.reader(f)
list1=list(objr)
for i in range(1,len(list1)):
    print(list1[i])
f.close()
#file is exist or not:
import os
import csv
fname=input("Enter file name:")
a=os.path.isfile(fname)
if a==True:
    print("file is exist")
    ch=input("if u want read the file say yes/no:")
    if ch.lower()!="yes":
        print("thank you for using this application")
        exit()
    else:
        f=open(fname,"r")
        objr=csv.reader(f)
        for i in objr:
            print(i)
else:
    print("we don't have such a file")




