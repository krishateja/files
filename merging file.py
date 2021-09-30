with open("pm.txt","w") as f1:
    f1.write("111,aaa,pm,50000\n222,bbb,pm,52000\n333,ccc,pm,54000\n")
with open("tm.txt","w") as f2:
    f2.write("111,aaa,tm,50000\n222,bbb,tm,52000\n333,ccc,tm,54000\n")
with open("devl.txt","w") as f3:
    f3.write("111,aaa,devl,50000\n222,bbb,devl,52000\n333,ccc,devl,54000")
with open("pm.txt","r") as f1:
    a=f1.read()
with open("tm.txt","r") as f2:
   b=f2.read()
with open("pm.txt","r") as f3:
    c=f3.read()
with open("all.txt","w+") as f4:
    f4.write(a)
    f4.write(b)
    f4.write(c)
    f4.seek(0)
    print(f4.read())
with open("pm.txt","w") as f1:
    f1.write("111,aaa,pm,50000\n222,bbb,pm,52000\n333,ccc,pm,54000\n")
with open("tm.txt","w") as f2:
    f2.write("111,aaa,tm,50000\n222,bbb,tm,52000\n333,ccc,tm,54000\n")
with open("devl.txt","w") as f3:
    f3.write("111,aaa,devl,50000\n222,bbb,devl,52000\n333,ccc,devl,54000")
with open("pm.txt","r") as f1:
    a=f1.read()
with open("tm.txt","r") as f2:
   b=f2.read()
with open("pm.txt","r") as f3:
    c=f3.read()
    d=a+b+c
with open("all.txt","w+") as f4:
    f4.write(d)
    f4.seek(0)
    e=f4.read()
    print(e)
#location problem
with open("C:/Users/SANDEEP/Desktop/files/abc.txt","w+") as f1:
    f1.write("i love python")
    f1.seek(0)
    a=f1.read()
    print(a)
    i=a.index("python")
    f1.seek(i)
    b=a.replace("python","java  ")
    f1.seek(0)
    print(b)
with open("C:/Users/SANDEEP/Desktop/files/teja.txt","r+") as f1:
    a=f1.read()
    print(a)
    i=a.index("java")
    f1.seek(i)
    f1.write("python")
    f1.seek(0)
    b=f1.read()
    print(b)
#zip file:
with open("teja.txt",'w') as f1:
    f1.write("teja doing coding")
with open("raju.txt",'w') as f2:
    f2.write("teja doing coding")
with open("chandu.txt",'w') as f3:
    f3.write("teja doing coding")
from zipfile import ZipFile
f4=ZipFile("z.zip","w")
f4.write("teja.txt")
f4.write("raju.txt")
f4.write("chandu.txt")
f4.close()
f4=ZipFile("z.zip","r")
a=f4.namelist()
print(a)
f4.extractall()
for i in a:
    print(i)
    file=open(i,"r")
    b=file.read()
    print(b)
    file.close()
