n = int(input())
salary = int(input())
tax = 0
for i in range(n):
    text = input()
    if text == "Facebook":
        tax += 150
    elif text == "Instagram":
        tax += 100
    elif text == "Reddit":
        tax += 50
    elif text == "":
        tax += 0
final = salary - tax
if salary <= tax:
    print("You have lost your salary.")
else:
    print(f"{final}")
