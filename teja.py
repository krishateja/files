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