from lib import sdcard
import json

SD = sdcard.SDCard()
SD.mount()
info = {
        'todo' : [],
        'done' : []
        }
def write_todo(obj):
    with open('/sd/todo.json', 'w') as f:
        json.dump(obj, indent = 1)

try:
    with open('/sd/todo.json', 'r') as f:
        info = json.load(f)
except:
    # if file does not exist, write a new one
    with open('/sd/todo.json', 'w') as f:
        json.dump(info, indent = 1)


