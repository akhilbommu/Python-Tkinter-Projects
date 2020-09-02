import tkinter
from tkinter import *
import random
from tkinter import messagebox

answers = ["python", "java", "swift", "canada", "india", "america", "london", ]
words = ["nptoyh", "avja", "wfsit", "cdanaa", "aidin", "aiearcm", "odnlon", ]

num = random.randrange(0, len(answers), 1)


def reset():
    global words, answers, num
    num = random.randrange(0, len(answers), 1)
    lbl.configure(text=words[num])
    e1.delete(0, END)


def default():
    global words, answers, num
    lbl.configure(text=words[num])


def checkans():
    global words, answers, num
    var = e1.get()
    if var == answers[num]:
        messagebox.showinfo("Success", "This is Correct Answer")
        reset()
    else:
        messagebox.showerror("Error", "This is not Correct")
        e1.delete(0, END)


# To get a main window
root = tkinter.Tk()

# Opens the window at center
root.geometry("350x400")

root.title("Jumbled Words")
root.configure(background="#000000")

lbl = Label(
    root,
    text="Your text here",
    font=("Verdana", 18),
    bg="#000000",
    fg="#ffffff",
)
lbl.pack(pady=30, ipadx=10, ipady=10)

ans1 = StringVar()
e1 = Entry(
    root,
    font=("Verdana", 16),
    textvariable=ans1,
)
e1.pack(ipady=5, ipadx=5)

btncheck = Button(
    root,
    text="Check",
    font=("Comic sans ms", 16),
    width=14,
    bg="#4C4B4B",
    fg="#6ab04c",
    relief=GROOVE,
    command=checkans,
)
btncheck.pack(pady=40)

btnreset = Button(
    root,
    text="Reset",
    font=("Comic sans ms", 16),
    width=14,
    bg="#4C4B4B",
    fg="#EA425C",
    relief=GROOVE,
    command=reset,
)
btnreset.pack()

default()

root.mainloop()
