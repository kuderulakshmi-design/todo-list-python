print("Simple Calculator")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter your choice: ")

if choice == "1":
    print("Answer:", num1 + num2)

elif choice == "2":
    print("Answer:", num1 - num2)

elif choice == "3":
    print("Answer:", num1 * num2)

elif choice == "4":
    print("Answer:", num1 / num2)

else:
    print("Invalid choice")
