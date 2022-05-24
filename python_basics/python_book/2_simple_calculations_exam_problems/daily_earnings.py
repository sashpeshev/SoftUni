working_days_in_mount = int(input())
wage = float(input())
usd_to_bgn = float(input())

monthly_salary = working_days_in_mount * wage
bonus = 2.5 * monthly_salary
annual_earnings = monthly_salary * 12 + bonus
taxes = annual_earnings * 0.25
net_annual_earnings = annual_earnings - taxes
annual_earnings_in_bgn = net_annual_earnings * usd_to_bgn
net_wage_in_bgn = annual_earnings_in_bgn / 365

print(f"{net_wage_in_bgn:.2f}")
