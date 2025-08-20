from lib.display import Display

display = Display()
# Draw text to the framebuffer, then write the frambuffer to the display:
display.text("DONE", x=5, y=10, color=display.palette[10])
display.show()
