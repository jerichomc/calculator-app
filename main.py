from tkinter import *
from functions import *

window = Tk()
window.title("Calculator App")
window.geometry("400x500")
window.resizable(False, False)


current_amount = 0

frame = Frame(window, bg="#F4EDD3", bd=5, relief=SUNKEN, width=200, height=100)
frame.pack(side="top", fill="x")
label = Label(frame, text=current_amount, font=("Roboto", 25), bg="#F4EDD3", anchor="e")
label.pack(fill="both", expand=True)


window.mainloop()

