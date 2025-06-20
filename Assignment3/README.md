# 🧮Factorial Calculator- Task 1

## 📋 Description

This Python program calculates the **factorial** of a given non-negative integer using a **recursive function**.

### 🧠 What is a Factorial?

The factorial of a number `n` (written as `n!`) is the product of all positive integers less than or equal to `n`.

Example:
- `5! = 5 × 4 × 3 × 2 × 1 = 120`
- `0! = 1` (by definition)

### 🔁 Logic

- The program defines a function `factorial(number)` that:
  - Returns `1` if `number < 2` (base case)
  - Otherwise, returns `number * factorial(number - 1)` (recursive call)
- It takes an integer input from the user.
- Calls the `factorial()` function and displays the result.

## 💬 Example
<img width="467" alt="t1" src="https://github.com/user-attachments/assets/6c7b2307-d921-4cd3-8568-c406ce746d21" />

⚠️ Note
Recursive calls can lead to stack overflow for very large inputs.
For large values, an iterative or math module-based approach is more efficient.


# 📐Math Operations using Python's `math` Module- Task 2

## 📋 Description

This Python program uses the built-in `math` module to perform three mathematical operations on a user-input number:

1. ✅ **Square Root**
2. ✅ **Natural Logarithm (base e)**
3. ✅ **Sine (in radians)**

### 🔍 Functionality

- **`math.sqrt(number)`**  
  Computes the **square root** of the input number.

- **`math.log(number)`**  
  Calculates the **natural logarithm** (log base `e`) of the input number.  
  ⚠️ Note: Input must be a positive number (> 0).

- **`math.sin(number)`**  
  Computes the **sine** of the input number (in **radians**).

## 💬 Example
<img width="483" alt="t2" src="https://github.com/user-attachments/assets/883ca61d-a148-4721-880d-5fda33434add" />

## ⚠️ Warnings

- The program will raise a **`ValueError`** if:
  - You input a **negative number** for `math.sqrt()`.
  - You input **zero or a negative number** for `math.log()`.

- The `math.sin()` function expects the input **in radians**, **not degrees**.
  - If you want to input degrees, convert it first using:
    ```python
    math.radians(degree_value)
    ```
