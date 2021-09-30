import PyPDF2
f=open("C:/Users/SANDEEP/Desktop/pythonvariables.pdf","rb")
pdfr=PyPDF2.PdfFileReader(f)
pdfw=PyPDF2.PdfFileWriter()
npage=pdfr.getNumPages()
print("nuber of pages:",npage)
for i in range(npage):
    a=pdfr.getPage(i)
    pdfw.addPage(a)
pdfw.encrypt(user_pwd="teja@007",owner_pwd=None,use_128bit=True)
f1=open("new.pdf","wb")
pdfw.write(f1)
f1.close()
f.close()