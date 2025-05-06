# find the frequency of the given digit in a given number

def freq():
    n = 0
    x = 0
    count = 0
    rem = 0
    n = int(input("Enter a number = "))
    x = int(input("Enter a digit = "))

    while n!=0:
        rem = n % 10
        if(rem == x):
            count+1
        n = n / 10
    print("Count = ",count)

freq()