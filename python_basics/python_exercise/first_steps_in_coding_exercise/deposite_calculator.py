deposit = float(input())
months = int(input())
interest_rate = float(input())

annual_interest = deposit * interest_rate / 100
monthly_interest = annual_interest / 12
total_sum = deposit + months * monthly_interest
print(total_sum)
