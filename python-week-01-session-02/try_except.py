try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Can't divide by zero")

except ValueError:
    print("Invalid input")

finally:
    print("Program completed")
