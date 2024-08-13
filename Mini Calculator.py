print(" Mini Calculator")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Press 1 for addition \n Press 2 for subtraction \n Press 3 for multiplication \n Press 4 for division \n Press 5 for modulus ")

choice = int(input("Enter your choice: "))

if choice == 1:
    print(" The addition of given number is ", num1 + num2)
elif choice == 2:
    print(" The subtraction of given number is", num1 - num2)
elif choice == 3:
    print("The multiplication of given number is", num1 * num2)
elif choice == 4:
    print("The division of input number is", num1 / num2)
elif choice == 5:
    print("The modulus of given number is", num1 % num2)
else:
    print("Invalid input ")

