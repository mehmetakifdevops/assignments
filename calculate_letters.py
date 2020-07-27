sentence = input("enter a sentence: ")

sent_list = list(sentence)
x_dict = {}



for i in sent_list:
    a = sent_list.count(i)   
    my_dict = {i : a}
    x_dict.update(my_dict)
print(x_dict)
    