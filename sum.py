import tkinter as tk
from tkinter import messagebox

def calculate_sum():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create main window
root = tk.Tk()
root.title("Sum Calculator")
root.geometry("300x200")

# First number
tk.Label(root, text="First Number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

# Second number
tk.Label(root, text="Second Number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

# Calculate button
tk.Button(root, text="Calculate Sum", command=calculate_sum).pack(pady=10)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=5)

# Run the application
root.mainloop()
