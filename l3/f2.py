# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
def is_good_movie(movie):
    return movie["imdb"] > 5.5
movie = {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"}
print(is_good_movie(movie))  
def filter_good_movies(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]
good_movies = filter_good_movies(movies)
for movie in good_movies:
    print(movie["name"])
def filter_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]
romance_movies = filter_by_category(movies, "Romance")
for movie in romance_movies:
    print(movie["name"])
def average_imdb(movies):
    total_imdb = sum(movie["imdb"] for movie in movies)
    return total_imdb / len(movies) if movies else 0
avg_imdb = average_imdb(movies)
print(avg_imdb)
def average_imdb_by_category(movies, category):
    category_movies = filter_by_category(movies, category)
    return average_imdb(category_movies)
avg_romance_imdb = average_imdb_by_category(movies, "Romance")
print(avg_romance_imdb)

