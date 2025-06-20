def factorial(number: int) -> int:
    if number < 2:
        return 1
    return number * factorial(number-1)


number = int(input("Enter a number: "))
result = factorial(number)
print(f"Factorial of {number} is:", result)
