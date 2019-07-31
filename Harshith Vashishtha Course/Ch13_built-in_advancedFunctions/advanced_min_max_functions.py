names = ['hamza', 'khurram', 'musab']

#max() ->it gives name on basis on length 
print(max(names, key = lambda item : len(item)))

#min() ->it gives name on basis on length 
print(min(names, key = lambda item : len(item)))

students_dict = {     #dict inside dict
    'hamza' : {'score' : 10, 'age' : 22},
    'uzair' : { 'score' : 70, 'age' : 20},
    'khurram' : { 'score' : 40, 'age' : 20}
}
print(  max( students_dict, key = lambda item : students_dict[item]['score'] ) )# student[key][value]

students_lst = [      #dict inside list
    {'name' : 'hamza', 'score' : 10, 'age' : 22},
    {'name' : 'uzair', 'score' : 70, 'age' : 20},
    {'name' : 'khurram', 'score' : 40, 'age' : 20}
]
#high scored person name
print( max(students_lst, key = lambda a : a.get('score'))['name'] ) 
