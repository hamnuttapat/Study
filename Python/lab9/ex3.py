from tkinter import *
master = Tk()

canvas = Canvas(master, width=600, height=300, bg='white')
canvas.pack(padx=20, pady=20)


def clear():
    canvas.delete("all")
Button(master, text="Clear", command=clear).pack()

def click(click_event):
    global prev
    prev = click_event


def move(move_event):
    global prev
    canvas.create_line(prev.x, prev.y, move_event.x, move_event.y, width=2)
    prev = move_event 


canvas.bind('<Button-1>', click)
canvas.bind('<B1-Motion>', move)

mainloop()