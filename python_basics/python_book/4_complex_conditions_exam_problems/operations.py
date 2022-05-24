num1 = int(input())
num2 = int(input())
operator = input()

result = 0
output = ""

if num2 == 0 and (operator == "/" or operator == "%"):
    output = f"Cannot divide {num1} by zero"
elif operator == "/":
    result = num1 / num2
    output = f"{num1} {operator} {num2} = {result:.2f}"
elif operator == "%":
    result = num1 % num2
    output = f"{num1} % {num2} = {result}"
else:
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    if result % 2 == 0:
        output = f"{num1} {operator} {num2} = {result} - even"
    else:
        output = f"{num1} {operator} {num2} = {result} - odd"

print(output)
