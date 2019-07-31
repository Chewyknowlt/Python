import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os

root = tk.Tk()
root.title('Interface')

#labels
#name
name_label = ttk.Label(root, text='Enter your name: ') # 1st arg-> pasting area, 2nd arg->text to be paste
name_label.grid(row=0, column=0, sticky=tk.W) #grid(row, col) -> postion
#email
email_label = ttk.Label(root, text='Enter ypur E-mail: ')
email_label.grid(row=1, column=0, sticky=tk.W) #sticky = tk.W ->responsive
# age 
age_label = ttk.Label(root, text='Enter your age: ')
age_label.grid(row=2, column=0, sticky=tk.W)
# gender 
gender_label = ttk.Label(root, text='Select your gender: ')
gender_label.grid(row=3, column=0, sticky=tk.W)

#empty box -> for input
#name
name_var = tk.StringVar() 
name_entrybox = ttk.Entry(root, width=16, textvariable=name_var)  #1st arg-> pasting area, 2nd arg->area of box
name_entrybox.grid(row=0, column=1)
name_entrybox.focus() # points cursor when windows open 
#email
email_var = tk.StringVar() #input variable
email_entrybox = ttk.Entry(root, width=16, textvariable=email_var) #3rd arg-> data pointed to input variable
email_entrybox.grid(row=1, column=1)
#name
age_var = tk.StringVar()  
age_entrybox = ttk.Entry(root, width=16, textvariable=age_var)
age_entrybox.grid(row=2, column=1)

#combo box 
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(root, width=14, textvariable=gender_var, state='readonly') # state='readonly -> choice to choose options 
gender_combobox['values'] = ('Male', 'Female', 'Others') #options to be choose
gender_combobox.current(0) #-> bydefault choose option of given index 
gender_combobox.grid(row=3, column=1)

#radio buttons -> student/teacher
userType_var = tk.StringVar() #only 1 var to select 1 option
radiobtn1 = ttk.Radiobutton(root, text='Student', value='Sudent', variable=userType_var)#select value pints variable sends to its input var 
radiobtn1.grid(row=4, column=0)
#Teacher
radiobtn2 = ttk.Radiobutton(root, text='Teacher', value='Teacher', variable=userType_var)
radiobtn2.grid(row=4, column=1)

#check button
checkbtn_var = tk.IntVar() #uncheck -> zero bydefault else 1 for check
checkbtn = ttk.Checkbutton(root, text='Select this butto if you agree otherwise.', variable=checkbtn_var)
checkbtn.grid(row=5, columnspan=2) #columnspan can use given col withot disturbing others 

# #button
# def txt():
#   user_name = name_var.get()
#   user_age = age_var.get()
#   user_email = email_var.get()
#   user_gender = gender_var.get()
#   user_type = userType_var.get()
#   if checkbtn_var.get() == 0:
#     subscribed = 'No'
#   else:
#     subscribed = 'Yes'
#   print(f'{user_name} {user_age} {user_email}')
#   print(f'{user_gender} {user_type} {subscribed}')

#   with open('file.txt', 'a') as f: #data write
#     f.write(f'\n{user_name},{user_email},{user_age},{user_type},{user_gender},{subscribed}')
  
#   #reset entry boxes
#   name_entrybox.delete(0, tk.END)
#   age_entrybox.delete(0, tk.END)
#   email_entrybox.delete(0, tk.END)
#   name_label.configure(foreground='#73c2f0') # label color -> yellow, green, cyan, red,etc
#   # submit_button.configure(foreground='Blue')

#button
def csv():
  user_name = name_var.get()
  user_age = age_var.get()
  user_email = email_var.get()
  user_type = userType_var.get()
  user_gender = gender_var.get()
  if checkbtn_var.get() == 0:
    subscribed = 'No'
  else:
    subscribed = 'Yes'
  with open('file.csv', 'a', newline='') as f:
    dict_writer = DictWriter(f, fieldnames=['Name', 'Email', 'Age', 'Gender', 'User Type', 'Subscribed'])
    if os.stat('file.csv').st_size == 0: # Check csv is empty or not to write header
      dict_writer.writeheader()

    dict_writer.writerow({
      'Name' : user_name,
      'Email' : user_email,
      'Age' : user_age,
      'Gender' : user_gender,
      'User Type' :  user_type,
      'Subscribed' : subscribed
    })

    #reset entry boxes
    name_entrybox.delete(0, tk.END)
    age_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)
    submit_button.configure(foreground='Blue')
      
#reset entry boxes
name_entrybox.delete(0, tk.END)
age_entrybox.delete(0, tk.END)
email_entrybox.delete(0, tk.END)
submit_button = tk.Button(root, text='submit', command=csv) # command to respones what to in above f() 
submit_button.grid(row=6, column=1) 
root.mainloop() # tends to open until user close it