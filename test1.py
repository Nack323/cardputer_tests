from lib import sdcard
import json

SD = sdcard.SDCard()
SD.mount()
info = {
        'todo' : [],
        'done' : []
        }
try:
    with open('todo.json', 'r') as f:
        info = json.load(f)
except:
    # if file does not exist, write a new one
    with open('todo.json', 'w') as f:
        json.dump(info, indent = 1)


