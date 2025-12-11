from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x400")

def msg():
    #messagebox.showwarning('Alert', "stop! Virus detected") 
    messagebox.showinfo('Info','Click this button to see how to open a new tab')

button = Button(root, text="Click this button to see how to open a new tab" ,command= msg)
button.place(x= 40, y= 80)

root.mainloop()
