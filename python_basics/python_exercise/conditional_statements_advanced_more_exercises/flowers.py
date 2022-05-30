chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
its_holiday = input()
bouquet_arrangement = 2

flowers_price = 0
if season == "Summer" or season == "Spring":
    chrysanthemum_price = 2.00
    rose_price = 4.10
    tulip_price = 2.50
    flowers_price = chrysanthemum_price * chrysanthemums + rose_price * roses + tulip_price * tulips
    if its_holiday == "Y":
        increase_in_price = flowers_price * 0.15
        flowers_price += increase_in_price
    if season == "Spring" and tulips > 7:
        discount = flowers_price * 0.05
        flowers_price -= discount
elif season == "Autumn" or season == "Winter":
    chrysanthemum_price = 3.75
    rose_price = 4.50
    tulip_price = 4.15
    flowers_price = chrysanthemum_price * chrysanthemums + rose_price * roses + tulip_price * tulips
    if its_holiday == "Y":
        increase_in_price = flowers_price * 0.15
        flowers_price += increase_in_price
    if season == "Winter" and roses >= 10:
        discount = flowers_price * 0.10
        flowers_price -= discount
if chrysanthemums + roses + tulips > 20:
    discount = flowers_price * 0.20
    flowers_price -= discount
flowers_price = flowers_price + bouquet_arrangement
print(f"{flowers_price:.2f}")
