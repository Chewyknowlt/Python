import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Logging Data')

# 1.   menubar -> as like Menu on top bar
#making 'File' sub menu downward
def menu(): print('menu called ')

main_menu = tk.Menu(root)
file_menu = tk.Menu(main_menu, tearoff=0)
file_menu.add_command(label='Show .txt', command=menu)
file_menu.add_command(label='Show .csv', command=menu)
file_menu.add_separator()
file_menu.add_command(label='Quit', command=menu)

# 'Tool' sub menu downward
tool_menu = tk.Menu(main_menu, tearoff=0)
tool_menu.add_command(label='About', command=menu)
#Adding to menu buttons to window
main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_cascade(label='Tools', menu=tool_menu)

root.config(menu=main_menu)

#  2.    Notebook/tab -> To switch page
#Making notebook/tab
nb = ttk.Notebook(root)
#Notebook pages -> signim, signup
signIn = ttk.Frame(root) 
signUp = ttk.Frame(root)
#adding  pages to notebook
nb.add(signIn, text='Sign In')
nb.add(signUp, text='Sign Up')  

nb.grid(row=0, column=0)
nb.pack(expand=True, fill='both')

#   3.   Frame -> Separate sections
#Frame for sign in
signInFrame = ttk.LabelFrame(signIn, text='Fill these fields: ')
signInFrame.grid(row=0, column=40)

#Frame for sign up
signUpFrame = ttk.LabelFrame(signUp, text='Fill these fields: ')
signUpFrame.grid(row=0, column=40)
 
#   4.   Labels -> user interaction text
#Labels for sign in frame
signIn_labels = (
  'Enter email: ',
  'Enter password: ',
  'Select user:'
)
for i in range(len(signIn_labels)):
  current_label = 'label' + str(i) #create variables in loop -> label0, labe1, etc
  current_label = ttk.Label(signInFrame, text=signIn_labels[i])
  current_label.grid(row=i, column=0, sticky=tk.W) 

#label for sign up
signUp_labels = (
  'First name: ',
  'Last name: ',
  'Email: ',
  'Password: ',
  'Age: ',
  'Select gender: ',
  'Select what you are: '
)
for i in range(len(signUp_labels)):
  current_label = 'label' + str(i) #create variables in loop -> label0, labe1, etc
  current_label = ttk.Label(signUpFrame, text=signUp_labels[i])
  current_label.grid(row=i, column=0, sticky=tk.W) 

#   5.  Entrybox -> eempty spaces for input

#entry box for signIn in  signInFrame
signIn_try = {
  'email' : tk.StringVar(),
  'password' : tk.StringVar(),
}
for counter, item in enumerate(signIn_try):
  current_entrybox= 'entry_' + str(item) #create variables in loop -> entry_name, entry_age
  current_entrybox = ttk.Entry(signInFrame, width=15, textvariable=signIn_try[item])
  current_entrybox.grid(row=counter, column=1)
  #focus of cursor
  current_entrybox.focus()

#entry box for signUp in signUpFrame
signUp_try = {
  'First name' : tk.StringVar(),
  'Last name' : tk.StringVar(),
  'Email' : tk.StringVar(),
  'Password' : tk.StringVar(),
  'Age' : tk.StringVar()
}
for counter, item in enumerate(signUp_try):
  current_entrybox= 'entry_' + str(item) #create variables in loop -> entry_name, entry_age
  current_entrybox = ttk.Entry(signUpFrame, width=15, textvariable=signUp_try[item])
  current_entrybox.grid(row=counter, column=1)
  #focus of cursor
  current_entrybox.focus()

#    6.   ComboBox  -> as like pop up menu
#comboBox -> gender 
signUp_try['gender'] = tk.StringVar()
gender_combobox = ttk.Combobox(signUpFrame, width=14, textvariable=signUp_try['gender'], state='readonly') # state='readonly -> choice to choose options 
gender_combobox['values'] = ('Male', 'Female', 'Others') #options to be choose
gender_combobox.current(0) #-> bydefault choose option of given index 
gender_combobox.grid(row=5, column=1)

