import tkinter as tk
import tkinter.ttk as ttk

class CompLamp:
    def __init__(self, parent, width, order, color="red", *args, **kwargs):
        self.frame = ttk.Frame(parent.frame, *args, **kwargs)
        self.canvas = tk.Canvas(self.frame, width=width, height=width, bg="gray",highlightthickness=0)
        self.canvas.pack()
        self.color = color
        offset = width//8
        self.lamp = self.canvas.create_oval(offset, offset,7*offset,7*offset,fill='black')

        self.frame.grid(row=order, column=0)
        self.state = "off"

    def turn_on(self):
        self.state = "on"
        self.canvas.itemconfigure(self.lamp, fill=self.color)
        
    def turn_off(self):
        self.state = "off"
        self.canvas.itemconfigure(self.lamp, fill='black')    

class CompTrafficLight:
    def __init__(self, root, wd, initial_color="red", *args, **kwargs):
        if initial_color not in ("red", "yellow", "green"):
            raise ValueError(initial_color + " is not a valid color")
        
        self.frame = ttk.Frame(root, width=wd, *args, **kwargs)
        self.frame.grid(row=0, column=0)
        self.color = initial_color

        self.lamps = dict(zip(('red', 'yellow', 'green'),(CompLamp(self, wd, 0, 'red'),CompLamp(self, wd, 1, 'yellow'),CompLamp(self, wd, 2, 'green'))))
        self.lamps[self.color].turn_on()

    def change(self):
        if self.color == 'red':
           new_color = 'green'
        elif self.color == 'green':
           new_color = 'yellow'
        elif self.color == 'yellow':
           new_color = 'red'
        self.lamps[self.color].turn_off()
        self.color = new_color
        self.lamps[self.color].turn_on()
    def resize(self, width):
        for lamp in self.lamps.values():
            lamp.resize(width) 

