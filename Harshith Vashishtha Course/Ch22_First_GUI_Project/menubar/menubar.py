import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title('Menubar tutorial')

def func():
    print('func called ')

main_menu = tk.Menu(root)
file_menu = tk.Menu(main_menu, tearoff=0)
file_menu.add_command(label='New File', command=func)
file_menu.add_command(label='New Window', command=func)
file_menu.add_separator()
file_menu.add_command(label='Save File', command=func)

## edit menu
edit_menu = tk.Menu(main_menu, tearoff=0)
edit_menu.add_command(label='Undo', command=func)
edit_menu.add_command(label='Redo', command=func)

main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_cascade(label='Edit', menu=edit_menu)


root.config(menu=main_menu)

root.mainloop()