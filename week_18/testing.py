```
In this exercise, we want to test functions using pytest. First, we need to install this library. Thus,
create a virtual environment (python -m venv venv), activate it (. ./venv/bin/activate) and install
pytest (pip install pytest). (You can also skip the virtual environment step.)
Now, create a file main.py that contains code we want to test. For now, create a function vowels which
takes a string and returns the set of all vowels that appear in it. For example, for vowels("aabbee"), we should get {"a", "e"}.
Next, write some tests in a file test_vowels.py. Use import to access the functions from main.py and
write a test function like the following:
   def test_vowels_simple():
   # Replace ... with the right answer
   assert main.vowels("abcabc") == ...
Run pytest in the directory. You should see a positive result (if not, try to fix the problems).
Create a few further tests – think about special cases such as a string without any vowels, an empty string, repeated vowels, etc.


# main.py:
def vowels(s):
  return {c for c in s if c in set("aeiou")}

# test_vowels.py:
import main

def test_vowels_simple():
  assert main.vowels("abcabc") == {"a"}
  assert main.vowels("xyai") == {"a", "i"}

def test_vowels_empty():
  assert main.vowels("") == set()
  
def test_vowels_repeat():
  assert main.vowels("iiiii") == {"i"}




