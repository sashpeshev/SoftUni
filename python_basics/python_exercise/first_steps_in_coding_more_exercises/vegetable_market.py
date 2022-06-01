vegetables_price = float(input())
fruits_price = float(input())
kg_of_vegetables = int(input())
kg_of_fruits = int(input())
bgn_per_euro = 1.94

profit = (vegetables_price * kg_of_vegetables) + \
         (fruits_price * kg_of_fruits)
profit_in_euro = profit / 1.94

print(f"{profit_in_euro:.2f}")
