heritage = float(input())
year = int(input())
age_counter = 18
for year in range(1800, year + 1):
    if year % 2 == 0:
        heritage -= 12000
    else:
        heritage -= 12000 + age_counter * 50
    age_counter += 1

print(f"Yes! He will live a carefree life and will have {heritage:.2f} dollars left.") \
    if heritage >= 0 \
    else print(f"He will need {abs(heritage):.2f} dollars to survive.")
