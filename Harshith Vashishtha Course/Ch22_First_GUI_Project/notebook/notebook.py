import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('TAB Control')

nb = ttk.Notebook(root)

pg1 = ttk.Frame(root)
pg2 = ttk.Frame(root)

nb.add(pg1, text='ONE')
nb.add(pg2, text='TWO')
nb.grid(row=0, column=0)
nb.pack(expand=True, fill='both')

label1 = ttk.Label(pg1, text="This's label: ").grid(row=0, column=0)
entry1 = ttk.Entry(pg1, width=15).grid(row=0, column=1)

root.mainloop()