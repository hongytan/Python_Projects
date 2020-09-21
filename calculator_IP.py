# Calculator

import tkinter as tk

# Defines functions
def add():
    

# Sets up GUI window
root = tk.Tk()
root.title("Calculator")
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH).pack()

# Label for the screen
screen = tk.Label(root, bg = 'black').place(relwidth=1, relheight=0.2)

# Sets up the GUI for buttons
button_7 = tk.Button(root, text='7').place(rely=0.2, relwidth=0.25, relheight=0.2)
button_8 = tk.Button(root, text='8').place(relx=0.25, rely=0.2, relwidth=0.25, relheight=0.2)
button_9 = tk.Button(root, text='8').place(relx=0.5, rely=0.2, relwidth=0.25, relheight=0.2)

button_4 = tk.Button(root, text='4').place(rely=0.4, relwidth=0.25, relheight=0.2)
button_5 = tk.Button(root, text='5').place(relx=0.25, rely=0.4, relwidth=0.25, relheight=0.2)
button_6 = tk.Button(root, text='6').place(relx=0.5, rely=0.4, relwidth=0.25, relheight=0.2)

button_1 = tk.Button(root, text='1').place(rely=0.6, relwidth=0.25, relheight=0.2)
button_2 = tk.Button(root, text='2').place(relx=0.25, rely=0.6, relwidth=0.25, relheight=0.2)
button_3 = tk.Button(root, text='3').place(relx=0.5, rely=0.6, relwidth=0.25, relheight=0.2)

button_0 = tk.Button(root, text='0').place(rely=0.8, relwidth=0.5, relheight=0.2)

button_equal = tk.Button(root, text='=').place(relx=0.5, rely=0.8, relwidth=0.25, relheight=0.2)
 
button_add = tk.Button(root, text='+', command=add).place(relx=0.75, rely=0.2, relwidth=0.25, relheight=0.2)
button_sub = tk.Button(root, text='-', command=sub).place(relx=0.75, rely=0.4, relwidth=0.25, relheight=0.2)
button_div = tk.Button(root, text='/', command=div).place(relx=0.75, rely=0.6, relwidth=0.25, relheight=0.2)
button_mul = tk.Button(root, text='*', command=mul).place(relx=0.75, rely=0.8, relwidth=0.25, relheight=0.2)



root.mainloop()
