fruit = input()
package = input()
number_of_package = int(input())
price = 0

if package == "small":
    if fruit == "Watermelon":
        price = 56
    elif fruit == "Mango":
        price = 36.66
    elif fruit == "Pineapple":
        price = 42.10
    elif fruit == "Raspberry":
        price = 20
    price *= 2
elif package == "big":
    if fruit == "Watermelon":
        price = 28.70
    elif fruit == "Mango":
        price = 19.60
    elif fruit == "Pineapple":
        price = 24.80
    elif fruit == "Raspberry":
        price = 15.20
    price *= 5

price *= number_of_package

if 400 <= price <= 1000:
    price *= 0.85
elif price > 1000:
    price *= 0.50

print(f"{price:.2f} lv.")
