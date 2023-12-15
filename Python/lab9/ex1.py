from tkinter import*
a = 0
def pressadd():
    global a
    a += 1
    label.config(text=str(a))
def pressdec():
    global a
    a -= 1
    label.config(text=str(a))
def pressreset():
    global a 
    a = 0
    label.config(text=str(a))
window = Tk()
window.title("Spinner")

label = Label(window, text=str(a))
btAdd = Button(window, text = "+", command = pressadd, width=10, height=2)
btDec = Button(window, text = "-", command = pressdec, width=10, height=2)
btReset = Button(window, text = "Reset", command = pressreset, width=10, height=2)

btAdd.pack()
btDec.pack()
btReset.pack()
label.pack()

window.mainloop()