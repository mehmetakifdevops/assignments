while True:
    number = input(
        "Please enter a number to check if it's an Armstrong Number : ")
    len_num = len(number)
    list_num = list(number)
    armstrong_aa = 0

    if  not number.isdigit() or number.isalpha():
        print("Just integer number please: ")
    else:
        for i in list_num:
            armstrong_aa += int(i) ** len_num                
        if int(number) == armstrong_aa:
            print(armstrong_aa, "is a Armstrong Number")
            break
        else:
            print(int(number), "isn't a Armstrong Number", "because the total number is", armstrong_aa)
            break                               
            