#   7. Radio butttons  -> choose 1 option only 
#user type: student/teacher -> signInFrame
signIn_try['user'] = tk.StringVar() ##only 1 var to select 1 option
#Student
radio_signIn_1 = ttk.Radiobutton(signInFrame, text='User', value='Sudent', variable=signIn_try['user'])#select value pints variable sends to its input var 
radio_signIn_1.grid(row=4, column=0)
#Teacher
radio_signIn_2 = ttk.Radiobutton(signInFrame, text='Admin', value='Teacher', variable=signIn_try['user'])
radio_signIn_2.grid(row=4, column=1)

#user type: student/teacher -> signUpFrame
signUp_try['user'] = tk.StringVar() ##only 1 var to select 1 option
#Student
radio_signUp_1 = ttk.Radiobutton(signUpFrame, text='User', value='User', variable=signUp_try['user'])#select value pints variable sends to its input var 
radio_signUp_1.grid(row=7, column=0)
#Teacher
radio_signUp_2 = ttk.Radiobutton(signUpFrame, text='Admin', value='Admin', variable=signUp_try['user'])
radio_signUp_2.grid(row=7, column=1)

#    8.    check button   -> as like tick for term & cond.
# Terms&Conditions button -> signInFrame
signIn_try['terms'] = tk.IntVar() #uncheck -> zero bydefault else 1 for check
checkbtn = ttk.Checkbutton(signInFrame, text='Agee, with terms & conditiions.', variable=signIn_try['terms'])
checkbtn.grid(row=8, columnspan=2, sticky=tk.W) #columnspan can use given col withot disturbing others 

# Terms&Conditions check button -> signInFrame
signUp_try['terms'] = tk.IntVar() #uncheck -> zero bydefault else 1 for check
checkbtn = ttk.Checkbutton(signUpFrame, text='Agee, with terms & conditiions.', variable=signUp_try['terms'])
checkbtn.grid(row=8, columnspan=2, sticky=tk.W) #columnspan can use given col withot disturbing others 

#    9. Submit button -> to response final button
#submit button-> sign in 
def sign_in():
  lst = [value.get() for value in signIn_try.values()]
  for i in lst: print(i)
  if signIn_try['user'].get() == 0:
    subscribed = 'No'
  else:
    subscribed = 'Yes'
 
  # with open('file.txt', 'a') as f: #data write
  #   f.write(f'\n{user_name},{user_email},{user_age},{user_type},{user_gender},{subscribed}')
  
  # #reset entry boxes
  # name_entrybox.delete(0, tk.END)
  # email_entrybox.delete(0, tk.END)
  # name_label.configure(foreground='#73c2f0') # label color -> yellow, green, cyan, red,etc
  # submit_button.configure(foreground='Blue')

signInButton = ttk.Button(signInFrame, text='Sign In', command=sign_in)
signInButton.grid(row= 9, columnspan=2)

#submit button-> sign up
def sign_up():
  lst = [str(value.get()) for value in signUp_try.values()]
  for i in lst: print(i)
  if signUp_try['user'].get() == 0:
    subscribed = 'No'
  else:
    subscribed = 'Yes'
  with open('signUp.txt', 'a') as f: #data write
    f.write(f'\n{lst[0]},{lst[1]},{lst[2]},{lst[3]},{lst[4]},{lst[5]},{lst[6]},{lst[7]}')
  
  # #reset entry boxes
  # name_entrybox.delete(0, tk.END)
  # email_entrybox.delete(0, tk.END)
  # name_label.configure(foreground='#73c2f0') # label color -> yellow, green, cyan, red,etc
  # submit_button.configure(foreground='Blue')
  #  
signUpButton = ttk.Button(signUpFrame,text='Sign Up', command=sign_up)
signUpButton.grid(row= 9, columnspan=2)

#    10. padding -> for spaces 
for child1, child2 in zip(signInFrame.winfo_children(), signUpFrame.winfo_children()):# method took out list of widgets used in the abovee code
  child1.grid_configure(padx=5, pady=2)#e.g; widgets-> labels, entryBox, submit buttns > .grid(row, col, paadx, pady)
  child2.grid_configure(padx=5, pady=2)#e.g; widgets-> labels, entryBox, submit buttns > .grid(row, col, paadx, pady)

root.mainloop()