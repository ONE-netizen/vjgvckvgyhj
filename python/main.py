
from tkinter import *

def get_entry():
    value = int(entry.get())
    value1 = int(entry2.get())

    txt["text"] = value + value1

root = Tk()
root.title("My app")
root.geometry("400x300")

entry = Entry()
entry.pack()

entry2 = Entry()
entry2.pack()

txt = Label(text="New text...")
txt.pack()

btn=Button(text="Hui!", command=get_entry)
btn.pack()

root.mainloop()