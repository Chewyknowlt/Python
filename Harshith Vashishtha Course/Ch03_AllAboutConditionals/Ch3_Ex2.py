# COCO watch movie
#Only name starts with 'a' and age is 10 and above
name, age = input("Enter name, age separated by  ' , ' ").split(',')
if (name.lower()[0] == 'a') and (int(age.strip()) >= 10) :  print("You can enjoy")
else :  print("Sorry!")