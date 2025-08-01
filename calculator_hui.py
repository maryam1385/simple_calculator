import tkinter as tk


def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)


def calculate():
    try:
        result = eval(entry.get()) 
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


def clear():
    entry.delete(0, tk.END)
    
root = tk.Tk()
root.title("Calculator")


entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="ridge", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', 'C', '+'
]


row_val = 1
col_val = 0
for button in buttons:
    action = lambda x=button: click_button(x) if x != 'C' else clear()
    tk.Button(root, text=button, width=5, height=2, font=('Arial', 18), command=action).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1


equals_button = tk.Button(root, text='=', width=22, height=2, font=('Arial', 18), command=calculate)
equals_button.grid(row=row_val, column=0, columnspan=4, pady=10)

root.mainloop()
