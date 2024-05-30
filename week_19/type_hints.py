```
Consider the following code (also available on Moodle):
  # Date, Running time, Release
  movie_db = [
    ("Holy Grail", 1.52, 1975),
    ("Completely Different", 1.5, 1971),
    ("Life of Brian", 1.57, 1979),
    ("A Space Odyssey", 2.32, 1968),
    ("Dr. Strangelove", 1.57, 1964)
  ]
  # Hint: Write "Movie = tuple[...]" to define a type alias
  
  def find_movies(name, movies):
    matched = []
    for movie in movies:
      if name in movie[0]:
        matched.append(movie)
    return matched
  
  def by_name(movies):
    return {m[0]: m for m in movies}
  
  def minutes(movie):
    return movie[0] * 60
  
  def show(movies):
    for name, hours, year in movies:
      print(f"{name} ({year}), running {int(hours * 60)} min")
  
  # Get all movies that contain given string in their title
  filtered = find_movies("a", movie_db)
  # Find the longest of these movies
  longest = max(filtered, key=minutes)
  # Display it
  show(longest)

Try to understand this code. Add typing hints to each of the functions (both to each argument and return
types). Remember: Write variable: int to indicate that the variable should be of type int and def
function(...) -> int: to indicate a function returns int. Do you see anything that is used incorrectly?
Try to fix the issues and then run the code to see whether everything is as it should be.
Hint: Replace searching for Dr. by searching for a.
Try to use generic types where appropriate (e.g. Iterable instead of list) etc.
In case you want to verify that your type annotations match usage, you can use mypy. Install it with pip
install mypy (as usual, using a venv), and run pypy program.py. This will print any problems.
```
                                            
from typing import Iterable

Movie = tuple[str, float, int]

# Date, Running time, Release
movie_db: list[Movie] = [
  ("Holy Grail", 1.52, 1975),
  ("Completely Different", 1.5, 1971),
  ("Life of Brian", 1.57, 1979),
  ("A Space Odyssey", 2.32, 1968),
  ("Dr. Strangelove", 1.57, 1964),
]

def find_movies(name: str, movies: Iterable[Movie]) -> list[Movie]:
  matched = []
  for movie in movies:
    if name in movie[0]:
      matched.append(movie)
  return matched
         
def by_name(movies: Iterable[Movie]) -> dict[str, Movie]:
  return {m[0]: m for m in movies}

def minutes(movie: Movie) -> int:
  return int(movie[1] * 60)
                                            
def show(movies: Iterable[Movie]) -> None:
  for name, hours, year in movies:
    print(f"{name} ({year}), running {int(hours * 60)} min")

# Get all movies that contain given string in their title
filtered = find_movies("a", movie_db)
# Find the longest of these movies
longest = max(filtered, key=minutes)
# Display it
show([longest])
