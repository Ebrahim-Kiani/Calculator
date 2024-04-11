import tkinter as tk
from tkinter import messagebox
from project import CalculateRun
def calculate():
    try:
        result = CalculateRun(entry.get())
        messagebox.showinfo("Result", f"The result is: {result}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def add_to_expression(value):
    entry.insert(tk.END, value)

def clear_entry():
    entry.delete(0, tk.END)

def delete_last_character():
    entry.delete(len(entry.get()) - 1)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the entry widget for the math expression
entry = tk.Entry(window, width=20, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

# Define button styles
button_width = 5
button_height = 2
button_font = ("Arial", 12)

# Create buttons for each key
keys = [
    '7', '8', '9', 
    '4', '5', '6', 
    '1', '2', '3', 
    '0','.','*',
    '-','+','/',
    '(',')','^',
    'C','⌫','Enter'  # Delete key
]

row = 1
col = 0

for key in keys:
    if key == 'Enter':
        button = tk.Button(window, text=key, width=button_width, height=button_height, font=button_font, command=calculate)
    elif key == 'C':
        button = tk.Button(window, text=key, width=button_width, height=button_height, font=button_font, command=clear_entry)
    elif key == '⌫':
        button = tk.Button(window, text=key, width=button_width, height=button_height, font=button_font, command=delete_last_character)
    else:
        button = tk.Button(window, text=key, width=button_width, height=button_height, font=button_font, command=lambda value=key: add_to_expression(value))
    
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    col += 1

    if col > 2:
        col = 0
        row += 1

# Configure grid column and row weights
for i in range(3):
    window.grid_columnconfigure(i, weight=1)
for i in range(row):
    window.grid_rowconfigure(i, weight=1)

# Run the main event loop
window.mainloop()