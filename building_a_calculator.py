#float() / int() - To convert a string into a number
number1_from_user = float(input("Enter in your number: "))
operator_from_user = input("Enter operator: ")
number2_from_user = float(input("Enter in your second number: "))

if operator_from_user == "+" or operator_from_user == "add":
    print(number1_from_user + number2_from_user)
elif operator_from_user == "-" or operator_from_user == "subtract":
    print(number1_from_user - number2_from_user)
elif operator_from_user == "*" or operator_from_user == "multiply":
    print(number1_from_user * number2_from_user)
elif operator_from_user == "/" or operator_from_user == "divide":
    print(number1_from_user / number2_from_user)
else:
    print("===INVALID OPERATOR===")

