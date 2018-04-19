import PyPDF2


read1=open('meetingminutes1.pdf','rb')
read2=open('meetingminutes2.pdf','rb')

reader1=PyPDF2.PdfFileReader(read1)
reader2=PyPDF2.PdfFileReader(read2)

writer=PyPDF2.PdfFileWriter()

for file1 in range(reader1.numPages):
   page=reader1.getPage(file1)
   writer.addPage(page)
   
for file2 in range(reader2.numPages):
   page=reader1.getPage(file2)
   writer.addPage(page)

outfile=open('combinedmeetingminutes.pdf','wb')
writer.write(outfile)
read1.close()
read2.close()
outfile.close()
