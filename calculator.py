import tkinter as tk
import math

current_expression = ""
def on_button_click(button):
    global current_expression

    if button == "C":
        current_expression = ""
        display.delete(0, tk.END)
    
    elif button == "=":
        try:
            result = eval(current_expression)
            display.delete(0, tk.END)
            display.insert(0, str(result))
            current_expression = str(result)
        except Exception:
            display.delete(0, tk.END)
            display.insert(0, "Error")
            current_expression = ""

    elif button == "√":
        try:
            result = math.sqrt(float(current_expression))
            display.delete(0, tk.END)
            display.insert(0, str(result))
            current_expression = str(result)
        except Exception:
            display.delete(0, tk.END)
            display.insert(0, "Error")
            current_expression = ""

    elif button == "^":
        current_expression += "**"
        display.delete(0, tk.END)
        display.insert(0, current_expression)
    else:
        current_expression += str(button)
        display.delete(0, tk.END)
        display.insert(0, current_expression)

def set_theme(theme):
    if theme == "light":
        root.config(bg="white")
        display.config(bg = "lightgray", fg = "black")
    elif theme == "dark":
        root.config(bg="black")
        display.config(bg = "gray", fg = "white")
    elif theme == "neutral-black":
        root.config(bg="#2e292c")
        display.config(bg = "#2e292c", fg = "#dcc4b0")
    elif theme == "copper":
        root.config(bg="#2e292c")
        display.config(bg = "#754c2c", fg = "#ede7d5")
    elif theme == "dark-blue":
        root.config(bg="#0b1c29")
        display.config(bg = "#040414", fg = "#ede7d5")
    for button in buttons:
        button.config(bg="lightgray" if theme == "light" else "darkgray" if theme == "dark" else "#5199e3"
                       if theme == "neutral-black" else "#754c2c" if theme == "copper" else "#799ba8",  
                       fg="black" if theme != "dark" else "white")
        
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")

display = tk.Entry(root, font=("Arial", 24), justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Calculator buttons
buttons = []
button_texts = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+", 
    "√", "^",
]

row_val = 1
col_val = 0

# Making the buttons
for text in button_texts:
    button = tk.Button(root, text=text, font=("Arimo", 18), width=5, height=2, command=lambda text=text: on_button_click(text))
    button.grid(row=row_val, column=col_val, padx=5, pady=5)
    buttons.append(button)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Menu
menubar = tk.Menu(root)
theme_menu = tk.Menu(menubar, tearoff=0)
theme_menu.add_command(label="Light theme", command=lambda: set_theme("light"))
theme_menu.add_command(label="Dark theme", command=lambda: set_theme("dark"))
theme_menu.add_command(label="Neutral-black theme", command=lambda: set_theme("neutral-black"))
theme_menu.add_command(label="Copper theme", command=lambda: set_theme("copper"))
theme_menu.add_command(label="Dark-blue theme", command=lambda: set_theme("dark-blue"))
menubar.add_cascade(label="Settings", menu=theme_menu)
root.config(menu=menubar)
root.mainloop()
