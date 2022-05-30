screening_type = input().lower()
rows = int(input())
columns = int(input())

income = 0
capacity = rows * columns

if screening_type == "premiere":
    income = capacity * 12.00
elif screening_type == "normal":
    income = capacity * 7.50
elif screening_type == "discount":
    income = capacity * 5.00
print(f"{income:.2f} leva")
