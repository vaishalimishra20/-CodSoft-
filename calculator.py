import tkinter as tk

def button_click(char):
    current = display.get()
    if char == "C":
        display.set("")
    elif char == "=":
        try:
            result = eval(current)
            display.set(result)
        except:
            display.set("Error")
    else:
        display.set(current + str(char))

r= tk.Tk()
r.title("Calculator")

display = tk.StringVar()
display.set("")

display_label = tk.Label(r, textvariable=display, anchor="e", font=("Arial", 30), bd=20)
display_label.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row = 1
col = 0

for button in buttons:
    tk.Button(r, text=button, command=lambda b=button: button_click(b), font=("Arial", 25)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

r.mainloop()
