number = int(input("enter a integer to chech whether it's prime number or not: "))


if 2 ** number % number == 2 or number == 2:
    print(number ,"is a prime number")
else:
    print(number, "is not a prime number")