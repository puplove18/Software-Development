```
Read a string from the user and split it into words by using split.
Gather all words that are longer than their position in the word-list into a new list, join it together using
spaces, and print the new “sentence”.
Example: For aaa a bb bbbbb the output should be aaa bbbbb.
Try to use enumerate and list comprehension. Can you solve the whole task in one line?
```


print(" ".join(w for i, w in enumerate(input().split()) if len(w) > 1)))
