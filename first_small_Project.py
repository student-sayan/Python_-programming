num_1 = float(input("Enter the first number = "))
num_2 = float(input("Enter the second number = "))

choice = input("Enter your choice ('+' / '-' / '*' / '/') = ")

if choice == "+":
    print(f'Addition: {num_1 + num_2}')

elif choice == "-":
    print(f'Subtraction: {num_1 - num_2}')

elif choice == "*":
    print(f'Multiplaction: {num_1 * num_2}')

elif choice == "/":
    print(f'Divition: {num_1 / num_2}')
    
else:
    print("Invalid rasult")
