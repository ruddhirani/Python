try:
    print("Reading file content: ")
    with open("Assignment4\sample.txt", "r") as file:
        reading_file = file.readlines()
        print("Line 1:", reading_file[0])
        print("Line 2:", reading_file[1])

except FileNotFoundError:
    print('Error: The file "sample.txt" is not found.')
