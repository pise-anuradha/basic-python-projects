<h1>Problem Statement</h1>
Design and implement a simple calculator program that allows users to perform basic arithmetic operations.

<h2>Solution</h2>
<h3>Approach :</h3>
The approach involves using Python to create a console-based calculator that can handle addition, subtraction, multiplication, and division operations based on user input.

<h2>Steps :</h2>

## Input Handling

- Prompt the user to enter two numbers and an arithmetic operator (+, -, *, /).
- Use Python's `input()` function to capture these inputs.

## Validation
- Ensure that the input for numbers are valid integers or floats, handling potential exceptions if non-numeric values are entered.

## Operation Selection

- Based on the operator input (+, -, *, /), perform the corresponding arithmetic operation:
  - Addition (+): Add the two numbers.
  - Subtraction (-): Subtract the second number from the first.
  - Multiplication (*): Multiply the two numbers.
  - Division (/): Divide the first number by the second (handle division by zero).

## Output

![image](https://github.com/pise-anuradha/simple-calculator/assets/167015021/2983948e-1eb7-4256-905d-cb07d75b43a8)


<h2>Solution Explanation :</h2>

## Input Handling:
The program starts by prompting the user to input two numbers and an operator. It uses input() function to capture these inputs as strings.

## Validation:
It checks if the input numbers can be converted to valid numerical values (integers or floats). If the input is not valid, it prompts the user to enter valid numbers.

## Operation Selection:
Based on the operator entered by the user, the program decides which arithmetic operation to perform using conditional statements (if, elif, else).

## Output:
After performing the calculation, the program prints the result to the console, ensuring it's formatted clearly for the user to understand.


