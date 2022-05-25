hall_rent = int(input())

figurines_price = hall_rent * 0.70
catering_price = figurines_price * 0.85
sound_price = catering_price * 0.50
total_price = hall_rent + figurines_price\
              + catering_price + sound_price
print(f"{total_price:.2f}")
