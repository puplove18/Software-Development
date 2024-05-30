```
Part I
  • Think of the translations for the words “Hello”, “Goodbye”, “University”, “Computer”, and “Dic-
  tionary” to your mother tongue (if English is your mother tongue or these words do not translate
  well, just make up translations). Write these translations into a Python dictionary, using a literal
  expression, and print it.
  • Add a few more words with the d[key] = value syntax.
  • Print the dictionary by displaying one line <word> translates to <translation> for each entry
  in the dictionary, sorted by key (like a “real” dictionary).
  • Take the string "Hello I am at Lancaster University". Go over it and apply all translations present
  in your dictionary, leaving words for which you do not have a translation untouched. Print the
  translated string.
  • Extend this approach by also tracking which words are unknown, i.e. for which you do not yet have
  a translation, and print this collection. Which data structure is appropriate here?
  • In English, capitalization is hardly relevant. Think how you can make sure that no matter how the
  words is capitalized, the translation is applied. Concretely, it should not matter whether Hello,
  hello, or HeLlO is written – your translation should always put the same translated word.
  • Replace the concrete string with input() and again try out your implementation.
Part II
  • Take Part II of the set exercise. Instead of tracking the first appearance, we want to store for each
  word all “capitalizations” in which the word appears. For example, in the string "Hello hello hellO
  hello" the capitalizations Hello, hello, and hellO appear. Modify your implementation to solve
  this problem. Think about which data structures are appropriate.
  As a test, for the string "Hello hello I say HELLO", your program should output
    
      1 Hello hello HELLO
      2 I
      3 say
    (in any order)

  • Now, group words together that are the same after removing all vowels. For example, Hello, hallo,
  and hlluouai all belong to the same “group”. Again, print each group in separate lines.
  • Instead of considering the “sequence” of consonants, group words by which consonants appear. So,
  hallo, hallllouh, and aolh are the “same” (both contain the consonants h and l) but different
  from xhallo (which also contains x).
  • Finally, we want to group words if they have the same number of consonants, irrespective of their
  order. (Note: This is more difficult than the previous exercise. Remember that dict are unhashable.)


#part 1
en_to_de = {"Hello": "Hallo", "Goodbye": "Auf Wiedersehen", "University": "Universität", "Computer": "Computer", "Dictionary": "Wörterbuch"}Òæ
en_to_de["Curtain"] = "Vorhang"
en_to_de["I"] = "Ich"

print("My dictionary:")
for en, de in en_to_de.items():
  print(f" {en} translates to {de}")

lowered_dictionary = {k.lower(): w for k, w in en_to_de.items()}

string = "Hello I am at Lancaster University"
words = string.split()
translation = []
unknown_words_set = set()
for word in words:
  lower = word.lower()
  if lower in lowered_dictionary:
    translation.append(lowered_dictionary[lower])
  else:
    translation.append(word)
    unknown_words_set.add(lower)

print(f"Translation: {' '.join(translation)}")
if unknown_words_set:
  print(f"I don't know the words {', '.join(sorted(unknown_words_set))}")

#Part 2
words = input().split()

appearances = dict()
for w in words:
  lower = w.lower() # Choose any "canonical form" here
  if lower not in appearances:
    appearances[lower] = set()
  appearances[lower].add(w)
print("Capitalizations:")
for v in appearances.values():
  print(' '.join(sorted(v)))
print()

# A small utility function to add set to the dict
# Can also use collections.defaultdict for this
def get(d, k, default):
  if k not in d:
    d[k] = default()
  return d[k]


without_vowels = dict()
for w in words:
  # Instead of maketrans can also call .replace several times
  key = w.lower().translate(str.maketrans({v: "" for v in "aeiou"}))
  get(without_vowels, key, set).add(w)
print("Without Vowels:")
for v in without_vowels.values():
  print(' '.join(sorted(v)))
print()


consonant_sets = dict()
# Derive this from the without vowels dictionary
# Could also do from scratch again
for k, k_words in without_vowels.items():
  key = frozenset(k)
  get(consonant_sets, key, set).update(k_words)
print("Consonant Sets:")
for k, v in consonant_sets.items():
  print(f"{''.join(k)}: {' '.join(sorted(v))}")
print()


# "hacky" solution: Sorted tuple of all consonants as key
# Here: Pairs of consonant and frequency
vowel_set = set("aeiou")
consonant_frequency = dict()
for w in words:
  # There also is collections.Counter to do this
  frequency = dict()
  for letter in w.lower():
    if letter in vowel_set:
      continue
    if letter in frequency:
      frequency[letter] += 1
    else:
      frequency[letter] = 1
  key = frozenset(frequency.items())
  get(consonant_frequency, key, set).add(w)

print("Consonant Frequency:")
for frequencies, words in consonant_frequency.items():
  freq_string = ','.join(f"{c}={f}" for c, f in sorted(frequencies))
  if not freq_string:
  print(f"{freq_string}: {' '.join(sorted(words))}")
print()












