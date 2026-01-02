import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        P = float(entry_principal.get())
        T = float(entry_time.get())
        R = float(entry_rate.get())

        # Simple Interest
        simple_interest = (P * R * T) / 100

        # Compound Interest
        compound_interest = P * ((1 + R / 100) ** T) - P

        label_si_result.config(text=f"Simple Interest: {simple_interest:.2f}")
        label_ci_result.config(text=f"Compound Interest: {compound_interest:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values")

# Create main window
root = tk.Tk()
root.title("Interest Calculator")
root.geometry("350x300")

# Labels and Entry fields
tk.Label(root, text="Principal Amount").pack(pady=5)
entry_principal = tk.Entry(root)
entry_principal.pack()

tk.Label(root, text="Time Period (years)").pack(pady=5)
entry_time = tk.Entry(root)
entry_time.pack()

tk.Label(root, text="Rate of Interest (%)").pack(pady=5)
entry_rate = tk.Entry(root)
entry_rate.pack()

# Calculate Button
tk.Button(root, text="Calculate Interest", command=calculate_interest).pack(pady=15)

# Result Labels
label_si_result = tk.Label(root, text="Simple Interest: ")
label_si_result.pack(pady=5)

label_ci_result = tk.Label(root, text="Compound Interest: ")
label_ci_result.pack(pady=5)

# Run the application
root.mainloop()
