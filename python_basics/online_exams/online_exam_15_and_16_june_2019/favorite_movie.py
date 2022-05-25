movie = input()

movie_counter = 0
favorite_movie = ""
favorite_ascii_sum = 0
flag = False

while movie != "STOP":
    movie_counter += 1
    if movie_counter == 7:
        flag = True
        break
    ascii_sum = 0
    for char in movie:
        int_value = ord(char)
        if int_value in range(65, 91):
            ascii_sum += int_value - len(movie)
        elif int_value in range(97, 123):
            ascii_sum += int_value - 2 * len(movie)
        else:
            ascii_sum += int_value
    if ascii_sum > favorite_ascii_sum:
        favorite_ascii_sum = ascii_sum
        favorite_movie = movie
    movie = input()

if flag:
    print("The limit is reached.")
print(f"The best movie for you is {favorite_movie} with {favorite_ascii_sum} ASCII sum.")
