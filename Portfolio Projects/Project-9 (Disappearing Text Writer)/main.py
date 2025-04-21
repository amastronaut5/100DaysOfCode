#text disappearing

from tkinter import *
from tkinter import ttk, Text

from win32ui import MessageBox

window = Tk()
window.geometry('500x500')

window.title('Disappearing Text Writer')
txt = Text(window, height=500, width=500)
txt.pack()

#check if user stopped typing
def in_typing(event):
    global typing_after_id

    if typing_after_id != None:
        window.after_cancel(typing_after_id)

    typing_after_id = window.after(5000, stopped_typing)

def stopped_typing():
    txt.delete('1.0', END)

warning = MessageBox("The text will be removed after 5 seconds of inactivity","Warning")

txt.bind('<KeyRelease>',in_typing)
typing_after_id = None

window.mainloop()