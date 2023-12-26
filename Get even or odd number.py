def num():
    input_num = int(input("Please enter the number \n"))
    if input_num % 2 == 0:
        return "Entered number is even"
    else:
        return "Entered number is odd"

def greet():
    return "Hello, \nThis is the program to check whether the entered number is even or odd."
print(greet())
print(num())    