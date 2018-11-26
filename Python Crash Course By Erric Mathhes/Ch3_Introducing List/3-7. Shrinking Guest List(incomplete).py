print('3-7. Shrinking Guest List')

person = ['Uzair','Irteza','Kaleem']
persons =['Uzair','Irteza','Kaleem']
#Invitation & we have only 2 seats.
print(person[0] + ' ' + "We are inviting you for dinner & gracious for us.")
print(person[1] + ' ' + "We are inviting you for dinner & gracious for us.")
print(person[-1] + ' ' + "We are inviting you for dinner & gracious for us.")
print('I can invite only two people for dinner.')

#Use pop() to remove guest. 
print(person.pop(-1)+ ' ' +"Sorry I can't invite you")
print(person.pop(-2)+ ' ' +"Sorry I can't invite you")

#Reinstating invitation.
print(persons)




      

