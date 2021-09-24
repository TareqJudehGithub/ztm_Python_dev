"""
difflib built-in module
"""

# difflib allows us to compare matching strings
import difflib

match_my_word = difflib.get_close_matches(
  word="rain",
  possibilities=[
    "rain",
    "train",
    "money",
    "man",
    "brain"
    ]
  )
# match_my_word = difflib.get_close_matches("hello", "yellow")
print(match_my_word)
