import calculator

# Llamando a la función basic_operations directamente
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
results = calculator.basic_operations(num1, num2)

print(f"The sum of {num1} and {num2} is: {results[0]}")
print(f"The subtraction of {num1} and {num2} is: {results[1]}")
print(f"The multiplication of {num1} and {num2} is: {results[2]}")
print(f"The division of {num1} and {num2} is: {results[3]}")

# Llamando a la función main
calculator.main()


