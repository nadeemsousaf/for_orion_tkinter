from tkinter import * 
from tkinter import ttk
from text_graphics import *
from classes import *

window = Tk()
window.geometry("800x400")

#To edit from specific function: canvas.pack(fill="both", expand=True)

#canvas
canvas = Canvas(window, width=400, height=400)

#user's character object
user = character()

#widget holder
current_widgets = [] #widgets that do not disappear upon calling "canvas.delete('all')"

def opening_title():
    button_1 = Button(window, text="Start", font=fonts['4'], command=prologue)
    canvas.create_window(700, 400, anchor="nw", window=button_1)
    canvas.create_text(400, 300, anchor="nw", text="For Orion: A Sci-Fi RPG", font=fonts['2'])
    canvas.pack(fill="both", expand=True)

def loading_bar(): #just for graphics
    clean_canvas()
    load_bar = ttk.Progressbar(mode="determinate")
    current_widgets.append(load_bar)
    load_bar.place(x=600, y=380, width=350)
    load_bar.start()

def prologue():
    clean_canvas()
    type_text(dialogue['prologue_title'], dialogue_start_x, 100, fonts['3'])
    text_body = lambda: type_text(dialogue['prologue_body'], dialogue_start_x, 150, fonts['3'])
    window.after(line_speed, text_body)
    button_1 = Button(window, text="Continue...", font=fonts['3'], command=sign_off_report)
    appearing_button = lambda : canvas.create_window(700, 600, anchor="nw", window=button_1)
    window.after(button_speed, appearing_button)

def type_text(text, x, y, font):
    typing = lambda char: canvas.create_text(x, y, anchor="nw", text=char, font=font)
    for char in text:
        window.update()
        typing(char)
        window.after(typing_speed)
        x += 10
        if (x > dialogue_end_x):
            x = dialogue_start_x; y += 50
    
def sign_off_report():
    clean_canvas()
    name_label = Label(canvas, text="Signing off,", font=fonts['3'])
    name_entry = Entry(canvas, bd=10, width=40, font=fonts['3'])
    button_1 = Button(window, text="Submit", font=fonts['3'], command=save_name)
    name_label.grid(row=0, column=0, pady=100, padx=550)
    name_entry.grid(row=1, column=0, pady=0, padx=550)
    current_widgets.append(name_label)
    current_widgets.append(name_entry) #add last
    canvas.create_window(750, 330, anchor="nw", window=button_1)

def save_name():
    user.name = current_widgets[len(current_widgets)-1].get()
    clean_canvas()
    loading_bar()
    type_text(dialogue['save_name'], 550, 400, fonts['3'])
    window.after(6200, name_submission_page)

def name_submission_page():
    clean_canvas()
    button_1 = Button(window, text="Continue", font=fonts['3']) #, command=
    type_text(dialogue['name_submission_page'], 550, 400, fonts['3'])
    type_text(user.name, 550, 450, fonts['3'])
    canvas.create_window(700, 500, anchor="nw", window=button_1)

def clean_canvas():
    for i in current_widgets:
        i.destroy()
        current_widgets.remove(i)
    canvas.delete('all')

opening_title()

window.mainloop()
