money = float(input())
currency_in = input()
currency_out = input()

bgn = 1
usd = 1.79549
eur = 1.95583
gbp = 2.53405
result = 0

if currency_in == "BGN":
    currency_in = bgn
elif currency_in == "USD":
    currency_in = usd
elif currency_in == "EUR":
    currency_in = eur
elif currency_in == "GBP":
    currency_in = gbp

if currency_out == "BGN":
    result = money * currency_in / bgn
elif currency_out == "USD":
    result = money * currency_in / usd
elif currency_out == "EUR":
    result = money * currency_in / eur
elif currency_out == "GBP":
    result = money * currency_in / gbp

print(f"{result:.2f} {currency_out}")
