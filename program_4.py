# program to find if it is prime number or not using functions

def prime_num():
    a = 2
    num = 0
    temp = 0
    num = int(input("Enter the number to find if it is prime number or not = "))
    while a < num/2:
        if num % a == 0:
            temp+1
            a+1
    if temp == 0 and num != 1:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

prime_num()