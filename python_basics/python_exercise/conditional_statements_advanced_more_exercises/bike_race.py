juniors = int(input())
seniors = int(input())
road_type = input()

charity_fund = 0

if road_type == "trail":
    juniors_tax = juniors * 5.50
    seniors_tax = seniors * 7
    charity_fund += juniors_tax + seniors_tax
elif road_type == "cross-country":
    juniors_tax = juniors * 8
    seniors_tax = seniors * 9.50
    charity_fund += juniors_tax + seniors_tax
elif road_type == "downhill":
    juniors_tax = juniors * 12.25
    seniors_tax = seniors * 13.75
    charity_fund += juniors_tax + seniors_tax
elif road_type == "road":
    juniors_tax = juniors * 20
    seniors_tax = seniors * 21.50
    charity_fund += juniors_tax + seniors_tax
if juniors + seniors >= 50:
    charity_fund -= charity_fund * 0.25

expenses = charity_fund * 0.05
charity_fund = charity_fund - expenses
print(f"{charity_fund:.2f}")
