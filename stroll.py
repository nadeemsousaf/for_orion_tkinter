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
    button_1 = Button(window, text="Start", font=fonts['4'], command=loading_bar)
    canvas.create_window(700, 400, anchor="nw", window=button_1)
    canvas.create_text(400, 300, anchor="nw", text="For Orion: A Sci-Fi RPG", font=fonts['2'])
    canvas.pack(fill="both", expand=True)

def loading_bar():
    clean_canvas()
    load_bar = ttk.Progressbar(mode="indeterminate")
    current_widgets.append(load_bar)
    load_bar.place(x=600, y=400, width=350)
    load_bar.start()
    start_prologue = lambda: prologue()
    window.after(2000, start_prologue)
    

def prologue():
    clean_canvas()
    type_text("Mission Report:", 400, 100, fonts['3'])
    text_1 = lambda: type_text("Rocket is off course.", 400, 150, fonts['3'])
    window.after(1000, text_1)

def type_text(text, x, y, text_font):
    building_text = ""
    index = 0
    def typing():
        canvas.create_text(x, y, anchor="nw", text=building_text, font=text_font)
        index += 1
        print(index)
    try:
        building_text += text[index]
        #typing = lambda: canvas.create_text(x, y, anchor="nw", text=building_text, font=text_font); index += 1
        window.after(1000, typing())
        '''
        for char in text:
            building_text = building_text + char
            canvas.create_text(x, y, anchor="nw", text=building_text, font=text_font)
            typing = lambda: canvas.create_text(x, y, anchor="nw", text=building_text, font=text_font)
            window.after(1000, typing)
        '''
    except IndexError:
        return

def clean_canvas():
    for i in current_widgets:
        i.destroy()
        current_widgets.remove(i)
    canvas.delete('all')

opening_title()

window.mainloop()
