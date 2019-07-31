# count list in list

def sublist_counter(lst):
    counter = 0
    for i in lst:
        if type(i) == list: counter += 1
    return counter

multi_lst_data = [1 ,2, 3,[1, 2], [3, 4]]
print(sublist_counter(multi_lst_data))