import tkinter as tk
import random

def show_error_message():
    error_window = tk.Toplevel(master)
    error_window.title("Warning")
    error_label = tk.Label(error_window, text="Mouse pointer is not in rectangle")
    error_label.pack(padx=30, pady=30)

def click(click_event):
    x, y = click_event.x, click_event.y
    
    if 100 <= x <= 350 and 100 <= y <= 200:
        
        fill_color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
        canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=fill_color)
    else:
        show_error_message()

master = tk.Tk()

canvas = tk.Canvas(master, width=450, height=300, bg='white')
canvas.pack()


canvas.create_rectangle(100,100,350,200, outline="black")

canvas.bind('<Button-1>', click)

master.mainloop()
