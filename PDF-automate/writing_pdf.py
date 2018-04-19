import PyPDF2

#creating a pdf file by cpying from another pdf file

read=open('meetingminutes1.pdf','rb')

reader=PyPDF2.PdfFileReader(read)
writer=PyPDF2.PdfFileWriter()

for pagenum in range(reader.numPages):
   page=reader.getPage(pagenum)
   writer.addPage(page)


outfile=open('meetingminutes2.pdf','wb')
writer.write(outfile)
outfile.close()
read.close()
