import tkinter as tk
from tkinter import ttk

def fahrenheit_to_celsius():
    """Converts Fahrenheit to Celsius and updates the result label."""
    try:
        fahrenheit = float(ent_temperature.get())
        celsius = (fahrenheit - 32) * 5 / 9
        lbl_result.config(text=f"{round(celsius, 2)} °C", foreground="green")
    except ValueError:
        lbl_result.config(text="Invalid Input", foreground="red")

def clear_fields():
    """Clears the input field and result label."""
    ent_temperature.delete(0, tk.END)
    lbl_result.config(text="")

# Create main window
window = tk.Tk()
window.title("Temperature Converter")
window.geometry("300x150")
window.resizable(width=False, height=False)

# Styling
style = ttk.Style()
style.configure("TButton", font=("Arial", 12))
style.configure("TLabel", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))

# Input Field
frm_entry = ttk.Frame(window)
frm_entry.pack(pady=10)

ent_temperature = ttk.Entry(frm_entry, width=10)
ent_temperature.pack(side="left", padx=5)

lbl_temp = ttk.Label(frm_entry, text="°F")
lbl_temp.pack(side="left")

# Conversion & Clear Buttons
frm_buttons = ttk.Frame(window)
frm_buttons.pack(pady=10)

btn_convert = ttk.Button(frm_buttons, text="→ Convert", command=fahrenheit_to_celsius)
btn_convert.pack(side="left", padx=5)

btn_clear = ttk.Button(frm_buttons, text="Clear", command=clear_fields)
btn_clear.pack(side="left", padx=5)

# Output Label
lbl_result = ttk.Label(window, text="", font=("Arial", 14))
lbl_result.pack(pady=10)

# Run application
window.mainloop()
