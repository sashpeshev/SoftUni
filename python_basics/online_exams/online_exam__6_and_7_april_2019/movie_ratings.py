number_of_movies = int(input())

max_rating = 0
best_movie = ""
min_rating = 10.00
worst_movie = ""
ratings_sum = 0

for i in range(number_of_movies):
    movie = input()
    rating = float(input())
    ratings_sum += rating
    if rating > max_rating:
        max_rating = rating
        best_movie = movie
    elif rating < min_rating:
        min_rating = rating
        worst_movie = movie

average_rating = ratings_sum / number_of_movies

print(f"{best_movie} is with highest rating: {max_rating:.1f}")
print(f"{worst_movie} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
