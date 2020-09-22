# Calculator

import tkinter as tk

HEIGHT = 400
WIDTH = 300


# Sets up GUI window
root = tk.Tk()
root.title("Calculator")
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH).pack()

# Label for the screen
screen = tk.Entry(root, font=('Courier',30), bd=5)
screen.place(relwidth=1, relheight=0.2)

# Inserts number onto screen
def insert(number):
    current = screen.get()
    screen.delete(0, len(screen.get()))
    screen.insert(0, int(str(current) + str(number)))

# Define operation functions
def add():
    global screen_num
    global operation
    screen_num = screen.get()
    operation = "add"
    screen.delete(0,len(screen.get()))

def sub():
    global screen_num
    global operation
    screen_num = screen.get()
    operation = "sub"
    screen.delete(0,len(screen.get()))
    
def div():
    global screen_num
    global operation
    screen_num = screen.get()
    operation = "div"
    screen.delete(0,len(screen.get()))
    
def mul():
    global screen_num
    global operation
    screen_num = screen.get()
    operation = "mul"
    screen.delete(0,len(screen.get()))

def equal():
    num = screen.get()
    screen.delete(0,len(screen.get()))

    if operation == "add":
        final_num = int(screen_num) + int(num)
        screen.insert(0,final_num)
    elif operation == "sub":
        final_num = int(screen_num) - int(num)
        screen.insert(0,final_num)
    elif operation == "div":
        final_num = int(screen_num) / int(num)
        screen.insert(0,final_num)
    elif operation == "mul":
        final_num = int(screen_num) * int(num)
        screen.insert(0,final_num)

def clear():
    screen.delete(0, len(screen.get()))

# Sets up the GUI for buttons
button_7 = tk.Button(root, text='7', font=('Courier',20), command=lambda: insert(7)).place(rely=0.2, relwidth=0.25, relheight=0.2)
button_8 = tk.Button(root, text='8', font=('Courier',20), command=lambda: insert(8)).place(relx=0.25, rely=0.2, relwidth=0.25, relheight=0.2)
button_9 = tk.Button(root, text='9', font=('Courier',20), command=lambda: insert(9)).place(relx=0.5, rely=0.2, relwidth=0.25, relheight=0.2)

button_4 = tk.Button(root, text='4', font=('Courier',20), command=lambda: insert(4)).place(rely=0.4, relwidth=0.25, relheight=0.2)
button_5 = tk.Button(root, text='5', font=('Courier',20), command=lambda: insert(5)).place(relx=0.25, rely=0.4, relwidth=0.25, relheight=0.2)
button_6 = tk.Button(root, text='6', font=('Courier',20), command=lambda: insert(6)).place(relx=0.5, rely=0.4, relwidth=0.25, relheight=0.2)

button_1 = tk.Button(root, text='1', font=('Courier',20), command=lambda: insert(1)).place(rely=0.6, relwidth=0.25, relheight=0.2)
button_2 = tk.Button(root, text='2', font=('Courier',20), command=lambda: insert(2)).place(relx=0.25, rely=0.6, relwidth=0.25, relheight=0.2)
button_3 = tk.Button(root, text='3', font=('Courier',20), command=lambda: insert(3)).place(relx=0.5, rely=0.6, relwidth=0.25, relheight=0.2)

button_0 = tk.Button(root, text='0', font=('Courier',20), command=lambda: insert(0)).place(relx=0.25, rely=0.8, relwidth=0.25, relheight=0.2)
button_clear = tk.Button(root, text='clear', font=('Courier',15), command=clear).place(rely=0.8,relwidth=0.25,relheight=0.2)
button_equal = tk.Button(root, text='=', font=('Courier',20), command=equal).place(relx=0.5, rely=0.8, relwidth=0.25, relheight=0.2)
 
button_add = tk.Button(root, text='+', fg='red', font=('Courier',20), command=add).place(relx=0.75, rely=0.2, relwidth=0.25, relheight=0.2)
button_sub = tk.Button(root, text='-', fg='red', font=('Courier',20), command=sub).place(relx=0.75, rely=0.4, relwidth=0.25, relheight=0.2)
button_div = tk.Button(root, text='/', fg='red', font=('Courier',20), command=div).place(relx=0.75, rely=0.6, relwidth=0.25, relheight=0.2)
button_mul = tk.Button(root, text='*', fg='red', font=('Courier',20), command=mul).place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.2)










































root.mainloop()
