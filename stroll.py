from tkinter import * 
from tkinter import ttk
from text_graphics import *
from classes import *

window = Tk()
window.geometry("800x400")

#canvas
canvas = Canvas(window, width=400, height=400)

#user's character object
user = character()

#widget holder
current_widgets = [] #widgets that do not disappear upon calling "canvas.delete('all')"

def opening_title():
    button_1 = Button(window, text="Start", font=fonts['4'], command=loading_bar)
    canvas.create_window(700, 400, anchor="nw", window=button_1)
    canvas.create_text(400, 300, anchor="nw", text="For Orion: A Sci-Fi RPG", font=fonts['2'])
    canvas.pack(fill="both", expand=True)

def loading_bar(): #just for graphics
    clean_canvas()
    load_bar = ttk.Progressbar(mode="determinate")
    current_widgets.append(load_bar)
    load_bar.place(x=600, y=380, width=350)
    load_bar.start()

    prologue() #speeding up for now

    #start_prologue = lambda: prologue() #need
    #window.after(6200, start_prologue) #need

def prologue():
    clean_canvas()
    type_text(dialogue['prologue_title'], dialogue_start_x, 100, fonts['3'])
    text_body = lambda: type_text(dialogue['prologue_body'], dialogue_start_x, 150, fonts['3'])
    window.after(1000, text_body)
    button_1 = Button(window, text="Continue...", font=fonts['3'], command=sign_off_report)
    appearing_button = lambda : canvas.create_window(700, 600, anchor="nw", window=button_1)
    window.after(12000, appearing_button)

def type_text(text, x, y, font):
    typing = lambda char: canvas.create_text(x, y, anchor="nw", text=char, font=font)
    for char in text:
        window.update()
        typing(char)
        window.after(100)
        x += 10
        if (x > dialogue_end_x):
            x = dialogue_start_x; y += 50
    
def sign_off_report():
    clean_canvas()
    name_entry = Entry(canvas, bd=8, width=80)
    #name_entry.grid(400,150)
    current_widgets.append(name_entry)
    name_entry.pack()
    name = ""
    user.name = name
    
def clean_canvas():
    for i in current_widgets:
        i.destroy()
        current_widgets.remove(i)
    canvas.delete('all')

opening_title()

window.mainloop()
