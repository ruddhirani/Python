# 📄 Read a File and Handle Errors - Task 1

## 📋 Description

This Python program demonstrates how to **read the contents of a text file** and safely handle the case where the file may not exist.

It attempts to:
1. Open a file named `sample.txt` from the `Assignment4` folder.
2. Read all lines using `readlines()`.
3. Print the **two lines** from the file.

If the file is not found, it catches the `FileNotFoundError` and prints an appropriate error message.

---

### 🔁 Logic

- Uses a `try` block to attempt file access and reading.
- Uses an `except FileNotFoundError` block to catch missing file errors gracefully.

---

## 💬 Example 
- If the file exists: <br>
  <img width="480" alt="t1" src="https://github.com/user-attachments/assets/754408ee-d040-4352-8333-7cecfcd95e7a" />

- If the file does not exist: <br>
  <img width="476" alt="t1" src="https://github.com/user-attachments/assets/a0653896-93b3-48f4-93a9-07813c000b5f" />


## ⚠️ Notes

- Make sure the file path is correctly specified depending on your operating system.
  - For Windows: `Assignment4\\sample.txt` or `r"Assignment4\sample.txt"`
  - For Linux/Mac: `Assignment4/sample.txt`

- If fewer than two lines exist in the file, the script will raise an **IndexError**.
  


# 📝 Write and Append Data to a file - Task 2

## 📋 Description

This Python program demonstrates how to perform **file handling operations** including:

1. **Writing** user input to a new file (`output.txt`)
2. **Appending** additional input to the same file
3. **Reading** and displaying the first two lines of the file

All operations are performed on `output.txt` located in the `Assignment4` folder.

---

## 🔧 Functionality

### 1. Write to File
- Takes the first user input.
- Removes leading/trailing whitespace using `.strip()`.
- Writes it to `output.txt` using write (`"w"`) mode (overwrites if file already exists).

### 2. Append to File
- Takes the second user input.
- Appends it to the file using append (`"a"`) mode.

### 3. Read and Display
- Opens the file in read (`"r"`) mode.
- Reads all lines using `.readlines()`.
- Displays the **two lines** of the file.

---

## 💬 Example
<img width="478" alt="t2" src="https://github.com/user-attachments/assets/638fae7f-2890-43ab-ab48-fc602b87676b" />

## ⚠️ Notes
- The file is overwritten every time the script is run due to the use of `"w"` mode initially.
- Ensure `Assignment4` directory exists to avoid a `FileNotFoundError`.
- Here Only the **two lines** are printed.
- More content in the file will not be shown unless added and displayed using loop.
