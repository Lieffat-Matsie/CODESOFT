# Heading of the app
print("Calculator")
print("-----------------------------------------")

# let the user choose which operator they want to use
print("1 -- Subtract")
print("2 -- Multiply")
print("3 -- Divide")
print("4 -- Add")
choice = int(input("Chose an operator: "))
result = 0

# checks which operation is chosen
if choice in [1,2,3,4]:
    num1 = int(input("Input first number: "))
    num2 = int(input("Input second number: "))

    if choice == 1:
        result = num1 - num2
    elif choice == 2:
        result = num1 * num2
    elif choice == 3:
        result = num1 / num2
    elif choice == 4:
        result = num1 + num2
else:
    print("Operator Unknown! Please chose valid operator")
  
# this prints the results of your chosen operation
print("Your answer is {}".format(result))
