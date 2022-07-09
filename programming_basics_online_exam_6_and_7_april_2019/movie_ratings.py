import sys

number_of_movies = int(input())

max_rating = -sys.maxsize
min_rating = sys.maxsize
total_rating = 0
movie_with_max_rating = ''
movie_with_min_rating = ''

for movie in range(number_of_movies):
    current_movie = input()
    movie_rating = float(input())

    if movie_rating > max_rating:
        max_rating = movie_rating
        movie_with_max_rating = current_movie

    elif movie_rating < min_rating:
        min_rating = movie_rating
        movie_with_min_rating = current_movie

    total_rating += movie_rating

average_rating = total_rating / number_of_movies

print(f"{movie_with_max_rating} is with highest rating: {max_rating:.1f}")
print(f"{movie_with_min_rating} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")