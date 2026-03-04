# Movie dataset
movies = [
    {"name": "Avengers", "genre": "Action"},
    {"name": "Batman", "genre": "Action"},
    {"name": "Titanic", "genre": "Romance"},
    {"name": "Notebook", "genre": "Romance"},
    {"name": "Conjuring", "genre": "Horror"},
    {"name": "Insidious", "genre": "Horror"}
]

print("Movie Recommendation System")
user_genre = input("Enter your favorite genre (Action/Romance/Horror): ")

print("\nRecommended Movies:")

for movie in movies:
    if movie["genre"].lower() == user_genre.lower():
        print("-", 
  #output
              Movie Recommendation System
Enter your favorite genre: Action

Recommended Movies:
- Avengers
- Batman
