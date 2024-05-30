```
We now want to modify the code of the first exercise. Instead of tracking which vowels appear, we want
to track which sets of vowels appear per word. For example, in the text "aaa aio iouxyz" we have the
sets of vowels {{"a"}, {"a", "i", "o"}, {"i", "o", "u"}}. However, we now want to try out test driven development.
Create an empty function def word_vowels(s) in your main.py that simply returns an empty set. Now,
think of several example inputs and what the output of your function should be. Again, also think of
corner cases, e.g., an empty string, a string with only one word, words without vowels, ... Try to come
up with at least five different inputs and the output you expect (note the similarity to the coursework).
Remember to use frozenset to make sets of sets.
After writing these tests for word_vowels, try to implement the function. Run pytest to check if your
function satisfies all tests. If no, try to fix the errors. Running pytest -v gives you more insights.
Once your code satisfies your tests, try introducing a subtle bug into your function (e.g. by also treating x
as a vowel), write a test that triggers the faulty behaviour, and fix the function.
Bonus: You can actually use pytest to automate testing of your coursework submissions! For python,
you can use monkeypatching and output capture as follows.
 
   import io
  
   # Note the added argument
   def test_coursework_templonian_one(monkeypatch, capsys):
     stdin = """6 p 
     aaabbb
     """
    
     # This replaces the stdin with fixed text
     monkeypatch.setattr('sys.stdin', io.StringIO(stdin))
    
     templonian_function()
    
     # This gets the output of your code
     output = capsys.readouterr().out.rstrip()
    
     assert output == "3a3b"
     
assuming that templonian_function contains the function that solves the “Templonian Messages” problem.
(Or you rewrite the function to take the input string.) Note that the added arguments need to be named exactly in this way!
For C, you can use subprocess to call an external program. We will learn about this library later, but for now you can use the following

  def test_coursework_templonian_one():
    stdin = """6 p 
    aaabbb
    """
    p = subprocess.run(["c_templonian"], input=stdin, text=True)
    assert p.returncode == 0
    assert p.stdout.rstrip() == "3a3b"
(You can also use subprocess to call gcc before every test.)
```

# main.py:
def word_vowels(s):
  return {frozenset(c for c in w if c in set("aeiou")) for w in s.split()}

# test_vowels.py:
import main

def test_word_vowels_simple():
  assert main.word_vowels("abcabc") == {frozenset("a")}

def test_word_vowels_longer():
  assert main.word_vowels("aa ab io oi axi") == {
    frozenset("a"),
    frozenset("io"),
    frozenset("ai"),
  }
  
def test_word_vowels_empty():
  assert main.word_vowels("") == set()

def test_word_vowels_none():
  assert main.word_vowels("xxxx zzz") == {frozenset()}
