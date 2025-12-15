from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile

root = Tk()
root.geometry("400x400")

def save():

    files = [("All files", "*.*"),
             ("Python files", "*.py"), 
             ("Text Document", "*.txt")]
    file = asksaveasfile(filetypes = files, defaultextension = files)

btn = Button(root, text= 'Save' , command = lambda : save())
btn.pack(side = LEFT)

def open_file():
    filepath = askopenfilename(
        filetypes= [("Text Files", "*.txt"), ("All files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
        input_file.close
    root.title(f"codingal's text editor - {filepath}")

txt_edit = Text(root)

btn = Button(root, text= 'Open' , command = lambda : open_file())
btn.pack(side = RIGHT)

mainloop()
