import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Laebel Frame')

label_frame = ttk.LabelFrame(root, text='Enter details below: ')
label_frame.grid(row=0, column=40)

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
  current_label = ttk.Label(label_frame, text=labels[i])
  current_label.grid(row=i, column=0, sticky=tk.W) 

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
  current_entrybox = ttk.Entry(label_frame, width=15, textvariable=user_info[item])
  current_entrybox.grid(row=counter, column=1)

#submit_btn
def submit():
  for value in user_info.values():
    print(value.get())
    
submit_btn = ttk.Button(label_frame, text='Submit', command=submit)
submit_btn.grid(row=6, columnspan=2)

#padding for spacing in pixels 
for child in label_frame.winfo_children():# method took out list of widgets used in the abovee code
  child.grid_configure(padx=2, pady=2)#e.g; widgets-> labels, entryBox, submit buttns > .grid(row, col, paadx, pady)

root.mainloop()