from tkinter import *
from random import choice, randint

class RandomColors_Lines(Frame):
    '''canvas on frame'''
    def __init__(self, root):
        Frame.__init__(self, master=root)
        # set bg from Canvas widget
        self.canvasLines = Canvas(self, width=400, height=400, bg='white')
        self.canvasLines.grid(row=0, column=0) #griding 

    def color_generator(self):
        '''This create random colors'''
        # 0x ff ff ff = RGB in hexa 
        # :06x = obtained upto 6 digits
        return f"#{randint(0, 0xffffff):06x}" 
    
    def randomChooser_inCanvas(self):
        '''Generating lines of random colors & line width'''
        # co-ordinates 
        x1 = randint(0, 400)
        y1 = randint(0, 400)
        x2 = randint(0, 400)
        y2 = randint(0, 400)
        self.canvasLines.create_line(
            x1, y1, x2, y2,              # co-ordinates
            fill=self.color_generator(), # random color assign
            width=randint(1, 25)         # random width size 
        )
        self.canvasLines.update() # this update screen everytime

root = Tk()
frame = RandomColors_Lines(root) # Calling class
frame.grid(row=0, column=0) # griding
while(1):
    frame.randomChooser_inCanvas()
root.mainloop()