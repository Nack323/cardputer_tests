from lib import sdcard

SD = sdcard.SDCard()
SD.mount()

with open("/sd/test1.txt", "w") as f:
    f.write("testing")
