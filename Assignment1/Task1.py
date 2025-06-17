first_number = int(input("Enter the First Number: "))
second_number = int(input("Enter the Second Number: "))
addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number / \
    second_number if second_number != 0 else "Undefined (cannot divide by zero)"

print("\nAddition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
