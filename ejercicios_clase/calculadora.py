def basic_operations(num1, num2):
    sum = num1 + num2
    subtract = num1 - num2
    multiply = num1 * num2
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Cannot divide by zero"
    return sum, subtract, multiply, division

   

def main():

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    results = basic_operations(num1, num2)
    
    print(f"The sum of {num1} and {num2} is: {results[0]}")
    print(f"The subtraction of {num1} and {num2} is: {results[1]}")
    print(f"The multiplication of {num1} and {num2} is: {results[2]}")
    print(f"The division of {num1} and {num2} is: {results[3]}")

if __name__ == "__main__":
    main()
