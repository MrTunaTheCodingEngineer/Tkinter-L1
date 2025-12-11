from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Event Handler")

def Handle_keypress(event):
    print(event.char)

window.bind("<Key>", Handle_keypress)

def Handle_click(event):
    print("\nThe button was clicked!")

button = Button(text= "click me!")
button.pack()

button.bind("<Button-1>", Handle_click)

window.mainloop()