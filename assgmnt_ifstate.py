name = input("What is your name: ").title().strip()



if name == "Joseph":

    message = ("Hello, {}! The password is : W@12".format(name))

else:

    message = ("Hello, {}! See you later".format(name))

print(message)