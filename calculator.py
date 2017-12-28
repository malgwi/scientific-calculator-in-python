# A simple calculator
 
while True:
    print('****OPTIONS****')
    print("Enter '+' to add two numbers.")
    print("Enter '-' to subtract two numbers.")
    print("Enter '*' to multiply two numbers.")
    print("Enter '/' to divid two numbers.")
    print("Else enter 'EXIT' to end program")
    user_input=input("")
 
    if user_input == "EXIT":
        break
    elif user_input == "+":
        num1 = float(input('Enter first number'))
        num2 = float(input('Enter the other number'))
        result = str(num1+num2)
        print('The answer is: '+result)
        break
    elif user_input == "-":
        num1 = float(input('Enter first number'))
        num2 = float(input('Enter the other number'))
        result = str(num1-num2)
        print('The answer is: '+result)
        break
    elif user_input == "*":
        num1 = float(input('Enter first number'))
        num2 = float(input('Enter the other number'))
        result = str(num1*num2)
        print('The answer is: '+result)
        break
    elif user_input == "/":
        num1 = float(input('Enter first number'))
        num2 = float(input('Enter the other number'))
        result = str(num1/num2)
        print('The answer is: '+result)
        break
    else:
        print("Unknown input")
        break
 
print("\n\n Powered by Santos")
