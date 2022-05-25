movie = input()
days = int(input())
number_of_tickets = int(input())
ticket_price = float(input())
cinema_tax = int(input())

income = days * number_of_tickets * ticket_price
tax = income * cinema_tax / 100
total = income - tax

print(f"The profit from the movie {movie} is {total:.2f} lv.")
