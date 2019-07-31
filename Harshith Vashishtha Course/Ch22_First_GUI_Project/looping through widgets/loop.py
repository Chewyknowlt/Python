import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Loop')

#Labels
labels = (
  'Enter name: ',
  'Enter age: ',
  'Enter gender: ',
  'Enter country: ',
  'Enter state: ',
  'Enter city: '
)

for i in range(len(labels)):
  current_label = 'label' + str(i) #create variables in loop -> label0, labe1, etc 
  current_label = ttk.Label(root, text=labels[i])
  current_label.grid(row=i, column=0, sticky=tk.W, padx=2, pady=2) 

#entry box
user_info = {
  'name' : tk.StringVar(),
  'age' : tk.StringVar(),
  'gender' : tk.StringVar(),
  'country' : tk.StringVar(),
  'state' : tk.StringVar(),
  'city' : tk.StringVar(),
}

for counter, item in enumerate(user_info):
  current_entrybox= 'entry_' + str(item) #create variables in loop ->_entry_name, entry_age
  current_entrybox = ttk.Entry(root, width=15, textvariable=user_info[item])
  current_entrybox.grid(row=counter, column=1, padx=2, pady=2)

#submit_btn
def submit():
  for value in user_info.values():
    print(value.get())
    
submit_btn = tk.Button(root, text='Submit', command=submit)
submit_btn.grid(row=6, columnspan=2)

root.mainloop()

