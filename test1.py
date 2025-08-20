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
        json.dump(obj)

try:
    with open('/sd/todo.json', 'r') as f:
        info = json.load(f)
except Exception as e:
    # if file does not exist, write a new one
    with open('/sd/todo.json', 'w') as f:
        json.dump(info)

# add a couple of entries for testing

info['todo'] = info['todo'].append('test1')
info['done'] = info['done'].append('test2')

write_todo(obj)
