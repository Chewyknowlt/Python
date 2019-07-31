# [1,2,5,8] - [1,2,7,6] = [1, 2]

def common_element(list1, list2):
    empty = []
    for i in list1:
        if i in list2:
            empty.append(i)
    return empty

data1 = [1,2,5,8]
data2 = [1,2,7,6]
print(common_element(data1, data2))