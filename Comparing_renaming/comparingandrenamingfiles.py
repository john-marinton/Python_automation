#! python3

import os
import json
from pprint import pprint


def rename(location1,location2):
   
   for filename in os.listdir(location1):
      
      #-- Asinging a new name to the file and slicing the extension and adding my defined extension--#
      finalfilename= 'Copied-'+filename[:-5]+'.json'
      
      #--loading the data----#
      data=json.load(open(location1+'\\'+filename,'r'))

                         #-----Or------#
      
      #----Using os.join method--#
##      data=json.load(open(os.path.join(idir,filename),'r')
      
      #--Joining the filename and the output directory
      finalpath=os.path.join(location2,finalfilename)

      #----Writing the data to the output directory---#
      with open(finalpath,'w') as outfile:
         json.dump(data,outfile,indent=3)


list1_=[]
list2_=[]
def difference1(location1):
   for filename in os.listdir(location1):
      f1=json.load(open(location1+'\\'+filename,'r'))
      dumps_=json.dumps(f1,indent=3)
      list1_.append(dumps_)

def difference2(location2):
   for filename in os.listdir(location2):
      f2=json.load(open(location2+'\\'+filename,'r'))
      dumps_=json.dumps(f2,indent=3)
      list2_.append(dumps_)
      
def compare(d1,d2):
   
   #--Checking whether the multiple files are same or not
   if str(d1.issubset(d2))=='True':   
      print('multiple files from two folders are same')
   else:   
      print('multiple files from two folders are not same')

   #--Checking  the difference of multiple files   
   if str(d1.difference(d2))=='set()':
      print('There is no difference in the files')
   else:
      print('The file is not same because of this contents is not present in output directory\n ')
      pprint(d1.difference(d2))

   
   
   


#Input Directory
location1=input(r'Enter your input Directory path: ')
location2=input(r'Enter your Output Directory path:')

#calling the rename function
rename(location1,location2)

#Calling the difference functtion
difference1(location1)
difference2(location2)

#Converting list to set
convert1=set(list1_)
convert2=set(list2_)

#Calling the compare function
compare(convert1,convert2)


