
while True:
    first_number = input("Enter first number")
    if first_number == "quit":
        print("Exit the program")
        break
    second_number = input("Enter second number")
    if second_number == "quit":
        print("Exit the program")
        break
    operator = input("Enter mathematical operator")
    if operator == "quit":
        print("Exit the program")
        break
    elif operator == '+':
        print(int(first_number) + int(second_number))
    elif operator == '-':
        print(int(first_number) - int(second_number))
    elif operator == '*':
        print(int(first_number) * int(second_number))
    elif int(second_number) == 0 and operator == '/':
        print("Second_number can't equal zero ")
    elif operator == '/':
        print(int(first_number) / int(second_number))
    elif operator == '%':
        print(int(first_number) % int(second_number))




