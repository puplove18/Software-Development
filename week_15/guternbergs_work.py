```
Go to 
https://www.gutenberg.org/ 
and search for a public domain book of your liking (or pick an　arbitrary one). For example, you could pick The Picture of Dorian Gray by Oscar Wilde, 
https://www.gutenberg.org/ebooks/174. 
Download the book’s content as Plain Text UTF-8 and store it in a　file called book.txt (you may need to right-click > “Save Link As...”).
Write a program that opens and reads the file, using pathlib. Print how many lines the book text has.
Once you are able to read in the text, we can perform a number of analyses:
  • Count how often each character appears in the book’s text. Compute the relative frequency (i.e.
  how many % of the book’s content are a particular letter) and display it, sorted by that frequency.
  • Find out what the 10 most frequent words in the book are. Ignore words shorter than 5 letters.
  Think about how to treat capitalization and punctuation.
  • Find all longest appearing words.
  (Bonus: Can you do that in one single pass over the list of words?)
  • Write all these statistics into a separate file stats.txt.


from pathlib import Path
import string

def read_book(path):
  with path.open("rt") as f:
    lines = f.readlines()

  count = 0
  frequency = dict()
  for l in lines:
    for c in l:
      if not c.isalpha():
        continue
      count += 1
      c = c.lower()
      if c in frequesncy:
        frequency[c] += 1
      else:
        frequency[c] = 1
  words = []
  for l in lines:
    for w in l.split():
      words.append(w.lower().strip(string.punctuation))

  word_frequency = dict()
  for w in words:
    if len(w) < 5:
      continue
    if w in word_frequency:
      word_frequency[w] += 1
    else:
      word_frequency[w] = 1

  def key(x):
    return -x[1], x[0]
  top_ten = list(sorted(word_frequency.items(), key=key)[:10])

  length = 0
  longest = set()
  for w in words:
    if w.startswith("www"):
      continue
    if len(w) > length:
      length = len(w)
      longest.clear()
    if len(w) == length:
      longest.add(w)

  with Path("stats.txt").open("wt") as f:

  f.write(" ".join(f'{k}: {v / count * 100:.2f}%' for k, v in sorted(frequency.items(),
  key=key)))Òæ
  f.write("\n")
  f.write(" ".join(f'{w}: {freq:d}' for w, freq in top_ten))
  f.write("\n")
  f.write(" ".join(sorted(longest)))

read_book(Path("book.txt")








