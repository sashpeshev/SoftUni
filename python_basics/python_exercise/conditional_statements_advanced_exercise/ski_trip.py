days = int(input())
room_type = input()
rating = input()
nights_cost = 0
if room_type == "room for one person":
    if days < 10 or 10 <= days <= 15 or days > 15:
        if rating == "positive":
            nights_cost = ((days - 1) * 18) * 1.25
        elif rating == "negative":
            nights_cost = ((days-1) * 18) * 0.90
elif room_type == "apartment" and rating == "positive":
    if days < 10:
        nights_cost = ((days - 1) * 25) * 0.70 * 1.25
    elif 10 <= days <= 15:
        nights_cost = ((days - 1) * 25) * 0.65 * 1.25
    elif days > 15:
        nights_cost = ((days - 1) * 25) * 0.50 * 1.25
elif room_type == "apartment" and rating == "negative":
    if days < 10:
        nights_cost = ((days - 1) * 25) * 0.70 * 0.90
    elif 10 <= days <= 15:
        nights_cost = ((days - 1) * 25) * 0.65 * 0.90
    elif days > 15:
        nights_cost = ((days - 1) * 25) * 0.50 * 0.90
elif room_type == "president apartment" and rating == "positive":
    if days < 10:
        nights_cost = ((days - 1) * 35) * 0.90 * 1.25
    elif 10 <= days <= 15:
        nights_cost = ((days - 1) * 35) * 0.85 * 1.25
    elif days > 15:
        nights_cost = ((days - 1) * 35) * 0.80 * 1.25
elif room_type == "president apartment" and rating == "negative":
    if days < 10:
        nights_cost = ((days - 1) * 35) * 0.90 * 0.90
    elif 10 <= days <= 15:
        nights_cost = ((days - 1) * 35) * 0.85 * 0.90
    elif days > 15:
        nights_cost = ((days - 1) * 35) * 0.80 * 0.90

print(f"{nights_cost:.2f}")
