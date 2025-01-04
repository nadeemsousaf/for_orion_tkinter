from tkinter import * 
from tkinter import ttk
from fonts import *
from classes import *

window = Tk()
window.geometry("800x400")

#canvas
canvas = Canvas(window, width=400, height=400)

#user's character object
user = character()

#widget holder
current_widgets = []

def opening_title():
    button_1 = Button(window, text="Start", font=fonts['1'], command=prologue)
    canvas.create_window(700, 400, anchor="nw", window=button_1)
    canvas.create_text(400, 300, anchor="nw", text="For Orion: A Sci-Fi RPG", font=fonts['2'])
    canvas.pack(fill="both", expand=True)
    
def prologue():
    clean_canvas()
    ok = 1

def clean_canvas():
    for i in current_widgets:
        i.destroy()
        current_widgets.remove(i)
    canvas.delete('all')

opening_title()

window.mainloop()
