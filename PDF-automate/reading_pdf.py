import PyPDF2

#opening the pdf file with normal open method.but have to read it in(read binary)
read=open('meetingminutes1.pdf','rb')

#Creating Reader object to read the pdf file
reader=PyPDF2.PdfFileReader(read)
##print(reader)

#Getting the number of pages in a pdf using numPages method 
##print(reader.numPages)

#-----------or---------------
print(reader.getNumPages())

#Get the page layout. See setPageLayout() for a description of valid layouts.
##print(reader.getPageLayout())

#Retrieve page number of a given PageObject

page=reader.getPage(1)
print(reader.getContents(pages))

#the getpage method will create the page object to access the page
##page=reader.getPage(0)

#the extract text method will get the info from particular page and
#prints it in string
##print(page.extractText())


#------------OR--------------

##page=reader.getPage(0).extractText()
##print(page)

#Extracting the whole pdf page by iterating the pdf file
##for pagenum in range(reader.numPages):
##   print(reader.getPage(pagenum).extractText())
