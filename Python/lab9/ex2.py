from tkinter import *

class MoneyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        self.usd_to_thb_button = Button(self.root, text="USD -> THB", command=self.convert_usd_to_thb, width=30, height=1)
        self.usd_to_thb_button.grid(row=2, column=1, padx=5, pady=5)

        self.thb_to_usd_button = Button(self.root, text="THB -> USD", command=self.convert_thb_to_usd, width=30, height=1)
        self.thb_to_usd_button.grid(row=3, column=1, padx=5, pady=5)

        self.entry = Entry(self.root, width=40)
        self.entry.grid(row=1, column=1, padx=5, pady=5, )

    def convert_usd_to_thb(self):
            amount_usd = float(self.entry.get())
            amount_thb = amount_usd * 30  
            result_window = Toplevel(self.root)
            result_window.title("USD -> THB")
            result_window.geometry("250x50")
            Label(result_window, text=f"{amount_usd} USD = {amount_thb} THB").pack()
 

    def convert_thb_to_usd(self):
            amount_thb = float(self.entry.get())
            amount_usd = amount_thb / 30 
            result_window = Toplevel(self.root)
            result_window.title("THB -> USD")
            result_window.geometry("250x50")
            Label(result_window, text=f"{amount_thb} THB = {amount_usd:.2f} USD").pack()


root = Tk()
app = MoneyConverter(root)
root.mainloop()
