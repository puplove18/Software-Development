```
Part I
  • Create a list containing the numbers 1, 2, 1, 3, 1, 4, using, e.g., literals. Now create a set containing
  these numbers using literal expressions. Which size do you expect for the set? Print the list and the
  set and compare the two.
  • Create the set of all numbers from 0 to 10 not in this set. Can you use comprehension and range?
Part II
  • Begin with the string "I like Sets and sets And dictionaries" Create a set of all words contained
  in this string (use .split()). How do you expect this set to look like?
  • Create the set of all words converted to lower case, using comprehension.
  • Print for each word in the string the first time it appears in any capitalization. For the example
  string, we want to see 1: I, 2: like, 3: Sets, 4: and, 7: dictionaries. This does not print
  sets and And since they already appeared (with different capitalization).
  • Replace the example string with input() and try out your implementation.
```

#part 1
list_1 = [1, 2, 1, 3, 1, 4]
set_1 = {1, 2, 1, 3, 1, 4} # Size: 4
print(len(list_1), len(set_1))
print(list_1, set_1)

set_2 = {i for i in range(10) if i not in set_1}
set_3 = set(range(10)) - set_1
print(set_2 == set_3)

#part 2
words = input().split()
word_set = set(w.lower() for w in words)

appearances = []
seen = set()
for i, w in enumerate(words):
  lower = w.lower()
  if lower not in seen:
    appearances.append((i + 1, w))
    seen.add(lower)
 print(", ".join(f"{i}: {w}" for i, w in appearances))






