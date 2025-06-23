user_input1 = input("Enter text to write to the file: ")
with open("Assignment4\\output.txt", "w") as file:
    file.write(user_input1.strip() + '\n')
    print("Data successfully written to output.txt.")

user_input2 = input("\nEnter additional text to append: ")
with open("Assignment4\\output.txt", "a") as file1:
    file1.write(user_input2.strip())
    print("Data successfully appended.")

print("\nFinal content of output.txt: ")
with open("Assignment4\\output.txt", "r") as file2:
    reading_file = file2.readlines()
    print(reading_file[0], end='')
    print(reading_file[1])
