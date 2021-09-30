# file should be in msword file without any photos
# getting single page
import PyPDF2
f=open("C:/Users/SANDEEP/Desktop/ugc first paper.pdf","rb")
pdfobjr=PyPDF2.PdfFileReader(f)
pageno=pdfobjr.getNumPages()
print("no of pages in pdf:",pageno)
pageobj=pdfobjr.getPage(2)
a = pageobj.extractText()
print(a)
f1=open("teja.txt","w")
f1.write(a)
f1.close()
f.close()
#getting all pages
# file should be in msword file without any photos
import PyPDF2
f=open("C:/Users/SANDEEP/Desktop/ugc first paper.pdf","rb")
pdfobjr=PyPDF2.PdfFileReader(f)
pageno=pdfobjr.getNumPages()
print("no of pages in pdf:",pageno)
for i in range(pageno):
    pageobj=pdfobjr.getPage(i)
    a = pageobj.extractText()
    print(a)
    f1 = open("teja1.txt", "w")
    f1.write(a)
    f1.close()
f.close()
#selected file extracting
# file should be in msword file without any photos
import PyPDF2
f=open("C:/Users/SANDEEP/Desktop/ugc first paper.pdf","rb")
pdfobjr=PyPDF2.PdfFileReader(f)
pageno=pdfobjr.getNumPages()
print("no of pages in pdf:",pageno)
l1=[0,2,3]
for i in l1:
    pageobj=pdfobjr.getPage(i)
    a = pageobj.extractText()
    print(a)
    f1 = open("teja2.txt", "w")
    f1.write(a)
    f1.close()
f.close()
#creating one new pdf file and extract one page from other pdf file and dump into created file
import PyPDF2
f=open("C:/Users/SANDEEP/Desktop/ugc first paper.pdf","rb")
pdfr=PyPDF2.PdfFileReader(f)
pdfw=PyPDF2.PdfFileWriter()
pager=pdfr.getPage(2)
pdfw.addPage(pager)
newpdf=open("copy file.pdf","wb")
pdfw.write(newpdf)
newpdf.close()
f.close()
#coping all pages into new pdf file
import PyPDF2
f=open("C:/Users/SANDEEP/Desktop/ugc first paper.pdf","rb")
pdfr=PyPDF2.PdfFileReader(f)
pdfw=PyPDF2.PdfFileWriter()
pagenum=pdfr.getNumPages()
print("toatal number of pages:",pagenum)
for i in range(pagenum):
    pager = pdfr.getPage(i)
    pdfw.addPage(pager)
newpdf=open("copyall.pdf","wb")
pdfw.write(newpdf)
newpdf.close()
f.close()
#selected pages dump into new created pdf file
import PyPDF2
f=open("C:/Users/SANDEEP/Desktop/ugc first paper.pdf","rb")
pdfr=PyPDF2.PdfFileReader(f)
pdfw=PyPDF2.PdfFileWriter()
pagenum=pdfr.getNumPages()
print("toatal number of pages:",pagenum)
l1=[0,3]
for i in l1:
    pager = pdfr.getPage(i)
    pdfw.addPage(pager)
newpdf=open("copylist.pdf","wb")
pdfw.write(newpdf)
newpdf.close()
f.close()
#password for pdf file
import PyPDF2
f = open("C:/Users/SANDEEP/Desktop/ugc first paper.pdf","rb")
pdfr=PyPDF2.PdfFileReader(f)
pdfw=PyPDF2.PdfFileWriter()
pagenum=pdfr.getNumPages()
print(pagenum)
list=[0,3]
for i in list:
    pager=pdfr.getPage(i)
    pdfw.addPage(pager)
pdfw.encrypt(user_pwd="teja@123",owner_pwd=None,use_128bit=True)
new=open("enc.pdf","wb")
pdfw.write(new)
new.close()
f.close()
#coping one pdf file to new pdf file
import PyPDF2
f=open("C:/Users/SANDEEP/Desktop/ugc first paper.pdf","rb")
pdfr=PyPDF2.PdfFileReader(f)
pdfw=PyPDF2.PdfFileWriter()
pagenum=pdfr.getNumPages()
print("no of pages in pdf:",pagenum)
for i in range(pagenum):
    pager=pdfr.getPage(i)
    pdfw.addPage(pager)
pdfw.encrypt(user_pwd="teja@123",owner_pwd=None,use_128bit=True)
new=open("eny.pdf","wb")
pdfw.write(new)
new.close()
f.close()
#one file to multiple files
import PyPDF2
f=open("C:/Users/SANDEEP/Desktop/ugc first paper.pdf","rb")
pdfr=PyPDF2.PdfFileReader(f)
pdfw=PyPDF2.PdfFileWriter()
pnum=pdfr.getNumPages()
for i in range(pnum):
    pager=pdfr.getPage(i)
    pdfw.addPage(pager)
    pdfn="split"+str(i)+".pdf"
    new=open(pdfn,"wb")
    pdfw.write(new)
    new.close()
f.close()
#merging file
import PyPDF2
f=open("C:/Users/SANDEEP/Desktop/ugc first paper.pdf","rb")
pdfr=PyPDF2.PdfFileReader(f)
pdfw=PyPDF2.PdfFileWriter()
pagenum=pdfr.getNumPages()
print("no of pages in pdf:",pagenum)
for i in range(pagenum):
    pager=pdfr.getPage(i)
    pdfw.addPage(pager)
f1=open("C:/Users/SANDEEP/Desktop/teja bro resume.pdf","rb")
pdfr=PyPDF2.PdfFileReader(f)
pagenum1=pdfr.getNumPages()
print("no of pages in pdf:",pagenum1)
for i in range(pagenum1):
    pager=pdfr.getPage(i)
    pdfw.addPage(pager)
new=open("eny.pdf","wb")
pdfw.write(new)
new.close()
f1.close()
f.close()