import tkinter as tk
import math

# Create main window
win = tk.Tk()
win.title("Calculator")
win.geometry("360x540")
win.configure(bg="#1e272e")

# Display box
box = tk.Entry(win, font=("Arial", 28, "bold"), bd=0,
               bg="#2f3640", fg="white", justify="right")
box.pack(fill="both", padx=10, pady=15, ipady=20)

# Functions
def press(x):
    box.insert(tk.END, x)

def clear():
    box.delete(0, tk.END)

def equal():
    try:
        val = eval(box.get())
        box.delete(0, tk.END)
        box.insert(0, val)
    except:
        box.delete(0, tk.END)
        box.insert(0, "err")

def root_fun():
    try:
        val = float(box.get())
        box.delete(0, tk.END)
        box.insert(0, math.sqrt(val))
    except:
        box.delete(0, tk.END)
        box.insert(0, "err")

# Handle keyboard input
def key_press(event):
    key = event.keysym
    if key in ('0','1','2','3','4','5','6','7','8','9'):
        press(key)
    elif key in ('plus','KP_Add'):
        press('+')
    elif key in ('minus','KP_Subtract'):
        press('-')
    elif key in ('asterisk','KP_Multiply'):
        press('*')
    elif key in ('slash','KP_Divide'):
        press('/')
    elif key in ('period','KP_Decimal'):
        press('.')
    elif key in ('Return','KP_Enter'):
        equal()
    elif key in ('BackSpace',):
        box.delete(len(box.get())-1, tk.END)
    elif key.lower() == 'c':
        clear()
    elif key.lower() == 'r':
        root_fun()

# Bind keys
win.bind("<Key>", key_press)

# Frame for buttons
frame = tk.Frame(win, bg="#1e272e")
frame.pack(pady=10)

# Round button using canvas
def round_btn(parent, text, cmd, r, c, color):
    canvas = tk.Canvas(parent, width=80, height=80,
                       bg="#1e272e", highlightthickness=0)
    canvas.grid(row=r, column=c, padx=10, pady=10)

    canvas.create_oval(5, 5, 75, 75, fill=color, outline=color)
    canvas.create_text(40, 40, text=text, fill="white",
                       font=("Arial", 16, "bold"))

    canvas.bind("<Button-1>", lambda e: cmd())

# Buttons layout
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('+',4,2), ('=',4,3),
]

# Create buttons
for (t, r, c) in buttons:
    if t == "=":
        round_btn(frame, t, equal, r, c, "#00cec9")
    else:
        round_btn(frame, t, lambda x=t: press(x), r, c, "#485460")

# Extra buttons
round_btn(frame, "C", clear, 5, 0, "#ff6b6b")
round_btn(frame, "√", root_fun, 5, 1, "#feca57")
round_btn(frame, "Enter", equal, 5, 2, "#00cec9")

win.mainloop()
