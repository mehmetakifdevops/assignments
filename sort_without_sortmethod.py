elements_of_list = [999, 333, 2, 8982, 12, 45, 77, 99, 11]
list2 = []


while elements_of_list != []:   
    a = min(elements_of_list)
    list2.append(a)
    elements_of_list.remove(a)
    
print(list2)
            